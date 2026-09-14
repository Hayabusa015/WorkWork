# SHULL Science Preview Card

Use this small file for title-slide previews only. For final deck generation, read the
full design doc listed below.

## Files

- Full design doc: `bold-template-pack/templates/shull-science/design.md`
- Preview card: `bold-template-pack/templates/shull-science/preview.md`

## Selection Metadata

- Slug: `shull-science`
- Tagline: Matthew Shull's locked classroom system — Archivo on white or asphalt, one course colour, a 32px floor nobody reads below.
- Mood: legible, unfussy, built for a projector and the back row
- Tone: direct, teacherly, plain
- Formality: medium
- Density: low — a slide is what a student reads while listening, not a document
- Scheme: light by default; five named layouts run dark
- Best for: Any Chemistry, Physics or Geology section deck in the SHULL system. The
  only template here that is on-brand for Matthew's classroom.
- Avoid for: Anything outside SHULL. The palette, the geometry and the floor are locked
  by `brand/tokens.json` and are not stylistic choices.

## Visual Snapshot

Archivo on white, one course colour carrying identity, and a great deal of restraint.
Chemistry is Lab Lime, Physics is Quantum Gold, Geology is Terra Teal — the deck picks
exactly one and never mixes them. A 26px accent rail on the left
edge of the headline block and a 216px hairline under the
eyebrow are the only standing decoration. Title, section, divider, concept-image and
index slides invert to the asphalt ground, where the course display colour clears AAA.

Nothing on a student-facing slide is smaller than **32px** (16pt).
The running footer is the single exception. No full-bleed colour, no gradient behind
type, no decorative image under text — a projector in a bright classroom eats all three.

## Preview Ingredients

- Palette (Chemistry): #A3E635 on #FFFFFF;
  dark layouts invert to #14161B
- Typography: Trade Gothic Next, Archivo, Liberation Sans, sans-serif — one family, weight and colour carry hierarchy
- Signature move: the course accent rail down the left edge of the headline block
- Signature move: exactly one highlight block per slide, never two
- Signature move: `U## / S##.#` set plain in the footer — the rounded chip was
  withdrawn by decision, not by default
- Signature move: reserved height — the highlight block's space is subtracted before
  body text is placed, which is what stops text clipping

## Preview Rules

- Build exactly one title slide at 1920x1080 inside the fixed-stage model.
- Use the real unit and section title; never invent a `U##/S##.#` code.
- Never place internal workflow text on the slide.
- Do not read `template.html` for preview generation.
- Do not read other templates' `design.md` files.
