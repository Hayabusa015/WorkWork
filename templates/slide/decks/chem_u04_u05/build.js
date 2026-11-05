/* Chemistry U4 + U5 combined deck: Bonding, Molecular Structure & Intermolecular Forces.
 *
 *   cd templates/slide && node decks/chem_u04_u05/build.js [out.pptx]
 *   python3 ../../scripts/add_click_builds.py out.pptx      (run by this script)
 *
 * Why a deck script instead of a build_deck.js spec: this deck needs three things the spec
 * format cannot express. (1) Two units and nine sections in one file - Matt's instruction,
 * 2026-11-04. (2) Embedded video. (3) Lewis structures, dipoles and IMF figures built as
 * native shapes so they can reveal one click at a time - Matt approved hand-building these
 * as an exception to SHULL-CHG-0042 for this deck, same conversation. The masters still come
 * from build.js, so the deck cannot invent a colour or a layout: every placeholder below is
 * one the master declared, and every free-drawn figure sits inside a slot the master reserved.
 *
 * Click builds: any object whose objectName starts "c<N>_" appears (fade) on click N.
 * add_click_builds.py turns those names into PowerPoint timing XML after the file is written.
 *
 * Electronegativity: Pauling, two decimals. Bond-type cutoffs from OpenStax Chemistry 2e,
 * Fig. 7.8: under 0.40 nonpolar, 0.40-1.80 polar covalent, over 1.80 ionic.
 */
const fs = require("fs");
const path = require("path");
process.env.SHULL_COURSE = "chemistry";
const pres = require("../../build");
const K = require("../../tokens.generated");

const HERE = __dirname;
const OUT = process.argv[2] || path.join(HERE, "Unit 4-5 Slides.pptx");

/* Same check build_deck.js makes: every section code used here must exist in the decisions file. */
const DECISIONS = fs.readFileSync(path.join(HERE, "..", "..", "..", "..", "courses", "chemistry", "DECISIONS.md"), "utf8");
const USED = ["4.1", "4.2", "4.3", "4.5", "4.6", "5.1", "5.2", "5.4", "5.5"];
for (const c of USED) {
  if (!new RegExp(`(?<![\\d.])${c.replace(".", "\\.")}(?![\\d])`).test(DECISIONS.split("## Course sequencing rules")[0])) {
    console.error(`section ${c} is not in courses/chemistry/DECISIONS.md - stop and ask`); process.exit(1);
  }
}

const G = K.ground, CO = K.courses.chemistry, F = K.fonts;
const INK = G.asphalt, PAPER = G.parchment, DEEP = CO.primaryDeep, ORANGE = CO.primary, CYAN = CO.secondary;
pres.title = "Unit 4-5 Slides - Bonding, Molecular Structure & IMFs";

const { rich, line, dot, oval, rect, label, dipole, lewis, at, MOL, bondDipole, water, hbond } = require("./molecules")(pres);
/* ----------------------------------------------------------------- slide furniture */
const SLOT = pres.SLOTS;
const PH_BUILDS = [];
/* Hide a master image slot's dashed frame under a solid panel; 0.02in of bleed covers the dash. */
const cover = (s, master, slot, color) => { const r = SLOT[master][slot]; rect(s, r.x - 0.02, r.y - 0.02, r.w + 0.04, r.h + 0.04, color); return r; };

function slide(master, fields, o = {}) {
  const s = pres.addSlide({ masterName: master });
  const declared = pres.PLACEHOLDERS[master];
  const f = Object.assign({}, fields);
  if (declared.includes("eyebrow") && !("eyebrow" in f)) f.eyebrow = `UNIT 0${o.unit || 4}  •  CHEMISTRY`;
  if (declared.includes("code") && !("code" in f)) f.code = o.code;
  for (const [ph, txt] of Object.entries(f)) {
    if (txt == null) continue;
    if (!declared.includes(ph)) throw new Error(`${master}: no placeholder ${ph}`);
    s.addText(rich(txt), { placeholder: ph });
    const click = (o.clicks || {})[ph];
    if (click) {   // pptxgenjs drops objectName on placeholders, so builds are keyed by placeholder idx
      const lay = pres._slideLayouts.find((l) => l._name === master);
      const idx = lay._slideObjects.find((x) => x._type === "placeholder" && x.options.placeholder === ph).options._placeholderIdx;
      PH_BUILDS.push({ slide: pres.slides.length, idx, click });
    }
  }
  if (o.notes) s.addNotes(o.notes);
  return s;
}
/* The divider's image slot runs under its floating card; cover around the card, not over it. */
function dividerCover(s) {
  rect(s, 4.30, 0, 0.38, 1.6, INK); rect(s, 4.30, 5.66, 0.38, K.geom.H - 5.66, INK);
  rect(s, 4.68, 0, K.geom.W - 4.68, K.geom.H, INK);
}
const code = (u, sec) => sec ? `U0${u} • S0${sec}` : `U0${u}`;
function video(s, file, master = "03_GROUPED_CONCEPT", slot = "concept") {
  const r = SLOT[master][slot];
  const poster = fs.readFileSync(path.join(HERE, file.replace(".mp4", "_poster.png"))).toString("base64");
  s.addMedia({ type: "video", path: path.join(HERE, file), x: r.x, y: r.y, w: r.w, h: r.h,
    cover: "data:image/png;base64," + poster, objectName: "Video" });
}

/* Mini electronegativity bar for the small aside slots. Numbers only: the words live on the slide. */
function miniScale(s, master) {
  const r = cover(s, master, "aside", PAPER);
  const y = r.y + r.h * 0.62, x0 = r.x + 0.18, x1 = r.x + r.w - 0.18, a = x0 + (x1 - x0) * 0.22, b = x0 + (x1 - x0) * 0.62;
  rect(s, x0, y - 0.09, a - x0, 0.18, G.ruleHairline);
  rect(s, a, y - 0.09, b - a, 0.18, CYAN);
  rect(s, b, y - 0.09, x1 - b, 0.18, ORANGE);
  label(s, "0.40", a, r.y + 0.38, 0.7, 0.3, { size: 16 });
  label(s, "1.80", b, r.y + 0.38, 0.7, 0.3, { size: 16 });
  line(s, a, r.y + 0.56, a, y + 0.12, { width: 1.5 }); line(s, b, r.y + 0.56, b, y + 0.12, { width: 1.5 });
  label(s, "ΔEN →", r.x + r.w / 2, r.y + r.h - 0.22, 1.2, 0.26, { size: 16, bold: false });
}

/* Water molecule for networks: O at (x, y); the H atoms point along `dir`. Returns atom positions. */
function network(s, cx, cy, u, fs_, color, hcolor) {
  /* Centre molecule donates both H atoms and accepts at both lone pairs: the tetrahedral
     hydrogen-bond pattern of liquid water and ice, flattened to 2D. */
  const O = [cx, cy - 0.15 * u];
  const W1 = water(s, O[0], O[1], 90, u, { fs: fs_, color });
  const along = (p, deg, r) => [p[0] + at(deg, r)[0], p[1] + at(deg, r)[1]];
  const W2 = water(s, ...along(O, 142.25, 2.6 * u), 142.25, u, { fs: fs_, color });
  const W3 = water(s, ...along(O, 37.75, 2.6 * u), 37.75, u, { fs: fs_, color });
  const W4 = water(s, ...along(O, -35, 2.55 * u), 145 - 52.25, u, { fs: fs_, color });
  const W5 = water(s, ...along(O, -145, 2.55 * u), 35 + 52.25, u, { fs: fs_, color });
  hbond(s, W1.H1, W2.O, hcolor); hbond(s, W1.H2, W3.O, hcolor);
  hbond(s, W4.H1, W1.O, hcolor); hbond(s, W5.H2, W1.O, hcolor);
  return { W1, W2, W3, W4, W5 };
}

/* ================================================================== THE DECK */

/* 1 — Unit title */
{
  const s = slide("01_UNIT_TITLE", {
    headline: "Bonding &\nMolecular\nStructure",
    subhead: "Units 4 and 5: how atoms bond, what shape molecules take, and what holds them together.",
    eyebrow: "UNITS 04 – 05  •  CHEMISTRY", code: "U04 – U05",
  }, { notes: "Units 4 and 5 run as one deck. Dark dividers mark each unit; every slide footer carries its real section code, so you can stop at any divider when the bell rings." });
  const r = cover(s, "01_UNIT_TITLE", "hero", INK);
  network(s, r.x + r.w / 2, r.y + r.h / 2 + 0.05, 0.66, 26, PAPER, ORANGE);
}

/* 2 — What we're covering */
{
  const s = slide("07_COMPARISON_CARDS", {
    headline: "What We're Covering",
    subhead: "Two units, one deck. The dark dividers mark where each one starts.",
    k1_l: "UNIT 4 • BONDING", k1_b: "Why atoms bond\nIonic vs. covalent\nBond polarity (ΔEN)",
    k2_l: "UNIT 5 • STRUCTURE", k2_b: "Lewis structures\nVSEPR\nMolecular polarity",
    k3_l: "UNIT 5 • FORCES", k3_b: "Intermolecular forces\nHydrogen bonding\nDipole–dipole, LDF",
    mustwrite: "Every property in these units comes back to where the electrons are.",
  }, { code: "U04 – U05", eyebrow: "UNITS 04 – 05  •  CHEMISTRY" });
  const r = cover(s, "07_COMPARISON_CARDS", "aside", PAPER);
  lewis(s, MOL.H2O, r.x + r.w / 2, r.y + r.h / 2 - 0.12, 0.62, { fs: 24 });
}

/* 3 — Unit 4 divider */
{
  const s = slide("04_DIVIDER", { eyebrow: "UNIT 04", headline: "Chemical\nBonding",
    subhead: "Why atoms bond, and which kind of bond they make." }, { code: code(4) });
  dividerCover(s);
  // Sodium chloride lattice: alternating ions, as in the crystal.
  for (let i = 0; i < 6; i++) for (let j = 0; j < 5; j++) {
    const x = 5.35 + i * 1.3, y = 1.05 + j * 1.3, na = (i + j) % 2 === 0;
    if (na) { oval(s, x, y, 0.62, 0.62, { fill: ORANGE }); label(s, "Na⁺", x, y, 0.8, 0.4, { size: 16, color: INK }); }
    else { oval(s, x, y, 0.92, 0.92, { fill: G.graphite, line: CYAN, lineWidth: 2 }); label(s, "Cl⁻", x, y, 0.8, 0.4, { size: 18, color: PAPER }); }
  }
}

/* 4 — 4.1 Why atoms bond */
{
  const s = slide("07_COMPARISON_CARDS", {
    headline: "Why Atoms Bond",
    subhead: "Atoms bond to reach the stable setup that noble gases already have.",
    k1_l: "STABILITY", k1_b: "Noble gases have a full outer shell. They rarely bond.",
    k2_l: "OCTET RULE", k2_b: "Most atoms are stable with 8 valence electrons. H needs only 2.",
    k3_l: "LOWER ENERGY", k3_b: "Bonded atoms have less energy than the same atoms apart.",
    mustwrite: "Atoms bond to get a full valence shell, which lowers their energy.",
  }, { code: code(4, "4.1"), notes: "4.1 Why Atoms Bond. The neon figure is the target every other atom is chasing: 8 valence electrons. Helium is the exception at 2, which is why H stops at 2." });
  const r = cover(s, "07_COMPARISON_CARDS", "aside", PAPER);
  lewis(s, { atoms: { Ne: ["Ne", 0, 0] }, bonds: [], pairs: [["Ne", 0], ["Ne", 90], ["Ne", 180], ["Ne", -90]] },
    r.x + 0.85, r.y + r.h / 2, 1, { fs: 30 });
  label(s, "Ne\nfull shell", r.x + 2.05, r.y + r.h / 2, 1.3, 0.7, { size: 16 });
}

/* 5 — 4.2 Ionic bonding (video) */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Ionic Bonding: Electrons Transfer",
    subhead: "A metal gives up electrons and a nonmetal takes them. The ions that form attract.",
    c1_l: "WHAT IT IS", c1_b: "Metal + nonmetal\nElectrons transferred\nForms a crystal lattice\nSolid at room temp",
    c2_l: "PROPERTIES", c2_b: "High melting points\nHard, brittle crystals\nConduct when melted\nor dissolved",
    mustwrite: "An ionic bond is the attraction between oppositely charged ions.",
  }, { code: code(4, "4.2"), notes: "Click the video to play it (16 s, five steps: Na 2,8,1 and Cl 2,8,7 → electron transfer → Na⁺ and Cl⁻). Conductivity: the ions can only carry charge when they are free to move, so solid NaCl does not conduct but molten or dissolved NaCl does." });
  video(s, "chem_u04_s4.2_ionic_bonding_dark.mp4");
}

/* 6 — 4.3 Covalent bonding (video) */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Covalent Bonding: Electrons Are Shared",
    subhead: "Two nonmetals both need electrons, so they share pairs instead of trading them.",
    c1_l: "WHAT IT IS", c1_b: "Nonmetal + nonmetal\nElectrons shared in pairs\nForms molecules",
    c2_l: "PROPERTIES", c2_b: "Low melting points\nOften gases or liquids\nSoft if solid\nUsually don't conduct",
    mustwrite: "A covalent bond is a pair of electrons shared between two atoms.",
  }, { code: code(4, "4.3"), notes: "Click the video to play it (15 s, six steps building H₂O: O has 6 valence e⁻, each H has 1 → shared pairs → every shell full: O 8, H 2)." });
  video(s, "chem_u04_s4.3_covalent_bonding_dark.mp4");
}

/* 7 — 4.5 Electronegativity scale */
{
  const s = slide("05_PROCESS_TIMELINE", {
    headline: "Electronegativity Difference Sets the Bond Type",
    subhead: "Electronegativity (EN) is how hard an atom pulls on shared electrons. Use two decimals.",
    s1_l: "LOOK UP", s1_b: "Find both EN values.",
    s2_l: "SUBTRACT", s2_b: "Larger − smaller = ΔEN",
    s3_l: "COMPARE", s3_b: "Place ΔEN on the scale.",
    s4_l: "NAME IT", s4_b: "Nonpolar, polar, or ionic.",
  }, { code: code(4, "4.5"), notes: "Cutoffs: OpenStax Chemistry 2e, Fig. 7.8 (less than 0.40 nonpolar; 0.40–1.80 polar covalent; greater than 1.80 ionic). EN values are Pauling, two decimals: H 2.20, B 2.04, C 2.55, N 3.04, O 3.44, F 3.98, Na 0.93, Cl 3.16. The cutoffs are guidelines: bond character changes gradually, so a value right at a cutoff is a judgment call, not a trick question." });
  rect(s, 0.75, 2.62, 11.83, 2.20, INK);
  const x0 = 1.05, x1 = 12.28, a = 4.1, b = 8.7, y = 3.82;
  label(s, "NONPOLAR COVALENT", (x0 + a) / 2, 2.98, 3.0, 0.34, { size: 16, color: PAPER });
  label(s, "POLAR COVALENT", (a + b) / 2, 2.98, 3.0, 0.34, { size: 16, color: PAPER });
  label(s, "IONIC", (b + x1) / 2, 2.98, 3.0, 0.34, { size: 16, color: PAPER });
  line(s, x0, y, x1, y, { color: PAPER, width: 3.5, end: "triangle", begin: "triangle" });
  for (const x of [a, b]) line(s, x, 3.62, x, 4.02, { color: ORANGE, width: 3 });
  label(s, "0.40", a, 3.4, 0.8, 0.3, { size: 18, color: ORANGE });
  label(s, "1.80", b, 3.4, 0.8, 0.3, { size: 18, color: ORANGE });
  label(s, "under 0.40  •  shared equally", (x0 + a) / 2, 4.4, 3.0, 0.34, { size: 16, bold: false, color: G.mutedOnDark });
  label(s, "0.40 to 1.80  •  shared unequally", (a + b) / 2, 4.4, 3.4, 0.34, { size: 16, bold: false, color: G.mutedOnDark });
  label(s, "over 1.80  •  transferred", (b + x1) / 2, 4.4, 3.0, 0.34, { size: 16, bold: false, color: G.mutedOnDark });
}

/* 8 — 4.5 Classify each bond (click per bond) */
{
  const s = slide("07_COMPARISON_CARDS", {
    headline: "Classify Each Bond",
    subhead: "Find ΔEN, then use the scale. One click per bond.",
    k1_l: "C–H", k1_b: "2.55 − 2.20 = 0.35\nLess than 0.40\nNonpolar covalent",
    k2_l: "C–O", k2_b: "3.44 − 2.55 = 0.89\nBetween 0.40 and 1.80\nPolar covalent",
    k3_l: "Na–Cl", k3_b: "3.16 − 0.93 = 2.23\nGreater than 1.80\nIonic",
    mustwrite: "Under 0.40: nonpolar. 0.40 to 1.80: polar. Over 1.80: ionic.",
  }, { code: code(4, "4.5"), clicks: { k1_b: 1, k2_b: 2, k3_b: 3 },
       notes: "Ask for each ΔEN before you click. Click 1: C–H 0.35, nonpolar. Click 2: C–O 0.89, polar. Click 3: Na–Cl 2.23, ionic. C–H is why hydrocarbons are nonpolar." });
  miniScale(s, "07_COMPARISON_CARDS");
}

/* 9 — 4.6 Polar vs nonpolar (new motion graphic) */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Polar vs. Nonpolar Covalent Bonds",
    subhead: "When one atom pulls harder, the shared electrons shift toward it.",
    c1_l: "NONPOLAR COVALENT", c1_b: "Shared equally\nΔEN less than 0.40\nNo partial charges\nH–H, Cl–Cl, C–H",
    c2_l: "POLAR COVALENT", c2_b: "Shared unequally\nΔEN 0.40 to 1.80\nPartial charges δ+ δ−\nH–Cl, O–H, C–O",
    mustwrite: "In a polar bond, the atom with higher EN becomes partially negative (δ−).",
  }, { code: code(4, "4.6"), notes: "Click the video to play it (16 s, four steps): H–H and H–Cl both share a pair → Cl (3.16) pulls harder than H (2.20) and the pair shifts → δ+ on H, δ− on Cl → dipole arrow. ΔEN: H–H 0.00, H–Cl 0.96." });
  video(s, "chem_u04_s4.6_bond_polarity_dark.mp4");
}

/* 10 — 4.6 Dipole arrow (click build) */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Drawing the Dipole Arrow",
    subhead: "Show which way the electrons shift in a polar bond.",
    a1_l: "δ−  •  PARTIAL NEGATIVE", a1_b: "The atom with higher EN. Electrons shift here.",
    a2_l: "δ+  •  PARTIAL POSITIVE", a2_b: "The atom with lower EN. Electrons shift away.",
    a3_l: "DIPOLE ARROW", a3_b: "Points toward δ−. The cross marks the δ+ end.",
  }, { code: code(4, "4.6"), clicks: { a1_b: 1, a2_b: 1, a3_b: 2 },
       notes: "Click 1: partial charges. Click 2: the dipole arrow. The arrow is the habit students need for 5.4, where they add dipoles up to decide whether a whole molecule is polar." });
  const cx = 3.45, cy = 4.55;
  oval(s, cx + 0.42, cy, 2.9, 1.25, { fill: CYAN, transparency: 72 });
  const P = lewis(s, MOL.HCl, cx, cy, 1.6, { fs: 40 });
  label(s, "δ+", P("H")[0], cy - 0.95, 0.6, 0.45, { size: 26, click: 1 });
  label(s, "δ−", P("Cl")[0], cy - 0.95, 0.6, 0.45, { size: 26, click: 1 });
  dipole(s, P("H")[0] - 0.1, 3.35, P("Cl")[0] + 0.15, 3.35, DEEP, 2, 3.5);
}

/* 11 — U4 summary */
{
  const s = slide("07_COMPARISON_CARDS", {
    headline: "Bond Types at a Glance",
    subhead: "Keep this one. The cutoffs are guidelines, not hard walls.",
    k1_l: "IONIC", k1_b: "Metal + nonmetal\nElectrons transferred\nΔEN greater than 1.80\nHard, high melting point",
    k2_l: "POLAR COVALENT", k2_b: "Two nonmetals\nShared unequally\nΔEN 0.40 to 1.80\nPartial charges δ+ δ−",
    k3_l: "NONPOLAR COVALENT", k3_b: "Two nonmetals\nShared equally\nΔEN less than 0.40\nNo partial charges",
    mustwrite: "The bigger the electronegativity difference, the more ionic the bond.",
  }, { code: code(4), notes: "Unit 4 summary. Metallic bonding (4.4) is skipped this year by Matt's call, 2026-11-04." });
  miniScale(s, "07_COMPARISON_CARDS");
}

/* 12 — Unit 5 divider */
{
  const s = slide("04_DIVIDER", { eyebrow: "UNIT 05", headline: "Molecular\nStructure",
    subhead: "Draw the molecule, predict its shape, decide if it is polar." }, { unit: 5, code: code(5) });
  dividerCover(s);
  lewis(s, MOL.CH2O, 8.8, 4.15, 2.0, { fs: 60, color: PAPER });
}

/* 13 — 5.2 VSEPR */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "VSEPR: Electron Pairs Push Apart",
    subhead: "Valence Shell Electron Pair Repulsion: pairs spread as far apart as they can.",
    c1_l: "BONDING PAIRS", c1_b: "Shared by two atoms\nDrawn as a line\nHold atoms together",
    c2_l: "LONE PAIRS", c2_b: "Belong to one atom\nDrawn as two dots\nRepel more strongly\nSqueeze bond angles",
    mustwrite: "Lone pairs repel more strongly than bonding pairs, so bond angles shrink.",
  }, { unit: 5, code: code(5, "5.2"), notes: "All three have four electron pairs around the central atom. Each lone pair swapped in for a bond pushes the remaining bonds closer: 109.5° → 107° → 104.5°. The shaded lobes show the lone pairs taking up more room. Shape names come from the students' reference sheet in the activity." });
  const r = cover(s, "03_GROUPED_CONCEPT", "concept", PAPER);
  const cy = r.y + 1.05, u = 0.6, opts = { fs: 22 };
  const lobe = (x, y, ang) => { const [dx, dy] = at(ang, 0.42); oval(s, x + dx, y + dy, 0.62, 0.4, { fill: ORANGE, transparency: 70, rotate: ang }); };
  const panels = [
    ["CH₄", "109.5°", { atoms: { C: ["C", 0, 0], H1: ["H", ...at(-90)], H2: ["H", ...at(30)], H3: ["H", ...at(150)], H4: ["H", 0, 1] },
       bonds: [["C", "H1", 1], ["C", "H2", 1], ["C", "H3", 1], ["C", "H4", 1]], pairs: [] }, []],
    ["NH₃", "107°", { atoms: { N: ["N", 0, 0], H1: ["H", ...at(155)], H2: ["H", ...at(90)], H3: ["H", ...at(25)] },
       bonds: [["N", "H1", 1], ["N", "H2", 1], ["N", "H3", 1]], pairs: [["N", -90]] }, [-90]],
    ["H₂O", "104.5°", { atoms: { O: ["O", 0, 0], H1: ["H", ...at(142.25)], H2: ["H", ...at(37.75)] },
       bonds: [["O", "H1", 1], ["O", "H2", 1]], pairs: [["O", -135], ["O", -45]] }, [-135, -45]],
  ];
  panels.forEach(([name, ang, mol, lobes], i) => {
    const x = r.x + 0.85 + i * 1.7;
    lobes.forEach((a) => lobe(x, cy, a));
    lewis(s, mol, x, cy, u, opts);
    label(s, `${name}  ${ang}`, x, r.y + r.h - 0.3, 1.6, 0.34, { size: 16 });
  });
}

/* 14 — 5.1 Lewis steps */
{
  const s = slide("05_PROCESS_TIMELINE", {
    headline: "Drawing Lewis Structures",
    subhead: "Four steps, every time. We will build three molecules with them.",
    s1_l: "COUNT", s1_b: "Add up all valence e⁻.",
    s2_l: "SKELETON", s2_b: "Center atom, single bonds.",
    s3_l: "FILL", s3_b: "Lone pairs on outer atoms.",
    s4_l: "CHECK", s4_b: "Center short? Make a double bond.",
  }, { unit: 5, code: code(5, "5.1"), notes: "Step 2: the least electronegative atom goes in the center, and H is never central. Step 3: leftover electrons go on the central atom. Step 4: if the central atom has fewer than 8, turn an outer lone pair into a shared pair (B is the exception: stable at 6)." });
  rect(s, 0.75, 2.62, 11.83, 2.20, INK);
  const rules = [["Each line", "= 2 shared e⁻"], ["Each dot pair", "= 2 unshared e⁻"], ["H is never", "the center atom"], ["Least EN atom", "goes in the center"]];
  rules.forEach(([a, b], i) => {
    const x = 0.75 + 11.83 / 8 * (2 * i + 1);
    label(s, a, x, 3.42, 2.7, 0.4, { size: 20, color: PAPER });
    label(s, b, x, 3.9, 2.7, 0.4, { size: 16, bold: false, color: G.mutedOnDark });
  });
}

/* Worked-example builders --------------------------------------------------- */
const DIAG = { cx: 3.525, cy: 4.45 };
function solutionSlide(title, fields, mol, u, fs_, notes, extra) {
  const s = slide("10_WORKED_SOLUTION", Object.assign({ headline: title }, fields), { unit: 5, code: code(5, "5.1"), notes });
  const r = cover(s, "10_WORKED_SOLUTION", "data", PAPER);
  const P = lewis(s, mol, r.x + r.w / 2 + (extra && extra.dx || 0), r.y + r.h / 2 + (extra && extra.dy || 0), u, { fs: fs_ });
  if (extra && extra.draw) extra.draw(s, P, r);
  return s;
}
function clean(f) { const o = Object.assign({}, f); delete o._code; return o; }

/* 15–16 — BF3 */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Worked Example: BF₃", subhead: "Draw the Lewis structure for boron trifluoride. One click per step.",
    a1_l: "1  •  COUNT", a1_b: "B 3 + F 7 × 3 = 24 valence e⁻",
    a2_l: "2  •  SKELETON", a2_b: "B in the center. 3 single bonds use 6 e⁻.",
    a3_l: "3  •  FILL + CHECK", a3_b: "18 e⁻ = 3 pairs on each F. B keeps 6: allowed.",
  }, { unit: 5, code: code(5, "5.1"), clicks: { a1_b: 1, a2_b: 3, a3_b: 4 },
       notes: "Click 1: count (24). Click 2: atoms, B in the center (least electronegative). Click 3: three single bonds (6 e⁻). Click 4: lone pairs, 3 on each F (18 e⁻). 6 + 18 = 24. Boron ends with 6, which is the expected exception." });
  lewis(s, MOL.BF3, DIAG.cx, DIAG.cy + 0.2, 1.15, { fs: 34, clicks: { atoms: 2, bonds: 3, pairs: 4 } });
}
solutionSlide("Solution: BF₃", clean({
  subhead: "24 valence electrons, all placed. Boron is a known exception.",
  f1_l: "VALENCE ELECTRONS", f1_b: "B: 3\nF: 7 × 3 = 21\nTotal: 24 e⁻",
  work: "3 bonds = 6 e⁻\n9 pairs = 18 e⁻\n6 + 18 = 24",
  mustwrite: "Boron is stable with 6 valence electrons, an exception to the octet rule.",
}), MOL.BF3, 0.92, 28, "Every F has 8. B has 6 and stays that way: making a B=F double bond would put a positive formal charge on F, the most electronegative element.", { dy: 0.18 });

/* 17–19 — CO2 */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Worked Example: CO₂", subhead: "Draw the Lewis structure for carbon dioxide. One click per step.",
    a1_l: "1  •  COUNT", a1_b: "C 4 + O 6 × 2 = 16 valence e⁻",
    a2_l: "2  •  SKELETON", a2_b: "C in the center. 2 single bonds use 4 e⁻.",
    a3_l: "3  •  FILL", a3_b: "12 e⁻ left = 3 pairs on each O.",
  }, { unit: 5, code: code(5, "5.1"), clicks: { a1_b: 1, a2_b: 3, a3_b: 4 },
       notes: "Click 1: count (16). Click 2: atoms, C in the center. Click 3: two single bonds (4 e⁻). Click 4: three pairs on each O (12 e⁻). All 16 placed, but ask: how many electrons does carbon have? Only 4. Next slide fixes it." });
  lewis(s, MOL.CO2_single, DIAG.cx, DIAG.cy, 1.25, { fs: 36, clicks: { atoms: 2, bonds: 3, pairs: 4 } });
}
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "CO₂: Check the Center", subhead: "All 16 e⁻ are placed, but carbon only has 4. Fix it.",
    a1_l: "4  •  CHECK", a1_b: "C has 2 bonds = 4 e⁻. It needs 8.",
    a2_l: "5  •  SHARE", a2_b: "Each O turns one lone pair into a bond.",
    a3_l: "6  •  RECOUNT", a3_b: "Two double bonds. C has 8, each O has 8.",
  }, { unit: 5, code: code(5, "5.1"), clicks: { a1_b: 1, a2_b: 2, a3_b: 3 },
       notes: "Click 1: circle carbon, count 4. Click 2: arrows, one lone pair from each O moves into the bond. Click 3: recount, then go to the solution slide to see the double bonds. The electron total does not change: a lone pair just becomes a shared pair." });
  const P = lewis(s, MOL.CO2_single, DIAG.cx, DIAG.cy, 1.25, { fs: 36 });
  const [cx, cy] = P("C");
  oval(s, cx, cy, 0.78, 0.78, { line: DEEP, lineWidth: 3, click: 1 });
  for (const [o, side] of [["O1", 1], ["O2", -1]]) {
    const [ox, oy] = P(o);
    line(s, ox + side * 0.14, oy - 0.5, (ox + cx) / 2 - side * 0.05, oy - 0.13, { color: DEEP, width: 3, end: "triangle", click: 2 });
  }
}
solutionSlide("Solution: CO₂", clean({
  subhead: "Two double bonds. Every atom has an octet.",
  f1_l: "VALENCE ELECTRONS", f1_b: "C: 4\nO: 6 × 2 = 12\nTotal: 16 e⁻",
  work: "2 double bonds\n= 8 e⁻\n4 pairs = 8 e⁻\n8 + 8 = 16",
  mustwrite: "If the center atom is short, turn an outer lone pair into a double bond.",
}), MOL.CO2, 1.25, 30, "Each double bond is 4 shared electrons. C: 4 + 4 = 8. Each O: 4 shared + 2 pairs = 8.");

/* 20–22 — CH2O */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Worked Example: CH₂O", subhead: "Draw the Lewis structure for formaldehyde. One click per step.",
    a1_l: "1  •  COUNT", a1_b: "C 4 + H 1 × 2 + O 6 = 12 valence e⁻",
    a2_l: "2  •  SKELETON", a2_b: "C in the center. 3 single bonds use 6 e⁻.",
    a3_l: "3  •  FILL", a3_b: "6 e⁻ left = 3 pairs on O. Each H is full at 2.",
  }, { unit: 5, code: code(5, "5.1"), clicks: { a1_b: 1, a2_b: 3, a3_b: 4 },
       notes: "Three elements: C goes in the center because H can only make one bond and C is less electronegative than O. Click 1: 12. Click 2: atoms. Click 3: three single bonds (6). Click 4: three pairs on O (6). Carbon has 6, so the next slide fixes it." });
  lewis(s, MOL.CH2O_single, DIAG.cx, DIAG.cy + 0.15, 1.15, { fs: 34, clicks: { atoms: 2, bonds: 3, pairs: 4 } });
}
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "CH₂O: Check the Center", subhead: "All 12 e⁻ are placed, but carbon only has 6. Fix it.",
    a1_l: "4  •  CHECK", a1_b: "C has 3 bonds = 6 e⁻. It needs 8.",
    a2_l: "5  •  SHARE", a2_b: "O turns one lone pair into a second bond.",
    a3_l: "6  •  RECOUNT", a3_b: "C=O double bond. C has 8, O 8, each H 2.",
  }, { unit: 5, code: code(5, "5.1"), clicks: { a1_b: 1, a2_b: 2, a3_b: 3 },
       notes: "Click 1: circle carbon, count 6. Click 2: one lone pair on O moves into the C–O bond. Click 3: recount. Solution slide next." });
  const P = lewis(s, MOL.CH2O_single, DIAG.cx, DIAG.cy + 0.15, 1.15, { fs: 34 });
  const [cx, cy] = P("C"), [ox, oy] = P("O");
  oval(s, cx, cy, 0.76, 0.76, { line: DEEP, lineWidth: 3, click: 1 });
  line(s, ox + 0.62, oy + 0.2, cx + 0.12, (oy + cy) / 2 + 0.05, { color: DEEP, width: 3, end: "triangle", click: 2 });
}
solutionSlide("Solution: CH₂O", clean({
  subhead: "One C=O double bond. C and O have 8; each H has 2.",
  f1_l: "VALENCE ELECTRONS", f1_b: "C: 4\nH: 1 × 2 = 2\nO: 6\nTotal: 12 e⁻",
  work: "C=O = 4 e⁻\n2 C–H = 4 e⁻\n2 pairs = 4 e⁻\nTotal = 12",
  mustwrite: "Hydrogen only ever makes one bond, so it is never the center atom.",
}), MOL.CH2O, 0.95, 28, "Formaldehyde. The double bond is to O, not H: H holds only 2 electrons.", { dy: 0.22 });

/* 23 — 5.4 Bond vs molecular polarity */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Bond Polarity vs. Molecular Polarity",
    subhead: "A bond can be polar while the whole molecule is not. Shape decides.",
    c1_l: "BOND POLARITY", c1_b: "One bond\nTwo atoms\nSet by ΔEN",
    c2_l: "MOLECULAR POLARITY", c2_b: "The whole molecule\nSet by bond polarity\nAND by shape",
    mustwrite: "Polar bonds in a symmetric shape cancel, so the molecule is nonpolar.",
  }, { unit: 5, code: code(5, "5.4"), notes: "HCl has one polar bond, so the molecule is polar. CO₂ has two polar bonds (ΔEN 0.89 each), but they point in opposite directions with equal strength and cancel: CO₂ is nonpolar. Tug-of-war with equal teams." });
  const r = cover(s, "03_GROUPED_CONCEPT", "concept", PAPER);
  const y = r.y + 1.25;
  const P1 = lewis(s, MOL.HCl, r.x + 1.15, y, 0.95, { fs: 26 });
  dipole(s, P1("H")[0] - 0.05, y - 0.62, P1("Cl")[0] + 0.1, y - 0.62, DEEP);
  label(s, "H–Cl\npolar molecule", r.x + 1.15, r.y + r.h - 0.45, 2.0, 0.6, { size: 16 });
  const P2 = lewis(s, MOL.CO2, r.x + 3.65, y, 0.95, { fs: 26 });
  const [cx] = P2("C");
  dipole(s, cx - 0.08, y - 0.62, P2("O1")[0] + 0.05, y - 0.62, DEEP);
  dipole(s, cx + 0.08, y - 0.62, P2("O2")[0] - 0.05, y - 0.62, DEEP);
  label(s, "O=C=O\ndipoles cancel: nonpolar", r.x + 3.65, r.y + r.h - 0.45, 2.6, 0.6, { size: 16 });
}

/* 24 — 5.4 Symmetric vs asymmetric */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Symmetric vs. Asymmetric",
    subhead: "If the bond dipoles pull equally in opposite directions, they cancel.",
    c1_l: "SYMMETRIC  →  NONPOLAR", c1_b: "Dipoles cancel\nCO₂, BF₃, CH₄, CCl₄",
    c2_l: "ASYMMETRIC  →  POLAR", c2_b: "Dipoles add up\nH₂O, NH₃, HCl, CH₃Cl",
    mustwrite: "Lone pairs on the central atom usually make a molecule asymmetric.",
  }, { unit: 5, code: code(5, "5.4"), notes: "Outer-atom lone pairs are left off these two so the dipole arrows can be seen; the full structures are on the worked examples. BF₃: three equal pulls 120° apart cancel. NH₃: the lone pair sits on top, all three N–H dipoles point up toward N, and they add to a net dipole (the long arrow)." });
  const r = cover(s, "03_GROUPED_CONCEPT", "concept", PAPER);
  const y = r.y + 1.18, u = 0.92;
  const bf3 = { atoms: MOL.BF3.atoms, bonds: MOL.BF3.bonds, pairs: [] };
  const P1 = lewis(s, bf3, r.x + 1.3, y, u, { fs: 24 });
  for (const f of ["F1", "F2", "F3"]) bondDipole(s, P1, "B", f, 1, DEEP, 0, 0.22, 0.25, 0.7);
  label(s, "BF₃: nonpolar", r.x + 1.3, r.y + r.h - 0.25, 1.8, 0.32, { size: 16 });
  const P2 = lewis(s, MOL.NH3, r.x + 3.45, y - 0.1, u, { fs: 24 });
  for (const h of ["H1", "H2", "H3"]) bondDipole(s, P2, h, "N", h === "H1" ? -1 : 1, DEEP, 0, 0.22, 0.25, 0.7);
  dipole(s, r.x + 4.75, y + 0.85, r.x + 4.75, y - 0.6, DEEP, 0, 3.5);
  label(s, "NH₃: polar", r.x + 3.45, r.y + r.h - 0.25, 1.8, 0.32, { size: 16 });
}

/* 25–30 — molecular polarity worked examples */
function polarityExample(o) {
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: `Worked Example: Is ${o.f} Polar?`, subhead: "Draw it, check each bond, then look at the shape.",
    a1_l: "1  •  DRAW IT", a1_b: o.a1, a2_l: "2  •  BOND DIPOLES", a2_b: o.a2, a3_l: "3  •  SHAPE", a3_b: o.a3,
  }, { unit: 5, code: code(5, "5.4"), clicks: { a1_b: 1, a2_b: 2, a3_b: 3 }, notes: o.notes });
  const P = lewis(s, o.mol, DIAG.cx + (o.dx || 0), DIAG.cy + (o.dy || 0), o.u, { fs: o.fs, clicks: { atoms: 1, bonds: 1, pairs: 1 } });
  o.dip(s, P, 2);
  o.net(s, P, 3);
  const sol = slide("10_WORKED_SOLUTION", {
    headline: `Solution: ${o.f} Is ${o.verdict}`, subhead: o.solSub,
    f1_l: "ΔEN", f1_b: o.f1, work: o.work, mustwrite: o.must,
  }, { unit: 5, code: code(5, "5.4") });
  const r = cover(sol, "10_WORKED_SOLUTION", "data", PAPER);
  const Q = lewis(sol, o.mol, r.x + r.w / 2 + (o.sdx || 0), r.y + r.h / 2 + (o.sdy || 0), o.su, { fs: o.sfs });
  o.dip(sol, Q, 0, o.su / o.u);
  o.net(sol, Q, 0, o.su / o.u);
}
polarityExample({
  f: "H₂O", verdict: "Polar", mol: MOL.H2O, u: 1.45, fs: 38, dy: -0.15, su: 1.1, sfs: 28, sdx: -0.35, sdy: -0.1,
  a1: "8 valence e⁻: 2 bonds, 2 lone pairs on O.", a2: "O 3.44 − H 2.20 = 1.24. Both bonds polar.",
  a3: "Bent. The dipoles add up: POLAR.",
  dip: (s, P, c, k = 1) => { bondDipole(s, P, "H1", "O", -1, DEEP, c, 0.24 * k); bondDipole(s, P, "H2", "O", 1, DEEP, c, 0.24 * k); },
  net: (s, P, c, k = 1) => { const [ox, oy] = P("O"); dipole(s, ox + 1.75 * k, oy + 1.1 * k, ox + 1.75 * k, oy - 0.45 * k, DEEP, c, 3.5); },
  solSub: "Polar bonds in a bent shape. The pulls do not cancel.",
  f1: "O 3.44\nH 2.20\nΔEN = 1.24\nPolar bonds", work: "Bent shape\nDipoles add\n→ POLAR",
  must: "Water is polar: polar bonds in a bent, asymmetric shape.",
  notes: "Click 1: structure (8 e⁻: two O–H bonds, two lone pairs on O). Click 2: both bond dipoles point toward O. Click 3: the shape is bent, both arrows lean up toward O, so they add: net dipole up. Water is polar.",
});
polarityExample({
  f: "NH₃", verdict: "Polar", mol: MOL.NH3, u: 1.35, fs: 38, dy: -0.25, su: 1.0, sfs: 28, sdx: -0.4, sdy: -0.2,
  a1: "8 valence e⁻: 3 bonds, 1 lone pair on N.", a2: "N 3.04 − H 2.20 = 0.84. All 3 bonds polar.",
  a3: "Pyramid. The dipoles add up: POLAR.",
  dip: (s, P, c, k = 1) => { for (const h of ["H1", "H2", "H3"]) bondDipole(s, P, h, "N", h === "H1" ? -1 : 1, DEEP, c, 0.24 * k); },
  net: (s, P, c, k = 1) => { const [nx, ny] = P("N"); dipole(s, nx + 1.95 * k, ny + 1.25 * k, nx + 1.95 * k, ny - 0.45 * k, DEEP, c, 3.5); },
  solSub: "Three polar bonds under a lone pair. The pulls add up.",
  f1: "N 3.04\nH 2.20\nΔEN = 0.84\nPolar bonds", work: "Pyramid shape\nDipoles add\n→ POLAR",
  must: "The lone pair on N makes NH₃ asymmetric, so it is polar.",
  notes: "Click 1: structure (8 e⁻: three N–H bonds, one lone pair). Click 2: three bond dipoles toward N. Click 3: trigonal pyramidal; the lone pair sits on one side so nothing cancels it: net dipole up. NH₃ is polar.",
});
polarityExample({
  f: "CCl₄", verdict: "Nonpolar", mol: MOL.CCl4, u: 1.02, fs: 30, dy: 0.05, su: 0.78, sfs: 22, sdx: -0.3,
  a1: "32 valence e⁻: 4 bonds, 3 pairs on each Cl.", a2: "Cl 3.16 − C 2.55 = 0.61. All 4 bonds polar.",
  a3: "Symmetric. The dipoles cancel: NONPOLAR.",
  dip: (s, P, c, k = 1) => { for (const x of ["A", "B", "D", "E"]) bondDipole(s, P, "C", x, 1, DEEP, c, 0.24 * k, 0.24, 0.6); },
  net: (s, P, c, k = 1) => { const [x, y] = P("C"); label(s, "net = 0", x + 1.6 * k + 0.35, y + 1.15 * k, 1.1, 0.36, { size: 18, click: c }); },
  solSub: "Four equal polar bonds, arranged symmetrically. They cancel.",
  f1: "Cl 3.16\nC 2.55\nΔEN = 0.61\nPolar bonds", work: "Tetrahedral\nDipoles cancel\n→ NONPOLAR",
  must: "CCl₄ has polar bonds but is nonpolar: four equal pulls cancel.",
  notes: "Click 1: structure (C 4 + Cl 7 × 4 = 32 e⁻). Click 2: four bond dipoles, each pointing out toward Cl. Click 3: the real shape is tetrahedral, four equal pulls in symmetric directions, so they cancel: no net dipole. Contrast with CH₃Cl, which swaps one Cl for H and becomes polar.",
});

/* 31 — IMF divider */
{
  const s = slide("04_DIVIDER", { eyebrow: "UNIT 05  •  5.5", headline: "Intermolecular\nForces",
    subhead: "What holds one molecule to the next." }, { unit: 5, code: code(5, "5.5") });
  dividerCover(s);
  network(s, 8.9, 3.95, 1.05, 36, PAPER, ORANGE);
}

/* 32 — Intra vs inter */
{
  const s = slide("03_GROUPED_CONCEPT", {
    headline: "Intramolecular vs. Intermolecular",
    subhead: "Bonds hold a molecule together. IMFs hold molecules to each other.",
    c1_l: "INTRAMOLECULAR", c1_b: "Inside one molecule\nThe covalent bonds\nStrong",
    c2_l: "INTERMOLECULAR", c2_b: "Between molecules\nAttractions, not bonds\nMuch weaker\nSet the boiling point",
    mustwrite: "Stronger intermolecular forces mean higher melting and boiling points.",
  }, { unit: 5, code: code(5, "5.5"), notes: "Boiling water breaks the attractions between molecules (the dashed line), not the O–H bonds inside them. Steam is still H₂O. That is why IMFs, not bonds, set melting and boiling points." });
  const r = cover(s, "03_GROUPED_CONCEPT", "concept", PAPER);
  const u = 0.62, A = [r.x + 1.45, r.y + 1.0];
  const W1 = water(s, A[0], A[1], -30, u, { fs: 24 });
  const B = [A[0] + at(22.25, 2.6 * u)[0], A[1] + at(22.25, 2.6 * u)[1]];
  water(s, B[0], B[1], -60, u, { fs: 24 });
  hbond(s, W1.H1, B, DEEP, 0.17, 0.26);
  const ly = r.y + r.h - 0.42;
  line(s, r.x + 0.3, ly, r.x + 0.7, ly, { width: 2.75 });
  label(s, "intramolecular\n(the O–H bond)", r.x + 1.75, ly, 1.9, 0.6, { size: 16, align: "left" });
  line(s, r.x + 2.85, ly, r.x + 3.25, ly, { color: DEEP, width: 2.25, dash: "dash" });
  label(s, "intermolecular\n(the attraction)", r.x + 4.3, ly, 1.9, 0.6, { size: 16, align: "left" });
}

/* 33 — Hydrogen bonding */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Hydrogen Bonding", subhead: "The strongest IMF. It is why water boils at 100 °C instead of far below 0 °C.",
    a1_l: "WHAT IT IS", a1_b: "H on N, O, or F pulled to another N, O, or F.",
    a2_l: "STRENGTH", a2_b: "Strongest of the three IMFs.",
    a3_l: "EXAMPLES", a3_b: "H₂O, NH₃, HF. Also holds DNA strands together.",
  }, { unit: 5, code: code(5, "5.5"), notes: "The dashed lines are hydrogen bonds: an H that is bonded to O is attracted to a lone pair on a neighboring O. It is a strong dipole–dipole attraction, not a covalent bond. Without it, water (molar mass 18) would boil far below 0 °C, like H₂S does at −60 °C." });
  network(s, 3.5, 4.45, 0.5, 20, INK, DEEP);
  label(s, "hydrogen bond", 5.25, 4.65, 1.6, 0.32, { size: 16 });
}

/* 34 — Dipole–dipole */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "Dipole–Dipole Forces", subhead: "Polar molecules line up: δ+ end of one, δ− end of the next.",
    a1_l: "WHAT IT IS", a1_b: "δ+ of one polar molecule attracts δ− of the next.",
    a2_l: "WHO HAS IT", a2_b: "Polar molecules only.",
    a3_l: "EXAMPLES", a3_b: "HCl, CH₃Cl, SO₂",
  }, { unit: 5, code: code(5, "5.5"), notes: "Each HCl is a small dipole. The molecules turn so opposite partial charges sit next to each other (dashed lines). Weaker than hydrogen bonding, stronger than London dispersion for molecules of similar size." });
  const mol = (x, y, flip) => {
    const m = flip ? { atoms: { Cl: ["Cl", -0.5, 0], H: ["H", 0.5, 0] }, bonds: [["H", "Cl", 1]], pairs: [] }
                   : { atoms: { H: ["H", -0.5, 0], Cl: ["Cl", 0.5, 0] }, bonds: [["H", "Cl", 1]], pairs: [] };
    const P = lewis(s, m, x, y, 0.8, { fs: 28 });
    const dy = flip ? 0.45 : -0.45;
    label(s, "δ+", P("H")[0], y + dy, 0.5, 0.3, { size: 16 });
    label(s, "δ−", P("Cl")[0], y + dy, 0.5, 0.3, { size: 16 });
    return P;
  };
  const A = mol(1.95, 3.6, false), B = mol(4.45, 3.6, false), C = mol(1.95, 4.95, true), D = mol(4.45, 4.95, true);
  const dash = (p, q) => line(s, p[0], p[1], q[0], q[1], { color: DEEP, width: 2.25, dash: "dash" });
  dash([A("Cl")[0] + 0.32, 3.6], [B("H")[0] - 0.2, 3.6]);
  dash([C("H")[0] + 0.2, 4.95], [D("Cl")[0] - 0.32, 4.95]);
  for (const [p, q] of [[A("H"), C("Cl")], [A("Cl"), C("H")], [B("H"), D("Cl")], [B("Cl"), D("H")]])
    dash([p[0], 3.85], [q[0], 4.7]);
}

/* 35 — London dispersion */
{
  const s = slide("08_DIAGRAM_ANNOTATION", {
    headline: "London Dispersion Forces", subhead: "Even nonpolar molecules attract, for an instant at a time.",
    a1_l: "WHAT IT IS", a1_b: "A brief electron shift makes a temporary dipole.",
    a2_l: "WHO HAS IT", a2_b: "Every molecule. The only IMF in nonpolar ones.",
    a3_l: "BIGGER = STRONGER", a3_b: "More electrons, stronger LDF: I₂ is a solid.",
  }, { unit: 5, code: code(5, "5.5"), notes: "Row 1: electrons spread evenly. Row 2: for an instant they bunch on one side, a temporary dipole. Row 3: that dipole pushes the neighbor's electrons away, inducing a matching dipole, and the two attract. It flickers constantly. More electrons means a bigger, easier-to-distort cloud: F₂ and Cl₂ are gases, Br₂ a liquid, I₂ a solid." });
  const rows = [3.3, 4.38, 5.46], xa = 1.75, xb = 3.35, R = 0.78;
  const cloud = (x, y, shift) => {
    oval(s, x, y, R, R, { fill: CYAN, transparency: 80, line: G.graphite, lineWidth: 1 });
    if (shift) oval(s, x + shift * 0.17, y, R * 0.6, R * 0.8, { fill: CYAN, transparency: 45 });
    dot(s, x, y, 0.1, INK);
    if (shift) {
      label(s, "δ−", x + shift * 0.24, y - 0.56, 0.36, 0.28, { size: 16 });
      label(s, "δ+", x - shift * 0.24, y - 0.56, 0.36, 0.28, { size: 16 });
    }
  };
  cloud(xa, rows[0], 0); cloud(xb, rows[0], 0);
  cloud(xa, rows[1], -1); cloud(xb, rows[1], 0);
  cloud(xa, rows[2], -1); cloud(xb, rows[2], -1);
  line(s, xa + R / 2 + 0.06, rows[2], xb - R / 2 - 0.06, rows[2], { color: DEEP, width: 2.25, dash: "dash" });
  label(s, "1  Even cloud", 5.15, rows[0], 2.1, 0.34, { size: 16, align: "left" });
  label(s, "2  Temporary dipole", 5.15, rows[1], 2.1, 0.34, { size: 16, align: "left" });
  label(s, "3  Neighbor induced", 5.15, rows[2], 2.1, 0.34, { size: 16, align: "left" });
}

pres.writeFile({ fileName: OUT }).then((f) => {
  console.log(`wrote ${f}`);
  const side = f + ".builds.json";
  fs.writeFileSync(side, JSON.stringify(PH_BUILDS));
  const r = require("child_process").spawnSync("python3",
    [path.join(HERE, "..", "..", "..", "..", "scripts", "add_click_builds.py"), f, side], { encoding: "utf8" });
  fs.unlinkSync(side);
  process.stdout.write(r.stdout || ""); if (r.status !== 0) { console.error(r.stderr); process.exit(1); }
});
