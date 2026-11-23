/* Ball-and-stick VSEPR sketches for the 5.3 PhET Molecule Shapes sheet: one picture per
 * row of the key, and the worked example on the student copy.
 *
 *   cd templates/slide && node decks/chem_u04_u05/vsepr_sketches.js
 *
 * Drawn the way a student can copy it from PhET: a dark central atom, outer atoms as open
 * circles, a solid wedge for a bond toward you, a dashed wedge for one away, and lone pairs
 * as shaded lobes. Each picture is a 2.0 x 1.15 in slide rendered to PNG through LibreOffice
 * into templates/worksheet/assets/chem_u05_s05.3/.
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");
const K = require("../../tokens.generated");

const W = 2.0, H = 1.15, CX = W / 2, CY = H / 2 + 0.02, U = 0.42;
const INK = K.ground.asphalt, GRAPHITE = K.ground.graphite, HAIR = K.ground.ruleHairline, PAPER = K.ground.parchment;
const pres = new pptxgen();
pres.defineLayout({ name: "SK", width: W, height: H });
pres.layout = "SK";
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_s05.3");

const rad = (d) => d * Math.PI / 180;
const pt = (deg, r) => [CX + Math.cos(rad(deg)) * r, CY + Math.sin(rad(deg)) * r];

function line(s, x1, y1, x2, y2, o = {}) {
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2),
    w: Math.max(Math.abs(x2 - x1), 0.001), h: Math.max(Math.abs(y2 - y1), 0.001),
    flipH: x2 < x1, flipV: y2 < y1, line: { color: o.color || INK, width: o.width || 1.75 } });
}
function bond(s, deg, style, len) {
  const r0 = 0.09, r1 = len * U - 0.08;
  const [x0, y0] = pt(deg, r0), [x1, y1] = pt(deg, r1);
  const ux = Math.cos(rad(deg)), uy = Math.sin(rad(deg)), half = 0.045;
  if (style === "wedge") {
    const P = [[x0, y0], [x1 - uy * half, y1 + ux * half], [x1 + uy * half, y1 - ux * half]];
    const mx = Math.min(...P.map((q) => q[0])), my = Math.min(...P.map((q) => q[1]));
    s.addShape(pres.shapes.CUSTOM_GEOMETRY, { x: mx, y: my,
      w: Math.max(Math.max(...P.map((q) => q[0])) - mx, 0.01), h: Math.max(Math.max(...P.map((q) => q[1])) - my, 0.01),
      points: [...P.map((q) => ({ x: q[0] - mx, y: q[1] - my })), { close: true }],
      fill: { color: INK }, line: { color: INK, width: 0.5 } });
  } else if (style === "dash") {
    for (let i = 0; i < 5; i++) {
      const f = (i + 0.5) / 5, h = half * (0.3 + 0.7 * f), mx = x0 + (x1 - x0) * f, my = y0 + (y1 - y0) * f;
      line(s, mx - uy * h, my + ux * h, mx + uy * h, my - ux * h, { width: 1.25 });
    }
  } else line(s, x0, y0, x1, y1, { width: 2 });
}
function atom(s, deg, len) {
  const [x, y] = pt(deg, len * U), d = 0.16;
  s.addShape(pres.shapes.OVAL, { x: x - d / 2, y: y - d / 2, w: d, h: d, fill: { color: "FFFFFF" }, line: { color: INK, width: 1.25 } });
}
function lonePair(s, deg) {
  const [x, y] = pt(deg, 0.27);
  s.addShape(pres.shapes.OVAL, { x: x - 0.15, y: y - 0.085, w: 0.3, h: 0.17, rotate: deg,
    fill: { color: PAPER }, line: { color: GRAPHITE, width: 1 } });
  for (const sg of [-1, 1]) {
    const [dx, dy] = [Math.cos(rad(deg + 90)) * 0.035 * sg, Math.sin(rad(deg + 90)) * 0.035 * sg];
    s.addShape(pres.shapes.OVAL, { x: x + dx - 0.017, y: y + dy - 0.017, w: 0.034, h: 0.034, fill: { color: INK }, line: { color: INK, width: 0.5 } });
  }
}
function centre(s) {
  const d = 0.2;
  s.addShape(pres.shapes.OVAL, { x: CX - d / 2, y: CY - d / 2, w: d, h: d, fill: { color: GRAPHITE }, line: { color: INK, width: 1 } });
}

/* Angles are screen angles: 0 = right, 90 = DOWN (y grows downward).
   Each shape: [angle, "bond" style or "lp", length]. Lengths below 1 foreshorten a bond that
   points toward or away from the viewer. */
const B = (deg, style = "plain", len = 1) => ({ deg, style, len });
const L = (deg) => ({ deg, style: "lp" });
const SHAPES = {
  "2_2_0": [B(180), B(0)],
  "3_3_0": [B(-90), B(150), B(30)],
  "3_2_1": [L(-90), B(150), B(30)],
  "4_4_0": [B(-90), B(155), B(15, "wedge", 0.9), B(62, "dash", 0.85)],
  "4_3_1": [L(-90), B(155), B(15, "wedge", 0.9), B(62, "dash", 0.85)],
  "4_2_2": [L(-125), L(-55), B(142), B(38)],
  "5_5_0": [B(-90), B(90), B(180), B(330, "wedge", 0.9), B(30, "dash", 0.85)],
  "5_4_1": [B(-90), B(90), L(180), B(330, "wedge", 0.9), B(30, "dash", 0.85)],
  "5_3_2": [B(-90), B(90), B(180), L(330), L(30)],
  "5_2_3": [B(-90), B(90), L(180), L(330), L(30)],
  "6_6_0": [B(-90), B(90), B(180), B(0), B(145, "wedge", 0.85), B(-35, "dash", 0.8)],
  "6_5_1": [B(-90), L(90), B(180), B(0), B(145, "wedge", 0.85), B(-35, "dash", 0.8)],
  "6_4_2": [L(-90), L(90), B(180), B(0), B(145, "wedge", 0.85), B(-35, "dash", 0.8)],
};

const names = [];
for (const [name, parts] of Object.entries(SHAPES)) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  for (const p of parts) if (p.style === "lp") lonePair(s, p.deg);
  for (const p of parts) if (p.style !== "lp") bond(s, p.deg, p.style, p.len);
  centre(s);
  for (const p of parts) if (p.style !== "lp") atom(s, p.deg, p.len);
  names.push(name);
}

fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "vsepr-"));
const pptx = path.join(tmp, "sk.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "sk.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} sketches`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `shape_${names[i]}.png`)));
  console.log(`wrote ${names.length} sketches to ${OUT}`);
});
