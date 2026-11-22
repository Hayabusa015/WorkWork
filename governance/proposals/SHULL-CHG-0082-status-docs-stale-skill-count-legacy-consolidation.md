# SHULL-CHG-0082 — Status docs are stale: skill count, legacy retirement, Phase 13 line, current plan

Repeat of: SHULL-CHG-0046 (`SHULL-CHG-0046-phase-13-status-stale.md`) and
SHULL-CHG-0023-status-docs-stale-and-undocumented-app (status drift, 5th occurrence)

> No conflict with a LOCKED rule (none known). **Part B cannot be implemented on this record alone.**
> The legacy-retirement answer exists only as a quote in `docs/PLAN_2026-11-13_consolidate-and-ship.md`
> §10. It is not recorded on a change record. Under CHANGE_CONTROL §4, the main session must record
> Matt's decision verbatim on SHULL-CHG-0065 (or Matt confirms it again) before the Secretary edits
> CLAUDE.md.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0082 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` rows 17-20) |
| **Current Rule** | A: `CLAUDE.md` Status block: "all seven agents (`.claude/agents/`), and all twelve skills (`.claude/skills/`) exist". `README.md` line 34: "`.claude/skills/` \| All twelve skills and their enforcement hooks". `README.md` line 6: "**Status: see `CLAUDE.md`.** The phase and skill/agent existence facts live there, not here." B: `CLAUDE.md` Status block: "Legacy skill retirement is the last step of Phase 14 and is deliberately withheld until the system has been exercised on real work". C: `docs/SHULLOS_IMPLEMENTATION_PLAN.md` line 1031: "**Status as of 2026-09-08: Phases 1–12 complete. Phases 13–14 not started.**"; line 1150: "**Not started, deliberately.**" D: `CLAUDE.md` Status block: "Full record: `docs/SHULLOS_IMPLEMENTATION_PLAN.md`, Phase 10–14." |
| **Proposed Rule** | A: CLAUDE.md says fourteen skills, or points at `.claude/skills/README.md` instead of giving a count. README line 34 drops the count and points at `.claude/skills/README.md`. B: after Matt's decision is recorded on SHULL-CHG-0065, CLAUDE.md states the recorded decision and points at PLAN §11 for the uninstall list. C: both plan lines are edited to match the ✅ Phase 13 and 🟡 Phase 14 markers in the same section. D: one pointer line to `docs/PLAN_2026-11-13_consolidate-and-ship.md` (pointer, not restatement). |
| **Supersedes** | `CLAUDE.md` Status block, in part. `README.md` line 34. `docs/SHULLOS_IMPLEMENTATION_PLAN.md` lines 1031 and 1150. |
| **Reason** | A: 14 skill directories exist (confirmed by glob 2026-11-22; `humanize` and `reconcile-session-files` added 2026-10-15). README repeats a count it says lives only in CLAUDE.md, which is a CLAUDE.md §1 duplication. B: Matt answered "Legacy skills, retire them" on 2026-11-13 (PLAN §10 row 3), but SHULL-CHG-0065 still says "Q2 (legacy retirement) still open", and PLAN §11 step 1 is not done. C: SHULL-CHG-0046 fixed the heading and left these two lines. D: the 2026-11-13 consolidation and its freeze are not mentioned in the Status block. |
| **Affected Agents** | Secretary (edits), main session (records part B decision on SHULL-CHG-0065). |
| **Affected Skills** | None (the legacy installed skills are outside the repo). |
| **Affected Courses** | None. |
| **Risk** | Medium. The status block is the first thing every session reads. Part B tells agents legacy skills are still the working system. |
| **Recommendation** | Adopt A, C and D. For B, record the decision on SHULL-CHG-0065 first. Prefer pointers over counts in A so this does not drift a sixth time. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Part B: does Matt confirm "Legacy skills, retire them" (2026-11-13) as his decision on
   SHULL-CHG-0065 Q2? Only the main session can record it, quoting him verbatim.
