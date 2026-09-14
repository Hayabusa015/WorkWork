# SHULL Science — design doc

GENERATED FROM brand/tokens.json BY scripts/build_slide_html_template.py — DO NOT EDIT.
Re-run the script after changing any token. Hand-editing a value here puts it in two
places, which is the defect the whole repository is built to prevent.

**Authority.** `brand/tokens.json` owns every colour and measurement below.
`courses/<course>/DECISIONS.md` owns every unit and section code. This file is a
translation of those into the 1920x1080 stage, not a new design.

---

## 1. The stage is the SHULL slide, in different units

SHULL Slide System v2 is 13.333in x 7.5in (16:9).
At 144 px/in that is **1920 x 1080** — the same rectangle this skill already mandates.
So the fixed-stage rule is satisfied by construction: **inches x 144 = px**,
**points x 2 = px**. Do not reflow slide content for phones; the whole stage scales.

| Measurement | SHULL (in) | Stage (px) |
|---|---|---|
| Margin left / right | 0.75 / 0.75 | 108 / 108 |
| Margin top / bottom | 0.62 / 0.55 | 89 / 79 |
| Accent rail width | 0.18 | 26 |
| Eyebrow baseline Y | 0.42 | 60 |
| Hairline Y / width | 0.74 / 1.5 | 107 / 216 |
| Headline Y / height | 1.02 / 0.95 | 147 / 137 |
| Subhead Y | 2.02 | 291 |
| Body top Y | 2.62 | 377 |
| Footer Y | 6.98 | 1005 |
| Card padding h / v | 0.22 / 0.18 | 32 / 26 |

## 2. Type — one family, and a floor

`Trade Gothic Next, Archivo, Liberation Sans, sans-serif`. Trade Gothic Next is Monotype-licensed and is never committed to this
repository; Archivo is the OFL fallback that actually renders, and it ships in
`brand/fonts/`. **Do not substitute a "more distinctive" face.** One family; weight,
size and colour carry the hierarchy.

| Role | pt | px |
|---|---|---|
| Unit title | 40 | 80 |
| Section number | 44 | 88 |
| Headline | 28 | 56 |
| Subhead | 17 | 34 |
| Body | 16 | 32 |
| Work area | 19 | 38 |
| Card label | 12 | 24 |
| Eyebrow | 11 | 22 |
| Footer | 10 | 20 |

**The floor is 16pt = 32px** and it is LOCKED: nothing a student
reads from a seat goes below it. The running footer at 20px is the
only exception on the page.

## 3. Palette — one course per deck

- **Lab Lime** `#A3E635` — display colour. 12.0:1 on the dark ground (AAA); NOT type on white. **Aqua** `#22D3EE` — secondary display. **Lab Lime Deep** `#4D730E` — the only one of the three that may set type on a light ground (5.56:1 on white).

- **Quantum Gold** `#F5B82E` — display colour. 10.15:1 on the dark ground (AAA); NOT type on white. **Deep Purple** `#8B5CF6` — secondary display. **Quantum Gold Deep** `#896107` — the only one of the three that may set type on a light ground (5.56:1 on white).

- **Terra Teal** `#16B8A6` — display colour. 7.27:1 on the dark ground (AAA); NOT type on white. **Rust Orange** `#E85D24` — secondary display. **Terra Teal Deep** `#0E766A` — the only one of the three that may set type on a light ground (5.5:1 on white).

Grounds: white `#FFFFFF` by default, asphalt `#14161B` on the
dark layouts, parchment `#EDF0E5` as a special-purpose surface only.
Muted-on-dark `#BDB6AA`, hairline `#C8CDC2`,
footer `#61675B`.

**A deck uses exactly one course.** Mixing Lab Lime and Terra Teal in one deck is a
defect, not a palette. Semantic colour (danger, caution, success) always outranks course
identity — a safety warning is never restyled into the course colour.

These run dark: `01_UNIT_TITLE`, `02_SECTION_TITLE`, `04_DIVIDER`, `06_CONCEPT_IMAGE`, `12_DECK_INDEX`.

## 4. Line caps — the rule that prevents clipping

Text is not allowed to overflow its block, and the fix is never to shrink below the
floor. Caps per slide:

- `contentWithHighlight`: 3
- `contentWithoutHighlight`: 5
- `vocabularyTerms`: 4
- `workedExampleSteps`: 4
- `tableDataRows`: 6

**Reserved height.** Subtract the highlight block's space *before* placing body text,
never overlay it afterwards. Overlaying is how text clipped in v1, and it is the
highest-priority visual defect in `standards/QA_GATE.md`.

**One highlight block per slide. Never two.**

## 5. What this template refuses

The parent skill tells you to vary fonts and palettes, use atmospheric gradients and
layered backgrounds, and "think outside the box". For a SHULL classroom deck that
guidance is overridden:

- No font other than the stack above.
- No palette other than the selected course's.
- No gradient behind type, no image under text, no full-bleed colour field.
- No animation that moves content a student is reading. Entrance reveals on a slide's
  first paint are fine; looping motion behind text is not.
- No invented `U##/S##.#` code, unit title, lab, date or policy. Every code must exist
  in that course's `DECISIONS.md` — check before building. This is the check that
  would have caught the Geology numbering error before a packet printed wrong.

## 6. Footer

`U## / S##.#` set plain at Y 1005px in
20px footer grey. The rounded chip that print documents carry was
**withdrawn** for slides by user decision (SHULL-CHG-0013 finding 3), not by oversight.
Restoring the slide-to-print chip link would be a new proposal.
