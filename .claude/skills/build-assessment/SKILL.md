---
name: build-assessment
description: Build SHULL quizzes, unit tests, exit tickets, bell ringers, and question banks with parallel versions and separate answer keys. Use for any assessment-generation or alternate-version request.
---

# build-assessment

Voice: `standards/VOICE.md`. Assessment shape is a **course fact** — read
`courses/<course>/DECISIONS.md`. The three courses differ substantially here.

## Every item

- Maps to a learning target, and to an Ohio standard when alignment is requested.
- **If the exact standard code is uncertain, say so.** A wrong code is worse than none.
- Tests the intended reasoning, not confusing wording.
- Uses vocabulary already taught, or defines it.
- **Distractors are real student misconceptions**, never random wrong values.
- No "all of the above" or "none of the above". No trick questions on wording.
- **Exactly one unambiguously best answer.**
- No false rigor — extra reading, ugly numbers, and vague prompts do not make a question harder.

## Every calculation

**Solve it during generation.** Ugly or unrealistic answers mean changing the numbers, not shipping
them. Never generate an answer by pattern.

## Parallel versions are not shuffles

Reorder questions **and** answer positions, change given values, swap scenarios where possible.
Every version maps to the same blueprint with identical standards coverage and point totals.

> **Re-solve every version independently.** This is the step most often skipped and it is how a
> wrong key reaches a class.

## Answer keys

**Always a separate file**, ending `_Key`. Each item carries: the correct answer · point value ·
full worked solution with units and significant figures · model responses with grading guidance ·
the standard code · and, for a full teacher key, why each distractor is wrong.

Note common misconceptions and any grading judgment calls. **Keep teacher-only information off the
student version.**

## Open-response prompts

Replace "Explain your answer" with the evidence expected: *"Name the trend, compare the two atoms,
and explain the attraction responsible for the difference."*

Do not demand full sentences for simple labels or numerical results unless writing quality is part
of the goal.

## Study guides

Cover the same concepts and reasoning as the assessment **without copying its questions.** Help
students identify what to practise rather than handing them an enormous checklist. Do not promise
that every listed detail will appear unless that is true.

## Finishing

`anti-ai-slop`, then `audit-deliverable`. The gate re-checks that every number was re-solved and
that the key is a separate file.
