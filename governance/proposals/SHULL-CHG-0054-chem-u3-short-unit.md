# SHULL-CHG-0054 — Chemistry U3: a quiz replaces the unit test, and 3.5 Additional Periodic Trends is dropped

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0054 |
| **Date** | 2026-10-26 |
| **Source** | User. **Path A, a course fact.** It touches `courses/chemistry/DECISIONS.md` only. It is written as a record because only the Secretary may edit `courses/`, and only against an APPROVED record. The trigger was the main session's plan for a short U3 The Periodic Table unit (§1c). The quotes below reached the Secretary through the main session. The Secretary did not hear them directly. |
| **Current Rule** | See §1 |
| **Proposed Rule** | See §2 |
| **Supersedes** | (a) `courses/chemistry/DECISIONS.md`, Assessment shape, **Unit tests — two days**, lines 149–158, as it applies to U3: every unit, U3 included, ends with the two-day test. (b) The same file, Curriculum map, **U3 The Periodic Table**, lines 35–38, where "3.5 Additional Periodic Trends" is listed as a taught section. **Not LOCKED-rule drift.** The curriculum map and the assessment shape are CONFIRMED, and the user himself is changing them. No other record is superseded. |
| **Reason** | The user answered both questions the main session asked before building U3 (§1c). Both answers change course facts that `DECISIONS.md` currently states the other way. Until the file says so, a builder following `CLAUDE.md` §3 would still find S03.5 valid and would still build a two-day U3 test. |
| **Affected Agents** | Designer and builders (U3 assessment, chip and section codes). Auditor (checks codes against the map and assessments against the assessment shape). Librarian (any Drive `Section 03.5` folder; not surveyed, §5) |
| **Affected Skills** | None edited. No skill or template in the repository cites S03.5 or a U3 unit test (Grep, 2026-10-26, `legacy/` excluded) |
| **Affected Courses** | Chemistry only |
| **Risk** | **Low.** One course, one unit, and no code is renumbered. Two things to watch: the validator (§3), and the optional-worksheet policy, which is tied to "test time" (§4, question 3). |
| **Recommendation** | Apply §2a, §2b and §2c. For 3.5, **Option 1** in §3: keep it listed, mark it DROPPED, and retire the code. 3.6 and 3.7 keep their numbers. Validator sub-choice: see §3. |
| **Decision** | **Approved by the user, 2026-10-26**, in the main session, answering the two questions this record formalizes (does the quiz replace the U3 test; what to do with 3.5). Verbatim: *"Quiz replaces the test, drop 3.5, build all of it"*. Recorded under SHULL-CHG-0034. The user did not answer the validator sub-choice or the §4 follow-ups; those are not decided by this quote. |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | e180805. §2a, §2b and §2c are applied exactly as written, with sub-option **1(a)**. The user did not answer the validator sub-choice, so 1(a) is the **main session's default**, chosen to match the U1 precedent (SHULL-CHG-0036) and keep the two retired-code markings consistent. It is not a user choice, and it is not this record's recommendation (§3 recommended 1(b)). **1(b) was not applied and needs its own record.** The §4 follow-up questions (2 and 3) stay open. |
| **Verified** | **Yes, under validator option 1(a).** Secretary read-check 2026-10-26: §2a, §2b, §2c match the record word for word; the log entry is first under "Decision log" and no earlier entry changed; `Last updated` is 2026-10-26. Main session, after commit e180805: `scripts/validate_codes.py` passes with Chemistry at 90 valid codes (unchanged, as 1(a) predicts), and `validate_layers`, `validate_references`, `validate_agents` and `validate_schemas` pass. The commit touched only DECISIONS.md, this record and the CHANGELOG row; `legacy/` untouched. §4 questions remain open. |

---

## 1. Current Rule — verbatim

### 1a. `courses/chemistry/DECISIONS.md`, Curriculum map, lines 35–38

> **U3 The Periodic Table** (7 sections)
> 3.1 Organization, Families & Groups · 3.2 Metals, Nonmetals & Metalloids · 3.3 Atomic & Ionic
> Radius · 3.4 Ionization Energy & Electronegativity · 3.5 Additional Periodic Trends · 3.6
> Explaining Periodic Trends · 3.7 Ion Formation

The file names 3.5 but says nothing about what it contains.

### 1b. `courses/chemistry/DECISIONS.md`, Assessment shape, lines 144–158

> ### Quizzes (Friday)
> 5–6 questions, usually 3–4 equivalent versions, same skills and rigor with numbers/order
> changed. Occasional essay quiz. May include 1–2 short prior-unit recall items, especially
> durable skills like naming and formulas.
>
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

The decision log has **no entry** for either change.

### 1c. The user, verbatim, 2026-10-26

The main session proposed a short U3: Day 1 family coloring (3.1, 3.2); Day 2 Periodic Trends Gizmo
(3.3, 3.4); Day 3 a short deck and practice on electronegativity, explaining trends, and
cations/anions (3.4, 3.6, 3.7); Day 4 Operation Periodic Table v2; Day 5 a short quiz. It asked:

1. *"Quiz vs. unit test. Chem DECISIONS.md says each unit ends with a two-day test (about 25
   multiple choice, then about 5 calculation problems). Does this small quiz replace the U3 test, or
   do you still give the test? If it replaces it, I'll record that as a course decision."*
2. *"Section 3.5, 'Additional Periodic Trends'. The decisions file names it but doesn't say what goes
   in it. Is it electron affinity, reactivity, or something you want to drop from this shortened
   version? I won't guess."*

He replied: *"Quiz replaces the test, drop 3.5, build all of it"*

His reply answers both questions. Whether it also approves the `DECISIONS.md` text below, which was
written after he answered, is for the main session to record under `CHANGE_CONTROL.md` §4. The
Secretary does not read it as approval of this record.

**Scope as the Secretary reads it.** "This small quiz replaces the U3 test" is a U3-only answer. It
is not recorded as a change for any other unit. "Drop 3.5 from this shortened version" is recorded as
dropping the section from the course, because the curriculum map has one version of U3. If he meant
only "skip it this year", that is a different record (§4, question 1).

---

## 2. Proposed Rule

U3 ends with a single quiz in the standard quiz shape instead of the two-day unit test. This is a
U3-only exception; every other unit keeps the two-day test. Section 3.5 Additional Periodic Trends
is **dropped**. The code 3.5 is **retired, not reused**. 3.6 Explaining Periodic Trends and 3.7 Ion
Formation **keep their codes**.

The exception lives in **one place**, under "Unit tests — two days", because that is the rule it
modifies and where a builder of a unit test reads. The U3 curriculum-map line carries only the 3.5
change and a pointer to the log; it does not restate the quiz exception.

### 2a. The U3 line (replaces lines 35–38), Option 1, recommended

```
**U3 The Periodic Table** (7 section codes, 6 taught) — *3.5 is dropped; see the log*
3.1 Organization, Families & Groups · 3.2 Metals, Nonmetals & Metalloids · 3.3 Atomic & Ionic
Radius · 3.4 Ionization Energy & Electronegativity · 3.5 Additional Periodic Trends — DROPPED,
code retired, never reused · 3.6 Explaining Periodic Trends · 3.7 Ion Formation
```

This follows the U1 pattern set by SHULL-CHG-0036 (*"5 section codes, 4 taught — 1.4 is folded into
1.3; see the log"*). This is the validator sub-choice **1(a)**; §3 gives the 1(b) wording.

### 2b. Under "Unit tests — two days" (inserted after line 154, before the "Brief durable-skill recall" paragraph)

```
**Exception — U3 only:** U3 ends with one quiz in the Quizzes shape above, not a unit test. Every
other unit keeps the two-day test. See the 2026-10-26 decision-log entry.
```

### 2c. Decision-log entry, for the top of the log (`CHANGE_CONTROL.md` §5)

```markdown
### 2026-10-26 — U3: a quiz replaces the unit test; 3.5 Additional Periodic Trends dropped
U3 The Periodic Table ends with a single quiz in the standard quiz shape (Assessment shape →
Quizzes) instead of the two-day unit test. This is a U3-only exception; every other unit keeps the
two-day test. Section 3.5 Additional Periodic Trends is dropped. The code 3.5 is retired and never
reused; 3.6 Explaining Periodic Trends and 3.7 Ion Formation keep their codes, so nothing is
renumbered. Decided by Matt 2026-10-26 while planning a short U3 ("Quiz replaces the test, drop
3.5, build all of it"), in answer to whether the quiz replaces the U3 test and what 3.5 contains.
Supersedes: Assessment shape, "Unit tests — two days", as applied to U3; Curriculum map, U3 line,
"3.5 Additional Periodic Trends" as a taught section.
Status: CONFIRMED · SHULL-CHG-0054
```

`Status: CONFIRMED` is written only on implementation, after approval. The header line
`**Last updated:** 2026-10-15` becomes the implementation date.

---

## 3. Which form keeps codes stable

| Option | What it does | Codes |
|---|---|---|
| **1. Keep 3.5 listed, mark it DROPPED (recommended)** | §2a | **Stable.** 3.6 and 3.7 keep their numbers. The gap is explained on the line |
| 2. Remove 3.5, leave a gap (3.4, 3.6, 3.7) | Deletes the entry | Stable, but the gap has no explanation on the line, and the history is only in the log |
| 3. Remove 3.5 and renumber 3.6 → 3.5, 3.7 → 3.6 | Closes the gap | **Unstable.** Any S03.6 or S03.7 file, folder, chip or citation built before or during this unit would be wrong. **Not recommended** |

### The validator: a sub-choice inside Option 1

`scripts/validate_codes.py` gets its valid codes from the curriculum map through `section_codes()`
in `scripts/_shullos.py`, lines 42–62. Its plain-form pattern
`(?:^|[·|]\s*)(\d{1,2}\.\d)\s+(?=[A-Za-z(])` matches **"· 3.5 Additional"**. (SHULL-CHG-0036 quoted
lines 42–59 and a `[A-Z(]` lookahead. The function has since grown and the lookahead now accepts
lowercase; the conclusion is the same.) As a result:

- **1(a), as written in §2a.** 3.5 stays machine-valid. Nothing goes red, and the Chemistry code
  count stays 90. **But the validator will not catch a new S03.5 build.** Only the human check in
  `CLAUDE.md` §3 would, by reading "DROPPED". This matches what U1 has today.
- **1(b).** Write the entry so the pattern cannot match it:

  ```
  Radius · 3.4 Ionization Energy & Electronegativity · ~~3.5 Additional Periodic Trends~~ DROPPED,
  code retired, never reused · 3.6 Explaining Periodic Trends · 3.7 Ion Formation
  ```

  `~~` sits between the `·` and the digits, so 3.5 is not captured; 3.6 and 3.7 still are. The
  validator then rejects S03.5 from then on, and the Chemistry count drops from 90 to 89. **Unlike
  SHULL-CHG-0036, no live repository file depends on the code:** a Grep on 2026-10-26 for `S03.5`,
  `S3.5`, `U03` and "Additional Periodic Trends" outside `legacy/` finds only the DECISIONS line
  itself and doc mentions of a `CHEM_U03_…Periodic_Trends_v1` proposal with no section code. So 1(b)
  should not turn anything red. **Cost:** U1 and U3 would then mark retired codes two different ways.

**Recommendation: 1(b) for U3.** It costs nothing in the repository today, and it makes the
validator enforce the drop before any U3 material is built. If the user prefers the two units to
look alike, 1(a) is safe. This is a reading of the regex. It has not been run.

---

## 4. For the user

| # | Question |
|---|---|
| 1 | Approve recording both changes as §2a/§2b/§2c? Is 3.5 dropped from the course (as written), or only skipped this year? |
| 2 | Validator: 1(b) (recommended, the validator rejects S03.5) or 1(a) (matches U1, human check only)? |
| 3 | **Not resolved here.** The 2026-09-15 standing policy lets optional worksheets be turned in "at test time — the day of the relevant unit test" for +1 point each "on that test's score". U3 will have no unit test. Do U3 optional worksheets redeem on the U3 quiz, roll to the U4 test, or not apply in U3? This changes how a U3 optional worksheet's header is written, so it should be answered before one is built. |

---

## 5. Downstream. Noted, not fixed

These follow from the change. **None is edited by this record.** Each belongs to its owner.

| Item | Where | Issue | Owner |
|---|---|---|---|
| Pacing principles | `courses/chemistry/DECISIONS.md` line 287–288, "Preserve the two-day unit-test structure" | Reads as universal. The exception in §2b governs; this line is not restated, by design | None, unless the user wants a pointer added (would need its own approval) |
| Pacing guide | Same file, lines 300–301, "a 2-day Unit Test … at the end of each unit". PROVISIONAL | Q1/U3 day allocation now includes a quiz, not a 2-day test, and one fewer section | User, when the pacing guide is validated |
| Optional-worksheet policy | Same file, decision log 2026-09-15 | Tied to "test time"; U3 has none | User, §4 question 3 |
| Gradebook weight | Same file, Open question 3 (CONFLICT-24): Tests 55 / Quizzes 20 | U3's end-of-unit assessment moves from the Tests category to Quizzes. Noted only; Open question 3 stays OPEN | User |
| Drive `Section 03.5` folder | CHEM Unit 03 on Drive | **Not surveyed.** The 2026-09-23 survey did not sample CHEM U03. If a folder exists, it can be left as a marker or trashed with his approval and a pre-mutation log | Librarian / user |
| Lab and activity placement | Same file, Open question 4 | The short-unit plan uses a Periodic Trends Gizmo and Operation Periodic Table v2. Open question 4 confirms no lab past U1.1 and blocks building any lab past Unit 0 as final rather than draft. Whether these two count as labs is not decided by this record | User / main session before building |

---

## 6. Verification required before this is IMPLEMENTED

- [ ] `courses/chemistry/DECISIONS.md` U3 line matches the approved sub-option exactly (§2a, or the
      1(b) wording in §3)
- [ ] The U3-only exception appears under "Unit tests — two days" exactly as §2b, and nowhere else
      as a restated rule
- [ ] The decision-log entry is at the **top** of the log. No earlier entry is edited
- [ ] `Last updated` is set to the implementation date
- [ ] `python3 scripts/validate_codes.py` gives the expected result. Under 1(a): passes, and the
      Chemistry code count is unchanged (90). Under 1(b): passes, and the Chemistry count is 89
- [ ] `validate_layers`, `validate_references`, `validate_agents` and `validate_schemas` pass
- [ ] No other file changed in the commit except this record and its `change-log/CHANGELOG.md` row.
      `legacy/` untouched
- [ ] The commit carries `SHULL-CHG-0054`. `Implemented By` and `Verified` filled in here
