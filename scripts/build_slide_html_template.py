#!/usr/bin/env python3
"""Generate the SHULL template for the vendored frontend-slides skill.

frontend-slides builds HTML decks on a mandatory 1920x1080 fixed stage. SHULL's
Slide System v2 is 13.333in x 7.5in. At 144 px/in those are the same rectangle -
1920 x 1080 exactly - so every locked SHULL measurement converts to stage pixels
by x144 (inches) or x2 (points). The brand is not compromised to fit this skill;
it is the same geometry in different units.

That matters because the skill's own instructions tell the model to vary fonts and
palettes and "think outside the box". For a classroom deck that is wrong: the
palette is locked, the face is Archivo, and the 16pt floor is what a student in the
back row can read. This template is the on-brand option that makes the skill safe
to point at SHULL work.

    python3 scripts/build_slide_html_template.py
"""
import json, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, ".claude", "skills", "frontend-slides",
                   "bold-template-pack", "templates", "shull-science")

t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
g, courses, typ, geom = t["ground"], t["courses"], t["typography"], t["slideGeometry"]
scale = json.loads(open(os.path.join(REPO, "templates", "slide", "tokens.generated.js"))
                   .read().split("module.exports =", 1)[1].rstrip().rstrip(";"))["type"]

PX = 144          # px per inch on a 1920x1080 stage
PT = 2            # px per point (144/72)
inpx = lambda v: round(v * PX)
ptpx = lambda v: round(v * PT)

FLOOR_PT = typ["floors"]["slideContent"]["pt"]
m = geom["margins"]


def palette_row(key):
    c = courses[key]
    return (f"- **{c['primary']['name']}** `{c['primary']['hex']}` — display colour. "
            f"{c['primary']['measured']['onAsphalt']}:1 on the dark ground (AAA); "
            f"NOT type on white. **{c['secondary']['name']}** `{c['secondary']['hex']}` — "
            f"secondary display. **{c['primaryDeep']['name']}** `{c['primaryDeep']['hex']}` — "
            f"the only one of the three that may set type on a light ground "
            f"({c['primaryDeep']['measured']['onWhite']}:1 on white).")


preview = f"""# SHULL Science Preview Card

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
exactly one and never mixes them. A {inpx(geom['railWidthIn'])}px accent rail on the left
edge of the headline block and a {inpx(geom['hairlineWidthIn'])}px hairline under the
eyebrow are the only standing decoration. Title, section, divider, concept-image and
index slides invert to the asphalt ground, where the course display colour clears AAA.

Nothing on a student-facing slide is smaller than **{ptpx(FLOOR_PT)}px** ({FLOOR_PT}pt).
The running footer is the single exception. No full-bleed colour, no gradient behind
type, no decorative image under text — a projector in a bright classroom eats all three.

## Preview Ingredients

- Palette (Chemistry): {courses['chemistry']['primary']['hex']} on {g['white']['hex']};
  dark layouts invert to {g['asphalt']['hex']}
- Typography: {typ['stack']} — one family, weight and colour carry hierarchy
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
"""

design = f"""# SHULL Science — design doc

GENERATED FROM brand/tokens.json BY scripts/build_slide_html_template.py — DO NOT EDIT.
Re-run the script after changing any token. Hand-editing a value here puts it in two
places, which is the defect the whole repository is built to prevent.

**Authority.** `brand/tokens.json` owns every colour and measurement below.
`courses/<course>/DECISIONS.md` owns every unit and section code. This file is a
translation of those into the 1920x1080 stage, not a new design.

---

## 1. The stage is the SHULL slide, in different units

SHULL Slide System v2 is {geom['widthIn']}in x {geom['heightIn']}in ({geom['aspect']}).
At 144 px/in that is **1920 x 1080** — the same rectangle this skill already mandates.
So the fixed-stage rule is satisfied by construction: **inches x 144 = px**,
**points x 2 = px**. Do not reflow slide content for phones; the whole stage scales.

| Measurement | SHULL (in) | Stage (px) |
|---|---|---|
| Margin left / right | {m['left']} / {m['right']} | {inpx(m['left'])} / {inpx(m['right'])} |
| Margin top / bottom | {m['top']} / {m['bottom']} | {inpx(m['top'])} / {inpx(m['bottom'])} |
| Accent rail width | {geom['railWidthIn']} | {inpx(geom['railWidthIn'])} |
| Eyebrow baseline Y | {geom['eyebrowY']} | {inpx(geom['eyebrowY'])} |
| Hairline Y / width | {geom['hairlineY']} / {geom['hairlineWidthIn']} | {inpx(geom['hairlineY'])} / {inpx(geom['hairlineWidthIn'])} |
| Headline Y / height | {geom['headlineY']} / {geom['headlineHeightIn']} | {inpx(geom['headlineY'])} / {inpx(geom['headlineHeightIn'])} |
| Subhead Y | {geom['subheadY']} | {inpx(geom['subheadY'])} |
| Body top Y | {geom['bodyTopY']} | {inpx(geom['bodyTopY'])} |
| Footer Y | {geom['footerY']} | {inpx(geom['footerY'])} |
| Card padding h / v | {geom['cardPaddingIn']['horizontal']} / {geom['cardPaddingIn']['vertical']} | {inpx(geom['cardPaddingIn']['horizontal'])} / {inpx(geom['cardPaddingIn']['vertical'])} |

## 2. Type — one family, and a floor

`{typ['stack']}`. Trade Gothic Next is Monotype-licensed and is never committed to this
repository; Archivo is the OFL fallback that actually renders, and it ships in
`brand/fonts/`. **Do not substitute a "more distinctive" face.** One family; weight,
size and colour carry the hierarchy.

| Role | pt | px |
|---|---|---|
| Unit title | {scale['unitTitle']} | {ptpx(scale['unitTitle'])} |
| Section number | {scale['sectionNumber']} | {ptpx(scale['sectionNumber'])} |
| Headline | {scale['headline']} | {ptpx(scale['headline'])} |
| Subhead | {scale['subhead']} | {ptpx(scale['subhead'])} |
| Body | {scale['body']} | {ptpx(scale['body'])} |
| Work area | {scale['workArea']} | {ptpx(scale['workArea'])} |
| Card label | {scale['cardLabel']} | {ptpx(scale['cardLabel'])} |
| Eyebrow | {scale['eyebrow']} | {ptpx(scale['eyebrow'])} |
| Footer | {scale['footer']} | {ptpx(scale['footer'])} |

**The floor is {FLOOR_PT}pt = {ptpx(FLOOR_PT)}px** and it is LOCKED: nothing a student
reads from a seat goes below it. The running footer at {ptpx(scale['footer'])}px is the
only exception on the page.

## 3. Palette — one course per deck

{palette_row('chemistry')}

{palette_row('physics')}

{palette_row('geology')}

Grounds: white `{g['white']['hex']}` by default, asphalt `{g['asphalt']['hex']}` on the
dark layouts, parchment `{g['parchment']['hex']}` as a special-purpose surface only.
Muted-on-dark `{g['mutedOnDark']['hex']}`, hairline `{g['ruleHairline']['hex']}`,
footer `{g['footer']['hex']}`.

**A deck uses exactly one course.** Mixing Lab Lime and Terra Teal in one deck is a
defect, not a palette. Semantic colour (danger, caution, success) always outranks course
identity — a safety warning is never restyled into the course colour.

These run dark: {', '.join('`' + x + '`' for x in geom['darkGroundLayouts'])}.

## 4. Line caps — the rule that prevents clipping

Text is not allowed to overflow its block, and the fix is never to shrink below the
floor. Caps per slide:

{chr(10).join(f'- `{k}`: {v}' for k, v in geom['lineCaps'].items())}

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

`U## / S##.#` set plain at Y {inpx(geom['footerY'])}px in
{ptpx(scale['footer'])}px footer grey. The rounded chip that print documents carry was
**withdrawn** for slides by user decision (SHULL-CHG-0013 finding 3), not by oversight.
Restoring the slide-to-print chip link would be a new proposal.
"""

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "preview.md"), "w").write(preview)
open(os.path.join(OUT, "design.md"), "w").write(design)
print(f"build_slide_html_template: wrote {os.path.relpath(OUT, REPO)}/{{preview,design}}.md")
