---
name: reconcile-session-files
description: Check the documents created in this session against Google Drive and file any that are missing, after the user approves the list. Use at the end of a working session, before closing it, when the user asks "is everything filed", "check the session files" or "reconcile", and before reporting a multi-document task complete. Lists first and never files on its own.
---

# reconcile-session-files

Rules: `standards/DRIVE_ARCHITECTURE.md` §8 (when to file) and §3 (how). Naming:
`standards/NAMING.md`. Folder IDs: `config/drive.json`. This is the procedure.

> **Running this skill is not approval to file.** It lists what is missing and waits. Drafts from
> the middle of an iteration must not reach Drive.

## 1. Find the session's documents

```
python3 scripts/find_session_files.py
```

It prints JSON: every `.docx`, `.pptx`, `.pdf`, `.html` and `.xlsx` modified after the session-start
marker (`~/.shull-session-start`), under the repo, the scratchpad and `app/data`, with size and
SHA-256. It skips templates, previews, build leftovers and system folders.

- If it reports **no marker**, ask the user when the session started and pass `--since <time>`.
  Never guess a start time.
- It is read-only. A file it does not list was not created in this session, or was filed under a
  folder it skips. If the user names a file it missed, add it by path.

## 2. Check Drive for each file

Use the Drive connector, read-only (`search_files`). For each file, search by:

1. its **current name** (`title = '...'`)
2. its **old `SHULL_` name**, if the name has the old form
3. its file size, to tell a real copy from a same-named stub

Classify:

| Result | Meaning | Action |
|---|---|---|
| Same name, same size, in the right folder | **Already filed** | Nothing happens |
| Same name, in a different folder | **Misfiled** | Report it. Do not move without a yes |
| Same name, different size | **Different version on Drive** | Report both. Never overwrite |
| Not found | **Not filed** | Goes to step 3 |
| Found only in the Upload Inbox | **Waiting in the Inbox** | Needs its destination (step 3) |

## 3. Work out each destination

The new names carry no course. Take Course, Unit, Section and content type from, in this order:

1. a row in `reports/filing-queue.md`
2. the spec the file was built from (`templates/*/specs/`, `templates/slide/decks/`)
3. the user

Confirm the section code exists in that course's `courses/<course>/DECISIONS.md`. **If none of
these gives the destination, ask. One question. Never default to a misc folder.** Look up the
destination folder with `search_files` using `parentId`; if a section folder is missing, say so and
ask before creating it.

Group each student file with its **key** and its **PDF**. They are filed together.

## 4. List, then stop

Show one table, then wait for the user's answer:

| File | Destination | Goes with | Status |
|---|---|---|---|

Offer the words that count as approval: "file all", or name the rows to skip. Rows that need an
answer (destination unclear) are marked **Waiting on you** and are never filed.

## 5. File the approved rows

Only the rows the user approved. For each, follow `.claude/agents/librarian.md` §Filing a built
binary: **log first** to `reports/drive-operations/`, upload to the Upload Inbox with `gws`, then
reparent and rename with `update_file`, then **verify by an independent `parentId` lookup**.

- Confirm `gws auth status` shows only `drive.file` before the first upload.
- Never overwrite a file on Drive. A revision of a filed document is filed as `Version N`.
- If `GWS_CREDENTIALS_B64` is not set, or `gws` fails, do not pretend. Say the file is not filed.

## 6. Report

| File | Result | Drive path | File ID |
|---|---|---|---|

Results: **Filed**, **Already on Drive**, **Waiting on you**, **Could not file** (with the reason).
A file that is gone from disk and cannot be rebuilt from a spec is reported as **Lost**, never
skipped. Update the matching row in `reports/filing-queue.md` to Filed, with the path, ID and date.

## Limits

- It finds only files on this session's disk. Anything built in an earlier session is gone unless
  it was already filed or can be rebuilt from a committed spec.
- Hand-edited documents cannot be rebuilt. Run this skill **before** the session closes.
