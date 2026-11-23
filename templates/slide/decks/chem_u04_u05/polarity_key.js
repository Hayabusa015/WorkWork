/* Shape drawings with dipole arrows for the key of the 5.4 "Molecular Polarity" practice set:
 * one picture per row.
 *
 *   cd templates/slide && node decks/chem_u04_u05/polarity_key.js
 *
 * Drawn the way slides 24-30 draw them, with the same molecules.js code: the structure with
 * outer-atom lone pairs left off so the arrows can be seen, central-atom lone pairs kept, a
 * dipole arrow beside each POLAR bond pointing at the delta-minus atom (cross at the delta-plus
 * end, slide 10), then a long net arrow for a polar molecule or "net = 0" for a nonpolar one.
 * Nonpolar bonds (C-H, 0.35) get no arrow. Each picture is a 2.0 x 1.25 in slide rendered to
 * PNG into templates/worksheet/assets/chem_u05_s05.4_polarity/.
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");
const K = require("../../tokens.generated");

const W = 2.0, H = 1.25;
const pres = new pptxgen();
pres.defineLayout({ name: "PK", width: W, height: H });
pres.layout = "PK";
const ARROW = K.courses.chemistry.primaryDeep;
const { lewis, at, dipole, line, label } = require("./molecules")(pres);
/* A small bond dipole for a 2-inch picture. molecules.js puts the cross a fixed 0.13 in from the
   tail, which on a bond this short lands on the arrowhead; here it sits a third of the way along. */
function smallDipole(s, P, from, to, side, off = 0.1, f0 = 0.18, f1 = 0.86) {
  const [x1, y1] = P(from), [x2, y2] = P(to);
  const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, nx = -uy * side, ny = ux * side;
  const ax = x1 + ux * L * f0 + nx * off, ay = y1 + uy * L * f0 + ny * off;
  const bx = x1 + ux * L * f1 + nx * off, by = y1 + uy * L * f1 + ny * off;
  line(s, ax, ay, bx, by, { color: ARROW, width: 1.5, end: "triangle" });
  const t = Math.hypot(bx - ax, by - ay) * 0.28, cx = ax + ux * t, cy = ay + uy * t, h = 0.045;
  line(s, cx - uy * h, cy + ux * h, cx + uy * h, cy - ux * h, { color: ARROW, width: 1.5 });
}
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_s05.4_polarity");

const cross = (C, outer) => ({ atoms: { [C[0]]: [C[1], 0, 0], A: [outer[0], 0, -1], B: [outer[1], 1, 0], D: [outer[2], 0, 1], E: [outer[3], -1, 0] },
  bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], pairs: [] });

/* Each entry: mol, scale u, centre offset, the polar bonds as [from(δ+), to(δ−), side],
   and net: null (nonpolar) or [x1, y1, x2, y2] in inches relative to the picture centre. */
const MOLS = {
  CO2: { mol: { atoms: { O1: ["O", -1, 0], C: ["C", 0, 0], O2: ["O", 1, 0] }, bonds: [["O1", "C", 2], ["C", "O2", 2]], pairs: [] },
         u: 0.66, dy: -0.08, below: true, dip: [["C", "O1", 1], ["C", "O2", -1]], net: null },
  H2O: { mol: { atoms: { O: ["O", 0, 0], H1: ["H", ...at(142.25)], H2: ["H", ...at(37.75)] },
                bonds: [["O", "H1", 1], ["O", "H2", 1]], pairs: [["O", -135], ["O", -45]] },
         u: 0.56, dx: -0.2, dy: -0.12, dip: [["H1", "O", -1], ["H2", "O", 1]], net: [0.68, 0.38, 0.68, -0.38] },
  CH4: { mol: cross(["C", "C"], ["H", "H", "H", "H"]), u: 0.44, dx: -0.2, dip: [], net: null },
  NH3: { mol: { atoms: { N: ["N", 0, 0], H1: ["H", ...at(155)], H2: ["H", ...at(90)], H3: ["H", ...at(25)] },
                bonds: [["N", "H1", 1], ["N", "H2", 1], ["N", "H3", 1]], pairs: [["N", -90]] },
         u: 0.52, dx: -0.2, dy: -0.1, dip: [["H1", "N", -1], ["H2", "N", 1], ["H3", "N", 1]], net: [0.7, 0.42, 0.7, -0.38] },
  CCl4: { mol: cross(["C", "C"], ["Cl", "Cl", "Cl", "Cl"]), u: 0.44, dx: -0.2, dip: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], net: null },
  CHCl3: { mol: cross(["C", "C"], ["H", "Cl", "Cl", "Cl"]), u: 0.44, dx: -0.2, dip: [["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], net: [0.68, -0.38, 0.68, 0.4] },
  BCl3: { mol: { atoms: { B: ["B", 0, 0], A: ["Cl", ...at(-90)], C: ["Cl", ...at(150)], D: ["Cl", ...at(30)] },
                 bonds: [["B", "A", 1], ["B", "C", 1], ["B", "D", 1]], pairs: [] },
          u: 0.5, dx: -0.2, dy: 0.1, dip: [["B", "A", 1], ["B", "C", 1], ["B", "D", 1]], net: null },
  SO2: { mol: { atoms: { S: ["S", 0, 0], A: ["O", ...at(155)], B: ["O", ...at(25)] }, bonds: [["S", "A", 2], ["S", "B", 1]], pairs: [["S", -90]] },
         u: 0.6, dx: -0.2, dy: -0.12, dip: [["S", "A", 1], ["S", "B", -1]], net: [0.7, -0.38, 0.7, 0.4] },
  PCl5: { mol: { atoms: { P: ["P", 0, 0], A: ["Cl", 0, -1.1], B: ["Cl", 0, 1.1], D: ["Cl", -1.2, 0], E: ["Cl", ...at(-28, 1.35)], F: ["Cl", ...at(28, 1.35)] },
                 bonds: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1], ["P", "E", 1], ["P", "F", 1]], pairs: [] },
          u: 0.4, dx: -0.22, dip: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1], ["P", "E", 1], ["P", "F", 1]], net: null },
  PCl3: { mol: { atoms: { P: ["P", 0, 0], A: ["Cl", ...at(155)], B: ["Cl", ...at(90)], D: ["Cl", ...at(25)] },
                 bonds: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1]], pairs: [["P", -90]] },
          u: 0.52, dx: -0.2, dy: -0.1, dip: [["P", "A", 1], ["P", "B", 1], ["P", "D", -1]], net: [0.7, -0.38, 0.7, 0.42] },
  HCN: { mol: { atoms: { H: ["H", -1, 0], C: ["C", 0, 0], N: ["N", 1, 0] }, bonds: [["H", "C", 1], ["C", "N", 3]], pairs: [] },
         u: 0.66, dy: -0.15, dip: [["C", "N", -1]], net: [-0.5, 0.38, 0.5, 0.38] },
};

const names = [];
for (const [name, m] of Object.entries(MOLS)) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  const cx = W / 2 + (m.dx || 0), cy = H / 2 + (m.dy || 0);
  const P = lewis(s, m.mol, cx, cy, m.u, { fs: 13 });
  for (const [a, b, side] of m.dip) smallDipole(s, P, a, b, side);
  if (m.net) {
    const [x1, y1, x2, y2] = m.net;
    dipole(s, W / 2 + x1, H / 2 + y1, W / 2 + x2, H / 2 + y2, ARROW, 0, 3.25);
  } else {
    if (m.below) label(s, "net = 0", W / 2, H - 0.16, 1.2, 0.2, { size: 10, color: ARROW });
    else label(s, "net\n= 0", W / 2 + 0.7, H / 2, 0.5, 0.4, { size: 10, color: ARROW });
  }
  names.push(name);
}
fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "pk-"));
const pptx = path.join(tmp, "pk.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "pk.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} drawings`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `polar_${names[i]}.png`)));
  console.log(`wrote ${names.length} drawings to ${OUT}`);
});
