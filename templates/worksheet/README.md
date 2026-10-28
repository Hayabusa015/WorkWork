# Worksheets and practice sets

```bash
python3 templates/worksheet/build_worksheet_docx.py specs/<spec>.json out.docx
python3 scripts/audit_worksheet.py out.docx specs/<spec>.json     # pages + ink
python3 scripts/audit_fonts.py out.pdf                            # Archivo only
```

One builder, one spec format, three course profiles. The drawing primitives — how a work box
is drawn, how a fraction stacks, how a diagram block survives a page break — live in
`templates/_shull_docx.py` and are shared with the guided-notes builder, so the two cannot drift.

## The three profiles, and why they differ

They are enforced at build time. Each refusal names the rule and the change record.

| | Chemistry | Physics | Geology |
|---|---|---|---|
| Work areas | open box per math question, **SHOW WORK HERE** watermark | **none** — refused | none |
| Equations at top | required when the sheet has math | required | refused |
| Prior-knowledge block | optional | **required** | optional |
| Ramp | order enforced, counts free | **2 / 2 / 1 / 1**, enforced | not a question ladder |
| Visual work | diagrams and charts to complete | — | **required**: diagram, draw, cards, slots, sort, match or outline |
| Page budget | 4 for eight boxed questions | 1 per section | **1** normally; 2 for a cut-and-glue |

**Physics carries no work areas at all.** Students work in their Hayden-McNeil carbonless lab
notebooks, so a work box or a ruled answer line on a Physics sheet is a refusal, not a warning.
His existing U01 practice set had a work box under every question; removing them is what took that
packet from eight pages to four.

**Geology has no math and must have something to look at, label, order or match.** But it is a
range of formats, not one — **a Geology assignment is not a cut-and-glue by default.** The light
ones are `sort` and `match`: one page, ten minutes, no scissors, and the same learning as the
cut-out for most sequencing and vocabulary work. Cut-and-glue earns its two pages and its scissors
sometimes; it should not be what every sheet turns into. SHULL-CHG-0022.

A sheet that genuinely is a reading response sets `"proseOnly": true` and is allowed through.

Two demos are in `specs/` for exactly this reason: `geo_u01_s01.4` is the two-page cut-and-glue,
`geo_u04_s04.1` is a one-page label-match-order sheet.

## The page shape

Header → Name / Date / Period / **Score** → REMEMBER → BEFORE YOU START → equations →
directions → question cards → close. Each section starts a new page.

The layout follows his `Master_Physics` reference, with the two changes he asked for. **No work
space on a Physics sheet** — the notebooks are where problems get worked. And **no solid header
slab**: his banner measures a 7.61 in solid band, which fails the fill rule on its own, so the
shape survives as an outlined header with a heavy accent bar on the left edge, which is the one
place a solid mark earns its ink.

**One card per question**, number top left, tier top right, both in a single paragraph with a right
tab stop — a nested table there drags a blank paragraph in with it and the card gains a line of
nothing. **Two short questions share a row**; `is_short()` decides, so the pairing follows the
content rather than a hand-placed break.

**Tier tags** are all the muted label grey (SHULL-CHG-0055). The word names the tier and the
question order carries the difficulty; colour carries nothing, so amber and red stay free to mean
caution and danger.

- **The score total is summed from the questions, never typed.** A header reading `/ 20` over
  questions adding to 18 is one fact stored twice.
- **The concept block comes before anything is asked.** A student who has been away reads what the
  sheet is about before question 1, not after it.
- **Prior knowledge is the recall block** — the friction reminder before a friction problem. It
  names the section it came from so a student can go back to it.
- **Equations belong to the page they are usable on.** S1.1 does not show the kinematic equations,
  because S1.1 comes before them.

## Blocks

**The tier tag has its own column**, set right, so every tag ends on one edge and every prompt
begins on one — including wrapped lines, which used to run back underneath the tag. The column is
measured from the longest tier name against the shipped Archivo files, so it follows the names if
they are ever renamed. It carries **no box at all**: a run border cannot be padded, so a boxed tag
at 7pt is clamped to the cap height and looks stamped on, and a box drawn on the cell is a tall
empty rectangle beside one word. The word is the tag.

## Self-check answers

**Every calculation carries its answer except the last question**, so a student knows on the spot
whether their arithmetic is right. The last one they finish without a net — the builder *refuses* a
self-check on it, and refuses a calculation anywhere else that lacks one.

**Numeric results only.** A conceptual question keeps no bracket, because there the bracket hands
over the whole answer instead of confirming arithmetic. That is why a question is marked
`"calculation": true` in the spec rather than guessed at from its wording — "Name the kinematic
equation you would use" reads like a physics problem and has no number in it.

`questions` carry `tier`, `prompt`, `parts`, `points`, and optionally `calculation`, `math`,
`given`/`need`,
`diagram`, `draw`, `answerLines`, `selfCheck`. Beyond them a section can carry `blocks`:

- **`cards`** — cut-out cards, dashed border, title, text and a box to draw in.
- **`slots`** — numbered slots the cards are glued into, sized to match.
- **`sort`** — put things in order in place: printed scrambled with a box to write the number in.
  The one-page version of the cut-and-glue timeline.
- **`match`** — terms with a blank on the left, lettered descriptions on the right. The spec
  supplies the descriptions already shuffled, because a builder that shuffled them would produce a
  different sheet on every build and no answer key would survive one.
- **`draw`** — blank captioned panels, when there is nothing to cut.
- **`diagram`** — a figure with numbered label lines beside it.
- **`reflection`** — italic prompts with ruled lines, the written close on a Geology sheet.

### Project blocks

A project handout (a poster, a slide, anything students make rather than answer) needs a few
blocks a question sheet does not. All of them are opt-in: a spec that does not name them builds
exactly as before. Spec text in these blocks may carry `<b>`, `<i>` (genus and species names) and
`&nbsp;`, read by `rich()` in `templates/_shull_docx.py`. First use:
`specs/geo_u02_s02.3_dinosaur_poster.json`.

- **`outline`** — a labelled blank layout of the product: where each part goes. `zones` is a list
  of full-width zones (`kind`, `label`, `hint`, `heightIn`, optional `periods` for a timeline
  strip whose cells are sized to each period's length) or a `row` of side-by-side zones, each with
  a `share` of the width and an optional fossil-site style `legend`. A zone's `kind` is `facts`
  (solid course-colour border) or `pics` (dashed ink border). The two kinds differ by border style
  and label, never by hue alone, because Geology's two colours photocopy to the same grey.
  `legend` is three strings: the facts swatch, the pictures swatch, and a closing line. It counts
  as Geology visual work.
- **`list`** — a numbered requirement list in `across` columns. Each item is `[lead, text]`; the
  lead is bold. Just the number, no box (SHULL-CHG-0015).
- **`table`** — a reference table: `headers`, `widths` (fractions of the page), `rows`. A row may
  be `{"group": "..."}` to open a labelled group. The first column is bold unless
  `"boldFirst": false`. Optional `label`, `lead` and `size`. The header row repeats on a new page.
- **`notes`** — a `label` and bulleted `items`, or plain lines with `"bullets": false`.
- **`formats`** — two (or more) ways to do the same task, side by side: a `note` above the boxes,
  then `boxes`, each with a `title`, a `share` of the width, and `lines`, or a `lead` plus
  `bullets`.
- **`plan`** — labelled write-on lines. `rows` is a list of lines, each a list of `[label, flex]`
  fields; flex `0` is a label with no line (a circle-one choice). Ruled lines, because a plan is
  prose.
- **`rubric`** — draws the spec's top-level `rubric.rows` (`part`, `points`, `levels`, `full`,
  `partial`, `none`) with full level descriptors, a score box per row, and a TOTAL. Its points
  count toward the header's SCORE total, which stays summed, never typed.

Any block may carry **`gapBefore`** (points of space above it) and **`pageBreakBefore`** with a
**`heading`** (the page's title).

### Section and spec options

- **`eyebrowNote`** — text appended to the header eyebrow ("INDIVIDUAL PROJECT").
- **`directionsLabel`** — renames the DIRECTIONS label ("THE JOB").
- **`concept`** is optional. A project handout has no recall block; its job line is the
  directions.

### The grading sheet: `--rubric-sheet`

```bash
python3 templates/worksheet/build_worksheet_docx.py specs/<spec>.json out.docx --rubric-sheet
```

The same spec, drawn as the teacher's one-page grading sheet: the header, the fields in
`rubricSheet.fields` (with `rubricSheet.widths`), the rubric with each row's full-credit text as
its LOOK FOR (word for word, from the same `rubric.rows`), a comment column, the TOTAL,
`rubricSheet.pointer`, and a NOTES box (`rubricSheet.notesHeightIn`). The handout and the sheet
cannot drift, because there is one copy of the rubric. `audit_worksheet.py` has no sheet mode yet,
so it measures the sheet against `pagesPerSection` and reports a false budget fail.

### The key: `key.blocks`

`build_worksheet_key_docx.py` also renders a top-level `key` object: `key.title` replaces the
section title on the key, and `key.blocks` (kinds `table` and `notes`, as above) draw a project
key's reference tables and grading notes, after any worked questions. A key is teacher-only, so
PROVISIONAL labels belong there and never on the student page.

## Vertical space

Use `gap(doc, pt)`, never `doc.add_paragraph()` with a `space_after`. The second is not a gap of
that size — it is a full empty body line *plus* the space after it, so a "3pt" spacer costs about
16pt. Six between the questions of one section is most of an inch of nothing, and that inch is what
pushes a closing checklist onto a second sheet of paper. It cost four separate content trims before
it was diagnosed; the content all went back once the spacers were the size they claimed.

## Rules the builder enforces rather than trusts

1. The section code exists in that course's `DECISIONS.md`.
2. `sections` and `sectionsContent` name the same sections — they are one fact.
3. The course profile above.
4. The ramp: difficulty never goes backwards, and the multi-topic problem is last.
5. Every question stays whole across a page break. So does every card, slot and close block.

## Measured, not judged

`audit_print_ink.py` reports **three** numbers and they are not interchangeable. **Toner** is ink
volume — the mean darkness of the page, what a cartridge actually spends — and it is the budget.
**Marked** is the share of the page carrying any mark, a density reading, reported but not failed
on except at an extreme. **The widest solid band** is what the standard fails outright.

Using `marked` as the ink budget was wrong and it nearly cost a good design: it counts a 7% grey
tint exactly as hard as solid black, so it ranked a sheet with two pale panels (18.70% marked,
**4.68% toner**) as worse than one with solid navy banners on every page (12.47% marked, **8.15%
toner**) — when the second lays down 74% more ink. SHULL-CHG-0020.


`audit_worksheet.py` reads the budget from the spec, so a section that quietly grows a page fails
where a section that was always three pages passes. `audit_fonts.py` fails a PDF that renders in
anything but Archivo and **names the character that pulled the substitute in** — a single U+2610
checkbox pulls a whole second font, and the box the student ticks is then drawn by a face nobody
chose. That rule was written in four places in this repo and enforced in none until now.

## Ruled lines are for prose. Open boxes are for math.

This holds everywhere and is the reason a Geology reflection gets rules and a Chemistry conversion
gets a box.
