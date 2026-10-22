# SHULL-CHG-0046 — Phase 13 status stale in three places (4th occurrence of this defect class)

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review |
| **Resolves** | `CLAUDE.md`, `README.md`, and `docs/SHULLOS_IMPLEMENTATION_PLAN.md` all still claimed Phase 13 had not started, though it was activated 2026-09-24 (the Secretary's Desk dashboard and its weekly Routine). Repeat of SHULL-CHG-0024, which raised the same finding on 2026-09-27 but was never committed to `main` — see SHULL-CHG-0052. |
| **Current Rule** | `CLAUDE.md:6` said "Phase 13 not started (deliberately)"; `docs/SHULLOS_IMPLEMENTATION_PLAN.md:1139` carried an unchecked `⬜ Phase 13` with no "Actual" note. |
| **Proposed Rule** | Both files say Phase 13 is active, dated, and point at `workflows/weekly-system-review.md` for the mechanism. |
| **Supersedes** | `CLAUDE.md:6`; `docs/SHULLOS_IMPLEMENTATION_PLAN.md:1139-1142` |
| **Affected Agents** | None — documentation only |
| **Affected Skills** | None |
| **Affected Courses** | None |
| **Risk** | Low |
| **Recommendation** | Adopt |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:41:05Z. Confirmed in chat 2026-10-22: "scretary desk approved." |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `CLAUDE.md`, `docs/SHULLOS_IMPLEMENTATION_PLAN.md` |
| **Verified** | `CLAUDE.md:6` now reads "Phases 8–13 complete"; the implementation plan's Phase 13 section is checked `✅` with an "Actual" note citing the 2026-09-24 activation. |

## Why this kept recurring

The real defect was never the wording — it's that the fact "is Phase 13 active" lived in at least
three files (`CLAUDE.md`, `README.md`, `docs/SHULLOS_IMPLEMENTATION_PLAN.md`) and a fourth, the
weekly-review workflow doc itself, and only the workflow doc got updated on 2026-09-24. Three
separate sweeps (SHULL-CHG-0024, this record, and the governance proposals that preceded both) found
the same staleness because nobody closed the loop on all four copies at once. `README.md` was
already fixed to point at `CLAUDE.md` instead of restating the fact (see its own commit history);
this record does the same for the implementation plan by adding a dated "Actual" note rather than a
second independent status line.
