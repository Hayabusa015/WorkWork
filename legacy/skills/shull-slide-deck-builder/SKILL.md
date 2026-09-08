---
name: shull-slide-deck-builder
description: >
  Builds SHULL Science slide decks (.pptx) to Matt Shull's locked Slide Standard for his
  Chemistry, Physics, and Geology classes at James A. Garfield Local Schools. Use whenever
  the user asks for a slide deck, PowerPoint, presentation, lecture slides, section deck,
  or unit deck — including phrasing like "build a deck for Unit 8", "slides for section
  3.2", "make a PowerPoint on stoichiometry", "add a worked example slide", or "fix the
  clipping in this deck". Also use for revising, extending, or QA-ing an existing SHULL
  deck. Produces a .pptx plus a rasterized visual QA pass. Enforces the parchment/Deep
  Forest slide rules, the single Bio Lime highlight block, the 16pt floor, U#/S#.# footers,
  and the reserved-height rule that prevents text clipping.
---

# SHULL Slide Deck Builder

Requires `shull-studio` (brand, voice, codes, QA gate) and the course profile
(`shull-chemistry-guidelines`, `shull-physics-guidelines`, or `shull-geology-guidelines`).
Read `/mnt/skills/public/pptx/SKILL.md` before writing any build code.

Read `references/slide-standard.md` in this skill before laying out a single slide. It
contains the exact geometry rules, and three of them exist because a shipped deck broke.

---

## Step 1 — Scope the deck

A SHULL deck covers **one section**, not a whole unit, unless Matt says otherwise. A unit
deck is a set of section decks plus a title and a summary.

Infer and state back in one line: course, unit, section, section title, how many class
periods it covers. Ask only if the section is genuinely ambiguous — the course profile has
the unit/section map, so look there first.

Default length: 12–20 content slides for a one-period section. A 33-slide deck is a
multi-day section, not a default.

## Step 2 — Sequence

Use the master sequence, dropping types that don't apply:

1. Unit title (dark)
2. Agenda
3. Learning target
4. Vocabulary
5. Section divider (dark)
6. Content
7. Worked example → **solution slide immediately after, every time**
8. Lab / application
9. Formative check
10. Review
11. Unit summary (dark)

The worked-example → solution pairing is not optional. Matt teaches by working a problem,
then showing the complete solution. A worked example with no solution slide is a bug.

## Step 3 — Build

**Backgrounds.** Parchment `#EDF0E5` on every content slide. Deep Forest `#1A2318` reserved
for exactly three things: unit titles, section dividers, unit summaries. If a content slide
is dark, it's wrong.

**The highlight block.** Exactly one Bio Lime `#A8C97F` block per slide, and it is the only
write-this cue on the slide. If two things on a slide look like the must-write, students
write neither. If a slide has nothing worth writing, it gets no block.

**Type floor.** No student-facing body text below 16pt. Most body sits 19–24pt. This is
what keeps decks from turning into projected textbooks, and it is why the line caps below
exist rather than being arbitrary.

**Reserved height — the clipping rule.** The content column must *reserve* the highlight
block's height. Never layer the block over the text column and hope. A content slide with a
highlight block caps at **3 bullets, ≤ 2 lines each**. This rule exists because slides 8
and 17 of the U8 preview deck shipped with text cut off behind the block.

**Footer.** `U#/S#.#` chip on every slide, bottom right, matching the practice-set chip
style — outlined on dark slides, filled on light.

**Card color logic.** If a slide uses cards, either all cards are white, or green means
"write this definition" and the Slide Key slide says so. Never mix green and white cards
with no stated rule.

**Spacing.** At least 0.15" of fixed space after any subhead. Wrapped subheads running into
the first bullet is a known defect.

**Right-rail content** on solution slides gets vertically centered, not floated to the top
of an oversized card.

## Step 4 — Visuals

Hand-build every diagram as a shape group or SVG: particle diagrams, reaction schemes,
free-body diagrams, cross-sections, graphs. They stay on-palette, stay editable, and stay
accurate.

Go to Higgsfield only for photographic reference, 3D molecular renders, or minimal divider
art — and only after confirming with Matt. See `shull-studio/references/connectors.md`.
Verify anything generated for scientific accuracy; do not trust text rendered inside a
generated image.

## Step 5 — QA, mandatory

```
soffice --headless --convert-to pdf deck.pptx
```
then rasterize with `pdf2image` and **look at every page**.

Check, in this order:

1. **Clipped text.** Scan every slide edge and every box boundary. Highest priority defect.
2. Type floor — nothing under 16pt in the student-facing area.
3. One Bio Lime block per slide, no more.
4. Dark backgrounds only on title / divider / summary.
5. Footer code present and matching the filename.
6. Every worked example followed by its solution slide.
7. Headline grammar. Read them all. ("Terms You'll Need All Unit" → "Terms You'll Use All
   Unit" was a real catch.)

Report the checklist result in chat. If anything fails, fix and re-render before delivering.

## Step 6 — Deliver

Save as `SHULL_[COURSE]_Slides_U##_S##.#.pptx` in the section's `Presentations/` folder,
plus the exported PDF. Present both files.

Then, in two or three lines of chat: what the deck covers, how many slides, and any
assumption you made that Matt should sanity-check. No summary of the slides themselves —
he can open it.
