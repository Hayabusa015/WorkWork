# Drive operation log — PHYS U02 guided notes (student copy + teacher key)

**Logged:** 2026-10-14 · **Task:** file the Physics Unit 2 guided notes, as asked by Matt
**Status:** logged before execution, per `standards/DRIVE_ARCHITECTURE.md` and `shelve-drive-file`.

## Intended operations

| # | Operation | Destination | Prior state |
|---|---|---|---|
| 1 | upload `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3.docx` (student copy) | `Physics/Unit 02 - Motion in Two Dimensions/Guided Notes/` — `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` | folder exists, empty |
| 2 | upload `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3_Key.docx` (teacher key) | same folder | folder exists, empty |

No folders created, nothing renamed, moved, overwritten or trashed. The unit-level `Guided Notes`
folder is used because the packet spans S2.1–S2.3; the matching decks already sit in the unit-level
`Presentations` folder (`Physics Unit 2 - Quantum Gold.pptx`).

`create_file` takes content inline only, so each file is passed as base64 with
`disableConversionToGoogleType: true` (kept as .docx, not converted to a Google Doc). The files were
stripped of `stylesWithEffects.xml` and the thumbnail first; the rendered text and page count were
confirmed identical to the unstripped build.

## Result — NOT executed

| # | Operation | Status |
|---|---|---|
| 1 | upload student copy | **FAILED, nothing created** — `create_file` rejected the inline base64 ("not a valid base64 string") |
| 2 | upload teacher key | **not attempted** |

Same connector limit recorded in `2026-09-08_chem-u01-s01.4-slides.md`: `create_file` takes content
inline only, so a binary has to be re-emitted by the model character for character. At ~35,000
characters per file that is not reliable, and a file that passed validation could still be
silently corrupt. No retry was made. Drive was not modified: no folder created, no file written.

Destination stays resolved and verified for whoever files it:
`Physics/Unit 02 - Motion in Two Dimensions/Guided Notes/` — `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN`
(empty at 2026-10-14). Files: `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3.docx` and `..._Key.docx`.

## Retry 2026-10-15 via the Google Workspace credential — NOT executed

`GWS_CREDENTIALS_B64` (OAuth user credential for mshull@jagschools.org) refreshes a token, but its
only Drive scope is `drive.file`: it sees just the files this app created. The destination folder
`1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` returns 404, and searches for `SHULL`, `Physics` and `Guided Notes`
return nothing. Uploading into that folder would fail, and creating a new folder tree at the Drive
root would split the library, so nothing was created. Read-only calls only; no file was uploaded, moved
or changed. The `gws` binary itself is not installed in this container.
Fix: re-authorise the credential with the full `https://www.googleapis.com/auth/drive` scope.

## Plan 2026-10-15 — upload via Upload Inbox, then move and rename (logged BEFORE execution)

Credential scope stays `drive.file` (user instruction). Two-step route:

| # | Operation | Tool | From → To |
|---|---|---|---|
| 1 | upload `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3.docx` and `..._Key.docx` | Drive API, `drive.file` token | local → Upload Inbox `1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy` (inside SHULL Science) |
| 2 | move each to `Physics/Unit 02 - Motion in Two Dimensions/Guided Notes/` (`1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN`) | Drive connector `update_file` (parentId) | Upload Inbox → Guided Notes |
| 3 | rename per `standards/NAMING.md` on origin/main (SHULL-CHG-0024, unit-level because the packet covers S2.1–S2.3) | `update_file` (title) | see below |

Prior names (the upload names, i.e. the prior state for rollback):
`SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3.docx` → `Unit 2 Guided Notes - Motion in Two Dimensions.docx`
`SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3_Key.docx` → `Unit 2 Guided Notes Key - Motion in Two Dimensions.docx`
Topic "Motion in Two Dimensions" is the U2 title in `courses/physics/DECISIONS.md`. Object IDs and the
verified parent lookups are recorded below after execution.

## Result 2026-10-15 — executed and verified

| # | Object ID | Prior name / prior parent | Final name | Final parent |
|---|---|---|---|---|
| 1 | `1qd57XMECFshy4k71jgsk71dmvMw3bfcn` | `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3.docx` / Upload Inbox `1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy` | `Unit 2 Guided Notes - Motion in Two Dimensions.docx` | Guided Notes `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` |
| 2 | `1J9HMsmkMuyRVZa--odOKnlMDoiEsPua9` | `SHULL_PHYS_Guided_Notes_U02_S02.1-S02.3_Key.docx` / Upload Inbox | `Unit 2 Guided Notes Key - Motion in Two Dimensions.docx` | Guided Notes |

Upload: Drive API with the `drive.file` token (scope unchanged), checksum matched the local files
(43,189 and 46,188 bytes). Move and rename: connector `update_file`, one call per file, IDs preserved.
Verified afterwards by independent lookups: `parentId = Guided Notes` lists exactly these two files;
`parentId = Upload Inbox` is empty; Guided Notes' own parent is `Unit 02 - Motion in Two Dimensions`
(`1rB4t-tF-PygDHIFFQBleIpHV4GHJYBve`). Nothing overwritten, trashed or deleted.
