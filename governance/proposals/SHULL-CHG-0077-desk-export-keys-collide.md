# SHULL-CHG-0077 — Secretary's Desk export keys collide on duplicate Change IDs

Repeat of: SHULL-CHG-0052 (class: dashboard and repository out of step because of duplicate IDs)

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0077 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 7) |
| **Current Rule** | `scripts/desk_export.py` line 70 (the Janitor cites 69): `cid = f.name[:14]`. Each desk document's `id` is the bare Change ID. |
| **Proposed Rule** | Key desk documents on the filename stem (for example `SHULL-CHG-0068-physics-u3-six-sections`), keep `seq` as the integer, then re-sync the desk. |
| **Supersedes** | `scripts/desk_export.py` document keying, in part. |
| **Reason** | There are 78 record files in `governance/proposals/` but only 63 unique Change IDs (counted 2026-11-22). The 15 colliding records overwrite one another on the desk. For example, `SHULL-CHG-0068-print-document-format-fixes.md` (PENDING) and `SHULL-CHG-0068-physics-u3-six-sections.md` (APPROVED) share one slot, so Matt sees only one of them. A desk click could land on the wrong record. CHANGE_CONTROL §4 safeguard 2 (compare the title) catches this only if the main session checks. |
| **Affected Agents** | Secretary, main session (desk sync and click recording). |
| **Affected Skills** | weekly-system-review (surfaces proposals on the desk). |
| **Affected Courses** | None. |
| **Risk** | High. Approvals could attach to the wrong record. |
| **Recommendation** | Adopt. Any desk click on a colliding ID should be held until the re-sync. |
| **Decision** | Approved by the user in chat, 2026-11-23: "Do all 4", answering the main session's proposal to approve SHULL-CHG-0077 and SHULL-CHG-0078 and then (1) give each hidden record its own desk card, (2) fix the export for the old record format, (3) add a rule against duplicate numbers, (4) re-sync the desk. |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Changing the key changes every desk document's id. Do existing click rows in the `decisions`
   collection key on the bare Change ID? If so, the click-recording path in CHANGE_CONTROL §4 needs a
   matching change, which would be a governance edit needing its own approval.
