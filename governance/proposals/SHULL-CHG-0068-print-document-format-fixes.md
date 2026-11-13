# SHULL-CHG-0068 — Print documents: six format fixes found by building every template

> No conflict with a LOCKED rule is known. Item 6 changes a stated page budget; the writer did not
> check whether that budget is LOCKED, INHERITED or PROVISIONAL. Check before implementing item 6.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0068 |
| **Date** | 2026-11-09 |
| **Source** | User. Matt asked the main session on 2026-11-09: "is there anything you can do to improve my document format". The main session built a worksheet per course, the Physics guided notes, the lab master and the Chemistry snow-day sheet, and looked at every page. Shown the findings, he said: "yes draft it, tighten to 3 pages, blank space is deliberate". The Secretary did not write this record; the main session drafted it at the user's request. |
| **Current Rule** | See §1. |
| **Proposed Rule** | See §2. Six items, each separately approvable. |
| **Supersedes** | Items 1-2: `answer_box()` and the question text handling in `templates/snow_day/build_snow_day_docx.py`. Items 3-5: the `label()` calls for the cut label, the slot label, block labels, the equation label and the directions label in `templates/worksheet/build_worksheet_docx.py`. Item 6: `templates/worksheet/README.md`, profile table, Chemistry "Page budget: 4 for eight boxed questions"; and `pagesPerSection` and the `workHeightIn` values in `templates/worksheet/specs/chem_u07_s07.4.json`. |
| **Reason** | Each item is a defect or a waste visible on the printed page. Evidence in §1. |
| **Affected Agents** | Designer (builders), Auditor (verification, §5). |
| **Affected Skills** | None known. `build-document` was not re-read for a page-budget statement; check before implementing item 6. |
| **Affected Courses** | Items 1-2: every snow-day sheet. Items 3-5: every worksheet, all three courses. Item 6: Chemistry worksheets. No course `DECISIONS.md` is edited; the writer found no worksheet page budget stated in `courses/chemistry/DECISIONS.md`, by a keyword search only. |
| **Risk** | Low for items 1-5. Medium for item 6: students get less room to write. |
| **Recommendation** | Approve all six. Answer §4 first for item 6. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Drive verification is not needed; this is a repository-only change. No document already on Drive
is rebuilt by this record.

---

## 1. Current state, with evidence

All renders are LibreOffice conversions of the builders' `.docx` output, in Archivo. Word may place
a line slightly differently; items 1, 2 and 6 do not depend on that, items 3-5 should be re-checked
in Word if it matters.

| # | Document | What happens now | Evidence |
|---|---|---|---|
| 1 | Snow day | A question can sit at the bottom of one page with its answer box at the top of the next. `answer_box()` keeps the box whole but nothing ties the question to it. | `templates/snow_day/specs/chemistry.json`, question 5: text on page 1, box on page 2. |
| 2 | Snow day | A chemical formula typed in a spec prints as plain text: "CaCl2", "MgCl2". The worksheet builder prints the same kind of formula with subscripts. | Same sheet, question 5. Spec line 44. |
| 3 | Worksheet | The cut label is the first line inside the card with no space above it, so it sits on the dashed cut line. Cutting on the line cuts through the label. The default label also begins with a scissors character that does not appear in the render. | `geo_u01_s01.4.json`, all six cards. `build_worksheet_docx.py` line 200. |
| 4 | Worksheet | Small labels inside a bordered box touch the top border: "GLUE HERE — SLOT 1", "COMPLETE THE MAP". | `geo_u01_s01.4.json` page 2; `chem_u07_s07.4.json` question 5. |
| 5 | Worksheet | "EQUATIONS YOU MAY USE" and "DIRECTIONS" sit tight against the box or rule above them. "REMEMBER" and "BEFORE YOU START" have space above. | All three course sheets, page 1. |
| 6 | Worksheet | The Chemistry sheet is 4 pages. Page 4 holds one question and is more than half empty; pages 1 and 2 are about a quarter empty. | `chem_u07_s07.4.json`. Test on 2026-11-09: every work-box height scaled to 0.9 still gives 4 pages; scaled to 0.8 gives 3 pages. At 0.8 the smallest box goes from 1.4 in to 1.12 in and the largest from 3.0 in to 2.4 in. |

Not in this record, by Matt's decision ("blank space is deliberate"): the unruled gaps in the
guided-notes blocks and the mostly empty post-lab page on the lab master.

Not in this record, not raised with Matt as a change: the conversion-map figure in Chemistry 7.4
question 5 is a faint line of small text in a large box.

## 2. Proposed

**Item 1.** In the snow-day builder, a question's text stays on the same page as its answer box.
If both do not fit, both move to the next page.

**Item 2.** In the snow-day builder, a chemical formula in spec text prints with subscripts, using
the same routine the worksheet builder uses, not a second copy of it. The spec text is not
changed.

**Item 3.** The cut label sits inside the card with clear space between it and the dashed line.
The scissors character is either drawn in a face that has it or removed from the default label.

**Item 4.** A label that opens a bordered box has the same top padding as the text beside it has
from the side border.

**Item 5.** The equation label and the directions label get the same space above as the other
section labels.

**Item 6.** The Chemistry worksheet page budget for eight boxed questions becomes 3. The
`chem_u07_s07.4.json` work boxes are reduced to reach it, and `pagesPerSection` becomes 3. The
README table is changed to match. See §4.

## 3. What this does not do

- It changes no token in `brand/tokens.json` and no course `DECISIONS.md`.
- It does not change Physics or Geology page budgets.
- It does not rebuild or re-file any document already on Drive.

## 4. Questions for Matt

1. **Item 6.** Should the boxes shrink evenly (all to 0.8 of their size), or should the short
   warm-up boxes keep their size and the larger later boxes give up more? Even shrinking is
   proposed because it is the tested case.
2. **Item 6.** Is 3 pages the new rule for every eight-question Chemistry sheet, or only for this
   one? Proposed: the rule, since the README states the budget as a profile rule.

## 5. Verification, once implemented

- Each of the three course worksheets, and the three snow-day sheets, rebuilt, rasterised and
  every page looked at.
- `scripts/audit_worksheet.py` on the Chemistry sheet: 3 pages, inside its budget.
- `scripts/audit_print_ink.py` on each rebuilt PDF: under the ceiling.
- `scripts/validate_profiles.py` passes.
- `scripts/build_template_previews.py worksheet` re-run so the gallery matches.
