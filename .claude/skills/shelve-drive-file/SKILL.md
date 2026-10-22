---
name: shelve-drive-file
description: File a finished deliverable into the correct Google Drive location (loose in the parent when the matching content folder is absent) and verify the destination. Use whenever work is ready to be stored, or when correcting a misfiled document. Every operation is logged before it happens.
---

# shelve-drive-file

Tree, routing rules, and authority: `standards/DRIVE_ARCHITECTURE.md`. IDs: `config/drive.json`.

## The rule that defines this skill

> **Never claim a file has been shelved until you have verified the destination.**

Verification is an independent `parentId` lookup confirming the object is where you say it is. Not
the create call returning success. Not your intention. A confirmed lookup, after the fact.

## Procedure

0. **Confirm the document was approved to file** (`standards/DRIVE_ARCHITECTURE.md` §8): the user
   said "file it" or ticked its row in `reports/filing-queue.md`. If not, stop. Iterations are not
   filed.
1. **Resolve Course → Unit → Section → content type *before* saving.** Not after.
2. **Check the name** with `naming`. Fix it before filing, not after.
3. **Look for existing folders** and reuse them exactly, matching case-insensitively. If the
   matching content folder is absent, file loose in its parent. Never create a content folder. Rules:
   `standards/DRIVE_ARCHITECTURE.md` §2.
4. **If the unit or section is unclear, ask.** Never default to a misc folder.
5. **Log the intended operation** to `reports/drive-operations/` — object ID, prior name, prior
   parent, intended change.
6. Upload. A **built binary** (`.pptx`, `.docx`, PDF) cannot go through the connector:
   upload it with `gws` into the Upload Inbox, then reparent and rename it with `update_file`. The
   procedure and the fallback are in `.claude/agents/librarian.md` §Filing a built binary.
7. **Verify by independent lookup.** Report the confirmed path and ID.

## Folders

Content folders are never created. The only folders you may create are a missing Unit or Section
folder, under `standards/DRIVE_ARCHITECTURE.md` §2 rule 3. Follow its grammar exactly — hyphen
separator, **never an en dash**, which creates a near-duplicate folder.

## Saving markdown

`disableConversionToGoogleType: true` with `contentMimeType: text/plain`, or Drive silently converts
it into a Google Doc and the file stops being diffable.

## Authority

| | |
|---|---|
| Create, upload | Files: yes, in authorised teaching locations. Folders: Unit and Section only, never a content folder. Built binaries go through the Upload Inbox (`gws`, `drive.file` only). |
| Rename | Deterministic only — **log the prior name first** |
| **Move** | **Allowed when deterministic.** `update_file` with a new `parentId` reparents in place and **keeps the file ID**. Log the prior parent first. **Never move by copy-and-trash** — that changes the ID and breaks links. |
| Overwrite | Explicit workflow authorisation |
| Trash | **User approval.** Recoverable. |
| Permanent delete | **Not possible.** No tool exists. |

## Never

- Copy a template into a course folder. Course decks reference `_Brand/Templates/`.
- Duplicate an image used by two courses — it moves to `Image Library/Shared/`.
- Batch-rename without confirmation.
