---
id: SHULL-CHG-0022
title: A Geology assignment is not a cut-and-glue by default
status: IMPLEMENTED
opened: 2026-09-09
decided: 2026-09-09
decided_by: Matthew Shull
---

# SHULL-CHG-0022 — Geology formats

## What he said

> "its important to note, i dont want every geology assignment to be a 6 page cut out."

## What was wrong

The Geology profile from SHULL-CHG-0019 refused any sheet without a `diagram`, `draw`, `cards` or
`slots` block. Three of those four are heavy. The only Geology demo in the repo was the two-page
cut-and-glue nebular timeline, and the only cheap way to satisfy the rule was a diagram — so the
mechanism was quietly pushing every Geology sheet toward the format he had shown me once.

That is the failure mode this system is supposed to prevent: a preference expressed once, turned by
a builder into a mandate.

## Decision

**Geology keeps a visual requirement, and gains light ways to meet it.**

- **`sort`** — put things in order *in place*. The items print scrambled with a box beside each and
  the student writes the number. Same learning as the cut-and-glue timeline for most sequencing
  work, on one page, in ten minutes, with no scissors.
- **`match`** — terms with a blank on the left, lettered descriptions on the right. The spec
  supplies the descriptions already shuffled: a builder that shuffled them would produce a different
  sheet on every build and no answer key would survive one.
- **`"proseOnly": true`** — an escape for a sheet that genuinely is a reading response.

The refusal message now names the light options first and says outright that cut-and-glue should
not be the default.

## The second demo

`templates/worksheet/specs/geo_u04_s04.1.json` — Layers of the Earth, **one page**: a cross-section
to label from a word bank, five layers to match, five materials to order by density, and one
written question. It is his own example ("if we're diagramming the different layers of the earth,
it would be cool to have a nice earth to label"), and it exists so the repo shows the light end of
the range as well as the heavy one.

The permissive side is tested too, in `validate_profiles.py`: a Geology sheet whose only visual
element is a matching grid **must build**, and so must a declared prose sheet. A profile that
refuses everything proves nothing.

## Three layout defects found while fitting it on one page

- **A blank final page on every document.** OOXML requires the body to end with a paragraph, and a
  body built entirely from tables does not have one — python-docx will write `</w:tbl></w:body>`.
  Word and LibreOffice repair that by inserting a paragraph of their own at full body height, and
  when the content already reaches the bottom of the page it does not fit: the file gains a blank
  final page carrying nothing but the footer. `trim_tail()` writes the paragraph deliberately and
  pins it to 1pt. The file becomes valid *and* the page count becomes the content's.
- **A reflection prompt separated from its answer lines.** The question ended a page and the two
  ruled lines started the next one — the student turns over to two rules belonging to nothing.
  Prompt and lines are now one non-splitting row.
- **And then the heading stranded from the prompt**, one level up, the same way the diagram block's
  heading once did. `cantSplit` holds a row and does nothing above it, so the heading went inside
  the row.

## Verification

- GEO U04 S4.1 **1 page**; GEO U01 S1.4 (the cut-and-glue) 2; PHYS 4; CHEM 4. All on budget.
- `validate_profiles.py` — 15 refusals fire, 2 allowances hold, 4 real specs build.
- Toner within budget, no solid band, Archivo only, `hook-validate.sh` clean.
