# SHULL-CHG-0047 — Three READMEs still say "Status: not yet written"

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0047 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. The "REPEAT" tag in the desk summary was not verified here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | The three status lines quoted in section 1. |
| **Reason** | Claim VERIFIED as still true. All three READMEs describe files that exist and work, then end with a status line saying the README is "not yet written". Every other README in the system carries a true status line (for example `standards/README.md` line 20). A reader cannot tell whether the README or the status line is wrong. |
| **Affected Agents** | Janitor (re-raises this each week until fixed). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low |
| **Recommendation** | Approve. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`schemas/README.md` line 10:

> *Status: not yet written. Phase 8–11.*

`governance/README.md` line 18:

> *Status: not yet written. Phase 8.*

`scripts/README.md` line 31:

> *Status: not yet written. Phase 9.*

Evidence the content exists: `schemas/` holds `change-proposal.schema.json` and `task-report.schema.json`,
both listed in the README table; `governance/` holds `GOVERNANCE.md` and `CHANGE_CONTROL.md`, both listed;
`scripts/` holds the validators and generators the README describes.

## 2. Proposed Rule

Replace each line with a true status, in the style of `standards/README.md` line 20:

- `schemas/README.md` line 10: "*Status: both schemas written and validated by `scripts/validate_schemas.py`.*"
- `governance/README.md` line 18: "*Status: written (Phase 8). Recording path added by SHULL-CHG-0034.*"
- `scripts/README.md` line 31: delete the line. SHULL-CHG-0048 rewrites that file's contents; if 0048 is
  approved, this item is absorbed into it and should not be applied twice.

The wording in quotes is a draft for the user to edit. Do not claim a validator covers a file unless
it does; the Secretary checks `scripts/validate_schemas.py` before writing the schemas line.

## 3. Interaction

SHULL-CHG-0048 edits `scripts/README.md`. Approve them together or sequence them, so the two edits do
not collide.
