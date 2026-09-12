---
id: SHULL-CHG-0023
title: The assessment build system - Day 1 item bank and Day 2 problems test
status: IMPLEMENTED
opened: 2026-09-12
decided: 2026-09-12
decided_by: Matthew Shull
---

# SHULL-CHG-0023 — Assessment template

## What was missing

Of the five document systems (lab, notes, worksheet, slide, assessment), `build-assessment` was the
only one that was fully specified as a skill — item rules, parallel-version rules, key format — and
had no renderer, no template, and no demo. Every other system had at least proven itself once.
Identified during a repository re-familiarization pass, then confirmed with Matthew as the next
build target.

## What he said

Chemistry's real classroom shape, described directly: Pear Assessment (formerly Edulastic) for a
Day 1 multiple-choice test, and a separate handwritten Day 2 "problems test" — five to seven
computed problems, thorough and complete, with real room to write the answer. This matches
`courses/chemistry/DECISIONS.md` §Assessment shape exactly (Day 1 conceptual MC, Day 2 computational
free-response) and confirms it against what was already on file rather than overriding it.

Two scoping decisions, taken by question rather than assumed:
- Day 1 output is an **item bank**, not a styled document — Pear is the delivery surface, a printed
  version would never be seen by a student.
- The platform is **Pear Assessment**, not Edulastic — the skill and any future spec should say Pear.

## Decision

**Two builders, one spec format, sharing `templates/_shull_docx.py` with the worksheet and notes
templates rather than redrawing their own primitives:**

- `templates/assessment/build_day1_item_bank.py` — plain-text item bank per version plus a separate
  key, for manual entry into Pear. Refuses: wrong choice count, no single correct answer, an
  "all/none of the above" catch-all, a wrong choice with no stated distractor rationale, and a
  version whose learning targets do not match the others in set and order.
- `templates/assessment/build_day2_test_docx.py` — styled `.docx` problems test reusing the
  worksheet's question-card and work-box drawing, one file per version plus a separate `_Key` with
  full worked steps. Refuses two fields that belong to ungraded practice and never to a graded test:
  `selfCheck` (SHULL-CHG-0021's self-check bracket would hand over the answer being graded) and a
  tier tag (the practice-set ramp does not apply to a scored problem).

**Demo:** `specs/chem_u07_unit_test.json`, Chemistry U7 (The Mole & Chemical Quantities) S7.1–S7.4 —
the section range the worksheet demo (SHULL-CHG-0019) already covers. Day 1: 8 conceptual items,
2 versions. Day 2: 5 computational problems, 2 versions, 22 points each, independently re-solved
with different compounds and numbers per version.

**Standard codes are marked PROVISIONAL.** Ohio HS Chemistry standard alignment for this unit has
not been confirmed; a wrong code is worse than none, so none is printed on any item.

## A defect found and fixed while building it

The first draft of the Day 1 demo put the correct answer at choice A on all 8 items in both
versions — technically valid against every rule that existed, and exactly the pattern a test-savvy
student finds in five minutes. No build-time check catches this yet; it was caught the way a
teacher catches it, by reading the bank back. The demo now varies the correct position across
A–D. Worth a future validator addition if it recurs.

## A second, unrelated defect fixed in passing

`section_span()` — the `S##.#` filename fragment — was implemented three separate times (notes,
worksheet, and now assessment), and none of the three copies zero-padded the unit digit before the
decimal, so a two-section Chemistry span rendered as `S7.1-S7.4` instead of the `S07.1-S07.4` that
`standards/NAMING.md`'s own worked examples show. This is the exact "a fact lives twice" defect the
naming standard exists to prevent, just not caught until a third copy was about to be written.
Consolidated into one function in `templates/_shull_docx.py`; all three builders now call it.
Regression-checked against the existing worksheet and notes demo specs before and after — both
still build.

## Verified

- All four validator refusals fire on deliberately broken specs (blueprint mismatch, `selfCheck` on
  a graded test, an "all of the above" choice, a missing distractor rationale) and the real demo
  spec builds clean through both.
- Day 2 rendered to PDF and rasterised at 110dpi, both versions and both keys: no clipped text, work
  boxes render at their specified height, equation bar and given/need tables render correctly.
- `pdffonts`: Archivo only (Bold + Regular), no DejaVu/Liberation fallback.
- `audit_print_ink.py`: 1.07% average toner (ceiling 9%), no solid band — well inside budget.
- Filenames, footer, and header chip all agree: `U07 / S07.1-S07.4`.
- Every Day 2 problem re-solved independently per version (different compounds, different masses);
  worked steps in each key checked by hand.
- Regression: `build_worksheet_docx.py` and `build_notes_docx.py` still run clean against their
  existing demo specs after the shared `section_span()` change.

## What is not built yet

- No real Pear Assessment import format (CSV/QTI) — the item bank is a manual-entry reference, not
  an integration, and is documented as such rather than implied to be more.
- Physics has no assessment-shape section in `courses/physics/DECISIONS.md` yet. Geology's
  single-day MC/matching shape is close to the Day 1 item bank but has not been built against.
- No dedicated audit script for the assessment system — a test has no fixed page budget the way a
  practice set does, so page count is checked by eye rather than by a script like `audit_worksheet.py`.

**Implemented by:** `templates/assessment/` (README, both builders, demo spec),
`templates/_shull_docx.py` (`section_span()`), `templates/notes/build_notes_docx.py` and
`templates/worksheet/build_worksheet_docx.py` (consuming the shared helper), `templates/README.md`
(status table corrected across all five systems).
