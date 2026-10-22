/* The SHULL filename grammar, in one place for the JS builders and the app.
 * Rule: standards/NAMING.md §2 (SHULL-CHG-0024, short topics SHULL-CHG-0041). The Python builders use
 * templates/_shull_name.py, which implements the same grammar; both are pinned to the
 * same examples by their tests.
 *
 *   1.2 Practice Set - Balancing Equations.docx
 *   1.2 Quiz A Key - Balancing Equations.docx
 *   Unit 1 Guided Notes - Motion in One Dimension.docx      (more than one section)
 */
function clean(text) {
  return String(text).replace(/[\\/:*?"<>|]/g, "").replace(/\s{2,}/g, " ").replace(/^[ .]+|[ .]+$/g, "");
}

const MAX_TOPIC = 20;

/* The short title for a section ("1.3") or unit ("U1"), from the Short titles table in a course's
 * DECISIONS.md text (SHULL-CHG-0041). undefined if there is no row: never auto-shortened. */
function shortTitle(decisionsText, key) {
  const m = decisionsText.match(/^## Short titles\s*$([\s\S]*?)(?=^## )/m);
  if (!m) return undefined;
  const norm = (k) => { k = String(k).trim(); return /^u/i.test(k) ? "U" + k.slice(1).replace(/^0+/, "") : k; };
  const want = norm(key);
  for (const row of m[1].matchAll(/^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$/gm)) {
    if (norm(row[1]) === want) return clean(row[2]) || undefined;
  }
  return undefined;
}

function documentName({ type, sections, unit, topic, unitTitle, version, key = false, extension = "docx", descriptor }) {
  let label = String(type).replace(/_/g, " ");
  if (version) label += ` ${version}`;
  if (key) label += " Key";
  const codes = sections.map(String);
  const single = codes.length === 1;
  const head = single ? codes[0] : `Unit ${Number(unit)}`;
  const tail = single ? topic : unitTitle;
  const t = tail ? clean(tail) : "";
  if (t.length > MAX_TOPIC) throw new Error(`topic "${t}" is ${t.length} characters; the limit is ${MAX_TOPIC}. Use the short title from the course decisions file.`);
  let name = `${head} ${label}${t ? ` - ${t}` : ""}`;
  if (descriptor) {
    const have = new Set(t.split(/\s+/).map((w) => w.toLowerCase()));
    const extra = clean(descriptor).split(/\s+/).filter((w) => w && !have.has(w.toLowerCase())).join(" ");
    if (extra) name += t ? ` ${extra}` : ` - ${extra}`;
  }
  return `${name}.${extension}`;
}

module.exports = { documentName, shortTitle, clean, MAX_TOPIC };
