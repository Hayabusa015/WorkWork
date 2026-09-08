---
name: shelve-drive-file
description: File a finished deliverable into the correct Google Drive location, create missing folders, and verify the destination. Use whenever work is ready to be stored, or when correcting a misfiled document. Every operation is logged before it happens.
---

# shelve-drive-file

Tree, routing rules, and authority: `standards/DRIVE_ARCHITECTURE.md`. IDs: `config/drive.json`.

## The rule that defines this skill

> **Never claim a file has been shelved until you have verified the destination.**

Verification is an independent `parentId` lookup confirming the object is where you say it is. Not
the create call returning success. Not your intention. A confirmed lookup, after the fact.

## Procedure

1. **Resolve Course → Unit → Section → content type *before* saving.** Not after.
2. **Check the name** with `naming`. Fix it before filing, not after.
3. **Look for existing folders** and reuse them exactly, matching case-insensitively.
   **Never create `Tests` beside `Tests-Quizizz`.**
4. **If the unit or section is unclear, ask.** Never default to a misc folder.
5. **Log the intended operation** to `reports/drive-operations/` — object ID, prior name, prior
   parent, intended change.
6. Create or upload.
7. **Verify by independent lookup.** Report the confirmed path and ID.

## Creating folders

`create_file` with the folder mimeType. Follow the grammar exactly — zero-padded unit, hyphen
separator, **never an en dash**. An en dash creates a near-duplicate folder that sorts beside the
real one and splits the unit in half.

Section subfolders are created on demand, when first needed.

## Saving markdown

`disableConversionToGoogleType: true` with `contentMimeType: text/plain`, or Drive silently converts
it into a Google Doc and the file stops being diffable.

## Authority

| | |
|---|---|
| Create, upload | Yes, in authorised teaching locations |
| Rename | Deterministic only — **log the prior name first** |
| **Move** | **BLOCKED pending test T-3.** Reparenting is unverified; copy-and-trash changes the file ID and breaks every link. **Propose moves; do not execute them.** |
| Overwrite | Explicit workflow authorisation |
| Trash | **User approval.** Recoverable. |
| Permanent delete | **Not possible.** No tool exists. |

## Never

- Copy a template into a course folder. Course decks reference `_Brand/Templates/`.
- Duplicate an image used by two courses — it moves to `Image Library/Shared/`.
- Batch-rename without confirmation.
