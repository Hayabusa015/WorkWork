# SHULL-CHG-0081 — Three PENDING records over a month old are moot

> Matt decides each one. This record changes no existing record's status. A REJECTED or withdrawn
> record is kept, not deleted (CHANGE_CONTROL §3).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0081 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` rows 14-16) |
| **Current Rule** | Each record below, Status: PENDING (confirmed 2026-11-22). |
| **Proposed Rule** | For each: Matt rejects it, defers it, or marks it superseded with the superseding commit or record named. The main session records the decision in the record's `Decision:` and `Status:` fields. |
| **Supersedes** | Nothing. |
| **Reason** | Each has been PENDING for 58–65 days, and the problem each describes has since been fixed or overtaken. Moot PENDING records hide live ones on the desk. |
| **Affected Agents** | Main session (records the decision). |
| **Affected Skills** | None. |
| **Affected Courses** | Physics (third row only). |
| **Risk** | Low. |
| **Recommendation** | Close all three. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

| Record | PENDING since | Why moot |
|---|---|---|
| `SHULL-CHG-0023-status-docs-stale-and-undocumented-app.md` | 2026-09-18 | Fixed by d50ca37 (2026-09-24) and `SHULL-CHG-0046-phase-13-status-stale.md`. |
| `SHULL-CHG-0024-validate-tokens-app-exclusion.md` | 2026-09-18 | `app/public/` now uses the generated `tokens.generated.css`, which is in `validate_tokens.py`'s `GENERATED` set (confirmed). |
| `SHULL-CHG-0024-physics-u1-vectors-section.md` | 2026-09-25 | 658d658 dropped the separate U1 section; vectors moved into U2 2.1/2.2. `courses/physics/DECISIONS.md` has no `1.0`. |

## Open question

1. Is "superseded" an acceptable outcome for a record that was never approved, or should these be
   REJECTED? CHANGE_CONTROL §3 has no SUPERSEDED or WITHDRAWN status for records; CHANGELOG has
   SUPERSEDED. Matt's choice of term decides what the main session writes.
