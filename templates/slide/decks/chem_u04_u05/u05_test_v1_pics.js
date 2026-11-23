/* Pictures for the Unit 5 test (no IMF), version 1, and its study guide.
 *
 *   cd templates/slide && node decks/chem_u04_u05/u05_test_v1_pics.js
 *
 * Full Lewis structures, every lone pair drawn, in the style of vsepr_lewis_key.js:
 *   sort_X   - the eight molecules students sort polar / nonpolar on Edulastic
 *   test_X   - key drawings for the paper test's four compounds
 *   guide_X  - key drawings for the study guide's four compounds (never on a test)
 * Output: templates/worksheet/assets/chem_u05_test_v1/.
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");

const W = 2.25, H = 1.3;
const pres = new pptxgen();
pres.defineLayout({ name: "TV", width: W, height: H });
pres.layout = "TV";
const { lewis, at, MOL } = require("./molecules")(pres);
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_test_v1");

const outer3 = (id, d) => [[id, d], [id, d + 90], [id, d - 90]];
const cross = (c, o, full) => {
  const pairs = [];
  if (full) ["A", "B", "D", "E"].forEach((id, i) => { if (o[i] !== "H") pairs.push(...outer3(id, [-90, 0, 90, 180][i])); });
  return { atoms: { C: [c, 0, 0], A: [o[0], 0, -1], B: [o[1], 1, 0], D: [o[2], 0, 1], E: [o[3], -1, 0] },
           bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], pairs };
};
const pyramid = (c, x) => ({ atoms: { P: [c, 0, 0], A: [x, ...at(155)], B: [x, ...at(90)], D: [x, ...at(25)] },
  bonds: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1]], pairs: [["P", -90], ...outer3("A", 155), ...outer3("B", 90), ...outer3("D", 25)] });
const bent = (c, x) => ({ atoms: { O: [c, 0, 0], A: [x, ...at(142.25)], B: [x, ...at(37.75)] },
  bonds: [["O", "A", 1], ["O", "B", 1]], pairs: [["O", -135], ["O", -45], ...outer3("A", 142.25), ...outer3("B", 37.75)] });
const linear3 = (a, c, b, order, pa, pb) => ({ atoms: { L: [a, -1, 0], C: [c, 0, 0], R: [b, 1, 0] },
  bonds: [["L", "C", order], ["C", "R", order]], pairs: [...pa.map((g) => ["L", g]), ...pb.map((g) => ["R", g])] });

const PICS = {
  sort_H2O:   { mol: MOL.H2O, u: 0.55, fs: 18, dy: -0.1 },
  sort_NH3:   { mol: MOL.NH3, u: 0.5, fs: 18, dy: -0.12 },
  sort_CH3Cl: { mol: (() => { const m = cross("C", ["H", "Cl", "H", "H"], true); return m; })(), u: 0.42, fs: 16 },
  sort_HF:    { mol: { atoms: { H: ["H", -0.5, 0], F: ["F", 0.5, 0] }, bonds: [["H", "F", 1]], pairs: outer3("F", 0) }, u: 0.7, fs: 18 },
  sort_CH4:   { mol: cross("C", ["H", "H", "H", "H"]), u: 0.45, fs: 18 },
  sort_N2:    { mol: { atoms: { A: ["N", -0.5, 0], B: ["N", 0.5, 0] }, bonds: [["A", "B", 3]], pairs: [["A", 180], ["B", 0]] }, u: 0.75, fs: 18 },
  sort_BeCl2: { mol: linear3("Cl", "Be", "Cl", 1, [180, -90, 90], [0, -90, 90]), u: 0.62, fs: 16 },
  sort_SiH4:  { mol: cross("Si", ["H", "H", "H", "H"]), u: 0.45, fs: 18 },
  test_PBr3:  { mol: pyramid("P", "Br"), u: 0.5, fs: 16, dy: -0.12 },
  test_CS2:   { mol: linear3("S", "C", "S", 2, [135, 225], [45, -45]), u: 0.62, fs: 18 },
  test_SiCl4: { mol: cross("Si", ["Cl", "Cl", "Cl", "Cl"], true), u: 0.42, fs: 15 },
  test_COF2:  { mol: { atoms: { C: ["C", 0, 0], O: ["O", 0, -1], A: ["F", ...at(150)], B: ["F", ...at(30)] },
                       bonds: [["C", "O", 2], ["C", "A", 1], ["C", "B", 1]],
                       pairs: [["O", -135], ["O", -45], ...outer3("A", 150), ...outer3("B", 30)] }, u: 0.46, fs: 16, dy: 0.12 },
  guide_OF2:  { mol: bent("O", "F"), u: 0.6, fs: 18, dy: -0.12 },
  guide_CO2:  { mol: MOL.CO2, u: 0.62, fs: 18 },
  guide_CF4:  { mol: cross("C", ["F", "F", "F", "F"], true), u: 0.42, fs: 15 },
  guide_CH2O: { mol: MOL.CH2O, u: 0.5, fs: 18, dy: 0.12 },
  /* written test, versions B and C */
  test_SiBr4: { mol: cross("Si", ["Br", "Br", "Br", "Br"], true), u: 0.42, fs: 15 },
  test_NF3:   { mol: pyramid("N", "F"), u: 0.5, fs: 16, dy: -0.12 },
  test_CSe2:  { mol: linear3("Se", "C", "Se", 2, [135, 225], [45, -45]), u: 0.62, fs: 17 },
  test_COCl2: { mol: { atoms: { C: ["C", 0, 0], O: ["O", 0, -1], A: ["Cl", ...at(150)], B: ["Cl", ...at(30)] },
                       bonds: [["C", "O", 2], ["C", "A", 1], ["C", "B", 1]],
                       pairs: [["O", -135], ["O", -45], ...outer3("A", 150), ...outer3("B", 30)] }, u: 0.46, fs: 16, dy: 0.12 },
  test_GeCl4: { mol: cross("Ge", ["Cl", "Cl", "Cl", "Cl"], true), u: 0.42, fs: 15 },
  test_PI3:   { mol: pyramid("P", "I"), u: 0.5, fs: 16, dy: -0.12 },
  test_OCS:   { mol: linear3("O", "C", "S", 2, [135, 225], [45, -45]), u: 0.62, fs: 18 },
  test_CSCl2: { mol: { atoms: { C: ["C", 0, 0], S: ["S", 0, -1], A: ["Cl", ...at(150)], B: ["Cl", ...at(30)] },
                       bonds: [["C", "S", 2], ["C", "A", 1], ["C", "B", 1]],
                       pairs: [["S", -135], ["S", -45], ...outer3("A", 150), ...outer3("B", 30)] }, u: 0.46, fs: 16, dy: 0.12 },
  /* written test challenge row: lone pair on the center AND a double bond */
  test_SeO2:  { mol: { atoms: { X: ["Se", 0, 0], A: ["O", ...at(150)], B: ["O", ...at(30)] },
                       bonds: [["X", "A", 2], ["X", "B", 1]], pairs: [["X", -90], ["A", 210], ["A", 90], ...outer3("B", 30)] }, u: 0.62, fs: 17, dy: -0.05 },
  test_SO2:   { mol: { atoms: { X: ["S", 0, 0], A: ["O", ...at(150)], B: ["O", ...at(30)] },
                       bonds: [["X", "A", 2], ["X", "B", 1]], pairs: [["X", -90], ["A", 210], ["A", 90], ...outer3("B", 30)] }, u: 0.62, fs: 17, dy: -0.05 },
  test_TeO2:  { mol: { atoms: { X: ["Te", 0, 0], A: ["O", ...at(150)], B: ["O", ...at(30)] },
                       bonds: [["X", "A", 2], ["X", "B", 1]], pairs: [["X", -90], ["A", 210], ["A", 90], ...outer3("B", 30)] }, u: 0.62, fs: 17, dy: -0.05 },
  test_NOF:   { mol: { atoms: { X: ["N", 0, 0], A: ["O", ...at(150)], B: ["F", ...at(30)] },
                       bonds: [["X", "A", 2], ["X", "B", 1]], pairs: [["X", -90], ["A", 210], ["A", 90], ...outer3("B", 30)] }, u: 0.62, fs: 17, dy: -0.05 },
  /* study-guide symmetry check: shape given, students decide polar or nonpolar */
  sym_CCl4:  { mol: cross("C", ["Cl", "Cl", "Cl", "Cl"], true), u: 0.42, fs: 15 },
  sym_BBr3:  { mol: { atoms: { B: ["B", 0, 0], A: ["Br", ...at(-90)], C: ["Br", ...at(150)], D: ["Br", ...at(30)] },
                      bonds: [["B", "A", 1], ["B", "C", 1], ["B", "D", 1]], pairs: [...outer3("A", -90), ...outer3("C", 150), ...outer3("D", 30)] }, u: 0.45, fs: 15, dy: 0.1 },
  sym_C2H2:  { mol: { atoms: { H1: ["H", -1.5, 0], C1: ["C", -0.5, 0], C2: ["C", 0.5, 0], H2: ["H", 1.5, 0] }, bonds: [["H1", "C1", 1], ["C1", "C2", 3], ["C2", "H2", 1]], pairs: [] }, u: 0.5, fs: 18 },
  sym_PCl3:  { mol: pyramid("P", "Cl"), u: 0.5, fs: 16, dy: -0.12 },
  sym_CHCl3: { mol: cross("C", ["H", "Cl", "Cl", "Cl"], true), u: 0.42, fs: 15 },
  sym_NOCl:  { mol: { atoms: { N: ["N", 0, 0], A: ["O", ...at(142.25)], B: ["Cl", ...at(37.75)] },
                      bonds: [["N", "A", 2], ["N", "B", 1]], pairs: [["N", -90], ["A", 142.25 + 55], ["A", 142.25 - 55], ...outer3("B", 37.75)] }, u: 0.6, fs: 16, dy: -0.1 },
};
const names = [];
for (const [n, m] of Object.entries(PICS)) {
  const s = pres.addSlide(); s.background = { color: "FFFFFF" };
  lewis(s, m.mol, W / 2 + (m.dx || 0), H / 2 + (m.dy || 0), m.u, { fs: m.fs });
  names.push(n);
}
fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "tv-"));
const pptx = path.join(tmp, "tv.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "tv.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} pictures`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `${names[i]}.png`)));
  console.log(`wrote ${names.length} pictures to ${OUT}`);
});
