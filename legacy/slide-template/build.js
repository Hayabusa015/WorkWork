const pptxgen = require("pptxgenjs");
/* Token set is swappable so a course can declare a palette exception without
   forking this file. Defaults to the shared Ink/Amber set. */
const { C, T, F, W, H, M, RAIL } = require(process.env.SHULL_TOKENS || "./tokens");

const IMG = "/home/claude/tmpl/img/";
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Matthew Shull";
pres.company = "SHULL Science";
pres.title = "SHULL Science — Slide Template";

/* ---------- furniture helpers (fresh objects every call) ---------- */

const rail = () => ({ rect: { x: 0, y: 0, w: RAIL, h: H, fill: { color: C.amber } } });

const bgDark  = () => ({ rect: { x: 0, y: 0, w: W, h: H, fill: { color: C.ink } } });
const bgLight = () => ({ rect: { x: 0, y: 0, w: W, h: H, fill: { color: C.paper } } });

/* eyebrow kicker + hairline, used on every slide */
const eyebrow = (dark) => ([
  { placeholder: {
      options: { name: "eyebrow", type: "body", x: M.l, y: 0.42, w: 7.0, h: 0.26,
                 fontFace: F.body, fontSize: T.eyebrow, bold: true, charSpacing: 1.6,
                 color: dark ? C.paper : C.ink, valign: "middle", margin: 0, isTextBox: true },
      text: "UNIT 00  •  COURSE" } },
  { line: { x: M.l, y: 0.74, w: 1.5, h: 0, line: { color: C.amber, width: 1.75 } } }
]);

/* footer: brand left, doc code right — both editable per course */
const footer = (dark) => ([
  { text: { text: "SHULL SCIENCE",
      options: { x: M.l, y: H - 0.52, w: 4.0, h: 0.26,
                 fontFace: F.body, fontSize: T.footer, bold: true, charSpacing: 1.4,
                 color: dark ? C.warm : C.mute, valign: "middle", margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: "code", type: "body", x: W - M.r - 3.0, y: H - 0.52, w: 3.0, h: 0.26,
                 fontFace: F.body, fontSize: T.footer, bold: true, charSpacing: 1.4,
                 align: "right", color: dark ? C.warm : C.mute, valign: "middle",
                 margin: 0, isTextBox: true },
      text: "U00 • S0.0" } }
]);

/* must-write bar — the single write-this cue. One per slide, never two. */
const mustWrite = (y) => ([
  { rect: { x: M.l, y: y, w: W - M.l - M.r, h: 0.62, fill: { color: C.ink } } },
  { text: { text: "MUST WRITE",
      options: { x: M.l + 0.22, y: y + 0.06, w: 1.3, h: 0.22, fontFace: F.body,
                 fontSize: 9, bold: true, charSpacing: 1.5, color: C.amber,
                 margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: "mustwrite", type: "body", x: M.l + 1.7, y: y + 0.08, w: W - M.l - M.r - 2.0,
                 h: 0.44, fontFace: F.body, fontSize: T.body, bold: true, color: C.paper,
                 valign: "middle", margin: 0, isTextBox: true },
      text: "The one sentence students copy down." } }
]);

/* a light content card */
const card = (name, x, y, w, h, labelText, bodyText, opts = {}) => ([
  { rect: { x, y, w, h, fill: { color: opts.dark ? C.inkCard : C.white },
            line: { color: opts.dark ? C.inkSoft : C.cardEdge, width: 1 } } },
  { placeholder: {
      options: { name: name + "_l", type: "body", x: x + 0.22, y: y + 0.18, w: w - 0.44, h: 0.24,
                 fontFace: F.body, fontSize: T.label, bold: true, charSpacing: 1.2,
                 color: opts.dark ? C.amber : C.mute, margin: 0, isTextBox: true },
      text: labelText } },
  { placeholder: {
      options: { name: name + "_b", type: "body", x: x + 0.22, y: y + 0.5, w: w - 0.44, h: h - 0.72,
                 fontFace: F.body, fontSize: T.cardBody,
                 color: opts.dark ? C.paper : C.ink, margin: 0, isTextBox: true },
      text: bodyText } }
]);

const headline = (dark, y = 1.02, w = W - M.l - M.r) => ({
  placeholder: {
    options: { name: "headline", type: "title", x: M.l, y: y, w: w, h: 0.95,
               fontFace: F.display, fontSize: T.headline, bold: true,
               color: dark ? C.white : C.ink, valign: "top", margin: 0, isTextBox: true },
    text: "Slide Headline Goes Here" }
});

const subhead = (dark, y, w = W - M.l - M.r) => ({
  placeholder: {
    options: { name: "subhead", type: "body", x: M.l, y: y, w: w, h: 0.42,
               fontFace: F.body, fontSize: T.subhead,
               color: dark ? C.warm : C.mute, margin: 0, isTextBox: true },
    text: "One line that frames what students should look for." }
});

/* ================= LAYOUTS ================= */

/* 01 — UNIT TITLE (dark, hero image right) */
pres.defineSlideMaster({
  title: "01_UNIT_TITLE", background: { color: C.ink },
  objects: [
    bgDark(),
    { image: { x: 6.05, y: 1.70, w: 7.28, h: 4.10, path: IMG + "atom_dark.png" } },
    { rect: { x: 0, y: 0, w: 6.05, h: H, fill: { color: C.ink } } },
    rail(),
    ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.30, w: 5.05, h: 2.10,
                   fontFace: F.display, fontSize: T.deckTitle, bold: true, color: C.white,
                   lineSpacingMultiple: 1.05, margin: 0, isTextBox: true },
        text: "Unit Title\nGoes Here" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 3.55, w: 4.85, h: 0.9,
                   fontFace: F.body, fontSize: T.subhead, color: C.warm, margin: 0, isTextBox: true },
        text: "One sentence on what this unit is actually about." } },
    { rect: { x: M.l, y: 5.55, w: 1.55, h: 0.36, fill: { color: C.amber }, rectRadius: 0.18 } },
    { text: { text: "MR. SHULL",
        options: { x: M.l, y: 5.58, w: 1.55, h: 0.30,
                   fontFace: F.body, fontSize: 10, bold: true, charSpacing: 1.2,
                   align: "center", color: C.ink, valign: "middle", margin: 0, isTextBox: true } } },
    ...footer(true)
  ]
});

/* 02 — SECTION TITLE (amber panel left, image right) */
pres.defineSlideMaster({
  title: "02_SECTION_TITLE", background: { color: C.ink },
  objects: [
    bgDark(),
    { rect: { x: 0, y: 0, w: 4.35, h: H, fill: { color: C.amber } } },
    { image: { x: 4.90, y: 0.85, w: 7.75, h: 4.36, path: IMG + "glassware_warm.png" } },
    { placeholder: {
        options: { name: "number", type: "body", x: 0.85, y: 0.55, w: 2.2, h: 0.95,
                   fontFace: F.display, fontSize: T.sectionNo, bold: true, color: C.ink,
                   margin: 0, isTextBox: true },
        text: "01" } },
    { text: { text: "SECTION TITLE",
        options: { x: 0.85, y: 1.62, w: 3.0, h: 0.24, fontFace: F.body, fontSize: T.eyebrow,
                   bold: true, charSpacing: 1.6, color: C.ink, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "headline", type: "title", x: 0.85, y: 2.02, w: 3.10, h: 1.85,
                   fontFace: F.display, fontSize: T.headline, bold: true, color: C.ink,
                   lineSpacingMultiple: 1.06, margin: 0, isTextBox: true },
        text: "1.1\nSection Name" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: 0.85, y: 4.10, w: 3.10, h: 1.2,
                   fontFace: F.body, fontSize: T.body, color: C.ink, margin: 0, isTextBox: true },
        text: "What students should be able to do by the end." } },
    { text: { text: "SHULL SCIENCE",
        options: { x: 0.85, y: H - 0.52, w: 3.0, h: 0.26, fontFace: F.body, fontSize: T.footer,
                   bold: true, charSpacing: 1.4, color: C.ink, valign: "middle",
                   margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "code", type: "body", x: W - M.r - 3.0, y: H - 0.52, w: 3.0, h: 0.26,
                   fontFace: F.body, fontSize: T.footer, bold: true, charSpacing: 1.4,
                   align: "right", color: C.warm, valign: "middle", margin: 0, isTextBox: true },
        text: "U00 • S0.0" } }
  ]
});

/* 03 — GROUPED CONCEPT (light, image + 2 cards + must-write) */
pres.defineSlideMaster({
  title: "03_GROUPED_CONCEPT", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false, 2.02),
    { image: { x: M.l, y: 2.60, w: 5.10, h: 2.87, path: IMG + "ice_beakers.png" } },
    ...card("c1", 6.05, 2.60, 3.45, 2.87, "PHYSICAL",
            "Matter looks different, but the substance is still the same."),
    ...card("c2", 9.75, 2.60, 3.45, 2.87, "CHEMICAL",
            "A new substance forms with new properties.", { dark: true }),
    ...mustWrite(5.82), ...footer(false)
  ]
});

/* 04 — SECTION DIVIDER (dark, full image, floating card) */
pres.defineSlideMaster({
  title: "04_DIVIDER", background: { color: C.ink },
  objects: [
    bgDark(),
    { image: { x: 3.20, y: 0, w: 10.13, h: H, path: IMG + "models_row.png" } },
    { rect: { x: 0, y: 0, w: 4.30, h: H, fill: { color: C.ink } } },
    rail(),
    { rect: { x: 0.62, y: 1.62, w: 4.05, h: 4.02, fill: { color: C.ink },
              line: { color: C.inkSoft, width: 1.25 } } },
    { placeholder: {
        options: { name: "eyebrow", type: "body", x: 0.92, y: 1.92, w: 3.45, h: 0.50,
                   fontFace: F.body, fontSize: T.eyebrow, bold: true, charSpacing: 1.5,
                   color: C.amber, margin: 0, isTextBox: true },
        text: "1.2  •  SECTION NAME" } },
    { placeholder: {
        options: { name: "headline", type: "title", x: 0.92, y: 2.52, w: 3.45, h: 1.55,
                   fontFace: F.display, fontSize: 26, bold: true, color: C.white,
                   lineSpacingMultiple: 1.08, margin: 0, isTextBox: true },
        text: "The Big Idea\nOf This Section" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: 0.92, y: 4.22, w: 3.45, h: 1.20,
                   fontFace: F.body, fontSize: T.body, color: C.warm, margin: 0, isTextBox: true },
        text: "One concept image, no decoration. Students see the story before the first bullet." } },
    ...footer(true)
  ]
});

/* 05 — PROCESS / TIMELINE (light, image band + 4 numbered steps) */
const step = (n, x) => ([
  { rect: { x: x, y: 5.05, w: 2.86, h: 1.30, fill: { color: C.white },
            line: { color: C.cardEdge, width: 1 } } },
  { rect: { x: x + 0.16, y: 5.20, w: 0.34, h: 0.34, fill: { color: C.ink } } },
  { text: { text: String(n),
      options: { x: x + 0.16, y: 5.20, w: 0.34, h: 0.34, fontFace: F.body, fontSize: 11,
                 bold: true, color: C.amber, align: "center", valign: "middle",
                 margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: "s" + n + "_l", type: "body", x: x + 0.60, y: 5.20, w: 2.10, h: 0.30,
                 fontFace: F.body, fontSize: T.label, bold: true, color: C.ink,
                 valign: "middle", margin: 0, isTextBox: true },
      text: "Step " + n } },
  { placeholder: {
      options: { name: "s" + n + "_b", type: "body", x: x + 0.16, y: 5.60, w: 2.54, h: 0.62,
                 fontFace: F.body, fontSize: T.cardBody, color: C.ink, margin: 0, isTextBox: true },
      text: "What changed, and why." } }
]);

pres.defineSlideMaster({
  title: "05_PROCESS_TIMELINE", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false, 2.02),
    { rect: { x: M.l, y: 2.62, w: W - M.l - M.r, h: 2.20, fill: { color: C.ink } } },
    { image: { x: 3.55, y: 2.72, w: 6.20, h: 2.00, path: IMG + "models_row.png" } },
    ...step(1, M.l), ...step(2, M.l + 3.02), ...step(3, M.l + 6.04), ...step(4, M.l + 9.06),
    ...footer(false)
  ]
});

/* 06 — CONCEPT + IMAGE PANEL (dark, amber panel right) */
pres.defineSlideMaster({
  title: "06_CONCEPT_IMAGE", background: { color: C.ink },
  objects: [
    bgDark(), rail(),
    { rect: { x: 6.75, y: 0.95, w: 5.85, h: 4.55, fill: { color: C.amber } } },
    { image: { x: 6.95, y: 1.42, w: 5.45, h: 3.06, path: IMG + "nucleus_gold.png" } },
    ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.30, w: 5.35, h: 0.95,
                   fontFace: F.display, fontSize: T.headline, bold: true, color: C.white,
                   margin: 0, isTextBox: true },
        text: "Concept Headline" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 2.35, w: 5.35, h: 1.10,
                   fontFace: F.body, fontSize: T.body, color: C.warm, margin: 0, isTextBox: true },
        text: "Two lines of framing. Keep it to what the image cannot say on its own." } },
    { rect: { x: M.l, y: 3.85, w: 5.35, h: 1.25, fill: { color: C.inkCard },
              line: { color: C.inkSoft, width: 1 } } },
    { text: { text: "KEY QUESTION",
        options: { x: M.l + 0.22, y: 4.00, w: 3.0, h: 0.24, fontFace: F.body, fontSize: 9,
                   bold: true, charSpacing: 1.4, color: C.amber, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "keyq", type: "body", x: M.l + 0.22, y: 4.32, w: 4.91, h: 0.62,
                   fontFace: F.body, fontSize: T.body, bold: true, color: C.paper,
                   margin: 0, isTextBox: true },
        text: "What tells us which element an atom is?" } },
    ...footer(true)
  ]
});

/* 07 — COMPARISON CARDS (light, 3 cards + image + must-write) */
pres.defineSlideMaster({
  title: "07_COMPARISON_CARDS", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false),
    headline(false, 1.02, 8.05), subhead(false, 2.02, 8.05),
    { rect: { x: 9.20, y: 1.05, w: 3.38, h: 2.20, fill: { color: C.amber } } },
    { image: { x: 9.34, y: 1.19, w: 3.10, h: 1.74, path: IMG + "atom_dark.png" } },
    ...card("k1", M.l, 3.05, 3.72, 2.55, "PROTON", "+1 charge\nIn the nucleus\nDetermines the element"),
    ...card("k2", M.l + 3.95, 3.05, 3.72, 2.55, "NEUTRON", "0 charge\nIn the nucleus\nChanges the isotope"),
    ...card("k3", M.l + 7.90, 3.05, 3.72, 2.55, "ELECTRON",
            "−1 charge\nOutside the nucleus\nControls bonding", { dark: true }),
    ...mustWrite(5.92), ...footer(false)
  ]
});

/* 08 — DIAGRAM + ANNOTATION (light, big diagram card + 3 support cards) */
pres.defineSlideMaster({
  title: "08_DIAGRAM_ANNOTATION", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false, 2.02),
    { rect: { x: M.l, y: 2.62, w: 5.55, h: 3.55, fill: { color: C.white },
              line: { color: C.cardEdge, width: 1 } } },
    { placeholder: {
        options: { name: "diagram", type: "body", x: M.l + 0.25, y: 2.90, w: 5.05, h: 3.0,
                   fontFace: F.display, fontSize: 20, color: C.mute, align: "center",
                   valign: "middle", margin: 0, isTextBox: true },
        text: "Drop the hand-built diagram here" } },
    ...card("a1", 6.70, 2.62, 6.05, 1.08, "LABEL ONE", "What this part of the diagram means."),
    ...card("a2", 6.70, 3.86, 6.05, 1.08, "LABEL TWO", "What this part of the diagram means."),
    ...card("a3", 6.70, 5.10, 6.05, 1.07, "LABEL THREE", "What this part of the diagram means."),
    ...footer(false)
  ]
});

/* 09 — EXAMPLE PROBLEM (light — problem, givens, work area, no answer) */
pres.defineSlideMaster({
  title: "09_EXAMPLE_PROBLEM", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false),
    headline(false, 1.02, 8.60), subhead(false, 2.02, 8.60),
    { rect: { x: 9.75, y: 1.05, w: 2.83, h: 1.85, fill: { color: C.white },
              line: { color: C.amber, width: 2 } } },
    { image: { x: 9.89, y: 1.19, w: 2.55, h: 1.44, path: IMG + "particles_trio.png" } },
    { rect: { x: M.l, y: 2.62, w: 5.90, h: 1.15, fill: { color: C.ink } } },
    { text: { text: "PROBLEM",
        options: { x: M.l + 0.22, y: 2.76, w: 2.0, h: 0.24, fontFace: F.body, fontSize: 9,
                   bold: true, charSpacing: 1.4, color: C.amber, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "problem", type: "body", x: M.l + 0.22, y: 3.06, w: 5.46, h: 0.60,
                   fontFace: F.body, fontSize: T.body, color: C.paper, margin: 0, isTextBox: true },
        text: "State the problem in one sentence." } },
    ...card("g1", M.l, 3.95, 2.85, 1.90, "GIVEN", "What the problem hands you."),
    ...card("g2", M.l + 3.05, 3.95, 2.85, 1.90, "NEED", "What you are solving for."),
    { rect: { x: 6.85, y: 2.62, w: 5.73, h: 3.23, fill: { color: C.white },
              line: { color: C.cardEdge, width: 1 } } },
    { text: { text: "WORK AREA",
        options: { x: 7.07, y: 2.80, w: 2.5, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.mute, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "work", type: "body", x: 7.07, y: 3.15, w: 5.29, h: 2.50,
                   fontFace: F.body, fontSize: 18, color: C.ink, margin: 0, isTextBox: true },
        text: "Work the problem live. Leave this blank in the projected copy." } },
    ...mustWrite(6.05), ...footer(false)
  ]
});

/* 10 — WORKED SOLUTION (light — image, formula, answer) */
pres.defineSlideMaster({
  title: "10_WORKED_SOLUTION", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false, 2.02),
    { rect: { x: M.l, y: 2.62, w: 4.55, h: 2.80, fill: { color: C.amber } } },
    { image: { x: M.l + 0.16, y: 2.78, w: 4.23, h: 2.48, path: IMG + "balance_masses.png" } },
    ...card("f1", 5.55, 2.62, 3.45, 2.80, "FORMULA",
            "(mass × abundance)\n+ (mass × abundance)"),
    { rect: { x: 9.20, y: 2.62, w: 3.38, h: 2.80, fill: { color: C.white },
              line: { color: C.cardEdge, width: 1 } } },
    { text: { text: "WORK",
        options: { x: 9.42, y: 2.80, w: 2.0, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.mute, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "work", type: "body", x: 9.42, y: 3.14, w: 2.94, h: 2.10,
                   fontFace: F.body, fontSize: 18, color: C.ink, margin: 0, isTextBox: true },
        text: "(10.01 × 0.199)\n+ (11.01 × 0.801)\n= 10.81 amu" } },
    ...mustWrite(5.62), ...footer(false)
  ]
});

/* 11 — GIVENS / EQUATION / ANSWER (light — works for any course) */
pres.defineSlideMaster({
  title: "11_GIVENS_EQUATION_ANSWER", background: { color: C.paper },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false, 2.02),
    { rect: { x: M.l, y: 2.62, w: 5.10, h: 2.87, fill: { color: C.amber } } },
    { image: { x: M.l + 0.16, y: 2.78, w: 4.78, h: 2.55, path: IMG + "ramp_timer.png" } },
    { rect: { x: 6.10, y: 2.62, w: 6.48, h: 1.05, fill: { color: C.ink } } },
    { text: { text: "PROBLEM",
        options: { x: 6.32, y: 2.74, w: 2.0, h: 0.22, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.amber, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "problem", type: "body", x: 6.32, y: 3.00, w: 6.04, h: 0.55,
                   fontFace: F.body, fontSize: T.body, color: C.paper, margin: 0, isTextBox: true },
        text: "State the problem in one sentence." } },
    ...card("q1", 6.10, 3.85, 3.14, 1.64, "GIVEN", "Values the problem supplies."),
    ...card("q2", 9.44, 3.85, 3.14, 1.64, "EQUATION", "The relationship you will use."),
    { rect: { x: 6.10, y: 5.68, w: 6.48, h: 0.85, fill: { color: C.amberPale },
              line: { color: C.amber, width: 1.5 } } },
    { text: { text: "ANSWER",
        options: { x: 6.32, y: 5.78, w: 2.0, h: 0.22, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.ink, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "answer", type: "body", x: 6.32, y: 6.02, w: 6.04, h: 0.42,
                   fontFace: F.display, fontSize: 20, bold: true, color: C.ink,
                   margin: 0, isTextBox: true },
        text: "0.80 m/s²" } },
    ...footer(false)
  ]
});

/* 12 — DECK INDEX (dark, 6 tiles) */
const tile = (n, label, sub, x, y) => ([
  { rect: { x, y, w: 2.90, h: 1.18, fill: { color: C.inkCard },
            line: { color: C.inkSoft, width: 1 } } },
  { text: { text: n,
      options: { x: x + 0.22, y: y + 0.16, w: 0.6, h: 0.26, fontFace: F.body, fontSize: 11,
                 bold: true, color: C.amber, margin: 0, isTextBox: true } } },
  { text: { text: label,
      options: { x: x + 0.80, y: y + 0.16, w: 1.95, h: 0.30, fontFace: F.body, fontSize: T.label,
                 bold: true, color: C.paper, margin: 0, isTextBox: true } } },
  { text: { text: sub,
      options: { x: x + 0.22, y: y + 0.62, w: 2.50, h: 0.40, fontFace: F.body, fontSize: 11,
                 color: C.warm, margin: 0, isTextBox: true } } }
]);

pres.defineSlideMaster({
  title: "12_DECK_INDEX", background: { color: C.ink },
  objects: [
    bgDark(), rail(), ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.20, w: 4.30, h: 1.40,
                   fontFace: F.display, fontSize: 30, bold: true, color: C.white,
                   lineSpacingMultiple: 1.06, margin: 0, isTextBox: true },
        text: "Template Slide\nFamily" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 2.75, w: 4.30, h: 1.0,
                   fontFace: F.body, fontSize: T.body, color: C.warm, margin: 0, isTextBox: true },
        text: "Twelve layouts shared by Chemistry, Physics, and Geology." } },
    { image: { x: M.l, y: 4.10, w: 4.30, h: 2.42, path: IMG + "notebook_desk.png" } },
    ...tile("01", "Unit Title",   "large image + subject",  5.55, 1.20),
    ...tile("02", "Section Title","amber panel + image",    8.65, 1.20),
    ...tile("03", "Grouped Concept","chunked ideas",        5.55, 2.58),
    ...tile("04", "Divider",      "visual reset",           8.65, 2.58),
    ...tile("05", "Process",      "numbered steps",         5.55, 3.96),
    ...tile("06", "Concept Image","panel + key question",   8.65, 3.96),
    ...tile("07", "Comparison",   "three cards",            5.55, 5.34),
    ...tile("08", "Diagram",      "figure + annotation",    8.65, 5.34),
    ...footer(true)
  ]
});

module.exports = pres;

/* ================= DEMO SLIDES ================= */
if (require.main === module) {
  const set = (s, ph, txt) => s.addText(txt, { placeholder: ph });

  let s;

  s = pres.addSlide({ masterName: "01_UNIT_TITLE" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Matter &\nAtomic Structure");
  set(s, "subhead", "How we describe matter, and what the atom is actually made of.");
  set(s, "code", "U01 • S1.0");

  s = pres.addSlide({ masterName: "02_SECTION_TITLE" });
  set(s, "number", "01");
  set(s, "headline", "1.1\nMatter & Change");
  set(s, "subhead", "Tell a physical change from a chemical change, and defend the call with evidence.");
  set(s, "code", "U01 • S1.1");

  s = pres.addSlide({ masterName: "03_GROUPED_CONCEPT" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Physical Change vs. Chemical Change");
  set(s, "subhead", "Group the evidence first. Memorize the list second.");
  set(s, "c1_l", "PHYSICAL");
  set(s, "c2_l", "CHEMICAL");
  set(s, "c1_b", "Matter looks different, but the substance is still the same.\n\nMelting, cutting, dissolving.");
  set(s, "c2_b", "A new substance forms with new properties.\n\nGas, color change, heat or light, precipitate.");
  set(s, "mustwrite", "Evidence matters more than memorizing examples.");
  set(s, "code", "U01 • S1.1");

  s = pres.addSlide({ masterName: "04_DIVIDER" });
  set(s, "eyebrow", "1.2  •  HISTORY OF THE ATOMIC MODEL");
  set(s, "headline", "Models Change\nWhen Evidence Changes");
  set(s, "subhead", "Each model was the best reading of the evidence available at the time.");
  set(s, "code", "U01 • S1.2");

  s = pres.addSlide({ masterName: "05_PROCESS_TIMELINE" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Atomic Models Tell the Story of Evidence");
  set(s, "subhead", "Organize each model by the evidence that forced the change.");
  set(s, "s1_l", "Dalton");    set(s, "s1_b", "Atoms are solid particles, all alike for one element.");
  set(s, "s2_l", "Thomson");   set(s, "s2_b", "Cathode rays showed atoms contain negative particles.");
  set(s, "s3_l", "Rutherford");set(s, "s3_b", "Most alpha particles passed through gold foil.");
  set(s, "s4_l", "Bohr");      set(s, "s4_b", "Electrons are arranged by energy level.");
  set(s, "code", "U01 • S1.2");

  s = pres.addSlide({ masterName: "06_CONCEPT_IMAGE" });
  set(s, "eyebrow", "1.3  •  ATOMIC STRUCTURE");
  set(s, "headline", "Inside the Atom");
  set(s, "subhead", "Protons, neutrons, and electrons explain identity, mass, and charge.");
  set(s, "keyq", "What tells us which element an atom is?");
  set(s, "code", "U01 • S1.3");

  s = pres.addSlide({ masterName: "07_COMPARISON_CARDS" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "The Three Main Subatomic Particles");
  set(s, "subhead", "Each particle gets a visual space and a job, not a wall of bullets.");
  set(s, "k1_l", "PROTON");
  set(s, "k1_b", "+1 charge\nIn the nucleus\nDetermines the element");
  set(s, "k2_l", "NEUTRON");
  set(s, "k2_b", "0 charge\nIn the nucleus\nChanges the isotope");
  set(s, "k3_l", "ELECTRON");
  set(s, "k3_b", "\u22121 charge\nOutside the nucleus\nControls bonding");
  set(s, "mustwrite", "Atomic number = number of protons.");
  set(s, "code", "U01 • S1.3");

  s = pres.addSlide({ masterName: "08_DIAGRAM_ANNOTATION" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Reading Nuclear Notation");
  set(s, "subhead", "The diagram gets room; the rules sit beside it.");
  set(s, "diagram", "Hand-built nuclear\nnotation diagram");
  set(s, "a1_l", "PROTONS");  set(s, "a1_b", "Atomic number = 6");
  set(s, "a2_l", "NEUTRONS"); set(s, "a2_b", "Mass − protons = 14 − 6 = 8");
  set(s, "a3_l", "ELECTRONS");set(s, "a3_b", "Neutral atom: electrons = protons = 6");
  set(s, "code", "U01 • S1.3");

  s = pres.addSlide({ masterName: "09_EXAMPLE_PROBLEM" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Example: Counting Subatomic Particles");
  set(s, "subhead", "Work area stays empty on the projected copy.");
  set(s, "problem", "How many protons, neutrons, and electrons are in carbon-14?");
  set(s, "g1_l", "GIVEN");
  set(s, "g2_l", "NEED");
  set(s, "g1_b", "Carbon-14\nAtomic number = 6");
  set(s, "g2_b", "Protons\nNeutrons\nElectrons");
  set(s, "work", "");
  set(s, "mustwrite", "For neutral atoms: protons = electrons.");
  set(s, "code", "U01 • S1.3");

  s = pres.addSlide({ masterName: "10_WORKED_SOLUTION" });
  set(s, "eyebrow", "UNIT 01  •  CHEMISTRY");
  set(s, "headline", "Example: Average Atomic Mass");
  set(s, "subhead", "Data, process, and answer stay visually separate.");
  set(s, "f1_l", "FORMULA");
  set(s, "f1_b", "(mass × abundance)\n+ (mass × abundance)");
  set(s, "work", "(10.01 × 0.199)\n+ (11.01 × 0.801)\n= 10.81 amu");
  set(s, "mustwrite", "Average atomic mass is a weighted average of naturally occurring isotopes.");
  set(s, "code", "U01 • S1.5");

  s = pres.addSlide({ masterName: "11_GIVENS_EQUATION_ANSWER" });
  set(s, "eyebrow", "UNIT 02  •  PHYSICS");
  set(s, "headline", "Example: Acceleration From Motion Data");
  set(s, "subhead", "Same template, different course.");
  set(s, "problem", "A cart changes velocity from 3.2 m/s to 4.0 m/s in 4.0 s. Find acceleration.");
  set(s, "q1_l", "GIVEN");
  set(s, "q2_l", "EQUATION");
  set(s, "q1_b", "v₀ = 3.2 m/s\nv = 4.0 m/s\nt = 4.0 s");
  set(s, "q2_b", "a = Δv / t");
  set(s, "answer", "0.20 m/s²");
  set(s, "code", "U02 • S2.3");

  s = pres.addSlide({ masterName: "12_DECK_INDEX" });
  set(s, "eyebrow", "SHULL SCIENCE  •  DECK SYSTEM");
  set(s, "code", "TEMPLATE");

  pres.writeFile({ fileName: "/home/claude/tmpl/SHULL_Science_Slide_Template.pptx" })
    .then(f => console.log("wrote", f));
}
