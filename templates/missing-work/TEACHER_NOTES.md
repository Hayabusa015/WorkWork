# Missing Work sheet - teacher notes (not for students)

Student page: `SHULL_Missing_Work_TEMPLATE.pdf` (neutral, tick the course) or the `_CHEM`, `_PHYS`,
`_GEO` versions. Rebuild all four: `python3 templates/missing-work/build_missing_work.py`.

## How to fill it in
1. Name, period, date issued, then the assignments, unit/section codes, type, points, due-by dates.
2. For a test, tick Edulastic or Paper. For an Edulastic test, write the password in PASSWORD.
3. Write the sum in TOTAL POINTS MISSING.
4. Staple the student's finished work to the sheet. The sheet points students to GMen time for help.

## Late-work policy: what the repo actually says

| Course | Source | Status | What the sheet does |
|---|---|---|---|
| Chemistry | `courses/chemistry/DECISIONS.md`, "Grading and late-work policy" | Defined (scale plus a hard cutoff at end of unit). Only the separate grade-weights question, CONFLICT-24, is open. | Nothing printed. Copy the scale from the source if you want it added. |
| Geology | `courses/geology/DECISIONS.md`, "PROVISIONAL" and open question 4 | PROVISIONAL, carried over from Chemistry, not confirmed | Nothing printed. Do not treat as settled. |
| Physics | `courses/physics/DECISIONS.md` | Not stated. Gradebook weights are explicitly not carried over. | Nothing printed. |

Not consistent across the three courses, so nothing is printed on the student page. The numbers are not
restated here, so there is one copy to go stale.

## Wording to confirm
The four student steps are procedural. The sheet does not print a turn-in location; it says the work
is attached to the sheet. "GMen time" is printed as you wrote it.

## Filing (proposal only, nothing shelved)
- Destination: `SHULL Science/_Brand/Templates/` (Drive folder ID in `config/drive.json`). It is used
  by all three courses, so one copy there, never copied into a course folder.
- Filename: `NAMING.md` grammar needs a course, a fixed Type, and a `U##_S##.#` code. This sheet has
  none of those and no Type fits. Working name follows the existing template precedent
  (`SHULL_Lab_TEMPLATE_MASTER`): `SHULL_Missing_Work_TEMPLATE`. Needs a Secretary proposal to
  either add a Template type or exempt it.
- The sheet loads colour tokens from `../lab/shull-lab-tokens.css`.
