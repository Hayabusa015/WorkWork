# Missing Work sheet - teacher notes (not for students)

Student page: `SHULL_Missing_Work_TEMPLATE.pdf` (neutral, tick the course) or the `_CHEM`, `_PHYS`,
`_GEO` versions. Rebuild all four: `python3 templates/missing-work/build_missing_work.py`.

## How to fill it in
1. Name, period, date issued, then the assignments, unit/section codes, points, due-by dates.
2. Write the sum in TOTAL POINTS MISSING.
3. Tick how it gets turned in and when help is available, and write the place and times on the line.
4. Fill FROM YOUR TEACHER. Late/make-up credit is left blank on purpose (below).

## Late-work policy: what the repo actually says

| Course | Source | Status | What the sheet does |
|---|---|---|---|
| Chemistry | `courses/chemistry/DECISIONS.md`, "Grading and late-work policy" | Defined (scale plus a hard cutoff at end of unit). Only the separate grade-weights question, CONFLICT-24, is open. | Blank line. Copy the scale from the source if you want it printed. |
| Geology | `courses/geology/DECISIONS.md`, "PROVISIONAL" and open question 4 | PROVISIONAL, carried over from Chemistry, not confirmed | Blank line. Do not treat as settled. |
| Physics | `courses/physics/DECISIONS.md` | Not stated. Gradebook weights are explicitly not carried over. | Blank line. |

Not consistent across the three courses, so nothing is printed on the student page. The numbers are not
restated here, so there is one copy to go stale.

## Wording to confirm
The five student steps are procedural. Step 5 ("tell me before it passes") is plain guidance, not a
grading rule, but it is my wording. The turn-in and help options (tray, Google Classroom, before
school, lunch) are unticked choices; delete any that do not exist in your room.

## Filing (proposal only, nothing shelved)
- Destination: `SHULL Science/_Brand/Templates/` (Drive folder ID in `config/drive.json`). It is used
  by all three courses, so one copy there, never copied into a course folder.
- Filename: `NAMING.md` grammar needs a course, a fixed Type, and a `U##_S##.#` code. This sheet has
  none of those and no Type fits. Working name follows the existing template precedent
  (`SHULL_Lab_TEMPLATE_MASTER`): `SHULL_Missing_Work_TEMPLATE`. Needs a Secretary proposal to
  either add a Template type or exempt it.
- The sheet loads colour tokens from `../lab/shull-lab-tokens.css`.
