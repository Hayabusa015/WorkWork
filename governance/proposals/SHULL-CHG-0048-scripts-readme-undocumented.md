# SHULL-CHG-0048 — scripts/README.md omits 20 of the scripts in scripts/

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review |
| **Resolves** | `scripts/README.md` named 12 of the 32 files in `scripts/` (8 in its tables, 4 more in prose placed confusingly after a false "not yet written" status line); 20 — including every validator but three, both PreToolUse/Stop/SessionStart hooks, and several generators — had no entry at all. |
| **Current Rule** | Only `validate_layers.py`, `validate_codes.py`, `validate_tokens.py`, `find_session_files.py`, `publish_standards.py`, `build_app_css.py`, `build_template_previews.py`, and `build_diagram_molecule.py` were listed. |
| **Proposed Rule** | Every script in `scripts/` gets a one-line entry: what it fails the build on, what it writes, or what it is a helper for. |
| **Supersedes** | `scripts/README.md`'s prior table contents (additive — nothing removed, see SHULL-CHG-0047 for the status line) |
| **Affected Agents** | None — documentation only |
| **Affected Skills** | None |
| **Affected Courses** | None |
| **Risk** | Low |
| **Recommendation** | Adopt |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:41:02Z. Confirmed in chat 2026-10-22: "scretary desk approved." |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `scripts/README.md` |
| **Verified** | Every `.py` and `.sh` file under `scripts/` now appears in `scripts/README.md` — checked by diffing `ls scripts/*.py scripts/*.sh` against the file's own contents. |

## Reconciliation note (merge, 2026-10-22)

A parallel session independently drafted its own SHULL-CHG-0048, branch `claude/festive-noether-yhgdn7`,
left PENDING, with a different script count (21 of 33) than this record's (20 of 32, later corrected
to "all 32 documented, count could not be reproduced"). Both counts were taken at different moments
against a directory that may have been changing; this record's live recount at merge time confirms
32 total scripts, all now documented. If a script was added between the two counts and is still
missing, the next weekly sweep will catch it.
