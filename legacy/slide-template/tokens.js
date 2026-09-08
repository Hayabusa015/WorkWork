/* SHULL Science — Slide Template tokens
   Palette and type scale extracted from Matt's approved prototype deck.
   Fonts moved from Aptos (Microsoft default, not portable) to Poppins. */

const C = {
  ink:      "111111",  // primary dark background
  inkCard:  "2F2F2F",  // dark card on dark ground
  inkSoft:  "444444",  // dark card border / secondary dark
  amber:    "FFCB74",  // accent — panels, must-write, rails
  amberPale:"FFE7B3",  // amber tint, answer boxes
  warm:     "BDB6AA",  // warm gray — secondary text on dark
  paper:    "F6F6F6",  // light background
  paperWarm:"EDEAE3",  // warm light background
  cardEdge: "E1E1E1",  // card border on light
  white:    "FFFFFF",
  mute:     "777777"   // secondary text on light
};

/* Type scale. Student-facing body never below 16.
   11–12pt is permitted ONLY for eyebrows, card labels, and footers. */
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

const W = 13.333, H = 7.5;          // slide, inches
const M = { l: 0.75, r: 0.75, t: 0.62, b: 0.55 };  // safe margins
const RAIL = 0.18;                   // amber left rail width

module.exports = { C, T, F, W, H, M, RAIL };
