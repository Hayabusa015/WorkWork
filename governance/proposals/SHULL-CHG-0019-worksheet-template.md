---
id: SHULL-CHG-0019
title: Worksheet and practice-set template, with three enforced course profiles
status: IMPLEMENTED
opened: 2026-09-09
decided: 2026-09-09
decided_by: Matthew Shull
---

# SHULL-CHG-0019 — Worksheets

## What he asked for

A worksheet template per class, from his own words:

> "Thorough header and a nice footer. Labels of concept. Name, Date, Period and Score labels. At
> the top, give a quick review of the concept that the practice or worksheet is for. If necessary
> add a quick recap of prior knowledge needed for a lesson… I like diagram labeling also."

- **Chemistry** — conceptual and math questions, diagrams and charts to complete, an open box for
  every math problem "with a watermark that says *Show work here*", equations at the top.
- **Physics** — "We work in Hayden McNeil carbonless lab notebooks, all problem sets are done in
  the notebooks, so we do not need room for problems to solve." Questions "easy to start and
  harder as it goes, last problem should be a full problem that has other unit connectors."
  20–40 minutes.
- **Geology** — no math, low rigour, visual and expressive. His example: drawing pictures for
  nebular theory and pasting them in the order it happens.
- Printer-ink saver throughout.

Two of his own sheets were supplied as references:
`SHULL_PHYS_Practice_Sets_U01.docx` (the one to improve on) and
`GEO_U1_S1.3_NebularTheory_CutGlue_Timeline.docx` ("I really like the setup and look").

## Decision

`templates/worksheet/build_worksheet_docx.py`, one spec format, three profiles **enforced at build
time**. Structure and the profile table: `templates/worksheet/README.md`.

The drawing primitives were first extracted to `templates/_shull_docx.py` and shared with the
guided-notes builder. Verified behaviour-preserving: both notes packets rebuilt to a
byte-identical `word/document.xml` before anything new was added.

## What changed against his existing Physics sheet

| His sheet | Here | Why |
|---|---|---|
| Solid navy banner on every page | Outlined header, heavy accent rule | Section 8 — no full-page colour banners. It was the largest single ink cost on the sheet. |
| Question numbers in solid navy squares | Just the number | SHULL-CHG-0015, and section 8. |
| Tier pills filled (light blue, solid navy) | No box, own right-aligned column | Section 8. See "the tier tag" below. |
| A work box under every question | None | His instruction. Students work in the Hayden-McNeil notebooks. |
| One-line "LEARNING GOALS" | Concept review + prior knowledge + equations | His instruction. |
| No Name / Date / Period / Score | All four, Score boxed | His instruction. |
| 8 pages for U01 | **4 pages** | Removing the work boxes, one section per page. |

## Two conflicts, both resolved toward the artifact, both worth his confirmation

**1. The practice-set shape.** `.claude/skills/build-document/SKILL.md` said "exactly 8 questions:
2 warm-up / 3 practice / 2 challenge / 1 multi-topic, strictly two pages". That figure is marked
**INHERITED** in `docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md` — carried from a legacy skill, never
confirmed. His shipped `SHULL_PHYS_Practice_Sets_U01.docx` runs **2 / 2 / 1 / 1**, six per section,
across all four sections. The artifact is the better evidence, so Physics now holds 2/2/1/1 and the
skill records the conflict. Chemistry has no shipped artifact to read, so it gets the ramp *order*
enforced and picks its own counts — inventing a Chemistry count and calling it locked is how the
8-question figure got in.

**2. The work-box label.** The same skill said work boxes carry "a border-tab label sitting *on*
the border, not floating grey text inside" — a decision that explicitly replaced floating grey
text. He has now asked for floating grey text: "a watermark that says Show work here in the area."
His instruction wins and the watermark is implemented. Its grey is computed from
`print.watermarkOpacityPct` in `tokens.json`, so the ink standard and the page agree by
construction rather than by a picked colour.

## A third conflict, not resolved — his call

His nebular sheet is filed as **`GEO_U1_S1.3`**. `courses/geology/DECISIONS.md` says `1.3` is *The
Scale of the Universe* and `1.4` is *Formation of a Solar System*, which is what nebular theory is.
The rebuild is at **1.4**. The same drift is in `templates/notes/specs/geo_u01_s01.2-s01.4.json`,
which puts *The Sun* at 1.4 where the roadmap says 1.5. `validate_codes.py` cannot catch this: it
checks that a code exists, not that the title matches it. **Confirm which numbering is right before
either file is used in class.**

## Mechanism, not documentation

Every rule below refuses a build rather than describing itself, and
`scripts/validate_profiles.py` — wired into the Stop hook — proves each refusal actually fires by
feeding it a spec built to trip it. A refusal that never fires is not a refusal.

- Physics: no work boxes, no ruled answers, prior knowledge required, equations required, the
  2/2/1/1 ramp.
- Geology: no equations, no math, and at least one thing to label, draw, cut or order.
- Chemistry: math questions require an equation bar.
- All: difficulty never goes backwards, the multi-topic problem is last, the section code exists in
  `DECISIONS.md`, and `sections` agrees with `sectionsContent`.

## The tier tag

Outlined pills were built first, inline with the prompt, in four border weights so the tiers would
survive greyscale. He rejected them on sight — "these look awful" — and he was right on three
counts. A run border (`w:bdr`) has no usable padding, so at 7pt the box clamps to the cap height
and looks stamped on. Four different border weights read as a rendering fault, not a scale. And an
inline tag of varying width leaves every prompt starting at a different place, with wrapped lines
running back underneath the tag.

Four alternatives were built and rendered before choosing: no box, a run-in head with an em rule, a
single uniform hairline box, and an accent bar. All four were better, and all four shared the
alignment fault. The fix is structural: **the tag gets its own column, set right**, so every tag
ends on one edge and every prompt begins on one. The column width is measured from the longest tier
name against the shipped Archivo files — picked by eye it would wrap "MULTI-TOPIC" and look worse
than what it replaced. No box at all: a box on the cell is a tall empty rectangle beside one word.

## Three defects found while building

- **Every printed file in this repo was rendering in two fonts.** `pdffonts` showed DejaVuSans in
  the notes packets and both new worksheets, and NotoColorEmoji in the Geology sheet. The cause was
  one character each: `☐` U+2610 and `✂` U+2702, neither of which Archivo has. The rule that this
  must not happen is stated in `QA_GATE.md`, `audit-deliverable`, `build-presentation` and
  `apply-shull-design` — four places, and enforced in none of them. `scripts/audit_fonts.py` now
  fails such a PDF and **names the character**, because "DejaVuSans is present" is not actionable.
  The checkbox is now drawn as a bordered run in Archivo metrics, sized from the real space
  advance; the scissors is gone, since the dashed border and the words "CUT ALONG THE DASHED LINE"
  already say it.
- **A blank page between every section.** The paragraph carrying the page break is full body
  height, so where a section ended flush with the bottom of its page that paragraph did not fit —
  it moved to the next page and only then broke, leaving a page carrying nothing but a footer.
  Pinned to a 1pt exact line, it always fits where it is written.
- **Every spacer was four times the size it claimed.** `doc.add_paragraph()` with a `space_after`
  is a full empty body line *plus* that space, so a "3pt" gap cost about 16pt and six of them
  between the questions of a section came to most of an inch. It was diagnosed only after four
  separate content trims had been made to pay for it — a key idea and three prior-knowledge items
  deleted from Physics sections to buy back space that empty paragraphs were spending. `gap(doc,
  pt)` pins the line, and every one of those trims was restored with every section still on one
  page.
- **Unit titles were typed into specs.** `validate_layers.py` caught it: a unit's name is a course
  fact and belongs in `DECISIONS.md`. Both builders now read it from there, and the field is gone
  from all five specs. The three roadmaps write their headings three different ways, so all three
  shapes are parsed rather than one being imposed on files that were already correct.

## The page budget

"Strictly two pages" is not one number for every course. A Physics section is one page because
there is nothing to write on it; a Chemistry section with eight work boxes is four, and the boxes
are the assignment; a cut-and-glue activity is two by construction — the cards, then the slots.
The spec declares `pagesPerSection` and `scripts/audit_worksheet.py` measures against it. The
failure is a section that quietly *grows* a page, not one that was always three.

## Verification

- Three real worksheets built and read page by page at 100 dpi.
- `audit_worksheet.py` — every section on its declared budget.
- `audit_print_ink.py` — CHEM 6.51%, PHYS 9.47%, GEO 9.12% marked at worst; widest solid band
  **0.00 in** in all three. No fills anywhere.
- `audit_fonts.py` — Archivo only, in all three worksheets and both notes packets.
- `validate_profiles.py` — 13 refusals fire, 3 real specs still build.
- `hook-validate.sh` clean.

## Still missing

No images. `diagram` blocks render a placeholder well naming the figure that is needed;
`scripts/image_prompts.py` refuses to guess a subject. The Chemistry conversion-map figure and any
Geology diagram have to be drawn before those sheets are classroom-ready.
