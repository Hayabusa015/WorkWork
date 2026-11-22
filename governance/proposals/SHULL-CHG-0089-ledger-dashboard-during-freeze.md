# SHULL-CHG-0089 — Ledger dashboard exporter was added during the dashboard freeze

> May be sanctioned; no record says so. Not resolved here. Matt confirms or not.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0089 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 27) |
| **Current Rule** | `docs/PLAN_2026-11-13_consolidate-and-ship.md` §9: "**Freeze:** until this phase is done, no new agents, skills, standards, dashboards or app features. Bug fixes that block a build are allowed." `reports/README.md` line 3: "Output from the Researcher, Janitor, and Auditor. Findings only — no agent applies its own findings." |
| **Proposed Rule** | Matt either confirms `scripts/branch_ledger.py` as an exception to the freeze (recorded here) or it is paused. Separately, move the hand-written input `reports/branch-ledger-notes.json` to `config/` and update the pointer in `scripts/README.md` line 20. |
| **Supersedes** | Nothing. |
| **Reason** | b51f0e0 (2026-11-13 16:04) added a "WorkWork Ledger dashboard" exporter after the freeze was declared the same day. `reports/branch-ledger-notes.json` is hand-written input data, but `reports/` is defined as findings output. |
| **Affected Agents** | Main session (records the exception), Secretary (file move, once approved). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Record an exception if Matt wants the ledger, since it reads git for the ID-collision work in SHULL-CHG-0078. Move the notes file either way. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Was the Ledger dashboard sanctioned as part of the consolidation work, and therefore inside the
   freeze's "bug fixes that block a build" allowance, or is it a new dashboard?
