/* SHULL Science — Slide Template tokens, PHYSICS ONLY
   Palette: "Quiet Voltage" — Porcelain / Chrome / Violet / Violet Static / Ink Black.
   Sampled from Matt's reference image, 2026-09-06.

   Physics is a declared course palette exception, the same way Geology's earth
   palette is. Chemistry and Geology keep `tokens.js` (Ink / Amber) untouched.

   Physics collapses the Slide System v2 medium split: one palette runs both the
   projected deck and the printed handouts. Violet on Porcelain measures 9.8:1,
   so it holds up in a lit room, and Porcelain is light enough to stay ink-cheap.

   The key NAMES below are the ones build.js already consumes. Nothing in
   build.js changes — only which token file it is handed. */

const C = {
  ink:      "0B0A0E",  // Ink Black — dark grounds, text, number squares
  inkCard:  "1A1622",  // dark card on dark ground
  inkSoft:  "3A2168",  // Violet — dark card border, secondary structure
  amber:    "A97BFF",  // Violet Static — accent panels, rails, must-write cue
  amberPale:"E8DCFF",  // violet tint — answer boxes
  warm:     "B9ADA6",  // Chrome — secondary text on dark
  paper:    "E7DDD7",  // Porcelain — light background
  paperWarm:"EFE8E3",  // warm porcelain
  cardEdge: "CFC5BF",  // hairline card border on light
  white:    "F7F3F0",  // Chrome Light — card fill on light
  mute:     "6B6157"   // secondary text on light
};

/* Type scale and geometry are unchanged — this is a colour exception only. */
const T = {
  deckTitle: 40,
  headline:  28,
  sectionNo: 44,
  subhead:   17,
  body:      16,
  cardBody:  16,
  label:     12,
  eyebrow:   11,
  footer:    10
};

const F = { display: "Poppins", body: "Poppins" };

const W = 13.333, H = 7.5;
const M = { l: 0.75, r: 0.75, t: 0.62, b: 0.55 };
const RAIL = 0.18;

module.exports = { C, T, F, W, H, M, RAIL };
