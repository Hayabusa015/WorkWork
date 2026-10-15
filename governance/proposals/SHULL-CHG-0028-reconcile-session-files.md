---
id: SHULL-CHG-0028
title: reconcile-session-files skill — find session documents that are not on Drive and file them
status: IMPLEMENTED
opened: 2026-10-15
source: User
decided: 2026-10-15
decided_by: Matthew Shull
---

# SHULL-CHG-0028 — reconcile-session-files

## What he asked for

"A skill that checks the files in the session and ensures that the files created in this session
are filed in the appropriate Google Drive folder. If they are there, nothing happens. If they
aren't, they are filed in the appropriate spot, so I am not losing documents we have created."

Answer on 2026-10-15: **list them, then file after my yes.** Running the skill is not approval.

## Why not file automatically

SHULL-CHG-0027 says iteration never reaches Drive. A skill that filed everything it found would
file drafts from the middle of an iteration. So it lists and waits, and the existing approval
words apply ("file all", or name the ones to skip).

## Current Rule

`standards/DRIVE_ARCHITECTURE.md` §8 and `.claude/agents/librarian.md`. They say how and when to
file one document. Nothing checks a whole session for documents that were never filed.

## Proposed Skill

`.claude/skills/reconcile-session-files/SKILL.md`. Procedure only. Rules stay in the standard.

1. **Find** documents created in this session: `.docx`, `.pptx`, `.pdf`, `.html` and `.xlsx`
   modified after the session-start marker, under the repo working tree, the scratchpad and
   `app/data`. The session-start marker is a file `~/.shull-session-start` that the startup script
   creates (a one-line addition to `scripts/setup-environment.sh`).
   Skipped: `templates/`, `legacy/`, `node_modules/`, preview images, `*_PREVIEW.*`,
   `*_TEMPLATE*`, `.assets/`, and anything in `reports/`.
2. **Check Drive** for each file: by its current name, by its old `SHULL_` name, and by file size.
   Same name in the right folder: **already filed, nothing happens.** Same name in a different
   folder: reported as **misfiled**, not moved without a yes.
3. **Work out the destination** for the rest. The new names carry no course, so the course, unit,
   section and content type come from, in this order: a row in `reports/filing-queue.md`; the
   spec the file was built from; the user. If none gives it, ask. One question. Never guess.
4. **List** the unfiled documents as a table: file, destination, what goes with it (key, PDF),
   status. **Stop and wait.** No upload before the user says yes.
5. **On yes, file** only the approved rows, using the SHULL-CHG-0026 flow through the Librarian:
   log first, upload to the Upload Inbox, move and rename with `update_file`, verify by looking up
   the parent. Student file, key and PDF go together.
6. **Report** a table: Filed (with path and file ID), Already on Drive, Waiting on you, Could not
   file (with the reason). A file that is gone from disk and cannot be rebuilt from a spec is
   reported as lost, not skipped.

## Invoked by

The user, for example "check the session files" or "reconcile". The Overseer also runs it at the
end of a multi-document task, before reporting WORK COMPLETE.

## Affected

| Place | Change |
|---|---|
| `.claude/skills/reconcile-session-files/SKILL.md` | New |
| `.claude/skills/README.md` | One row |
| `scripts/setup-environment.sh` | Write `~/.shull-session-start` |
| `.claude/agents/overseer.md` | Run the skill before WORK COMPLETE (one line) |

## Supersedes

Nothing.

## Risk

low. It lists before it files, and the filing path is the one already approved. The main limit:
documents built by hand rather than from a spec cannot be rebuilt if the session has already
ended, so the skill is most useful run **before** the session closes.

Decision: Approved by Matthew Shull, 2026-10-15.
Status: IMPLEMENTED
Implemented By: 4878b77
Verified: 2026-10-15. Validators clean. scripts/find_session_files.py tested: finds session documents after the marker, skips templates and previews, errors cleanly with no marker. Dry run against Drive classified one sample as a different version on Drive (same name, different size) and three as not on Drive. Nothing was filed. Not yet run end to end on a real unfiled deliverable.
