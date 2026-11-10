# SHULL-CHG-0064 — Four APPROVED records have not reached IMPLEMENTED

> **Aging, repeat-style.** Each item is a finding about an already-APPROVED record. This is not a
> request to re-approve any of them. No conflict with a LOCKED rule (none known). This record changes
> no existing record's status.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0064 |
| **Date** | 2026-11-08 |
| **Source** | Janitor finding, weekly sweep 2026-11-08 |
| **Current Rule** | Each record below, as approved. |
| **Proposed Rule** | For each: finish and verify, then mark IMPLEMENTED; or Matt defers. |
| **Supersedes** | Nothing. |
| **Reason** | "APPROVED is not IMPLEMENTED" (`governance/CHANGE_CONTROL.md` section 2). These have aged. |
| **Affected Agents** | Secretary (finish or backfill), Auditor (section 5 verification), Designer (CHG-0038 checks). |
| **Affected Skills** | None. |
| **Affected Courses** | None directly. |
| **Risk** | Low. |
| **Recommendation** | Run the follow-ups in the table. |
| **Decision** | Approved by the user via the Secretary's Desk, 2026-11-08T22:43:17.128Z. Still open — Questions for Matt, not answered by the click: (1) Finish CHG-0034 and CHG-0038, or defer? (2) For CHG-0035, drop the unpassable Tests-Quizizz check? |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is deferred: no Drive access this run. CHG-0035 item (a) needs Drive.

---

## 1. The four records

| Record | APPROVED since | State found | Next step |
|---|---|---|---|
| SHULL-CHG-0034 | 2026-09-23 | `overseer.md` row 3 not done: no verbatim-quoting rule in `.claude/agents/*.md`. `change-log/CHANGELOG.md` line 96: PARTIAL. | Secretary adds the missing rule from the record's text, or Matt defers. |
| SHULL-CHG-0038 | 2026-09-23 | Implemented By blank; Verified "No"; CHANGELOG line 95: PARTIAL. | Run the section 7 checks against `templates/notes/`; backfill. |
| SHULL-CHG-0039 | 2026-09-28 | Implemented By blank. Code appears shipped: the self-check handling in `templates/worksheet/build_worksheet_docx.py`; CHG-0045 and CHG-0055 built on it; the 2026-09-24 audit describes work boxes. Status is likely stale. | Auditor runs section 5 verification; backfill the commit ID. |
| SHULL-CHG-0035 | 2026-10-15 | PARTIAL (CHANGELOG line 73). Item (b), README "five content folders", is now fixed: grep finds none, so "Not done (b)" is stale. Item (a), per-unit folder IDs in `config/drive.json`, needs Drive. The Tests-Quizizz check cannot pass as written, because of the CHG-0030 supersession history. | Correct the stale note; do (a) with Drive; amend the check wording. |

## 2. What this does not do

- It does not change the status of any of the four records.
- It does not implement anything. The Secretary acts only against a committed APPROVED record.
