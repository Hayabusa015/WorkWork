# SHULL-CHG-0091 — SHULL-CHG-0062 was decided but not carried through; a fourth ramp override followed

Repeat of: SHULL-CHG-0062 (REPEAT x4 of the Physics ramp correction)

> SHULL-CHG-0062 is APPROVED: Matt answered "Yes, make it the rule" on 2026-11-08. This record does
> not re-ask that. It asks one question that blocks implementation, and proposes that the skill point
> at DECISIONS. It changes no existing record's status.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0091 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 3) |
| **Current Rule** | `templates/worksheet/build_worksheet_docx.py` line 70: `"physics": {"warm-up": 2, "practice": 2, "challenge": 1, "multi-topic": 1}`. `.claude/skills/build-document/SKILL.md` lines 70-72: "Physics holds his shipped shape exactly: **2 warm-up / 2 practice / 1 challenge / 1 multi-topic**, six per section." |
| **Proposed Rule** | Implement SHULL-CHG-0062 in this order: (1) a dated entry in `courses/physics/DECISIONS.md` with the Physics default ramp and "no tier label on Physics student pages"; (2) the builder default and tier-label rendering follow it; (3) the skill points at `courses/physics/DECISIONS.md` for the Physics ramp instead of stating counts (CLAUDE.md §1). |
| **Supersedes** | `.claude/skills/build-document/SKILL.md` lines 70-72, in part. `build_worksheet_docx.py` `RAMP["physics"]`. The 2/2/1/1 ramp (SHULL-CHG-0019), as already decided on SHULL-CHG-0062. |
| **Reason** | 0062 has Implemented By blank. DECISIONS has no entry, the builder still holds 2/2/1/1, and so does the skill. Three days later the FBD set became the fourth one-off override: `templates/worksheet/specs/build_phys_u03_fbd_problem_set_1.py` line 15 sets `{"warm-up": 3, "practice": 4, "challenge": 4, "multi-topic": 1}`. SHULL-CHG-0071 Part B still cites 2/2/1/1 as the current rule. The skill restating counts is the duplication that will go stale the moment 0062 lands. |
| **Affected Agents** | Secretary (DECISIONS entry, skill), Builder (builder default), Designer. |
| **Affected Skills** | build-document. |
| **Affected Courses** | Physics. |
| **Risk** | Medium. Changes how every new Physics worksheet builds. Filed worksheets are unaffected (no-retrofit). |
| **Recommendation** | Ask the question below, then implement under SHULL-CHG-0062 plus this record. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. What are the exact default Physics counts per tier? 0062 says "about 9-10" in total. The overrides
   so far are 4/3/1/1 (S1.1), 3/3/3/1 (S1.2) and 3/4/4/1 (U3 FBD set).
