/* Drawn answers for the Unit 4-5 guided-notes key: one picture per work box.
 *
 *   cd templates/slide && node decks/chem_u04_u05/key_structures.js
 *
 * Drawn with molecules.js, the same code and molecule table as the slide deck, so the key
 * and the slides cannot show two different structures. Each picture is a 3.3 x 1.6 in slide,
 * rendered to PNG through LibreOffice into templates/notes/assets/chem_u04-u05_key/.
 * Hand-built structures are Matt's approved exception to SHULL-CHG-0042 for this unit.
 */
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");
const K = require("../../tokens.generated");

const pres = new pptxgen();
pres.defineLayout({ name: "KEY", width: 3.3, height: 1.6 });
pres.layout = "KEY";
const M = require("./molecules")(pres);
const { line, dot, oval, label, dipole, lewis, at, MOL, bondDipole, INK, DEEP } = M;
const W = 3.3, H = 1.6, FS = 20;
const OUT = path.join(__dirname, "..", "..", "..", "notes", "assets", "chem_u04-u05_key");

const NAMES = [];
function pic(name, draw) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  draw(s);
  NAMES.push(name);
}
const small = (s, t, x, y, w = 0.9, o = {}) => label(s, t, x, y, w, 0.24, Object.assign({ size: 11 }, o));
const delta = (s, t, x, y) => label(s, t, x, y, 0.36, 0.24, { size: 12 });

/* 4 · ionic: Na gives its one electron to Cl */
pic("s04_ionic", (s) => {
  const y = 0.85;
  lewis(s, { atoms: { Na: ["Na", 0, 0] }, bonds: [], pairs: [["Na", 0, 0, 1]] }, 0.38, y, 1, { fs: FS });
  lewis(s, { atoms: { Cl: ["Cl", 0, 0] }, bonds: [],
    pairs: [["Cl", -90], ["Cl", 90], ["Cl", 0], ["Cl", 180, 0, 1]] }, 1.08, y, 1, { fs: FS });
  line(s, 0.58, y - 0.22, 0.82, y - 0.22, { color: DEEP, width: 1.75, end: "triangle" });
  label(s, "→", 1.66, y, 0.3, 0.4, { size: 20 });
  label(s, "Na", 1.98, y, 0.5, 0.4, { size: FS });
  small(s, "+", 2.23, y - 0.2, 0.2);
  label(s, "[", 2.4, y, 0.2, 0.6, { size: 30, bold: false });
  lewis(s, { atoms: { Cl: ["Cl", 0, 0] }, bonds: [],
    pairs: [["Cl", -90], ["Cl", 90], ["Cl", 0], ["Cl", 180]] }, 2.73, y, 1, { fs: FS });
  label(s, "]", 3.06, y, 0.2, 0.6, { size: 30, bold: false });
  small(s, "−", 3.18, y - 0.28, 0.2);
  small(s, "electron transfer", 0.78, 1.38, 1.3);
  small(s, "ions attract", 2.5, 1.38, 1.1);
});

/* 5 · covalent: H2O as an electron-dot structure, shared pairs circled */
pic("s05_covalent", (s) => {
  const O = [1.65, 0.62], u = 0.72, k = FS / 32;
  lewis(s, { atoms: { O: ["O", 0, 0], H1: ["H", ...at(142.25)], H2: ["H", ...at(37.75)] }, bonds: [],
    pairs: [["O", -135], ["O", -45]] }, O[0], O[1], u, { fs: FS });
  for (const d of [142.25, 37.75]) {
    const [mx, my] = [O[0] + at(d, u * 0.5)[0], O[1] + at(d, u * 0.5)[1]], a = d * Math.PI / 180;
    for (const sg of [-1, 1]) dot(s, mx - Math.sin(a) * 0.068 * k * sg, my + Math.cos(a) * 0.068 * k * sg, 0.085 * k, INK);
    oval(s, mx, my, 0.3, 0.3, { line: DEEP, lineWidth: 1.25, dash: "dash" });
  }
  small(s, "shared pairs (circled): O has 8, each H has 2", W / 2, 1.42, 3.2);
});

/* 8 · H-H nonpolar, H-Cl polar with its dipole arrow */
pic("s08_dipole", (s) => {
  const y = 0.95;
  lewis(s, { atoms: { A: ["H", -0.5, 0], B: ["H", 0.5, 0] }, bonds: [["A", "B", 1]], pairs: [] }, 0.75, y, 0.7, { fs: FS });
  small(s, "no arrow", 0.75, 1.42);
  const P = lewis(s, MOL.HCl, 2.25, y, 0.85, { fs: FS });
  delta(s, "δ+", P("H")[0], y - 0.32); delta(s, "δ−", P("Cl")[0], y - 0.38);
  dipole(s, P("H")[0] - 0.05, 0.3, P("Cl")[0] + 0.1, 0.3, DEEP, 0, 2);
});

/* 13-16 · Lewis structures */
pic("s13_bf3", (s) => lewis(s, MOL.BF3, W / 2, 0.95, 0.56, { fs: FS }));
pic("s14_co2", (s) => lewis(s, MOL.CO2, W / 2, H / 2, 0.95, { fs: FS }));
pic("s15_nh3", (s) => lewis(s, MOL.NH3, W / 2, 0.68, 0.62, { fs: FS }));
pic("s16_ch2o", (s) => lewis(s, MOL.CH2O, W / 2, 0.95, 0.56, { fs: FS }));

/* 21 · HCl polar; CO2 dipoles cancel */
pic("s21_hcl_co2", (s) => {
  const y = 0.85;
  const P = lewis(s, MOL.HCl, 0.7, y, 0.75, { fs: FS });
  dipole(s, P("H")[0] - 0.05, y - 0.42, P("Cl")[0] + 0.08, y - 0.42, DEEP, 0, 2);
  small(s, "polar", 0.7, 1.42);
  const Q = lewis(s, MOL.CO2, 2.4, y, 0.55, { fs: FS });
  const cx = Q("C")[0];
  dipole(s, cx - 0.06, y - 0.42, Q("O1")[0] + 0.04, y - 0.42, DEEP, 0, 2);
  dipole(s, cx + 0.06, y - 0.42, Q("O2")[0] - 0.04, y - 0.42, DEEP, 0, 2);
  small(s, "cancel: nonpolar", 2.4, 1.42, 1.3);
});

/* 22 · BF3 cancels; NH3 does not */
pic("s22_bf3_nh3", (s) => {
  const bf3 = { atoms: MOL.BF3.atoms, bonds: MOL.BF3.bonds, pairs: [] };
  const P = lewis(s, bf3, 0.8, 0.78, 0.5, { fs: FS });
  for (const f of ["F1", "F2", "F3"]) bondDipole(s, P, "B", f, 1, DEEP, 0, 0.12, 0.25, 0.7);
  small(s, "cancel: nonpolar", 0.8, 1.45, 1.3);
  const Q = lewis(s, MOL.NH3, 2.25, 0.62, 0.55, { fs: FS });
  for (const h of ["H1", "H2", "H3"]) bondDipole(s, Q, h, "N", h === "H1" ? -1 : 1, DEEP, 0, 0.12, 0.25, 0.7);
  dipole(s, 3.05, 1.15, 3.05, 0.35, DEEP, 0, 2.5);
  small(s, "net pull: polar", 2.3, 1.45, 1.2);
});

/* 23 · H2O */
pic("s23_h2o", (s) => {
  const P = lewis(s, MOL.H2O, 1.4, 0.6, 0.72, { fs: FS });
  bondDipole(s, P, "H1", "O", -1, DEEP, 0, 0.14);
  bondDipole(s, P, "H2", "O", 1, DEEP, 0, 0.14);
  delta(s, "δ−", P("O")[0] + 0.42, P("O")[1] - 0.3);
  delta(s, "δ+", P("H1")[0], P("H1")[1] + 0.25); delta(s, "δ+", P("H2")[0], P("H2")[1] + 0.25);
  dipole(s, 2.75, 1.25, 2.75, 0.3, DEEP, 0, 2.5);
  small(s, "net", 2.98, 0.78, 0.4);
});

/* 24 · NH3 */
pic("s24_nh3", (s) => {
  const P = lewis(s, MOL.NH3, 1.4, 0.6, 0.62, { fs: FS });
  for (const h of ["H1", "H2", "H3"]) bondDipole(s, P, h, "N", h === "H1" ? -1 : 1, DEEP, 0, 0.13);
  dipole(s, 2.6, 1.3, 2.6, 0.3, DEEP, 0, 2.5);
  small(s, "net", 2.83, 0.8, 0.4);
});

/* 25 · CCl4, tetrahedral with wedges; four equal pulls cancel */
const tetra = (X) => ({
  atoms: { C: ["C", 0, 0], A: [X[0], ...at(-90)], B: [X[1], ...at(195)], D: [X[2], ...at(20)], E: [X[3], ...at(110)] },
  bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", "wedge"], ["C", "E", "dash"]], pairs: [],
});
pic("s25_ccl4", (s) => {
  const m = tetra(["Cl", "Cl", "Cl", "Cl"]);
  m.pairs = [["A", -90], ["A", 0], ["A", 180], ["B", 195], ["B", 105], ["B", 285],
             ["D", 20], ["D", -70], ["D", 110], ["E", 110], ["E", 20], ["E", 200]];
  const P = lewis(s, m, 1.3, 0.76, 0.52, { fs: 18 });
  for (const x of ["A", "B", "D", "E"]) bondDipole(s, P, "C", x, 1, DEEP, 0, 0.13, 0.3, 0.66);
  small(s, "pulls cancel", 2.75, 0.7, 1.0); small(s, "net = 0", 2.75, 0.95, 1.0);
});

/* 26 · CCl4 cancels; CH3Cl has a net pull toward Cl */
pic("s26_ccl4_ch3cl", (s) => {
  const P = lewis(s, tetra(["Cl", "Cl", "Cl", "Cl"]), 0.8, 0.7, 0.5, { fs: 18 });
  for (const x of ["A", "B", "D", "E"]) bondDipole(s, P, "C", x, 1, DEEP, 0, 0.12, 0.3, 0.68);
  small(s, "net = 0", 0.75, 1.45);
  const Q = lewis(s, tetra(["Cl", "H", "H", "H"]), 2.3, 0.7, 0.5, { fs: 18 });
  bondDipole(s, Q, "C", "A", 1, DEEP, 0, 0.1, 0.28, 0.7);
  dipole(s, 3.05, 1.15, 3.05, 0.3, DEEP, 0, 2.5);
  small(s, "net pull to Cl", 2.4, 1.45, 1.2);
});

fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(require("os").tmpdir(), "keystruct-"));
const pptx = path.join(tmp, "key_structures.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "key_structures.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== NAMES.length) throw new Error(`rendered ${pages.length} pages for ${NAMES.length} pictures`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, NAMES[i] + ".png")));
  console.log(`wrote ${NAMES.length} key pictures to ${OUT}`);
});
