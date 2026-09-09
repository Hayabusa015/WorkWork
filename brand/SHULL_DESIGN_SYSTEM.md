# SHULL Studio — Master Design System

**Authority:** This file and `brand/tokens.json` are the design system. Nothing else states a
design rule. Where a skill needs one, it links here.
**Values:** Every hex, size, and measurement lives in `brand/tokens.json`. **This document names
tokens; it never repeats their values.** `scripts/validate_tokens.py` enforces that.
**Change control:** Secretary change record required. See `governance/CHANGE_CONTROL.md`.

---

## 1. What this system is

SHULL Studio is one shared design language with three course identities.

```
        SHULL STUDIO
   shared design language
             │
   ┌─────────┼─────────┐
Chemistry  Physics  Geology
```

Chemistry should look like SHULL Studio Chemistry. Physics like SHULL Studio Physics. Geology like
SHULL Studio Geology. **They must not look like three unrelated brands.**

All three share: typography, layout philosophy, white, neutrals, hierarchy, spacing, document and
presentation philosophy, and the quality standard. Each differs only in its identity colours and
its icon vocabulary.

### The visual philosophy

Clean. Modern. Mostly light. Professional. Human. Intentional.

Products should feel professional, intentional, human, teacher-created, purposeful, and visually
coherent. They should not feel generic, sterile, corporate, over-templated, AI-generated, or
soulless.

The failure this exists to prevent has a name and a definition, and it is the central
quality-control principle of the whole system:

> **AI slop is "generic with no soul."**

The operative test, applied to every finished artifact:

> **Would this actually look like something the teacher would hand to students?**

If not, revise it. `standards/ANTI_AI_SLOP_STANDARD.md` is the binding elaboration of that test.

---

## 2. Backgrounds

**White is the default.** It is an official design token, not the absence of one.

| Surface | Default |
|---|---|
| Documents | `ground.white` |
| Student materials | `ground.white`, essentially always |
| Presentations | `ground.white` or a light branded surface |
| Title slides, section dividers, major visual moments, image-heavy slides | A dark ground may be used |

**Dark grounds are structural, not decorative.** Unit title, section divider, unit summary, deck
index — and one deliberate exception layout where an image panel carries the slide. A dark
background is never chosen because a dark colour exists in the palette.

**Parchment is not a background.** `ground.parchment` remains an official SHULL colour and is now a
special-purpose branded surface: selected presentation surfaces, callout areas, selected branded
materials, intentional variation. It does not replace white. *(It was the default until 2026-09-07;
see CONFLICT-12.)*

---

## 3. Colour

### The hierarchy

```
PRIMARY  →  SECONDARY  →  SEMANTIC  →  NEUTRAL  →  WHITE
```

- **Primary** — the course's main identity colour.
- **Secondary** — supporting course identity.
- **Semantic** — used for *meaning*, not branding: `semantic.danger`, `semantic.caution`,
  `semantic.success`.
- **Neutral** — `ground.asphalt`, `ground.graphite`.
- **White** — `ground.white`.

### Course identity overrides nothing

**Semantic colours are permitted even when they are not in the course palette.** A safety warning is
red because it is a warning. Do **not** substitute a course colour to avoid using a semantically
correct one — a Chemistry hazard note in Lab Lime is a defect, not brand consistency.

### Course-first, but functional

Use the course palette. Use semantic colour where meaning requires it. Beyond that, stop.

- Colour must have a purpose.
- Do not turn course materials into rainbow documents.
- Do not use a colour because it is available.

### The rule that governs coloured type — read this one carefully

Every course primary and secondary was selected for a **dark** ground. When white became the default
background, four of the six stopped clearing WCAG as text on white and the other two reached
large-text-only. None passes body text. So:

> **On a light ground, coloured type uses the course's `primaryDeep`.
> On a dark ground, coloured type uses `primary` or `secondary`.
> Neither is ever used as type on the other.**

The display colours are unchanged for every non-type use: fills, highlight blocks, rules, chips, tag
pills, borders, dividers, and dark-ground accents.

Consult `measured.onWhiteVerdict` and `measured.onAsphaltVerdict` in `tokens.json` before using any
colour as type. Those fields are computed, not asserted. See SHULL-CHG-0008.

### Grayscale survival is not optional

Most student handouts are photocopied. **A categorical distinction must never rely on hue alone.**
Vary fill value, outline weight, and label together.

Two colours carrying a distinction must differ by at least `rules.grayscaleSeparationMin` grey
levels, or must additionally differ by border and label.

> **Geology requires particular care.** Terra Teal and Rust Orange sit six grey levels apart — they
> are effectively the same colour photocopied, in the course whose handouts are photocopied most.
> Any Geology categorical use of both **must** differ by border and label as well as fill.
> `scripts/measure_tokens.py` reports this automatically.

### One accent word

**One accent-coloured word per headline. No gradients on text, ever.**

---

## 4. Typography

`typography.primary` — **Trade Gothic Next** — is the SHULL Studio typeface, used throughout:
presentations, documents, worksheets, labs, guided and Cornell notes, assessments, headings, labels,
supporting material.

It is Monotype-licensed and is essentially never present in a render environment, so the stack is:

```
typography.stack           Trade Gothic Next → Archivo → Liberation Sans
typography.stackCondensed  Trade Gothic Next Condensed → Archivo Narrow → Liberation Sans Narrow
```

**Never substitute a font outside this stack.** Never a novelty "school" font. Never a convenient
one.

`brand/fonts/trade-gothic-next.conf` maps the brand name to Archivo inside the build container, so a
document that correctly names Trade Gothic Next renders as Archivo during QA rather than silently
becoming DejaVu Sans. Without that mapping, **the QA render and the classroom copy are different
documents** — which was the actual state of the system until 2026-09-08.

### Size floors

- `typography.floors.slideContent` — hard floor for anything read from a seat. The footer chip is
  the only exception.
- `typography.floors.printBody` — no student-page text below this except the running footer.
- `typography.floors.printFooter` — bounds that footer exception.

**If content exceeds a line cap, split the slide. Never shrink type to fit.**

---

## 5. Visual density

**Clean and moderately dense.** Enough information to be useful, enough whitespace to be readable,
no unnecessary empty space, no decorative clutter.

Both extremes fail:

| Too sparse | Too dense |
|---|---|
| "beautiful but useless" | "textbook page pasted onto a slide" |

---

## 6. Decoration

Minimal and purposeful. **Every visual element must serve at least one of:** hierarchy, navigation,
explanation, emphasis, identity, visual comprehension.

Decoration to fill space is a defect. So is a box, heading, or graphic that exists because the
template had a slot for it.

---

## 7. Imagery

When imagery improves learning, prefer scientifically accurate images, authentic photographs,
meaningful diagrams, explanatory illustrations, and accurate visual models.

**Do not use generic stock imagery because a slide has empty space.** Images must contribute to
instruction.

### Generated versus hand-built

| Generated | Hand-built |
|---|---|
| Real objects — glassware, apparatus, instruments, benches | Anything carrying a number, label, or formula |
| Atmosphere, mood, historical setting | Bohr diagrams, Lewis structures, orbitals |
| Landscape and texture | Free-body diagrams, graphs, vectors |

> **The test:** if students *read* it as science, it is built. If they only *look* at it, it may be
> generated.

A generated Bohr diagram will have the wrong electron count in a way nobody catches at a glance.

**Geology exception:** atmosphere may be generated; specimen photographs for rock and mineral
identification may not. A generated "quartz" is not quartz, and identification is the thing being
assessed. Those get photographed.

---

## 8. Print discipline — a hard rule

Applies to everything physically printed: worksheets, practice sets, guided and Cornell notes, labs,
study guides, reference sheets. Digital-only deliverables are exempt.

- **Outlined and bordered treatments replace solid fills.** No full-page colour banners, no shaded
  section backgrounds, no solid-fill headers.
- **Colour is a thin accent only** — a chip outline, a rule line, a small tag, a border. Never a
  fill covering more than a small label or icon.
- **Table rows use hairline borders**, never alternating solid shading. If shading is genuinely
  needed for scanability, use a very light grey tint — never a brand colour at medium or full
  saturation.
- **Chart areas are hatched, not tinted.**
- **A numbered list is just the number. No box, no square, no circle, in any format** — labs,
  guided notes, worksheets, practice sets, tests, slides. SHULL-CHG-0015, and it has no exceptions.
- Chips and border-tab labels stay outlined or light-fill. Solid fill is reserved for slides and
  digital-only use.
- Minimum weights: `print.weights.boxBorder`, `print.weights.writingLine`.
- Full-colour variants are preserved on request — **never shipped as the default print file.**

Ink is a real cost, and this rule is stronger than "white is the default background." It survives at
full strength. The QA gate measures it; see `standards/QA_GATE.md`.

**Watermark:** `print.watermarkOpacityPct` — normal, reduced on dense tables, omitted entirely on a
heavily-inked page rather than layered under existing content.

---

## 9. Student materials

Prioritise readability, printer-friendliness, efficient ink, clear hierarchy, writing space, useful
structure, and a professional appearance.

White background. Restrained colour. Name / Date / Period on the student document.

**Student materials must not look like marketing brochures.**

---

## 10. Teacher materials

The same visual identity. They may carry more colour, metadata, answer information, instructional
notes, and organisational elements — but they are recognisably the same system.

Teacher-only information never appears on the student version.

---

## 11. Documents

**Ruled lines are for prose. Open boxes are for math.** This holds in notes and practice sets alike.

- Blanks are sized to the expected answer. A one-word blank and a full-sentence blank must not look
  identical.
- Answer blanks that are clearly too small for the expected response are a defect.
- Dense tabular content uses real tables, never card or flexbox grids.
- Running footer with an auto-generated page count.
- Every answer-bearing document has a **separate** key file.

---

## 12. Presentations

**Teacher presentation first.** Slides support classroom instruction. They are not condensed
textbooks.

Use strong visual hierarchy, meaningful visuals, restrained text, purposeful diagrams, clear
sequencing, and varied but coherent layouts. A long deck needs enough variation that not every slide
looks identical — **but variation stays inside this system.**

### Non-negotiables

- **Build from the twelve-layout template. Never from scratch.**
- **Exactly one highlight / must-write block per slide.** Two cues means students copy neither.
- **Every worked example is followed by its solution slide, every time.** A worked example with no
  solution slide is a bug.
- **The reserved-height rule.** The highlight block is placed *first*; the content column height is
  computed as slide height minus block minus footer band; text flows into what remains. **Never
  place text first and overlay the block.** That is how a shipped preview came out clipped.
- Line caps in `slideGeometry.lineCaps`. Exceed one and you split the slide.
- Geometry and spacing in `slideGeometry`.
- Section markers on dark dividers are **circles**. Number **squares** are for print. Do not cross
  them.
- Card colour logic: either all cards neutral, or a coloured card means "write this definition" —
  and if so the deck says so in words. Never ship a deck that mixes them with no stated rule.

### Animation

Subtle, purposeful, professional. **Never animate because the software permits it.**

---

## 13. Course identity

Each course keeps the shared system and changes only its identity colours and icon vocabulary.
See `courses.<course>.icons` in `tokens.json`.

Reserve the atom, beaker, and molecule set for Chemistry. Geology favours the hammer, magnifier,
mountain, strata, wave, compass, timeline, and map.

Course-specific instructional conventions — reading level, activity formats, assessment shape — are
**course decisions**, not design rules. They live in `courses/<course>/DECISIONS.md`.

---

## 14. Applying this system

1. Read the course's `DECISIONS.md` for anything course-specific.
2. Read `tokens.json` for every value.
3. Check `measured.*` before using a colour as type.
4. Apply the appropriate section above.
5. Run `standards/QA_GATE.md` before shipping.

**Do not invent a new visual system for an assignment.** The design system exists so the whole
library looks like one course taught by one person, not a folder of downloads.
