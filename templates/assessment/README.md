# Unit tests

```bash
python3 templates/assessment/build_day1_item_bank.py specs/<spec>.json outdir/
python3 templates/assessment/build_day2_test_docx.py specs/<spec>.json outdir/
python3 scripts/audit_print_ink.py outdir/SHULL_..._Day2_A.pdf     # Day 2 only — Day 1 is plain text
python3 scripts/audit_fonts.py outdir/SHULL_..._Day2_A.pdf         # Archivo only
```

Chemistry's two-day unit test, per `courses/chemistry/DECISIONS.md`: Day 1 conceptual multiple
choice, four versions, delivered online; Day 2 free-response computation, work shown, graded for
partial credit. Two different shapes, one spec, two builders, because the day that lives in a
browser and the day that lives on paper are not the same document with a different wrapper.

This was the one build system with rules but no renderer — `build-assessment`'s parallel-version
and answer-key rules existed only as prose until this template. Everything here draws from
`templates/_shull_docx.py`, the same primitives the worksheet and notes builders use — a work box,
a given/need table, a page that does not gain a trailing blank sheet — because a graded test is not
a different fact from a practice set just because points are attached to it.

## Two rules a graded test enforces that a practice set does not

**No `selfCheck` brackets.** SHULL-CHG-0021 puts a bracketed answer beside a calculation so a
student can check their own arithmetic on *ungraded* practice. On a test that same bracket hands
over the answer being graded. `build_day2_test_docx.py` refuses a spec that carries one.

**No tier tags.** `warm-up` / `practice` / `challenge` is the practice-set ramp, a teaching device
for a sheet nobody is scored on relative to their neighbour. A test problem is just problem N,
worth N points — the refusal exists so a spec is not built by copying a worksheet section and
forgetting to strip what does not belong on it.

## Day 1 — item bank, not a document

Delivered through Pear Assessment (formerly Edulastic), not printed. This builder does not know
Pear's import format and does not pretend to — it writes a plain, ordered `.txt` per version that
gets typed or pasted into the platform, plus a separate key. Building an actual import file
(CSV/QTI) is future work, once the exact format the platform accepts is confirmed; inventing one
now would be a claim of integration this system does not have.

Checked before anything is written:

- exactly four choices, exactly one correct index
- no "all of the above" / "none of the above" — a real fourth option, always
- a stated distractor rationale for every wrong choice — a real misconception, not a placeholder
- every version covers the same learning targets in the same order, so "Version B" is a genuine
  equivalent form and not a shorter, easier test wearing the same name

**The demo spec deliberately varies which letter is correct.** The first draft of this spec put
the right answer at position A on every single item — technically valid, structurally lazy, and
exactly the kind of pattern a test-savvy student finds in the first five minutes. There is no
enforced rule against it yet; it was caught by inspection, the way it would be by a teacher
proofreading their own bank. Worth a build-time check if it recurs.

## Day 2 — the paper test

Same page grammar as the worksheet: header with the accent bar, Name / Date / Period / Score
(summed from the problems, never typed), directions, equation bar, then one bordered card per
problem — number, points, prompt, given/need, and an open work box sized for a full written
solution rather than a practice-set-sized box. **`VERSION A` / `VERSION B` prints in the header in
the display colour**, large enough that a proctor sorting a stack of collected tests can tell them
apart without opening one.

Each version becomes two files: the student test and a separate `_Key` where the blank work box is
replaced by a bordered answer block carrying the value and every worked step. `validate_versions()`
checks both versions share a blueprint — same problem count, same point value in every slot, same
total — before either is built. It cannot confirm a version was genuinely re-solved from scratch
rather than copied with the numbers swapped; that discipline is on whoever writes the spec, per the
skill's own rule, and the demo spec re-solves each version independently with different compounds.

## The demo

`specs/chem_u07_unit_test.json` — Chemistry U7 S7.1–S7.4 (the unit's name is read from
`courses/chemistry/DECISIONS.md` at build time, never typed into the spec), the same sections and
equations the worksheet demo (`SHULL-CHG-0019`) already covers. Day 1: 8
conceptual items, 2 versions (the real test runs ~25 per `DECISIONS.md`; 2 items' worth of scaling
proves the mechanic without writing the full bank twice for a demo). Day 2: 5 computational
problems, 2 versions, 22 points each. Sections 7.5–7.7 (percent composition, empirical and
molecular formulas) are real U7 content but have no demo anywhere in this repo yet, so the test is
scoped to what has actually been built, not the whole unit.

**Standard codes are marked `PROVISIONAL`.** Ohio HS Chemistry standard alignment for this unit has
not been confirmed with Matt. A wrong code is worse than none, so none is printed.

## What this does not do yet

- No Day-2 audit script (`audit_worksheet.py` does not apply — a test has no fixed page budget).
  Ink and font checks reuse the shared scripts; page count is read by eye.
- No real Pear Assessment export format.
- Only Chemistry's two-day shape is built. Physics has no assessment-shape section yet in
  `courses/physics/DECISIONS.md`; Geology's single-day MC/matching shape is close to Day 1's item
  bank but has not been built against.
