/* SHULL OS — twelve-layout slide template.
 *
 * Migrated from the legacy _Brand/Templates/build.js under SHULL-CHG-0013.
 * The twelve layouts, their geometry and their type scale are preserved. The
 * palette, the fonts and the token mechanism are not — see the change record for
 * all six findings, and legacy/slide-template/ for the byte-exact original.
 *
 *   SHULL_COURSE=chemistry node build.js out.pptx
 *
 * There is no per-course fork of this file and there never will be one. A course
 * is a parameter.
 */
const pptxgen = require("pptxgenjs");
const K = require("./tokens.generated");

const COURSE = (process.env.SHULL_COURSE || "chemistry").toLowerCase();
if (!K.courses[COURSE]) {
  console.error(`unknown course "${COURSE}" — expected one of ${Object.keys(K.courses).join(", ")}`);
  process.exit(1);
}
const OUT = process.argv[2] || `SHULL_Slide_Template_${COURSE}.pptx`;

const G = K.ground, CO = K.courses[COURSE], T = K.type, F = K.fonts;
const { W, H, M, RAIL, eyebrowY, hairlineY, hairlineW, headlineY, headlineH,
        subheadY, bodyTopY, footerY, mustWriteH, padX, padY } = K.geom;

/* Colour roles. Each name says what the colour is FOR, so a reader can check the
   choice against tokens.json rather than against taste. Every pairing below is
   measured in the change record; none of it is asserted here. */
const C = {
  darkGround:  G.asphalt,       // structural slides only
  lightGround: G.white,         // every content slide
  cardLight:   G.parchment,     // a callout surface on white — spec Part 7's sanctioned use
  cardDark:    G.graphite,      // a card on asphalt; the value step is the border
  cardEdge:    G.ruleHairline,
  textOnLight: G.asphalt,
  textOnDark:  G.parchment,
  mutedOnLight:G.graphite,
  mutedOnDark: G.mutedOnDark,
  /* ground.footer is the print running-footer colour and measures 4.98:1 on white -
   * below the 5.5 target in tokens.json. It is not changed here, because it is also the
   * printed lab template's footer and its value is not mine to move. The slide footer
   * uses ground.graphite instead (11.05:1), which costs nothing. The print-side question
   * is SHULL-CHG-0013 finding 8, and it is open. */
  footer:      G.graphite,
  accent:      CO.primary,      // fills, rails, panels, cues — display use
  accentText:  CO.primaryDeep,  // type on WHITE — SHULL-CHG-0008
};

/* Course colour is never a small label on a card, and this is measured, not taste.
 * primaryDeep on parchment is 4.77-4.82:1 and Terra Teal on graphite is 5.13:1 - all
 * below the 5.5 target in tokens.json, though above the WCAG AA floor. The accent
 * still carries the rails, the panels, the must-write cue and the numerals, every one
 * of which sits on white or asphalt and measures 7.3:1 or better.
 * Card labels are neutral, which is what the legacy template did too. */
const LABEL_ON_LIGHT_CARD = C.mutedOnLight;  // graphite on parchment,   11.05:1
const LABEL_ON_DARK_CARD  = C.mutedOnDark;   // mutedOnDark on graphite,  6.34:1

const CONTENT_W = W - M.l - M.r;

const pres = new pptxgen();

/* Every master's placeholder names, collected as the masters are defined rather than
 * maintained as a list beside them. build_deck.js checks against this, because
 * pptxgenjs silently turns an addText to a placeholder the master never declared into a
 * plain text box in a default font - which is how a stray DejaVu Sans run got into the
 * first CHEM deck built through the chain. Slide 1 uses 02_SECTION_TITLE, which has no
 * eyebrow. Nothing failed; the text simply arrived in the wrong font. */
const PLACEHOLDERS = {};
const SLOTS = {};   // name -> {x, y, w, h}, so a deck can fill a slot without knowing where it is
const defineMaster = (def) => {
  const phs = (def.objects || [])
    .filter(o => o.placeholder && o.placeholder.options && o.placeholder.options.name)
    .map(o => o.placeholder.options);
  PLACEHOLDERS[def.title] = phs.map(o => o.name);
  SLOTS[def.title] = {};
  for (const o of phs) SLOTS[def.title][o.name] = { x: o.x, y: o.y, w: o.w, h: o.h };
  pres.defineSlideMaster(def);
};

pres.layout = "LAYOUT_WIDE";
pres.author = "Matthew Shull";
pres.company = "SHULL Science";
pres.title = `SHULL Science — Slide Template (${CO.label})`;

/* ---------- furniture (fresh objects every call) ---------- */

const rail = () => ({ rect: { x: 0, y: 0, w: RAIL, h: H, fill: { color: C.accent } } });
const bgDark  = () => ({ rect: { x: 0, y: 0, w: W, h: H, fill: { color: C.darkGround } } });
const bgLight = () => ({ rect: { x: 0, y: 0, w: W, h: H, fill: { color: C.lightGround } } });

/* An empty image region. SHULL-CHG-0013 finding 4: the legacy masters baked seven
   full-resolution photographs in, which is why the template was 20 MB and why every
   deck arrived carrying an atom. The geometry is unchanged; the payload moved out. */
const imageSlot = (name, x, y, w, h, what, dark) => ([
  { rect: { x, y, w, h, fill: { color: dark ? C.cardDark : C.cardLight },
            line: { color: dark ? C.mutedOnDark : C.cardEdge, width: 1, dashType: "dash" } } },
  { placeholder: {
      options: { name, type: "pic", x, y, w, h, fontFace: F.body, fontSize: T.cardLabel,
                 color: dark ? C.mutedOnDark : C.mutedOnLight, align: "center", valign: "middle",
                 margin: 0, isTextBox: true },
      text: what } },
]);

const eyebrow = (dark) => ([
  { placeholder: {
      options: { name: "eyebrow", type: "body", x: M.l, y: eyebrowY, w: 7.0, h: 0.26,
                 fontFace: F.body, fontSize: T.eyebrow, bold: true, charSpacing: 1.6,
                 color: dark ? C.textOnDark : C.textOnLight, valign: "middle", margin: 0, isTextBox: true },
      text: `UNIT 00  •  ${CO.label}` } },
  { line: { x: M.l, y: hairlineY, w: hairlineW, h: 0, line: { color: C.accent, width: 1.75 } } },
]);

const footer = (dark) => ([
  { text: { text: "SHULL SCIENCE",
      options: { x: M.l, y: footerY, w: 4.0, h: 0.26, fontFace: F.body, fontSize: T.footer,
                 bold: true, charSpacing: 1.4, color: dark ? C.mutedOnDark : C.footer,
                 valign: "middle", margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: "code", type: "body", x: W - M.r - 3.0, y: footerY, w: 3.0, h: 0.26,
                 fontFace: F.body, fontSize: T.footer, bold: true, charSpacing: 1.4, align: "right",
                 color: dark ? C.mutedOnDark : C.footer, valign: "middle", margin: 0, isTextBox: true },
      text: "U00 • S0.0" } },
]);

/* The single write-this cue. One per slide, never two — two cues means students copy
   neither. Asphalt fill because a primaryDeep fill under parchment text measures 4.8:1,
   below the SHULL target of 5.5. */
const mustWrite = (y) => ([
  { rect: { x: M.l, y, w: CONTENT_W, h: mustWriteH, fill: { color: C.darkGround } } },
  { text: { text: "MUST WRITE",
      options: { x: M.l + padX, y: y + 0.06, w: 1.3, h: 0.22, fontFace: F.body, fontSize: 9,
                 bold: true, charSpacing: 1.5, color: C.accent, margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: "mustwrite", type: "body", x: M.l + 1.7, y: y + 0.08, w: CONTENT_W - 2.0,
                 h: 0.44, fontFace: F.body, fontSize: T.body, bold: true, color: C.textOnDark,
                 valign: "middle", margin: 0, isTextBox: true },
      text: "The one sentence students copy down." } },
]);

const card = (name, x, y, w, h, labelText, bodyText, opts = {}) => ([
  { rect: { x, y, w, h, fill: { color: opts.dark ? C.cardDark : C.cardLight },
            line: { color: opts.dark ? C.cardDark : C.cardEdge, width: 1 } } },
  { placeholder: {
      options: { name: name + "_l", type: "body", x: x + padX, y: y + padY, w: w - 2 * padX, h: 0.24,
                 fontFace: F.body, fontSize: T.cardLabel, bold: true, charSpacing: 1.2,
                 color: opts.dark ? LABEL_ON_DARK_CARD : LABEL_ON_LIGHT_CARD, margin: 0, isTextBox: true },
      text: labelText } },
  { placeholder: {
      options: { name: name + "_b", type: "body", x: x + padX, y: y + 0.5, w: w - 2 * padX, h: h - 0.72,
                 fontFace: F.body, fontSize: T.body,
                 color: opts.dark ? C.textOnDark : C.textOnLight, margin: 0, isTextBox: true },
      text: bodyText } },
]);

const headline = (dark, y = headlineY, w = CONTENT_W) => ({
  placeholder: {
    options: { name: "headline", type: "title", x: M.l, y, w, h: headlineH,
               fontFace: F.display, fontSize: T.headline, bold: true, align: "left",
               color: dark ? C.textOnDark : C.textOnLight, valign: "top", margin: 0, isTextBox: true },
    text: "Slide Headline Goes Here" },
});

const subhead = (dark, y = subheadY, w = CONTENT_W) => ({
  placeholder: {
    options: { name: "subhead", type: "body", x: M.l, y, w, h: 0.42,
               fontFace: F.body, fontSize: T.subhead,
               color: dark ? C.mutedOnDark : C.mutedOnLight, margin: 0, isTextBox: true },
    text: "One line that frames what students should look for." },
});

/* ================= THE TWELVE LAYOUTS ================= */

/* 01 — UNIT TITLE (dark, hero image right) */
defineMaster({
  title: "01_UNIT_TITLE", background: { color: C.darkGround },
  objects: [
    bgDark(),
    ...imageSlot("hero", 6.05, 1.70, 7.28, 4.10, "UNIT HERO IMAGE  •  16:9  •  1920×1080 min", true),
    rail(), ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.30, w: 5.05, h: 2.10,
                   fontFace: F.display, fontSize: T.unitTitle, bold: true, align: "left", color: C.textOnDark,
                   lineSpacingMultiple: 1.05, margin: 0, isTextBox: true },
        text: "Unit Title\nGoes Here" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 3.55, w: 4.85, h: 0.9,
                   fontFace: F.body, fontSize: T.subhead, color: C.mutedOnDark, margin: 0, isTextBox: true },
        text: "One sentence on what this unit is actually about." } },
    { rect: { x: M.l, y: 5.55, w: 1.55, h: 0.36, fill: { color: C.accent }, rectRadius: 0.18 } },
    { text: { text: "MR. SHULL",
        options: { x: M.l, y: 5.58, w: 1.55, h: 0.30, fontFace: F.body, fontSize: 10, bold: true,
                   charSpacing: 1.2, align: "center", color: C.darkGround, valign: "middle",
                   margin: 0, isTextBox: true } } },
    ...footer(true),
  ],
});

/* 02 — SECTION TITLE (accent panel left, image right) */
defineMaster({
  title: "02_SECTION_TITLE", background: { color: C.darkGround },
  objects: [
    bgDark(),
    { rect: { x: 0, y: 0, w: 4.35, h: H, fill: { color: C.accent } } },
    ...imageSlot("section", 4.90, 0.85, 7.75, 4.36, "SECTION IMAGE  •  16:9", true),
    { placeholder: {
        options: { name: "number", type: "body", x: 0.85, y: 0.55, w: 2.2, h: 0.95,
                   fontFace: F.display, fontSize: T.sectionNumber, bold: true, align: "left", color: C.darkGround,
                   margin: 0, isTextBox: true },
        text: "01" } },
    { text: { text: "SECTION TITLE",
        options: { x: 0.85, y: 1.62, w: 3.0, h: 0.24, fontFace: F.body, fontSize: T.eyebrow,
                   bold: true, charSpacing: 1.6, color: C.darkGround, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "headline", type: "title", x: 0.85, y: 2.02, w: 3.10, h: 1.85,
                   fontFace: F.display, fontSize: T.headline, bold: true, align: "left", color: C.darkGround,
                   lineSpacingMultiple: 1.06, margin: 0, isTextBox: true },
        text: "1.1\nSection Name" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: 0.85, y: 4.10, w: 3.10, h: 1.2,
                   fontFace: F.body, fontSize: T.body, color: C.darkGround, margin: 0, isTextBox: true },
        text: "What students should be able to do by the end." } },
    { text: { text: "SHULL SCIENCE",
        options: { x: 0.85, y: footerY, w: 3.0, h: 0.26, fontFace: F.body, fontSize: T.footer,
                   bold: true, charSpacing: 1.4, color: C.darkGround, valign: "middle",
                   margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "code", type: "body", x: W - M.r - 3.0, y: footerY, w: 3.0, h: 0.26,
                   fontFace: F.body, fontSize: T.footer, bold: true, charSpacing: 1.4, align: "right",
                   color: C.mutedOnDark, valign: "middle", margin: 0, isTextBox: true },
        text: "U00 • S0.0" } },
  ],
});

/* 03 — GROUPED CONCEPT (light, image + 2 cards + must-write) */
defineMaster({
  title: "03_GROUPED_CONCEPT", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false),
    ...imageSlot("concept", M.l, bodyTopY - 0.02, 5.10, 2.87, "CONCEPT IMAGE  •  16:9"),
    ...card("c1", 6.05, 2.60, 3.45, 2.87, "GROUP ONE", "The first idea, in one or two lines."),
    ...card("c2", 9.75, 2.60, 3.45, 2.87, "GROUP TWO", "The contrasting idea.", { dark: true }),
    ...mustWrite(5.82), ...footer(false),
  ],
});

/* 04 — SECTION DIVIDER (dark, full-bleed image, floating card) */
defineMaster({
  title: "04_DIVIDER", background: { color: C.darkGround },
  objects: [
    bgDark(),
    ...imageSlot("divider", 3.20, 0, 10.13, H, "FULL-BLEED CONCEPT IMAGE  •  one image, no decoration", true),
    { rect: { x: 0, y: 0, w: 4.30, h: H, fill: { color: C.darkGround } } },
    rail(),
    { rect: { x: 0.62, y: 1.62, w: 4.05, h: 4.02, fill: { color: C.darkGround },
              line: { color: C.accent, width: 1.25 } } },
    { placeholder: {
        options: { name: "eyebrow", type: "body", x: 0.92, y: 1.92, w: 3.45, h: 0.50,
                   fontFace: F.body, fontSize: T.eyebrow, bold: true, charSpacing: 1.5,
                   color: C.accent, margin: 0, isTextBox: true },
        text: "1.2  •  SECTION NAME" } },
    { placeholder: {
        options: { name: "headline", type: "title", x: 0.92, y: 2.52, w: 3.45, h: 1.55,
                   fontFace: F.display, fontSize: 26, bold: true, align: "left", color: C.textOnDark,
                   lineSpacingMultiple: 1.08, margin: 0, isTextBox: true },
        text: "The Big Idea\nOf This Section" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: 0.92, y: 4.22, w: 3.45, h: 1.20,
                   fontFace: F.body, fontSize: T.body, color: C.mutedOnDark, margin: 0, isTextBox: true },
        text: "Students see the story before the first bullet." } },
    ...footer(true),
  ],
});

/* 05 — PROCESS / TIMELINE (light, image band + 4 numbered steps) */
const step = (n, x) => ([
  { rect: { x, y: 5.05, w: 2.86, h: 1.30, fill: { color: C.cardLight },
            line: { color: C.cardEdge, width: 1 } } },
  { rect: { x: x + 0.16, y: 5.20, w: 0.34, h: 0.34, fill: { color: C.darkGround } } },
  { text: { text: String(n),
      options: { x: x + 0.16, y: 5.20, w: 0.34, h: 0.34, fontFace: F.body, fontSize: 11, bold: true,
                 color: C.accent, align: "center", valign: "middle", margin: 0, isTextBox: true } } },
  { placeholder: {
      options: { name: `s${n}_l`, type: "body", x: x + 0.60, y: 5.20, w: 2.10, h: 0.30,
                 fontFace: F.body, fontSize: T.cardLabel, bold: true, color: C.textOnLight,
                 valign: "middle", margin: 0, isTextBox: true },
      text: "Step " + n } },
  { placeholder: {
      options: { name: `s${n}_b`, type: "body", x: x + 0.16, y: 5.60, w: 2.54, h: 0.62,
                 fontFace: F.body, fontSize: T.body, color: C.textOnLight, margin: 0, isTextBox: true },
      text: "What changed, and why." } },
]);

defineMaster({
  title: "05_PROCESS_TIMELINE", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false),
    { rect: { x: M.l, y: bodyTopY, w: CONTENT_W, h: 2.20, fill: { color: C.darkGround } } },
    ...imageSlot("band", 3.55, 2.72, 6.20, 2.00, "PROCESS BAND  •  3:1  •  generate 16:9 and centre-crop", true),
    ...step(1, M.l), ...step(2, M.l + 3.02), ...step(3, M.l + 6.04), ...step(4, M.l + 9.06),
    ...footer(false),
  ],
});

/* 06 — CONCEPT + IMAGE PANEL (dark — the one deliberate dark content slide) */
defineMaster({
  title: "06_CONCEPT_IMAGE", background: { color: C.darkGround },
  objects: [
    bgDark(), rail(),
    { rect: { x: 6.75, y: 0.95, w: 5.85, h: 4.55, fill: { color: C.accent } } },
    ...imageSlot("concept", 6.95, 1.42, 5.45, 3.06, "CONCEPT IMAGE  •  16:9"),
    ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.30, w: 5.35, h: headlineH,
                   fontFace: F.display, fontSize: T.headline, bold: true, align: "left", color: C.textOnDark,
                   margin: 0, isTextBox: true },
        text: "Concept Headline" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 2.35, w: 5.35, h: 1.10,
                   fontFace: F.body, fontSize: T.body, color: C.mutedOnDark, margin: 0, isTextBox: true },
        text: "Keep it to what the image cannot say on its own." } },
    { rect: { x: M.l, y: 3.85, w: 5.35, h: 1.25, fill: { color: C.cardDark } } },
    { text: { text: "KEY QUESTION",
        options: { x: M.l + padX, y: 4.00, w: 3.0, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: LABEL_ON_DARK_CARD, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "keyq", type: "body", x: M.l + padX, y: 4.32, w: 4.91, h: 0.62,
                   fontFace: F.body, fontSize: T.body, bold: true, color: C.textOnDark,
                   margin: 0, isTextBox: true },
        text: "The one question this slide is asking." } },
    ...footer(true),
  ],
});

/* 07 — COMPARISON CARDS (light, 3 parallel cards) */
defineMaster({
  title: "07_COMPARISON_CARDS", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false),
    headline(false, headlineY, 8.05), subhead(false, subheadY, 8.05),
    { rect: { x: 9.20, y: 1.05, w: 3.38, h: 1.90, fill: { color: C.accent } } },
    ...imageSlot("aside", 9.45, 1.19, 2.88, 1.62, "SUPPORTING IMAGE"),
    ...card("k1", M.l, 3.05, 3.72, 2.55, "ITEM ONE", "Three parallel items.\nOne job each."),
    ...card("k2", M.l + 3.95, 3.05, 3.72, 2.55, "ITEM TWO", "Not a wall of bullets."),
    // All three neutral. "Three parallel items" means parallel: an unexplained dark card
    // emphasises whatever is listed third, which on the Isotopes deck was tritium - the
    // least important of the three. Design system: all-neutral, and the must-write bar
    // carries the one cue.
    ...card("k3", M.l + 7.90, 3.05, 3.72, 2.55, "ITEM THREE", "The third parallel item."),
    ...mustWrite(5.92), ...footer(false),
  ],
});

/* 08 — DIAGRAM + ANNOTATION (light, hand-built figure + 3 rule cards) */
defineMaster({
  title: "08_DIAGRAM_ANNOTATION", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false),
    { rect: { x: M.l, y: bodyTopY, w: 5.55, h: 3.55, fill: { color: C.cardLight },
              line: { color: C.cardEdge, width: 1 } } },
    { placeholder: {
        options: { name: "diagram", type: "body", x: M.l + 0.25, y: 2.90, w: 5.05, h: 3.0,
                   fontFace: F.display, fontSize: 20, color: C.mutedOnLight, align: "center",
                   valign: "middle", margin: 0, isTextBox: true },
        text: "Hand-built diagram here.\nAnything with a number or a label is built, not generated." } },
    ...card("a1", 6.70, bodyTopY, 6.05, 1.08, "LABEL ONE", "What this part of the diagram means."),
    ...card("a2", 6.70, 3.86, 6.05, 1.08, "LABEL TWO", "What this part of the diagram means."),
    ...card("a3", 6.70, 5.10, 6.05, 1.07, "LABEL THREE", "What this part of the diagram means."),
    ...footer(false),
  ],
});

/* 09 — EXAMPLE PROBLEM (light — problem, givens, EMPTY work area) */
defineMaster({
  title: "09_EXAMPLE_PROBLEM", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false),
    headline(false, headlineY, 8.60), subhead(false, subheadY, 8.60),
    { rect: { x: 9.75, y: 1.05, w: 2.83, h: 1.45, fill: { color: C.cardLight },
              line: { color: C.accent, width: 2 } } },
    ...imageSlot("aside", 10.13, 1.19, 2.08, 1.17, "SUPPORTING IMAGE"),
    // Graphite, not asphalt: the must-write bar below is the write-this cue and it needs
    // to be the only black block on the slide.
    { rect: { x: M.l, y: bodyTopY, w: 5.90, h: 1.15, fill: { color: C.cardDark } } },
    { text: { text: "PROBLEM",
        options: { x: M.l + padX, y: 2.76, w: 2.0, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.accent, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "problem", type: "body", x: M.l + padX, y: 3.06, w: 5.46, h: 0.60,
                   fontFace: F.body, fontSize: T.body, color: C.textOnDark, margin: 0, isTextBox: true },
        text: "State the problem in one sentence." } },
    ...card("g1", M.l, 3.95, 2.85, 1.90, "GIVEN", "What the problem hands you."),
    ...card("g2", M.l + 3.05, 3.95, 2.85, 1.90, "NEED", "What you are solving for."),
    { rect: { x: 6.85, y: bodyTopY, w: 5.73, h: 3.23, fill: { color: C.cardLight },
              line: { color: C.cardEdge, width: 1 } } },
    { text: { text: "WORK AREA",
        options: { x: 7.07, y: 2.80, w: 2.5, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.mutedOnLight, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "work", type: "body", x: 7.07, y: 3.15, w: 5.29, h: 2.50,
                   fontFace: F.body, fontSize: T.workArea, color: C.textOnLight, margin: 0, isTextBox: true },
        text: "Leave this blank in the projected copy. It is filled live on the board." } },
    ...mustWrite(6.05), ...footer(false),
  ],
});

/* 10 — WORKED SOLUTION (light — the 09 pair. Every example ships with its solution.) */
defineMaster({
  title: "10_WORKED_SOLUTION", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false),
    { rect: { x: M.l, y: bodyTopY, w: 4.55, h: 2.80, fill: { color: C.accent } } },
    ...imageSlot("data", M.l + 0.16, 2.78, 4.23, 2.48, "DATA IMAGE"),
    ...card("f1", 5.55, bodyTopY, 3.45, 2.80, "FORMULA", "The relationship, before any numbers."),
    { rect: { x: 9.20, y: bodyTopY, w: 3.38, h: 2.80, fill: { color: C.cardLight },
              line: { color: C.cardEdge, width: 1 } } },
    { text: { text: "WORK",
        options: { x: 9.42, y: 2.80, w: 2.0, h: 0.24, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.mutedOnLight, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "work", type: "body", x: 9.42, y: 3.14, w: 2.94, h: 2.10,
                   fontFace: F.body, fontSize: T.workArea, color: C.textOnLight, margin: 0, isTextBox: true },
        text: "The completed work,\nstep by step." } },
    ...mustWrite(5.62), ...footer(false),
  ],
});

/* 11 — GIVENS / EQUATION / ANSWER (light — any course) */
defineMaster({
  title: "11_GIVENS_EQUATION_ANSWER", background: { color: C.lightGround },
  objects: [
    bgLight(), ...eyebrow(false), headline(false), subhead(false),
    { rect: { x: M.l, y: bodyTopY, w: 5.10, h: 2.87, fill: { color: C.accent } } },
    ...imageSlot("setup", M.l + 0.16, 2.78, 4.78, 2.55, "SETUP IMAGE"),
    { rect: { x: 6.10, y: bodyTopY, w: 6.48, h: 1.05, fill: { color: C.cardDark } } },
    { text: { text: "PROBLEM",
        options: { x: 6.32, y: 2.74, w: 2.0, h: 0.22, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: C.accent, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "problem", type: "body", x: 6.32, y: 3.00, w: 6.04, h: 0.55,
                   fontFace: F.body, fontSize: T.body, color: C.textOnDark, margin: 0, isTextBox: true },
        text: "State the problem in one sentence." } },
    ...card("q1", 6.10, 3.85, 3.14, 1.64, "GIVEN", "Values the problem supplies."),
    ...card("q2", 9.44, 3.85, 3.14, 1.64, "EQUATION", "The relationship you will use."),
    { rect: { x: 6.10, y: 5.68, w: 6.48, h: 0.85, fill: { color: C.cardLight },
              line: { color: C.accent, width: 1.5 } } },
    { text: { text: "ANSWER",
        options: { x: 6.32, y: 5.78, w: 2.0, h: 0.22, fontFace: F.body, fontSize: 9, bold: true,
                   charSpacing: 1.4, color: LABEL_ON_LIGHT_CARD, margin: 0, isTextBox: true } } },
    { placeholder: {
        options: { name: "answer", type: "body", x: 6.32, y: 6.02, w: 6.04, h: 0.42,
                   fontFace: F.display, fontSize: 20, bold: true, color: C.textOnLight,
                   margin: 0, isTextBox: true },
        text: "with units" } },
    ...footer(false),
  ],
});

/* 12 — DECK INDEX (dark, reference. Delete before class.)
   SHULL-CHG-0013 finding 5: the legacy index listed 8 of 12 layouts, omitting the
   09/10 pair that carries the pedagogical rule. All twelve are listed now. */
const tile = (n, label, sub, x, y) => ([
  { rect: { x, y, w: 2.35, h: 1.02, fill: { color: C.cardDark } } },
  { text: { text: n,
      options: { x: x + 0.18, y: y + 0.14, w: 0.5, h: 0.24, fontFace: F.body, fontSize: 11,
                 bold: true, color: LABEL_ON_DARK_CARD, margin: 0, isTextBox: true } } },
  { text: { text: label,
      options: { x: x + 0.66, y: y + 0.14, w: 1.55, h: 0.28, fontFace: F.body, fontSize: T.cardLabel,
                 bold: true, color: C.textOnDark, margin: 0, isTextBox: true } } },
  { text: { text: sub,
      options: { x: x + 0.18, y: y + 0.52, w: 2.02, h: 0.38, fontFace: F.body, fontSize: 11,
                 color: C.mutedOnDark, margin: 0, isTextBox: true } } },
]);

const INDEX = [
  ["01", "Unit Title",    "opens a unit"],        ["02", "Section Title", "opens a section"],
  ["03", "Grouped",       "two contrasting ideas"],["04", "Divider",      "visual reset"],
  ["05", "Process",       "four numbered steps"], ["06", "Concept Image", "panel + key question"],
  ["07", "Comparison",    "three parallel items"],["08", "Diagram",       "figure + annotation"],
  ["09", "Example",       "empty work area"],     ["10", "Solution",      "pairs with 09"],
  ["11", "Given/Eq/Ans",  "any course"],          ["12", "Deck Index",    "delete before class"],
];

defineMaster({
  title: "12_DECK_INDEX", background: { color: C.darkGround },
  objects: [
    bgDark(), rail(), ...eyebrow(true),
    { placeholder: {
        options: { name: "headline", type: "title", x: M.l, y: 1.20, w: 3.50, h: 1.40,
                   fontFace: F.display, fontSize: 30, bold: true, align: "left", color: C.textOnDark,
                   lineSpacingMultiple: 1.06, margin: 0, isTextBox: true },
        text: "Template Slide\nFamily" } },
    { placeholder: {
        options: { name: "subhead", type: "body", x: M.l, y: 2.75, w: 3.50, h: 1.6,
                   fontFace: F.body, fontSize: T.body, color: C.mutedOnDark, margin: 0, isTextBox: true },
        text: "Twelve layouts shared by Chemistry, Physics, and Geology.\n\nNew slide → Layout → pick one. Never build from scratch." } },
    ...INDEX.flatMap(([n, l, s], i) =>
      tile(n, l, s, 4.85 + (i % 3) * 2.55, 1.20 + Math.floor(i / 3) * 1.22)),
    ...footer(true),
  ],
});

module.exports = pres;
module.exports.PLACEHOLDERS = PLACEHOLDERS;
module.exports.SLOTS = SLOTS;

/* ================= DEMO DECK ================= */
/* One slide per layout, so a build can be looked at rather than trusted. The content
   is deliberately structural placeholder text, NOT teaching content: a course fact in
   a template would put it in two places, which validate_layers.py exists to catch. */
if (require.main === module) {
  const set = (s, ph, txt) => s.addText(txt, { placeholder: ph });
  const CODE = "U00 • S0.0";
  const EYE = `UNIT 00  •  ${CO.label}`;

  /* Every placeholder in every layout gets filled, because an unfilled placeholder
     renders as nothing and a preview you cannot read the type on cannot be QA'd -
     which is how the legacy deck shipped slides 8 and 17 with clipped text. */
  const common = (s, dark) => { set(s, "eyebrow", EYE); set(s, "code", CODE); };
  const HEAD = "Slide Headline Goes Here";
  const SUB  = "One line that frames what students should look for.";
  const MW   = "The one sentence students copy down.";

  let s;

  s = pres.addSlide({ masterName: "01_UNIT_TITLE" }); common(s);
  set(s, "headline", "Unit Title\nGoes Here");
  set(s, "subhead", "One sentence on what this unit is actually about.");

  s = pres.addSlide({ masterName: "02_SECTION_TITLE" });
  set(s, "number", "01"); set(s, "code", CODE);
  set(s, "headline", "0.0\nSection Name");
  set(s, "subhead", "What students should be able to do by the end.");

  s = pres.addSlide({ masterName: "03_GROUPED_CONCEPT" }); common(s);
  set(s, "headline", HEAD); set(s, "subhead", SUB);
  set(s, "c1_l", "GROUP ONE"); set(s, "c1_b", "The first idea, in one or two lines.\n\nSupporting detail.");
  set(s, "c2_l", "GROUP TWO"); set(s, "c2_b", "The contrasting idea.\n\nSupporting detail.");
  set(s, "mustwrite", MW);

  s = pres.addSlide({ masterName: "04_DIVIDER" }); set(s, "code", CODE);
  set(s, "eyebrow", "0.0  •  SECTION NAME");
  set(s, "headline", "The Big Idea\nOf This Section");
  set(s, "subhead", "Students see the story before the first bullet.");

  s = pres.addSlide({ masterName: "05_PROCESS_TIMELINE" }); common(s);
  set(s, "headline", HEAD); set(s, "subhead", SUB);
  for (let n = 1; n <= 4; n++) { set(s, `s${n}_l`, "Step " + n); set(s, `s${n}_b`, "What changed, and why."); }

  s = pres.addSlide({ masterName: "06_CONCEPT_IMAGE" }); common(s);
  set(s, "headline", "Concept Headline");
  set(s, "subhead", "Keep it to what the image cannot say on its own.");
  set(s, "keyq", "The one question this slide is asking.");

  s = pres.addSlide({ masterName: "07_COMPARISON_CARDS" }); common(s);
  set(s, "headline", HEAD); set(s, "subhead", SUB);
  set(s, "k1_l", "ITEM ONE");   set(s, "k1_b", "Three parallel items.\nOne job each.");
  set(s, "k2_l", "ITEM TWO");   set(s, "k2_b", "Not a wall of bullets.");
  set(s, "k3_l", "ITEM THREE"); set(s, "k3_b", "The third parallel item.");
  set(s, "mustwrite", MW);

  s = pres.addSlide({ masterName: "08_DIAGRAM_ANNOTATION" }); common(s);
  set(s, "headline", HEAD); set(s, "subhead", "The diagram gets room; the rules sit beside it.");
  set(s, "diagram", "Hand-built diagram here.\nAnything with a number or a label is built, not generated.");
  set(s, "a1_l", "LABEL ONE");   set(s, "a1_b", "What this part of the diagram means.");
  set(s, "a2_l", "LABEL TWO");   set(s, "a2_b", "What this part of the diagram means.");
  set(s, "a3_l", "LABEL THREE"); set(s, "a3_b", "What this part of the diagram means.");

  s = pres.addSlide({ masterName: "09_EXAMPLE_PROBLEM" }); common(s);
  set(s, "headline", "Example: Problem Headline");
  set(s, "subhead", "Work area stays empty on the projected copy.");
  set(s, "problem", "State the problem in one sentence.");
  set(s, "g1_l", "GIVEN"); set(s, "g1_b", "What the problem hands you.");
  set(s, "g2_l", "NEED");  set(s, "g2_b", "What you are solving for.");
  set(s, "work", "");
  set(s, "mustwrite", MW);

  s = pres.addSlide({ masterName: "10_WORKED_SOLUTION" }); common(s);
  set(s, "headline", "Example: Worked Solution");
  set(s, "subhead", "Data, process, and answer stay visually separate.");
  set(s, "f1_l", "FORMULA"); set(s, "f1_b", "The relationship,\nbefore any numbers.");
  set(s, "work", "The completed work,\nstep by step.");
  set(s, "mustwrite", MW);

  s = pres.addSlide({ masterName: "11_GIVENS_EQUATION_ANSWER" }); common(s);
  set(s, "headline", "Example: Given, Equation, Answer");
  set(s, "subhead", "Same template, any course.");
  set(s, "problem", "State the problem in one sentence.");
  set(s, "q1_l", "GIVEN");    set(s, "q1_b", "Values the problem supplies.");
  set(s, "q2_l", "EQUATION"); set(s, "q2_b", "The relationship you will use.");
  set(s, "answer", "with units");

  s = pres.addSlide({ masterName: "12_DECK_INDEX" });
  set(s, "eyebrow", "SHULL SCIENCE  •  DECK SYSTEM");
  set(s, "code", "TEMPLATE");
  set(s, "headline", "Template Slide\nFamily");
  set(s, "subhead", "Twelve layouts shared by Chemistry, Physics, and Geology.\n\nNew slide \u2192 Layout \u2192 pick one. Never build from scratch.");

  pres.writeFile({ fileName: OUT }).then(f => console.log("wrote", f, `(${CO.label})`));
}
