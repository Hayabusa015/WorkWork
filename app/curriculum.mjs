/* The curriculum, read from courses/<course>/DECISIONS.md at request time.
 *
 * Nothing here is stored. A cached or generated copy of the unit and section
 * map would be a second place a course fact lives, and a stale one is exactly
 * the defect that put a U5 footer on a U4 packet. The decisions file is read,
 * parsed, and thrown away on every request.
 *
 * The three roadmaps are formatted differently, because each was adopted
 * verbatim from the document Matt already had:
 *
 *   ### U1 · The Universe & Solar System — 6 sections    (geology)
 *   **U0 · Physics Math Review** — 4 sections            (physics)
 *   **U0 Foundations of Chemistry** (4 sections)         (chemistry)
 *
 * All three shapes are read rather than one being imposed on files that were
 * correct already — the same choice templates/_shull_docx.py made.
 */

// The unit heading, in all three shapes. Group 1 is the unit number, group 2
// the title, groups 3/4 the declared section count in either notation.
const UNIT_HEADINGS = [
  /^###\s+U(\d{1,2})\s*[·.:]\s*(.+?)\s*—\s*(\d+)\s+sections?\b/,
  /^\*\*U(\d{1,2})\s*[·.:]?\s*([^*]+?)\*\*\s*(?:—\s*(\d+)\s+sections?\b|\((\d+)\s+sections?\))/,
];

// A phase heading ends the unit above it without starting a new one.
const PHASE = /^###\s+Phase\b/;
const NEXT_SECTION = /^##\s(?!#)/;

/** The curriculum-map region of a decisions file, or the whole file. */
function mapRegion(text) {
  const start = text.search(/^##\s+Curriculum map/m);
  if (start < 0) return text;
  const rest = text.slice(start + 3);
  const end = rest.search(NEXT_SECTION);
  return end < 0 ? rest : rest.slice(0, end);
}

function unitHeading(line) {
  for (const pattern of UNIT_HEADINGS) {
    const m = line.match(pattern);
    if (m) return {unit: Number(m[1]), title: m[2].trim().replace(/[\s·—-]+$/, ''),
                   declared: Number(m[3] ?? m[4]) || null};
  }
  return null;
}

/** The sections listed under one unit heading, backticked or plain. */
function sections(body, unit) {
  const out = [];
  for (const piece of body.split('·')) {
    // `4.1` Plate Boundaries   |   4.1 Plate Boundaries   |   9.5 Spontaneity `EXT`
    const m = piece.match(/^\s*`?(\d{1,2})\.(\d)`?\s+(.+?)\s*$/);
    if (!m || Number(m[1]) !== unit) continue;
    let title = m[3].replace(/`EXT`/g, '').replace(/\s{2,}/g, ' ').trim();
    const ext = /`EXT`/.test(m[3]);
    if (!title) continue;
    out.push({code: `${m[1]}.${m[2]}`, title, ext});
  }
  return out;
}

/**
 * Parse one course's decisions text.
 *
 * Every unit declares how many sections it has. When the parse disagrees with
 * that declaration the unit carries a `warning` and the app says so, because a
 * silently short section list is how a teacher builds against the wrong code.
 */
export function parseCurriculum(text, course) {
  const region = mapRegion(text);
  const lines = region.split(/\r?\n/);
  const units = [];
  let open = null, body = [];

  const close = () => {
    if (!open) return;
    const found = sections(body.join(' '), open.unit);
    if (open.declared && found.length !== open.declared) {
      open.warning = `The decisions file declares ${open.declared} sections for U${open.unit} `
                   + `but ${found.length} could be read. Check courses/${course}/DECISIONS.md `
                   + 'before building against this unit.';
    }
    units.push({...open, sections: found});
    open = null; body = [];
  };

  for (const line of lines) {
    const heading = unitHeading(line);
    if (heading) { close(); open = heading; continue; }
    if (PHASE.test(line)) { close(); continue; }
    // Block quotes are the roadmap's own commentary. They cite section codes
    // ("`4.4` covers all three convergent subtypes") and must not be read as
    // section entries.
    if (!open || /^\s*>/.test(line)) continue;
    body.push(line);
  }
  close();

  units.sort((a, b) => a.unit - b.unit);
  return {course, units};
}

/**
 * Every section code in the file, by the same pattern the print builders use
 * (templates/_shull_docx.py `known_sections`). The picker is cross-checked
 * against this: the app must never offer a code a builder would refuse.
 */
export function knownSections(text) {
  const end = text.indexOf('## Course sequencing rules');
  const scope = end > 0 ? text.slice(0, end) : text;
  return new Set(scope.match(/(?<![\d.])\d{1,2}\.\d(?![\d])/g) || []);
}

/** Drop anything the builders would not accept, and say what was dropped. */
export function curriculum(text, course) {
  const parsed = parseCurriculum(text, course);
  const known = knownSections(text);
  for (const unit of parsed.units) {
    const rejected = unit.sections.filter(s => !known.has(s.code));
    if (rejected.length) {
      unit.sections = unit.sections.filter(s => known.has(s.code));
      unit.warning = `${rejected.map(s => s.code).join(', ')} could not be confirmed against the `
                   + 'course decisions and has been withheld.';
    }
  }
  parsed.units = parsed.units.filter(u => u.sections.length);
  return parsed;
}

/**
 * The document types, read from standards/NAMING.md rather than listed here.
 * The fixed list is a standard, and a standard lives in exactly one place.
 */
export function documentTypes(namingText) {
  const m = namingText.match(/\*\*Types:\*\*([\s\S]*?)\n\n/);
  if (!m) return [];
  return [...m[1].matchAll(/`([A-Za-z_]+)`/g)].map(x => x[1]);
}

/**
 * The filename SHULL_[COURSE]_[Type]_U##_S##.#[...] from standards/NAMING.md
 * §2. The unit and the digits before the section's decimal point are both
 * zero-padded to two, so a filename sorts and compares against its folder.
 */
export const COURSE_CODE = {chemistry: 'CHEM', physics: 'PHYS', geology: 'GEO'};

export function documentName({course, type, unit, sections: codes, extension = 'docx'}) {
  const pad = code => {
    const [whole, decimal] = String(code).split('.');
    return `S${String(whole).padStart(2, '0')}.${decimal}`;
  };
  const span = codes.length > 1 ? `${pad(codes[0])}-${pad(codes[codes.length - 1])}` : pad(codes[0]);
  return `SHULL_${COURSE_CODE[course]}_${type}_U${String(unit).padStart(2, '0')}_${span}.${extension}`;
}
