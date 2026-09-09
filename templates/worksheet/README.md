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
| Visual work | diagrams and charts to complete | — | **required**: diagram, draw, cards or slots |
| Page budget | 4 for eight boxed questions | 1 per section | 2 for a cut-and-glue |

**Physics carries no work areas at all.** Students work in their Hayden-McNeil carbonless lab
notebooks, so a work box or a ruled answer line on a Physics sheet is a refusal, not a warning.
His existing U01 practice set had a work box under every question; removing them is what took that
packet from eight pages to four.

**Geology has no math and must have something to do with the hands** — a diagram to label, panels
to draw in, cards to cut, slots to glue them into. A Geology sheet with none of those is refused.

## The page shape

Header → Name / Date / Period / **Score** → the concept → prior knowledge → equations →
directions → questions → close. Each section starts a new page.

- **The score total is summed from the questions, never typed.** A header reading `/ 20` over
  questions adding to 18 is one fact stored twice.
- **The concept block comes before anything is asked.** A student who has been away reads what the
  sheet is about before question 1, not after it.
- **Prior knowledge is the recall block** — the friction reminder before a friction problem. It
  names the section it came from so a student can go back to it.
- **Equations belong to the page they are usable on.** S1.1 does not show the kinematic equations,
  because S1.1 comes before them.

## Blocks

`questions` carry `tier`, `prompt`, `parts`, `points`, and optionally `math`, `given`/`need`,
`diagram`, `draw`, `answerLines`, `selfCheck`. Beyond them a section can carry `blocks`:

- **`cards`** — cut-out cards, dashed border, title, text and a box to draw in.
- **`slots`** — numbered slots the cards are glued into, sized to match.
- **`draw`** — blank captioned panels, when there is nothing to cut.
- **`diagram`** — a figure with numbered label lines beside it.
- **`reflection`** — italic prompts with ruled lines, the written close on a Geology sheet.

## Rules the builder enforces rather than trusts

1. The section code exists in that course's `DECISIONS.md`.
2. `sections` and `sectionsContent` name the same sections — they are one fact.
3. The course profile above.
4. The ramp: difficulty never goes backwards, and the multi-topic problem is last.
5. Every question stays whole across a page break. So does every card, slot and close block.

## Measured, not judged

`audit_worksheet.py` reads the budget from the spec, so a section that quietly grows a page fails
where a section that was always three pages passes. `audit_fonts.py` fails a PDF that renders in
anything but Archivo and **names the character that pulled the substitute in** — a single U+2610
checkbox pulls a whole second font, and the box the student ticks is then drawn by a face nobody
chose. That rule was written in four places in this repo and enforced in none until now.

## Ruled lines are for prose. Open boxes are for math.

This holds everywhere and is the reason a Geology reflection gets rules and a Chemistry conversion
gets a box.
