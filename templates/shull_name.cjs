/* The SHULL filename grammar, in one place for the JS builders and the app.
 * Rule: standards/NAMING.md §2 (SHULL-CHG-0024). The Python builders use
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

function documentName({ type, sections, unit, topic, unitTitle, version, key = false, extension = "docx" }) {
  let label = String(type).replace(/_/g, " ");
  if (version) label += ` ${version}`;
  if (key) label += " Key";
  const codes = sections.map(String);
  const single = codes.length === 1;
  const head = single ? codes[0] : `Unit ${Number(unit)}`;
  const tail = single ? topic : unitTitle;
  return `${head} ${label}${tail ? ` - ${clean(tail)}` : ""}.${extension}`;
}

module.exports = { documentName, clean };
