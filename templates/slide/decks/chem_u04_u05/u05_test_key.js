/* Key pictures for the Unit 5 test, Day 2 charts.
 *
 *   cd templates/slide && node decks/chem_u04_u05/u05_test_key.js
 *
 * Chart 1 (structure) needs full Lewis structures, every lone pair drawn, in the style of
 * vsepr_lewis_key.js. Chart 2 (polarity) needs the dipole sketch in the style of
 * polarity_key.js / imf_key.js: outer lone pairs off, an arrow on each polar bond toward
 * delta-minus (none on C-H 0.35 or Si-H 0.30), a net arrow or "net = 0".
 * Output: templates/worksheet/assets/chem_u05_test/ (lewis_X.png, polar_X.png).
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");
const K = require("../../tokens.generated");

const W = 2.4, H = 1.3;
const pres = new pptxgen();
pres.defineLayout({ name: "TK", width: W, height: H });
pres.layout = "TK";
const ARROW = K.courses.chemistry.primaryDeep;
const { lewis, at, dipole, line, label, MOL } = require("./molecules")(pres);
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_test");

function smallDipole(s, P, from, to, side, off = 0.1, f0 = 0.18, f1 = 0.86) {
  const [x1, y1] = P(from), [x2, y2] = P(to);
  const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, nx = -uy * side, ny = ux * side;
  const ax = x1 + ux * L * f0 + nx * off, ay = y1 + uy * L * f0 + ny * off;
  const bx = x1 + ux * L * f1 + nx * off, by = y1 + uy * L * f1 + ny * off;
  line(s, ax, ay, bx, by, { color: ARROW, width: 1.5, end: "triangle" });
  const t = Math.hypot(bx - ax, by - ay) * 0.28, cx = ax + ux * t, cy = ay + uy * t, h = 0.045;
  line(s, cx - uy * h, cy + ux * h, cx + uy * h, cy - ux * h, { color: ARROW, width: 1.5 });
}
const outer3 = (id, dir) => [[id, dir], [id, dir + 90], [id, dir - 90]];
const cross = (c, o, pairs = []) => ({ atoms: { C: [c, 0, 0], A: [o[0], 0, -1], B: [o[1], 1, 0], D: [o[2], 0, 1], E: [o[3], -1, 0] },
  bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], pairs });
const OF2 = (pairsOuter) => ({ atoms: { O: ["O", 0, 0], A: ["F", ...at(142.25)], B: ["F", ...at(37.75)] },
  bonds: [["O", "A", 1], ["O", "B", 1]], pairs: [["O", -135], ["O", -45], ...(pairsOuter ? [...outer3("A", 142.25), ...outer3("B", 37.75)] : [])] });
const CH2O = (full) => ({ atoms: { C: ["C", 0, 0], O: ["O", ...at(-90)], H1: ["H", ...at(150)], H2: ["H", ...at(30)] },
  bonds: [["C", "O", 2], ["C", "H1", 1], ["C", "H2", 1]], pairs: full ? [["O", -135], ["O", -45]] : [] });

/* Lewis (full) */
const LEWIS = {
  SiH4: { mol: cross("Si", ["H", "H", "H", "H"]), u: 0.45, fs: 18 },
  CO2:  { mol: MOL.CO2, u: 0.62, fs: 18 },
  CH3F: { mol: cross("C", ["H", "F", "H", "H"], outer3("B", 0)), u: 0.45, fs: 18 },
  NH3:  { mol: MOL.NH3, u: 0.5, fs: 18, dy: -0.12 },
  OF2:  { mol: OF2(true), u: 0.6, fs: 18, dy: -0.12 },
  CH2O: { mol: CH2O(true), u: 0.5, fs: 18, dy: 0.12 },
};
/* Dipole sketches */
const POLAR = {
  SiH4: { mol: cross("Si", ["H", "H", "H", "H"]), u: 0.42, dx: -0.3, dip: [], net: null },
  CO2:  { mol: { atoms: { O1: ["O", -1, 0], C: ["C", 0, 0], O2: ["O", 1, 0] }, bonds: [["O1", "C", 2], ["C", "O2", 2]], pairs: [] },
          u: 0.66, dy: -0.1, below: true, dip: [["C", "O1", 1], ["C", "O2", -1]], net: null },
  CH3F: { mol: cross("C", ["H", "F", "H", "H"]), u: 0.42, dx: -0.3, dip: [["C", "B", -1]], net: [0.15, 0.5, 0.85, 0.5] },
  NH3:  { mol: MOL.NH3, u: 0.52, dx: -0.25, dy: -0.1, dip: [["H1", "N", -1], ["H2", "N", 1], ["H3", "N", 1]], net: [0.8, 0.42, 0.8, -0.38] },
  OF2:  { mol: OF2(false), u: 0.56, dx: -0.25, dy: -0.12, dip: [["O", "A", 1], ["O", "B", -1]], net: [0.8, -0.4, 0.8, 0.4] },
  CH2O: { mol: CH2O(true), u: 0.48, dx: -0.25, dy: 0.12, dip: [["C", "O", 1, 0.17]], net: [0.8, 0.4, 0.8, -0.4] },
};

const names = [];
for (const [n, m] of Object.entries(LEWIS)) {
  const s = pres.addSlide(); s.background = { color: "FFFFFF" };
  lewis(s, m.mol, W / 2 + (m.dx || 0), H / 2 + (m.dy || 0), m.u, { fs: m.fs });
  names.push("lewis_" + n);
}
for (const [n, m] of Object.entries(POLAR)) {
  const s = pres.addSlide(); s.background = { color: "FFFFFF" };
  const P = lewis(s, m.mol, W / 2 + (m.dx || 0), H / 2 + (m.dy || 0), m.u, { fs: 13 });
  for (const [a, b, side, off] of m.dip) smallDipole(s, P, a, b, side, off || 0.1);
  if (m.net) { const [x1, y1, x2, y2] = m.net; dipole(s, W / 2 + x1, H / 2 + y1, W / 2 + x2, H / 2 + y2, ARROW, 0, 3.25); }
  else if (m.below) label(s, "net = 0", W / 2, H - 0.2, 1.2, 0.2, { size: 10, color: ARROW });
  else label(s, "net\n= 0", W / 2 + 0.8, H / 2, 0.5, 0.4, { size: 10, color: ARROW });
  names.push("polar_" + n);
}
fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "tk-"));
const pptx = path.join(tmp, "tk.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "tk.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} pictures`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `${names[i]}.png`)));
  console.log(`wrote ${names.length} pictures to ${OUT}`);
});
