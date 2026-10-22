# SHULL-CHG-0046 — README.md, CLAUDE.md and the implementation plan still say Phase 13 is not started

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0046 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. The sweep's claim that this is the 4th occurrence is carried over from the desk summary and was not verified here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `README.md` lines 42-43; `CLAUDE.md` line 6 (the phrase "Phase 13 not started (deliberately)"); `docs/SHULLOS_IMPLEMENTATION_PLAN.md` lines 1139 and 1144-1145. |
| **Reason** | Claim VERIFIED as still true. Three files say Phase 13 has not started. `workflows/weekly-system-review.md` line 30 says it was activated on 2026-09-24. The same fact is written in four places and three copies are stale, which is the duplication the one rule in `CLAUDE.md` section 1 forbids. |
| **Affected Agents** | None changed. Overseer and every agent reads `CLAUDE.md` at session start, so a stale line there misleads all of them. |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low |
| **Recommendation** | Approve. Prefer the pointer wording in section 2, so the status is stated once. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`README.md` lines 42-43:

> **Not yet built:** the weekly-review Routine itself (Phase 13 — deliberately deferred until the
> system has real usage to report on).

`CLAUDE.md` line 6:

> **Status: Phases 8–12 complete; Phase 13 not started (deliberately); Phase 14's acceptance test

`docs/SHULLOS_IMPLEMENTATION_PLAN.md` line 1139 and lines 1144-1145:

> ### ⬜ Phase 13 — Weekly Researcher reporting

> **Not started, deliberately.** The Routine is scheduled only after the system has been exercised on
> real work — a weekly review of a system nobody has used yet reports on nothing.

The conflicting statement, `workflows/weekly-system-review.md` line 30:

> **Scheduled 2026-09-24 (Phase 13 activated).** A Routine fires a fresh session weekly, Sunday
> 21:56 UTC, running this workflow end to end and stopping at PENDING proposals for user sign-off.

## 2. Proposed Rule

1. `README.md` lines 42-43: replace the "Not yet built" paragraph with a pointer, for example: "The
   weekly-review Routine is active; its schedule and status are in `workflows/weekly-system-review.md`
   (section Schedule)." No date or time is restated.
2. `CLAUDE.md` line 6: replace "Phase 13 not started (deliberately)" with "Phase 13 active (see
   `workflows/weekly-system-review.md`)". Nothing else on that line changes.
3. `docs/SHULLOS_IMPLEMENTATION_PLAN.md` line 1139: change the marker from the empty box to the done
   marker used by the completed phases; lines 1144-1145: replace "Not started, deliberately ..." with
   "Activated 2026-09-24; see `workflows/weekly-system-review.md`."

Note on authority: `README.md`, `CLAUDE.md` and `docs/` are outside the four directories the Secretary
may edit (`brand/`, `standards/`, `governance/`, `courses/`). The user should say who applies items 1
to 3 when approving. The record itself is in `governance/`.

## 3. Check before implementing

Re-read all three locations. If another session has already corrected one, change only the remainder.
