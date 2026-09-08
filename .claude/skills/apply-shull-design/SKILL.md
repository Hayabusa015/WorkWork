---
name: apply-shull-design
description: Apply the SHULL Studio design system to a deliverable - course identity colours, typography, density, decoration, print discipline, and slide geometry. Use whenever building or revising any document, presentation, assessment, lab, or activity, and whenever checking whether something is on-brand.
---

# apply-shull-design

Rules: `brand/SHULL_DESIGN_SYSTEM.md`. Values: `brand/tokens.json`. This is the procedure.

## Every time

1. **Read `brand/tokens.json`.** Never type a value from memory. `scripts/validate_tokens.py` fails
   the build on a hex written anywhere else.
2. **Identify the course** and use its identity colours. Chemistry looks like SHULL Studio
   Chemistry, not like Physics.
3. **Identify the medium** — print or projected. It changes what is permitted.

## The rule most often broken

> On a light ground, coloured type uses the course's **`primaryDeep`**.
> On a dark ground, coloured type uses **`primary`** or **`secondary`**.
> Neither is ever type on the other.

**Check `measured.onWhiteVerdict` in `tokens.json` before colouring any text.** Four of the six
display colours read `NOT TYPE` on white — they were selected for a dark ground before white became
the default.

Display colours remain correct for fills, highlight blocks, rules, chips, tag pills, and borders.

## Grayscale

Any two colours carrying a categorical distinction must clear `rules.grayscaleSeparationMin`, **or**
differ by border and label as well as fill.

**Geology always needs the border-and-label treatment** when both its colours appear together —
they sit six grey levels apart, and Geology handouts are photocopied more than any others.

## Semantic colour beats course colour

A hazard warning is red because it is a warning. **Do not substitute a course colour to avoid using
a semantically correct one.**

## Print

Outline and rule treatments. No solid fills beyond a small tag, chip, or icon. No full-page banners,
no shaded section backgrounds, no medium-saturation table shading. Hairline table rules. Hatched
chart areas, not tinted.

## Type

Use `typography.stack`. Never a font outside it. Respect `typography.floors`. **If content exceeds a
line cap, split — never shrink type to fit.**

## Finishing

Run `standards/QA_GATE.md`. Confirm `pdffonts` shows Archivo. **If it shows DejaVu or Liberation,
the substitution did not take and you are looking at different metrics than the classroom copy.**
