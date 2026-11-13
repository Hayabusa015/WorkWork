# SHULL-CHG-0046 — Teacher keys list every equivalent form of a direction answer

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0046 |
| **Date** | 2026-10-21 |
| **Source** | User — Matt. Request, 2026-10-20: "so on the answer key, I think I'd like to put all of the possible angles that could be an answer, just so students can check". Asked whether this should become standard for every key with a direction answer, he answered, 2026-10-21: "make it the standard". Path B (build/standard change). |
| **Current Rule** | See §1. `standards/ANSWER_KEYS.md` has no rule about direction answers. It ends at §9. |
| **Proposed Rule** | See §2. One new section, §10, in `standards/ANSWER_KEYS.md`, plus one clause added to its Authority line. |
| **Supersedes** | Nothing. This adds a rule where none exists. `courses/physics/DECISIONS.md` lines 105-106 ("Vectors. Any vector quantity gets a direction, always.") is not changed. This record says how a direction is shown on a key, not whether one is required. |
| **Reason** | Direction answers have several correct written forms (337 degrees, -23 degrees, 23 degrees south of east, 67 degrees east of south). A student who gets a right answer in a different form cannot tell from a key that shows one form that they are right. Matt wants every acceptable form on the key so students can check. He made it standard rather than a one-off for Physics U2 S2.2. |
| **Affected Agents** | Designer (builds keys and must produce the line). Auditor (the QA gate checks that the line exists for every direction answer). Secretary (implements only after approval). |
| **Affected Skills** | `build-document`, `build-assessment`, `audit-deliverable`. All three point at `standards/ANSWER_KEYS.md` and restate none of it, so they are not edited by this record. Listed so the Auditor knows what to re-read. |
| **Affected Courses** | Physics now. Any course with direction answers later. No course `DECISIONS.md` is edited. |
| **Risk** | Low. Teacher keys only. Student pages are unchanged. One new section in one file, one revertible commit. |
| **Recommendation** | Approve. See §6. |
| **Decision** | "refile the 2.2 key and make it the standard" — Matt, 2026-10-21, replying to the question of whether this should become the standard for every key with a direction answer. Question 2 in §7 (naming the check in the QA gate) was not answered, so the §7 default stands: QA gate left alone. |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | commit c1fbf69 |
| **Verified** | Yes. 2026-10-21, main session: `git diff` showed only §10, the Authority-line clause, this record and the changelog row; `scripts/validate_references.py`, `validate_layers.py` and `validate_tokens.py` all report OK; §10 holds no font name, hex value, spec schema or `_dir_check()` code. Reference build: `phys_u02_s02.2.verify.py` passes (27 forms) and fails on a planted error. |

---

## 1. Current Rule — verbatim

`standards/ANSWER_KEYS.md` has nine sections (§1 Scope to §9 The audit) and none covers direction answers. The nearest text:

### 1a. §8, "The arithmetic is still re-solved"

> The handwritten look changes nothing about `standards/QA_GATE.md` §9. `verify-content` re-solves every
> number from the problem statement, each parallel version included, and reads each handwritten step
> **as printed**, not as the builder meant it. Every label on a sketch — value, unit, direction — is
> checked against the problem statement the same way.

### 1b. §1, "Scope"

> **Teacher answer keys only** — the separate `Key` file (`standards/NAMING.md` §2). Student pages are
> never handwritten and are unchanged: they stay in the brand face.

### 1c. `courses/physics/DECISIONS.md` lines 105-106, the course fact this touches but does not change

> **Vectors.** Any vector quantity gets a direction, always. Magnitude alone is an incomplete answer
> for displacement, velocity, acceleration, force, momentum, and field strength.

## 2. Proposed Rule

### 2a. Add a new section to `standards/ANSWER_KEYS.md`, after §9

> ## 10. Direction answers list every equivalent form
>
> A boxed answer that is a direction, an angle or a compass direction, is followed by one more line
> headed **same direction:**. It lists every other acceptable way to write that direction, so a
> student who reached a different form can check.
>
> 1. **Angle measured from the axes (0 to 360 degrees).** List the clockwise-negative form (the angle
>    minus 360), then both compass forms, one measured from each neighbouring axis. List the smaller
>    angle first. Use a true minus sign.
>    Example: 337 degrees = -23 degrees = 23 degrees south of east = 67 degrees east of south.
> 2. **Exactly on an axis.** Write the compass name, for example "due east".
> 3. **A launch angle given above or below the horizontal** (projectile sets, which have no compass).
>    List the clockwise or anticlockwise equivalent and the angle from straight up or straight down.
>    Example: 36 degrees above horizontal = -324 degrees = 54 degrees from straight up.
> 4. **Same page.** The line stays on the same page as its boxed answer and is never split from it.
> 5. **Verified at build.** Every listed form is checked independently: each form is turned back into a
>    direction and must match the boxed answer to within half a degree for a whole-degree answer. A
>    mismatch fails the build. The reference implementation is `_dir_check()` in
>    `templates/worksheet/specs/phys_u02_s02.2.verify.py`. This file does not restate it.
> 6. **Keys only.** Student pages are unchanged. The `"steps"` spec schema stays documented once, in
>    the docstring of `scripts/key_solution.py`.

(Wording is the Secretary's drafting of Matt's rule. The examples are Matt's. At implementation the Secretary may adjust formatting to match the file. The rule stays the same. The numerals in the examples are written as in the request, and the key itself prints a degree sign.)

### 2b. Authority line

Add "SHULL-CHG-0046 (§10, equivalent forms of a direction answer)" to the **Authority** line at the top of `standards/ANSWER_KEYS.md`, the way that file cites its changes.

No font name and no hex value is written. The file names tokens only, as SHULL-CHG-0044 Item F requires.

### 2c. Checks on the worked examples

- 337 degrees: 337 - 360 = -23. 360 - 337 = 23 degrees below the +x axis, so 23 degrees south of east. Measured from south (270 degrees), 337 - 270 = 67 degrees toward east, so 67 degrees east of south. All four forms agree.
- 36 degrees above horizontal: 36 - 360 = -324. From straight up (90 degrees), 90 - 36 = 54. Both agree.

## 3. Reference implementation (the worked example, not restated here)

Already committed on branch `claude/wizardly-mendel-p73co4`, commit `198695f` (main session's account; the Secretary has not inspected the commit):

- `templates/worksheet/specs/phys_u02_s02.2.json`: the "same direction:" rows in `"steps"`.
- `templates/worksheet/specs/phys_u02_s02.2.build.sh` and `phys_u02_s02.3_part*.build.sh`: the keep-together rule.
- The three `.verify.py` files, including `_dir_check()`, tested 2026-10-20 against a planted error.

This record does not edit any of them and does not copy their code. Approving §2 makes that work the example the standard points to.

## 4. Scope limits

- Teacher keys only. Student pages are unchanged.
- `standards/ANSWER_KEYS.md` only. No `QA_GATE.md` edit is proposed. The Auditor reaches the rule through `audit-deliverable`, which points at `ANSWER_KEYS.md`. If Matt wants an explicit line in the QA gate, that is a separate, small record.
- No change to the three skills, the agents, `scripts/`, `brand/`, or any course `DECISIONS.md`.
- Keys already built are not rebuilt by this record. Other Physics keys with direction answers pick up the rule when next rebuilt, or sooner if Matt asks.

## 5. Conflicts with LOCKED rules (the Secretary does not resolve these; Matt decides)

None found.

| # | Rule | Where | Conflict |
|---|---|---|---|
| 1 | Student pages unchanged | `standards/ANSWER_KEYS.md` §1 | **No conflict.** The new line is on the key only. |
| 2 | Re-solve every number and check every sketch direction label | `standards/ANSWER_KEYS.md` §8 | **No conflict.** §10 adds a build-time check on the new line. §8 stays as is. |
| 3 | Vectors always carry a direction | `courses/physics/DECISIONS.md` lines 105-106 | **No conflict.** The course fact is unchanged. |

No LOCKED, CONFLICT, PROVISIONAL or UNKNOWN item is changed or converted.

## 6. Recommendation

Approve. It is what Matt asked for, in his words, and he confirmed it should be standard. The rule is small, keys only, and has a working reference build with a negative test.

## 7. Questions for Matt

1. Approve the new §10 in `standards/ANSWER_KEYS.md` as drafted in §2a?
2. Should the QA gate also name this check explicitly, or is the pointer through `audit-deliverable` enough? (Default if you do not say: leave the QA gate alone.)

## 8. Verification plan (for the Secretary, after approval)

- `git diff` shows only: the new §10 and the Authority-line clause in `standards/ANSWER_KEYS.md`, this record, and the changelog row. One commit carrying SHULL-CHG-0046.
- Grep of `standards/ANSWER_KEYS.md` finds no font name and no hex value.
- The new section restates no spec schema and none of `_dir_check()`'s code.
- `scripts/validate_references.py`, `validate_layers.py`, `validate_tokens.py` pass (main session runs them if the Secretary has no shell).
- Fill in `Implemented By` with the commit SHA and `Verified` with the result.
- Later, outside this record: the Auditor spot-checks a rebuilt direction key for the line, on the same page as its box.

## 9. Not done by this record

No standard, skill, agent, brand, governance rule, course, template, or script file was edited. `standards/ANSWER_KEYS.md` is untouched. Nothing was committed. This is a proposal only. Implementation waits for a committed record with `Status: APPROVED` and a verbatim `Decision:` quote (`governance/CHANGE_CONTROL.md` §4). The `Decision:` field is empty for the main session to fill.
