---
id: SHULL-CHG-0026
title: Upload built files with gws into an Upload Inbox, then file them with the connector
status: IMPLEMENTED
opened: 2026-10-15
source: User
decided: 2026-10-15
decided_by: Matthew Shull
---

# SHULL-CHG-0026 — Upload Inbox

## What he asked for

"I keep having to manually upload my files to drive." The Drive connector's `create_file` takes
content inline, so a built `.pptx`, `.docx` or PDF is too large for it (`librarian.md` §What you
cannot do).

## Current Rule

`.claude/agents/librarian.md` and `.claude/skills/shelve-drive-file/SKILL.md`: from Claude Code a
built binary cannot be filed. The file is handed back for the user to upload.

## Proposed Rule

1. Build the file and verify it, as now.
2. Upload it from disk with the Google Workspace CLI into the `SHULL Science / Upload Inbox`
   folder (ID `1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy`, in `config/drive.json` once approved).
3. Reparent it into its Course / Unit / Section / content folder with the connector's
   `update_file`. This keeps the file ID.
4. Rename it to the `standards/NAMING.md` grammar (SHULL-CHG-0024) in the same call.
5. Log before moving. Verify the destination after.

The CLI runs with the `drive.file` scope only. It can see, change and trash only files it
created. It cannot see the library and cannot permanently delete anything there. Nothing about
trashing changes: it still needs the user's approval (`scripts/hook-drive-guard.sh`).

## Supersedes

`librarian.md` §What you cannot do, the Claude Project filing workaround.
`shelve-drive-file` step 6 for built binaries.

## Setup already in place

Startup script installs `gws` and writes the login from the environment variable
`GWS_CREDENTIALS_B64`. Verified 2026-10-15: scopes are `drive.file` plus sign-in only; a test
upload landed in the Inbox and was read back.

## Risk

low to medium. The login token sits in an environment variable that the settings page says is
visible to anyone using the environment. It is limited to files the tool creates. Revoke at
myaccount.google.com/permissions. The OAuth client secret appeared in a screenshot on
2026-10-15 and should be replaced (not done yet).

## Recommendation

Approve, then update `config/drive.json`, the librarian agent and the shelve skill.

Decision: Approved by Matthew Shull, 2026-10-15.
Status: IMPLEMENTED
Implemented By: 9a32369
Verified: 2026-10-15. Narrow scope confirmed (drive.file only); test upload landed in the Inbox and was read back; Inbox moved into SHULL Science by update_file with ID kept; validators clean. Full file-and-rename run on a real deliverable not yet done.
