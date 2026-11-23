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
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `scripts/desk_export.py`, `workflows/weekly-system-review.md` (commits 14e22b5, 7f47f8a), and the Secretary's Desk re-sync of 2026-11-23. Commit 14e22b5: each desk `proposals` document is keyed on the record filename stem; the bare ID moves to a `change_id` field; `seq` is unchanged. The export also reads the pre-template "Field:   value" record format (`SHULL-CHG-0023-status-docs-stale-and-undocumented-app.md` and `SHULL-CHG-0024-validate-tokens-app-exclusion.md` previously exported with title = bare ID and no date or summary), and a blank `Decision:` line no longer picks up the `Status:` line below it. The workflow now says one desk document per record file. Commit 7f47f8a: sync step 1 also deletes desk documents whose key no longer matches a record file, and sets `meta/sync` (the desk's "last synced" line had read 2026-10-22 / 43 records because no later sync wrote `meta/sync`). Re-sync 2026-11-23: 103 `proposals` documents written under filename keys; the 88 old bare-ID documents deleted. The 9 existing `decisions` rows (0053, 0058–0065, all `applied: true`, all on Change IDs that name only one record) were copied to filename-keyed rows carrying a `migrated_from` field; the original rows were left in place. No `applied: false` click existed, so none was held or misapplied. |
| **Verified** | 2026-11-23: field-by-field comparison of all 103 desk `proposals` documents against `python3 scripts/desk_export.py` output: 0 missing, 0 extra, 0 mismatched. |

## Open question

1. Changing the key changes every desk document's id. Do existing click rows in the `decisions`
   collection key on the bare Change ID? If so, the click-recording path in CHANGE_CONTROL §4 needs a
   matching change, which would be a governance edit needing its own approval.

   **Answered at implementation, 2026-11-23:** New desk clicks now key on the filename stem. The 9
   existing rows were copied to filename-keyed rows, as described under Implemented By.
   CHANGE_CONTROL §4 safeguard 2 (compare the title) is unchanged. This record made no edit to
   `governance/CHANGE_CONTROL.md` and needs none.
