/* Structure pictures for the 5.5 "Intermolecular Forces" practice set.
 *
 *   cd templates/slide && node decks/chem_u04_u05/imf_key.js
 *
 * Same drawing style as polarity_key.js (slides 24-30): outer-atom lone pairs left off,
 * central-atom lone pairs kept, a dipole arrow beside each POLAR bond pointing at the
 * delta-minus atom (cross at the delta-plus end), C-H bonds (0.35) and I-I get none.
 * Every molecule renders a key picture (with the long net arrow, or "net = 0"). Part A
 * molecules also render a student picture with the bond arrows only, so the student still
 * has to decide polar or nonpolar. Output: templates/worksheet/assets/chem_u05_s05.5_imf/.
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");
const K = require("../../tokens.generated");

const W = 2.4, H = 1.3;
const pres = new pptxgen();
pres.defineLayout({ name: "IK", width: W, height: H });
pres.layout = "IK";
const ARROW = K.courses.chemistry.primaryDeep;
const { lewis, at, dipole, line, label } = require("./molecules")(pres);
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_s05.5_imf");

function smallDipole(s, P, from, to, side, off = 0.1, f0 = 0.18, f1 = 0.86) {
  const [x1, y1] = P(from), [x2, y2] = P(to);
  const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, nx = -uy * side, ny = ux * side;
  const ax = x1 + ux * L * f0 + nx * off, ay = y1 + uy * L * f0 + ny * off;
  const bx = x1 + ux * L * f1 + nx * off, by = y1 + uy * L * f1 + ny * off;
  line(s, ax, ay, bx, by, { color: ARROW, width: 1.5, end: "triangle" });
  const t = Math.hypot(bx - ax, by - ay) * 0.28, cx = ax + ux * t, cy = ay + uy * t, h = 0.045;
  line(s, cx - uy * h, cy + ux * h, cx + uy * h, cy - ux * h, { color: ARROW, width: 1.5 });
}

const cross = (c, o) => ({ atoms: { C: [c, 0, 0], A: [o[0], 0, -1], B: [o[1], 1, 0], D: [o[2], 0, 1], E: [o[3], -1, 0] },
  bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], pairs: [] });
/* CH3-X-H skeleton for methanol / methylamine: C left, X right, three H on C */
const methyl = (x, extraH, pairs) => ({
  atoms: { C: ["C", -0.6, 0], X: [x, 0.5, 0], H1: ["H", -0.6, -1], H2: ["H", -1.6, 0], H3: ["H", -0.6, 1],
           ...Object.fromEntries(extraH.map((a, i) => ["HX" + i, ["H", 0.5 + at(a)[0], at(a)[1]]])) },
  bonds: [["C", "X", 1], ["C", "H1", 1], ["C", "H2", 1], ["C", "H3", 1], ...extraH.map((_, i) => ["X", "HX" + i, 1])],
  pairs: pairs.map((a) => ["X", a]) });

/* net: [x1, y1, x2, y2] in inches from the picture centre, or null for nonpolar.
   student: true = Part A, so also render the arrows-only picture. */
const MOLS = {
  CF4:    { mol: cross("C", ["F", "F", "F", "F"]), u: 0.42, dx: -0.3, student: true,
            dip: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], net: null },
  CH3OH:  { mol: methyl("O", [55], [-35, -110]), u: 0.4, dx: -0.25, student: true,
            dip: [["C", "X", 1], ["HX0", "X", 1]], net: [0.85, 0.4, 0.85, -0.4] },
  CH3Cl:  { mol: cross("C", ["H", "Cl", "H", "H"]), u: 0.42, dx: -0.3, student: true,
            dip: [["C", "B", -1]], net: [0.15, 0.5, 0.85, 0.5] },
  I2:     { mol: { atoms: { A: ["I", -0.5, 0], B: ["I", 0.5, 0] }, bonds: [["A", "B", 1]], pairs: [] }, u: 0.7, dy: -0.1, student: true,
            dip: [], net: null, below: true },
  CH3NH2: { mol: methyl("N", [0, 60], [-90]), u: 0.4, dx: -0.3, student: true,
            dip: [["C", "X", 1], ["HX0", "X", 1], ["HX1", "X", 1]], net: [0.85, 0.4, 0.85, -0.4] },
  SiCl4:  { mol: cross("Si", ["Cl", "Cl", "Cl", "Cl"]), u: 0.44, dx: -0.3,
            dip: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], net: null },
  HCl:    { mol: { atoms: { A: ["H", -0.5, 0], B: ["Cl", 0.5, 0] }, bonds: [["A", "B", 1]], pairs: [] }, u: 0.7, dy: -0.15,
            dip: [["A", "B", -1]], net: [-0.4, 0.38, 0.4, 0.38] },
  HF:     { mol: { atoms: { A: ["H", -0.5, 0], B: ["F", 0.5, 0] }, bonds: [["A", "B", 1]], pairs: [] }, u: 0.7, dy: -0.15,
            dip: [["A", "B", -1]], net: [-0.4, 0.38, 0.4, 0.38] },
  CH3F:   { mol: cross("C", ["H", "F", "H", "H"]), u: 0.42, dx: -0.3,
            dip: [["C", "B", -1]], net: [0.15, 0.5, 0.85, 0.5] },
  SF2:    { mol: { atoms: { S: ["S", 0, 0], A: ["F", ...at(142.25)], B: ["F", ...at(37.75)] },
                   bonds: [["S", "A", 1], ["S", "B", 1]], pairs: [["S", -135], ["S", -45]] }, u: 0.56, dx: -0.25, dy: -0.12,
            dip: [["S", "A", 1], ["S", "B", -1]], net: [0.8, -0.4, 0.8, 0.4] },
};

const names = [];
function render(name, m, withNet) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  const P = lewis(s, m.mol, W / 2 + (m.dx || 0), H / 2 + (m.dy || 0), m.u, { fs: 13 });
  for (const [a, b, side] of m.dip) smallDipole(s, P, a, b, side);
  if (withNet) {
    if (m.net) { const [x1, y1, x2, y2] = m.net; dipole(s, W / 2 + x1, H / 2 + y1, W / 2 + x2, H / 2 + y2, ARROW, 0, 3.25); }
    else if (m.below) label(s, "net = 0", W / 2, H - 0.2, 1.2, 0.2, { size: 10, color: ARROW });
    else label(s, "net\n= 0", W / 2 + 0.8, H / 2, 0.5, 0.4, { size: 10, color: ARROW });
  }
  names.push(withNet ? name : name + "_student");
}
for (const [name, m] of Object.entries(MOLS)) {
  render(name, m, true);
  if (m.student) render(name, m, false);
}
fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ik-"));
const pptx = path.join(tmp, "ik.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "ik.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} pictures`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `imf_${names[i]}.png`)));
  console.log(`wrote ${names.length} pictures to ${OUT}`);
});
