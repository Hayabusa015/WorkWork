# SHULL-CHG-0086 — CHANGELOG has missing rows, an off-vocabulary status, and out-of-order dates

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0086 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 24) |
| **Current Rule** | `change-log/CHANGELOG.md` line 23, Status: "`CONFIRMED` (approved and fully implemented) · `PARTIAL` (approved, implementation incomplete — the record says what is missing) · `PROPOSED` (awaiting the user) · `SUPERSEDED` (replaced; the superseding ID is named)". `governance/CHANGE_CONTROL.md` §6: "`change-log/CHANGELOG.md` is the human-readable index into it." |
| **Proposed Rule** | Add the missing rows. Map `APPROVED` to a vocabulary term, or add `APPROVED` to the vocabulary (Matt chooses). Reorder date sections newest-first. Do not edit the content of rows that have already shipped. |
| **Supersedes** | Nothing, unless Matt chooses to extend the Status vocabulary (then CHANGELOG line 23, in part). |
| **Reason** | No row for: 0023-assessment-template, 0023-status-docs, 0024-physics-u1-vectors, 0024-validate-tokens, 0031, 0037, 0040. Nine rows (0058–0065, 0066-study-guide) use `APPROVED`, which is outside the vocabulary. Date sections are out of order (11-10 above 11-12; 10-23 above 10-26), which breaks "append at the top". These look like merge artifacts from the 11-13 consolidation. |
| **Affected Agents** | Secretary, main session (writes CHANGELOG status on recording, CHANGE_CONTROL §4 item 2). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Adopt. The missing and off-vocabulary claims are as the Janitor reported them; re-check them at implementation. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

This sweep did not edit `change-log/CHANGELOG.md` and adds no rows for 0074–0089. The main session
decides whether they need rows.

## Open question

1. Records that are APPROVED but not implemented: is `PARTIAL` right, or should the vocabulary gain
   `APPROVED`? `PARTIAL` currently means "approved, implementation incomplete", which arguably
   covers "not started" too.
