# SHULL-CHG-0122 — Physics U4 reading: On Your Own boxes get work space (scoped exception)

> **No LOCKED rule is overridden, and nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.** The
> rule involved is the Physics "Worksheets" rule, marked CONFIRMED in `courses/physics/DECISIONS.md`.
> It names "practice sets, homework worksheets, and study guides". It does not name a unit reading.
> So this is a scoped exception and also a clarification for one reading (dossier finding A-17).
> The rule stays in force for every other Physics document.
>
> **One layer: Path A, a course fact** (`governance/CHANGE_CONTROL.md` §1). It affects Physics only
> (CLAUDE.md §2 test). No standard, skill, template, builder or validator is touched.
>
> **Format precedent:** the 2026-11-12 "One-time lab-template exceptions: '3.1 Lab - Newton's Laws'"
> entry in the Physics decision log (SHULL-CHG-0073): scoped to named files, not a precedent, shared
> files untouched.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0122 |
| **Date** | 2026-11-26 |
| **Source** | User. Matt, main session, 2026-11-26. He was asked "Your Physics rule says no work areas on student pages (students work in notebooks). How should the On Your Own boxes look?" The options were "No space, 'use notebook' (Recommended)" and "Add work space" (described as "Give each On Your Own box room to work, like the Chemistry readings."). He chose "Add work space". Recording it was requested by finding A-17 in `reports/phys_u04_reading_dossier.md`. |
| **Current Rule** | `courses/physics/DECISIONS.md`, "Worksheets — CONFIRMED, and it differs from Chemistry": "**No work areas on Physics worksheets.** Practice sets, homework worksheets, and study guides carry problems and prompts only — no ruled lines, no work boxes." and "Students do all calculation and reasoning in their lab notebooks." The rule's record is the 2026-09-08 decision-log entry "Physics decisions file created" (SHULL-CHG-0012, which moved it from `shull-physics-guidelines` §8). Its origin is Matt's words in `governance/proposals/SHULL-CHG-0019-worksheet-template.md`: "all problem sets are done in the notebooks, so we do not need room for problems to solve." The worksheet builder enforces it: `templates/worksheet/build_worksheet_docx.py` refuses with "no work areas at all". That refusal is exercised by `scripts/validate_profiles.py` cases "physics refuses a work box" and "physics refuses ruled answers". |
| **Proposed Rule** | A new decision-log entry goes at the top of the Physics decision log (draft below). For the **Physics U4 unit reading only** (`Unit 4 Reading - Work & Energy` and its `Unit 4 Reading Key - Work & Energy`), each On Your Own box gets open space to work in, like the Chemistry readings. The tear-off leaf keeps its handwriting space on the front and its ruled vocabulary write-in lines on the reverse. `workflows/unit-textbook.md` steps 4–5 require these for every unit reading in all three courses, whatever this exception says. The Worksheets rule text is **not edited**. It stays in force for practice sets, homework worksheets, study guides, and pre-lab and post-lab prompts. It also stays in force for any other Physics reading unless that reading gets its own record. |
| **Supersedes** | Nothing is replaced. This is a scoped exception to `courses/physics/DECISIONS.md` "Worksheets" (the no-work-area rule), for one document. The rule text is unchanged. |
| **Reason** | Matt chose work space for this reading's On Your Own boxes, and he gave the Chemistry readings as the model. A unit reading is a different document class from the three classes the rule names (A-17). Without a record, a later Auditor or builder could read the rule as covering the reading and strip the space out, or could cite this reading as permission to put work boxes on a Physics worksheet. Writing the exception down, scoped and marked as no precedent, blocks both mistakes. |
| **Affected Agents** | Textbook Page Designer (builds the boxes), Auditor (checks the reading against this exception rather than the Worksheets rule), Overseer (intake). Secretary (implementation only, and only on approval). |
| **Affected Skills** | None. `.claude/skills/build-document/SKILL.md` l.98 says "Physics carries no work areas at all". That sits in its worksheet guidance and is not edited. Note: that line restates the course rule more broadly than DECISIONS does. Under CLAUDE.md §2 the decisions file wins. This is reported here and not changed by this record. |
| **Affected Courses** | Physics only, and only the U4 unit reading. |
| **Risk** | Low. (1) **No validator changes.** Confirmed: `scripts/validate_profiles.py` builds only `templates/worksheet/build_worksheet_docx.py` (l.17 `BUILD`), using worksheet specs from `templates/worksheet/specs/`. It never invokes `templates/reading/build_reading_docx.py`. The reading builder has no Physics no-work-area check. (2) **No builder change.** `build_reading_docx.py` `on_your_own()` (l.703–715) already reserves open work space in every course (`workIn`, default 1.3 in). The docstring reads "open space to work in". So the Chemistry-style box is the builder's default. (3) **The scope is the risk.** If the entry is read as a precedent, it weakens the worksheet rule. The draft says "not a precedent" explicitly. (4) No Physics reading spec exists yet in `templates/reading/specs/`, so nothing already built is affected. |
| **Recommendation** | Approve, as Matt chose it. Declining would mean "No space, 'use notebook'", the other option he was offered. |
| **Decision** | 2026-11-26, user, in the main session, answering "Your Physics rule says no work areas on student pages (students work in notebooks). How should the On Your Own boxes look?" (option text: "Give each On Your Own box room to work, like the Chemistry readings."): "Add work space". |
| **Status** | **APPROVED** |
| **Implemented By** | pending commit |
| **Verified** | — |

---

## What changes, exactly

| File | Change | Protected? |
|---|---|---|
| `courses/physics/DECISIONS.md` "Decision log" | New entry at the top, above "2026-11-26 — U4 short title" (draft below) | Yes, Secretary only |

Not changed: the "Worksheets" section text, `scripts/validate_profiles.py`,
`templates/worksheet/build_worksheet_docx.py`, `templates/reading/build_reading_docx.py`,
`workflows/unit-textbook.md`, `.claude/skills/build-document/SKILL.md`, and every other file.

## Draft decision-log entry (for the top of the Physics log)

The quoted words are the ones in the Decision field once the main session records it. The implementer
copies them from there, verbatim.

```markdown
### 2026-11-26 — Scoped exception: work space in the U4 reading's On Your Own boxes
In the U4 unit reading, each On Your Own box gets open space to work in, like the Chemistry
readings. Matt was asked "Your Physics rule says no work areas on student pages (students work in
notebooks). How should the On Your Own boxes look?" and chose "Add work space" ("Give each On Your
Own box room to work, like the Chemistry readings."). The tear-off leaf keeps its handwriting space
and ruled vocabulary write-in lines, which `workflows/unit-textbook.md` requires for every unit
reading whatever this entry says.

**Scope, stated plainly:**
1. Scoped to the U4 unit reading only: `Unit 4 Reading - Work & Energy` and its
   `Unit 4 Reading Key - Work & Energy`.
2. **Not a precedent.** The Worksheets rule above stays in force everywhere else: practice sets,
   homework worksheets, study guides, pre-lab and post-lab prompts. Another Physics reading
   needing work space needs its own explicit request and its own record. It may not cite this one.
3. No validator or builder changes. `scripts/validate_profiles.py` exercises only the worksheet
   builder, and the reading builder's On Your Own box already reserves work space.

Supersedes: None. A scoped exception to the Worksheets rule, whose text is unchanged.
Status: CONFIRMED · SHULL-CHG-0122 — Path A (course-specific; no standard, skill, builder or validator touched).
```

## Verification plan (for a checker other than the implementer, after approval)

1. `git diff` of the implementing commit touches only `courses/physics/DECISIONS.md` (the one entry
   above), plus this record's `Implemented By`/`Verified` and its `change-log/CHANGELOG.md` row.
2. The "Worksheets — CONFIRMED" section text is byte-identical before and after.
3. `python3 scripts/validate_profiles.py` still passes, including "physics refuses a work box" and
   "physics refuses ruled answers".
4. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
5. Fill in `Implemented By` with the commit SHA and `Verified` with the results.
