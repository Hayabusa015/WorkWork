# SHULL-CHG-0032 — Chemistry U1: a single-day unit test, no Day 2

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0032 |
| **Date** | 2026-09-28 |
| **Source** | User. **Path A, a course fact, Chemistry only.** It touches `courses/chemistry/DECISIONS.md` only. It is written as a record because only the Secretary may edit `courses/`, and only against an APPROVED record. The quote below reached the Secretary through the main session. The Secretary did not hear it directly. |
| **Current Rule** | See §1 |
| **Proposed Rule** | See §2. **It is the main session's reading of his answer, not his words.** |
| **Supersedes** | `courses/chemistry/DECISIONS.md`, Assessment shape, **Unit tests — two days**, lines 149–154, **for Unit 1 only**. Also, as they apply to Unit 1: the Pacing paragraph, lines 300–301, and the Pacing principles sentence at line 288 (§5). **Not LOCKED-rule drift.** The rule is a course fact, and the user himself is changing it. The two-day form stays the default for every other unit. |
| **Reason** | He was asked to build a rough Unit 1 test, and whether Day 2's classification question should move to Day 1. He doubts Unit 1 has enough content for a Day 2. `DECISIONS.md` requires two days for every unit test, with no exception. Building a one-day test now would contradict the authoritative file. |
| **Affected Agents** | Designer and test builders (item counts, versions, Unit 1 test files). Auditor (checks tests against the Assessment shape). |
| **Affected Skills** | None edited. Any assessment or test-building skill that states the two-day form is stale for Unit 1 once this is approved, and is reported, not obeyed (`CLAUDE.md` §2). Not checked here. |
| **Affected Courses** | Chemistry only |
| **Risk** | **Low.** One course, one unit, and no section code changes. The two-day default is untouched. |
| **Recommendation** | Approve §2 after the user answers the open questions in §3. Question 1 (version count) changes what gets built, so it comes first. |
| **Decision** | **Rejected by the user, 2026-09-28**, in the main session. He first said *"I'm not sure if there's enough in this unit to have a day 2 test."* Then, while thinking it through, he asked: *"Could we add a day 2 written test. Usually I add problem. We could add average atomic mass problems. The table.. what else, I dont really wrong long answer on the day2"*. The main session proposed a short Day 2 (the fill-in chart plus three average-atomic-mass problems, no long answers) and he answered, verbatim: *"yes, do the two-day version."* Unit 1 therefore keeps the two-day unit-test form in `courses/chemistry/DECISIONS.md`, and no exception is needed. The Day 2 tests built earlier are superseded by a new Day 2, not by this record. Recorded under SHULL-CHG-0026. |
| **Status** | **REJECTED** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. Nothing has been implemented. The required checks are in §6. |

---

## 1. Current Rule — verbatim

### 1a. `courses/chemistry/DECISIONS.md`, Assessment shape, "Unit tests — two days", lines 149–158

> ### Unit tests — two days
> **Day 1, conceptual:** ~25 multiple choice, four versions (A–D), equivalent content and
> rigor, strong distractors from real misconceptions.
> **Day 2, computational:** ~5 free-response calculation problems, partial credit available,
> work and units required. Covers the current unit only — never insert an earlier-unit
> calculation just to make it cumulative.
>
> Brief durable-skill recall may appear on quizzes and the conceptual test; the computational
> test stays focused on the current unit. No curve. No retakes. Study guides align to concepts
> and skills but never duplicate test questions.

### 1b. `courses/chemistry/DECISIONS.md`, Pacing guide (PROVISIONAL), lines 300–301

> Within each quarter: roughly 1.5–2 days per section plus a 2-day Unit Test (Day 1 conceptual
> MC, Day 2 computational FR) at the end of each unit, with a buffer/review week at the end of

### 1c. Also found by the Secretary, not in the brief. `DECISIONS.md`, Pacing principles, lines 287–289

> Keep labs within one period. Preserve the
> two-day unit-test structure. No new content on planned substitute days.

This sentence is a third statement of the same two-day rule. It is not LOCKED and not marked
otherwise. It needs the same Unit 1 carve-out as 1a and 1b, or it will contradict them.

### 1d. The user, verbatim, 2026-09-28

He was asked to build a rough Unit 1 test: about 30 conceptual questions, plus whether Day 2's
classification question should move to Day 1. He answered:

> "I'm not sure if there's enough in this unit to have a day 2 test.  Create the test with average atomic madden calculations. Maybe 2 if them.  1 with atoms and 1 with abundance"

**How the Secretary reads this, and where it is weaker than the proposal.**
- The first sentence is a doubt, not a ruling. The instruction that follows ("Create the test with ...
  calculations") implies a single test, but he does not say "no Day 2" in words. Whether he means
  "drop Day 2 for Unit 1" is the main session's reading, and the user should confirm it.
- His answer does not address the classification question directly (move to Day 1, or not).
- "madden" is read as "mass" and "if them" as "of them". "1 with atoms" is read as isotope mass
  numbers with atom counts, and "1 with abundance" as mass numbers with percent abundances. These
  are readings of typos and shorthand.
- He gave no item count and no version count. "About 30" came from the question put to him.

---

## 2. Proposed Rule

**This is the main session's reading of his answer.** The wording below is the Secretary's draft.

- Unit 1 (Matter & Atomic Structure) has a **single-day unit test, with no Day 2**.
- It has **30 items: 28 multiple choice and 2 average-atomic-mass calculations.** One calculation
  gives isotope mass numbers with atom counts. The other gives mass numbers with percent
  abundances.
- The **two-day structure remains the default for every other unit.** This is a Unit 1 exception,
  not a general change.
- The Day 2 tests A–D built earlier (`SHULL_CHEM_Test_U01_S01.1-S01.5_Day2_*`) are **superseded for
  Unit 1. They are not deleted.**

### 2a. Draft edit to "Unit tests — two days" (Secretary's wording, for the user to adjust)

Inserted after line 158, leaving lines 149–158 untouched:

```
**Exception — Unit 1 is a single-day test.** Unit 1 (Matter & Atomic Structure) has one test day
and no Day 2: 30 items, 28 multiple choice and 2 average-atomic-mass calculations (one from
isotope mass numbers with atom counts, one from mass numbers with percent abundances). Every
other unit keeps the two-day form above. See the log, 2026-09-28.
```

### 2b. Draft decision-log entry, for the top of the log (`CHANGE_CONTROL.md` §5)

```markdown
### 2026-09-28 — U1: single-day unit test, no Day 2
The Unit 1 unit test is one day, 30 items: 28 multiple choice and 2 average-atomic-mass
calculations (one from isotope mass numbers with atom counts, one from mass numbers with percent
abundances). No Day 2 for Unit 1. The two-day form remains the default for all other units. The
earlier Day 2 tests A-D (SHULL_CHEM_Test_U01_S01.1-S01.5_Day2_*) are superseded for Unit 1 and are
not deleted. Matt, 2026-09-28: "I'm not sure if there's enough in this unit to have a day 2 test.
Create the test with average atomic madden calculations. Maybe 2 if them.  1 with atoms and 1 with
abundance"
Supersedes: Assessment shape, "Unit tests — two days", for Unit 1 only.
Status: CONFIRMED · SHULL-CHG-0032
```

`Status: CONFIRMED` is written only on implementation, after approval. The header line
`**Last updated:** 2026-09-23` becomes the implementation date.

---

## 3. Open questions. Listed, not resolved

| # | Question | Why it matters |
|---|---|---|
| 1 | **Version count.** 30 items in four versions (A–D), or in one? | The current rule requires four versions for Day 1. A one-version test is a second departure from the rule, and is not what he said. `standards/QA_GATE.md` requires identical blueprints across parallel versions, so four versions is also the larger build. |
| 2 | **Are the earlier-flagged Day 2 items now moot?** Q1 classification (audit item 27), and the two repeated items, Version B Q5 row 3 (item 24) and Version D Q1a (item 25). | If the Day 2 tests are set aside for Unit 1, these may only matter if the items are reused in the new test. Items 19–23, 26, 28 and 35 may be moot on the same reasoning, unless material is carried over. The calculator-policy question (item 28) may still apply to the new calculations. |
| 3 | **Should the "~25 multiple choice" figure change for Unit 1?** This test has 28. | The rule says "~25", and 28 is close but not equal. The user may treat "~" as covering it, or want the Unit 1 exception to state 28. §2a currently states 28. |
| 4 | **Should other short units get the same single-day form?** | This record makes Unit 1 the only exception. A general rule needs its own record. Not proposed here. |
| 5 | **Does the classification question move to Day 1?** | He was asked this and his answer does not address it. With no Day 2, the question may have no "from Day 2" to move from. Listed because it was the question he was actually asked. |
| 6 | **Does the rule "Brief durable-skill recall may appear on ... the conceptual test; the computational test stays focused on the current unit" apply to the combined test?** | The two calculations now share a test with the MC items. Not resolved here. |

---

## 4. For the user

| # | Question |
|---|---|
| 1 | Does "I'm not sure if there's enough ... for a day 2 test" mean: no Day 2 for Unit 1, as §2 reads it? |
| 2 | Four versions or one? (§3, question 1) |
| 3 | Approve recording §2a and §2b, with any changes to the wording? |

---

## 5. Downstream. Noted, not fixed

| Item | Where | Issue |
|---|---|---|
| Pacing paragraph | `DECISIONS.md` lines 300–301 | Says every unit ends with a "2-day Unit Test". It is a generic statement and is marked PROVISIONAL. It would be wrong for Unit 1 only. **This record does not edit it.** Whether to add a Unit 1 carve-out is the user's call. |
| Pacing principles | `DECISIONS.md` lines 287–289 | "Preserve the two-day unit-test structure." Same issue, not in the brief. |
| **Unit 1 calendar** | Not in `DECISIONS.md` | The authoritative file has **no per-unit calendar**, only the generic pacing paragraph, so **the file needs no calendar change beyond the above.** The branded week-by-week PDF pacing guide mentioned at line 306 is not in `courses/`, and the Secretary did not check it. If it shows a 2-day Unit 1 test, it would show one spare day. Whether to reuse that day (review, buffer) is Matt's decision, and no such use is proposed. |
| Unit review and study guide | Unit 1 review worksheet and key | **Unaffected.** Neither depends on the number of test days. The rule that study guides "never duplicate test questions" still applies, so the new test's items must be checked against the unit review, as the audit did for Day 2 (items 24, 25). |
| Existing Day 2 tests A–D + keys | Drive, `SHULL_CHEM_Test_U01_S01.1-S01.5_Day2_*` | Superseded for Unit 1, not deleted. Any move, rename or trash needs its own approval and a pre-mutation log. |
| Audit results for Day 2 | `reports/2026-09-23_chem-u01-qa-audit.md`, items 19–28, 35, 37, 38 | Listed as failing. See question 2 in §3. Not edited. |

---

## 6. Verification required before this is IMPLEMENTED

- [ ] `courses/chemistry/DECISIONS.md` lines 149–158 are unchanged, and the exception paragraph in
      §2a matches the approved wording exactly
- [ ] The decision-log entry is at the **top** of the log. No earlier entry is edited
- [ ] `Last updated` is set to the implementation date
- [ ] Whether lines 287–289 and 300–301 are edited is settled by the user's answer, and is recorded
      in `Decision:`. No edit is made without it
- [ ] The quote in the log entry matches §1d character for character, typos included
- [ ] No other file changed in the commit. `legacy/` untouched
- [ ] The commit carries `SHULL-CHG-0032`. `Implemented By` and `Verified` filled in here
