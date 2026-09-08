/* Build one section deck from a JSON spec, on the twelve-layout masters.
 *
 *   SHULL_COURSE=chemistry node build_deck.js decks/chem_u01_s01.4.json out.pptx
 *
 * The masters come from build.js; this file only places content into them. That split
 * is the point: a deck can never introduce geometry or colour of its own, because it
 * has no way to. Everything it can set is a placeholder the master already declared.
 */
const fs = require("fs");
const path = require("path");

const specPath = process.argv[2];
if (!specPath) {
  console.error("usage: SHULL_COURSE=<course> node build_deck.js <spec.json> [out.pptx]");
  process.exit(1);
}
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));

// The spec declares its own course. Trusting an env var over the spec is how a
// Chemistry deck gets built in Geology teal.
process.env.SHULL_COURSE = spec.course;

const pres = require("./build");
const K = require("./tokens.generated");

const COURSE_CODE = { chemistry: "CHEM", physics: "PHYS", geology: "GEO" };
const code = COURSE_CODE[spec.course];
if (!code) { console.error(`unknown course "${spec.course}"`); process.exit(1); }

/* Step 0 of workflows/build-deliverable.md: confirm the section code exists in that
 * course's DECISIONS.md before anything is built. Not in a skill, not in a filename
 * someone suggested - in the decisions file.
 *
 * This check runs HERE, at the build, because that is where it bites. T-10 found the
 * gap: a spec declaring Chemistry 1.9 produced a finished deck footered U01 S01.9, and
 * nothing objected. A wrong footer on a printed packet is the exact defect the naming
 * standard was written to stop, and a rule that lives only in a workflow document is
 * not a mechanism. */
const DECISIONS = path.join(__dirname, "..", "..", "courses", spec.course, "DECISIONS.md");
if (!fs.existsSync(DECISIONS)) {
  console.error(`build_deck: no decisions file at ${DECISIONS} — cannot verify the section code`);
  process.exit(1);
}
const decisions = fs.readFileSync(DECISIONS, "utf8");
const mapEnd = decisions.indexOf("## Course sequencing rules");
const curriculum = mapEnd > 0 ? decisions.slice(0, mapEnd) : decisions;
const known = new Set((curriculum.match(/(?<![\d.])\d{1,2}\.\d(?![\d])/g) || []));
if (!known.has(spec.section)) {
  console.error(`build_deck: section ${spec.section} is not in courses/${spec.course}/DECISIONS.md`);
  console.error("Nothing is built against a code that is not in the decisions file. Stop and ask.");
  process.exit(1);
}
const declaredUnit = parseInt(spec.section.split(".")[0], 10);
if (parseInt(spec.unit, 10) !== declaredUnit) {
  console.error(`build_deck: unit ${spec.unit} disagrees with section ${spec.section}`);
  process.exit(1);
}

/* PNG header read, so an image can be fitted to its slot without pulling in a library. */
function pngSize(file) {
  const b = fs.readFileSync(file, { start: 0, end: 32 });
  if (b.length < 24 || b.readUInt32BE(0) !== 0x89504e47) return null;
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

const pad = (n) => String(n).padStart(2, "0");
const UNIT = `U${pad(spec.unit)}`;
const SECT = `S${pad(spec.section.split(".")[0])}.${spec.section.split(".")[1]}`;
const OUT = process.argv[3] || `SHULL_${code}_Slides_${UNIT}_${SECT}.pptx`;

const EYEBROW = `UNIT ${pad(spec.unit)}  •  ${spec.course.toUpperCase()}`;
const FOOTER_CODE = `${UNIT} • ${SECT}`;

/* The line caps are the reason this file exists rather than someone hand-placing text.
   Slide System v2: over the cap you split the slide, you never shrink type to fit. */
const CAPS = K.lineCaps;

const problems = [];
let n = 0;

for (const slide of spec.slides) {
  n += 1;
  const s = pres.addSlide({ masterName: slide.master });
  const fields = Object.assign({}, slide.fields);

  const declared = pres.PLACEHOLDERS[slide.master];
  if (!declared) { problems.push(`slide ${n}: no master named ${slide.master}`); continue; }

  // Furniture every slide carries - but only where the master actually declares it.
  // 02_SECTION_TITLE has no eyebrow; adding one anyway is not a no-op, it is a stray
  // text box in whatever font the renderer picks.
  if (declared.includes("eyebrow") && !("eyebrow" in fields)) fields.eyebrow = EYEBROW;
  if (declared.includes("code") && !("code" in fields)) {
    fields.code = slide.master === "12_DECK_INDEX" ? "TEMPLATE" : FOOTER_CODE;
  }

  /* Images go into a named slot, never at coordinates. A deck that could place an image
     at an arbitrary x/y would be a deck that can invent geometry, which is the one thing
     this split exists to prevent. The image is fitted inside the slot and centred, so a
     wrong aspect ratio letterboxes instead of stretching. */
  for (const [slotName, imgRel] of Object.entries(slide.images || {})) {
    const slot = (pres.SLOTS[slide.master] || {})[slotName];
    if (!slot) { problems.push(`slide ${n} (${slide.master}): no slot "${slotName}"`); continue; }
    const imgPath = path.resolve(path.dirname(specPath), imgRel);
    if (!fs.existsSync(imgPath)) { problems.push(`slide ${n}: image not found — ${imgRel}`); continue; }
    const dim = pngSize(imgPath);
    let { x, y, w, h } = slot;
    if (dim) {
      const scale = Math.min(w / dim.w, h / dim.h);
      const fw = dim.w * scale, fh = dim.h * scale;
      x += (w - fw) / 2; y += (h - fh) / 2; w = fw; h = fh;
    }
    s.addImage({ path: imgPath, x, y, w, h });
    delete fields[slotName];   // the slot's prompt text is replaced by the image
  }

  for (const [ph, txt] of Object.entries(fields)) {
    if (txt === null || txt === undefined) continue;
    if (!declared.includes(ph)) {
      problems.push(`slide ${n} (${slide.master}): no placeholder "${ph}" — declared: ${declared.join(", ")}`);
      continue;
    }
    s.addText(String(txt), { placeholder: ph });
  }

  // Cap check. A card body of five lines is a slide that should have been two slides.
  const bodyKeys = Object.keys(fields).filter(k => /_b$/.test(k) || k === "mustwrite" || k === "subhead");
  for (const k of bodyKeys) {
    const lines = String(fields[k] || "").split("\n").filter(l => l.trim()).length;
    const cap = k === "mustwrite" ? 2 : 4;
    if (lines > cap) problems.push(`slide ${n} (${slide.master}) field ${k}: ${lines} lines, cap ${cap}`);
  }
  if (fields.mustwrite && String(fields.mustwrite).length > 110) {
    problems.push(`slide ${n}: must-write is ${String(fields.mustwrite).length} chars — it has to fit one bar`);
  }
}

if (problems.length) {
  console.error(`build_deck: refusing to write — ${problems.length} problem(s)`);
  for (const p of problems) console.error("  " + p);
  console.error(`\nLine caps: ${JSON.stringify(CAPS)}`);
  console.error("Over a cap, split the slide. Never shrink type to fit.");
  process.exit(1);
}

pres.writeFile({ fileName: OUT }).then(f => {
  console.log(`wrote ${f}  —  ${code} ${UNIT} ${SECT}, ${n} slides`);
  // pptxgenjs stores its zip parts almost uncompressed - about 5x larger than it
  // needs to be. Found during T-7, when the file size turned out to matter.
  const r = require("child_process").spawnSync(
    "python3", [path.join(__dirname, "..", "..", "scripts", "repack_pptx.py"), f],
    { encoding: "utf8" });
  if (r.status === 0) process.stdout.write(r.stdout);
  else console.error("repack skipped:", (r.stderr || "").trim());
});
