/* Lewis structures for the key of the 5.3 "VSEPR Structures" practice set: one picture per row.
 *
 *   cd templates/slide && node decks/chem_u04_u05/vsepr_lewis_key.js
 *
 * Drawn with molecules.js, the same code and molecule table as the U4-U5 deck and guided-notes
 * key, so a molecule looks the same everywhere it appears. Each picture is a 2.25 x 1.3 in slide
 * rendered to PNG into templates/worksheet/assets/chem_u05_s05.3_vsepr/.
 */
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");
const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.defineLayout({ name: "VK", width: 2.25, height: 1.3 });
pres.layout = "VK";
const { lewis, at, MOL } = require("./molecules")(pres);
const OUT = path.join(__dirname, "..", "..", "..", "worksheet", "assets", "chem_u05_s05.3_vsepr");
const W = 2.25, H = 1.3;

/* Three lone pairs on an outer atom, pointing away from the central atom. */
const outer3 = (id, dir) => [[id, dir], [id, dir + 90], [id, dir - 90]];
/* Same, fanned tighter, for a crowded central atom (PCl5). */
const outerFan = (id, dir) => [[id, dir], [id, dir + 62], [id, dir - 62]];

const MOLS = {
  CH4: { mol: { atoms: { C: ["C", 0, 0], A: ["H", 0, -1], B: ["H", 1, 0], D: ["H", 0, 1], E: ["H", -1, 0] },
                bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]], pairs: [] }, u: 0.45, fs: 18 },
  NH3: { mol: MOL.NH3, u: 0.5, fs: 18, dy: -0.12 },
  H2O: { mol: MOL.H2O, u: 0.55, fs: 18, dy: -0.1 },
  HCN: { mol: { atoms: { H: ["H", -1, 0], C: ["C", 0, 0], N: ["N", 1, 0] },
                bonds: [["H", "C", 1], ["C", "N", 3]], pairs: [["N", 0]] }, u: 0.6, fs: 18 },
  PCl3: { mol: { atoms: { P: ["P", 0, 0], A: ["Cl", ...at(155)], B: ["Cl", ...at(90)], D: ["Cl", ...at(25)] },
                 bonds: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1]],
                 pairs: [["P", -90], ...outer3("A", 155), ...outer3("B", 90), ...outer3("D", 25)] }, u: 0.5, fs: 16, dy: -0.12 },
  OF2: { mol: { atoms: { O: ["O", 0, 0], A: ["F", ...at(142.25)], B: ["F", ...at(37.75)] },
                bonds: [["O", "A", 1], ["O", "B", 1]],
                pairs: [["O", -135], ["O", -45], ...outer3("A", 142.25), ...outer3("B", 37.75)] }, u: 0.6, fs: 18, dy: -0.12 },
  SO2: { mol: { atoms: { S: ["S", 0, 0], A: ["O", ...at(155)], B: ["O", ...at(25)] },
                bonds: [["S", "A", 2], ["S", "B", 1]],
                pairs: [["S", -90], ["A", 155 + 60], ["A", 155 - 60], ...outer3("B", 25)] }, u: 0.62, fs: 18, dy: -0.05 },
  CHCl3: { mol: { atoms: { C: ["C", 0, 0], A: ["H", 0, -1], B: ["Cl", 1, 0], D: ["Cl", 0, 1], E: ["Cl", -1, 0] },
                  bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]],
                  pairs: [...outer3("B", 0), ...outer3("D", 90), ...outer3("E", 180)] }, u: 0.42, fs: 15 },
  CS2: { mol: { atoms: { S1: ["S", -1, 0], C: ["C", 0, 0], S2: ["S", 1, 0] },
                bonds: [["S1", "C", 2], ["C", "S2", 2]],
                pairs: [["S1", 135], ["S1", 225], ["S2", 45], ["S2", -45]] }, u: 0.62, fs: 18 },
  COCl2: { mol: { atoms: { C: ["C", 0, 0], O: ["O", 0, -1], A: ["Cl", ...at(150)], B: ["Cl", ...at(30)] },
                  bonds: [["C", "O", 2], ["C", "A", 1], ["C", "B", 1]],
                  pairs: [["O", -135], ["O", -45], ...outer3("A", 150), ...outer3("B", 30)] }, u: 0.46, fs: 16, dy: 0.12 },
  PCl5: { mol: { atoms: { P: ["P", 0, 0], A: ["Cl", 0, -1.1], B: ["Cl", 0, 1.1], D: ["Cl", -1.2, 0], E: ["Cl", ...at(-28, 1.35)], F: ["Cl", ...at(28, 1.35)] },
                 bonds: [["P", "A", 1], ["P", "B", 1], ["P", "D", 1], ["P", "E", 1], ["P", "F", 1]],
                 pairs: [...outerFan("A", -90), ...outerFan("B", 90), ...outer3("D", 180), ...outerFan("E", -28), ...outerFan("F", 28)] }, u: 0.34, fs: 13 },
};

const names = [];
for (const [name, m] of Object.entries(MOLS)) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  lewis(s, m.mol, W / 2 + (m.dx || 0), H / 2 + (m.dy || 0), m.u, { fs: m.fs });
  names.push(name);
}
fs.mkdirSync(OUT, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "vlk-"));
const pptx = path.join(tmp, "vk.pptx");
pres.writeFile({ fileName: pptx }).then(() => {
  execFileSync("soffice", ["--headless", "--convert-to", "pdf", "--outdir", tmp, pptx], { stdio: "ignore" });
  execFileSync("pdftoppm", ["-r", "300", "-png", path.join(tmp, "vk.pdf"), path.join(tmp, "p")]);
  const pages = fs.readdirSync(tmp).filter((f) => /^p-\d+\.png$/.test(f)).sort();
  if (pages.length !== names.length) throw new Error(`rendered ${pages.length} pages for ${names.length} structures`);
  pages.forEach((f, i) => fs.copyFileSync(path.join(tmp, f), path.join(OUT, `lewis_${names[i]}.png`)));
  console.log(`wrote ${names.length} structures to ${OUT}`);
});
