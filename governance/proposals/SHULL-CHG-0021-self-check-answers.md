---
id: SHULL-CHG-0021
title: Calculations carry their answer, except the last one
status: IMPLEMENTED
opened: 2026-09-09
decided: 2026-09-09
decided_by: Matthew Shull
---

# SHULL-CHG-0021 — Self-check answers

## What he asked for

> "on calculations, include answers so the students can self check, add this on all but the final
> challenge problem. You can also remove the thing on the bottom with the checkboxes for self check"

## Decision

**Every calculation question carries its answer in brackets, except the last question in the
section.** The last one is the one they have to commit to without a safety net, so it is not merely
allowed to lack an answer — the builder *refuses* a self-check on it, and refuses a calculation
anywhere else that lacks one.

**Numeric results only**, which is the standing rule and now the reason for a new spec field. A
conceptual question keeps no bracket, because there the bracket hands over the whole answer rather
than confirming arithmetic. The builder cannot tell the two apart from the wording — "Name the
kinematic equation you would use" reads exactly like a physics problem and has no number in it — so
the spec marks a question `"calculation": true` and the builder enforces against that rather than
guessing. `"math": true` (a Chemistry question with a work box) implies it.

Two questions were deliberately left unmarked on that basis: PHYS 1.2 q2 ("name the equation, and
say which quantity it leaves out") and PHYS 1.4 q2 ("state the value and the sign of a"). Both are
recall, and in both the answer *is* the whole question.

## The bottom checklist

Removed from Physics and Chemistry. It duplicated the self-check role, and its banner read "NUMERIC
ANSWERS SELF-CHECK ON THE TEACHER COPY", which stopped being true the moment the answers moved onto
the student sheet.

**Kept on Geology**, where it is a different thing: "All six cards are glued down, in order, with
nothing loose" is a turn-in check on physical completeness, not a check on answers. Flagged for him
rather than removed on an assumption.

## The answers themselves

All twenty were computed rather than recalled, and the working is in the commit. One judgement:
Ca(NO₃)₂ comes to **164.09 g/mol** from precise atomic masses and **164.10** from the values on a
classroom periodic table. The sheet says 164.10, because that is what a student will get and a
self-check that disagrees with correct work is worse than no self-check.

## Mechanism

`check_profile()` refuses:

- a calculation that is not the last question and has no `selfCheck`;
- any `selfCheck` on the last question.

`scripts/validate_profiles.py` exercises both by feeding the builder a spec built to trip each —
15 refusals now, all firing, with the three real specs still building.

## Verification

- PHYS 4 pages, CHEM 4, GEO 2, all on their declared budgets.
- Answers render on questions 1–5 of each Physics section and on 1–7 of the Chemistry section;
  none on any last question.
- Toner within budget, no solid band, Archivo only.
- `hook-validate.sh` clean.
