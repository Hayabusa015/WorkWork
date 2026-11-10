# Geology Unit 2 Study Guide filing, 2026-11-10

Approval (relayed by the Overseer): Matt in chat 2026-11-10, "file it to drive"; earlier, "Replace it"
for the old study guide (trash recoverably only after the new one is filed). No row for this
document exists in `reports/filing-queue.md`; the Overseer should add/mark it.

Procedure: SHULL-CHG-0026 (gws upload to Upload Inbox, then `update_file` reparent, ID kept).
Format: the set per `standards/DRIVE_ARCHITECTURE.md` §8.4 — student file, separate key, print PDF,
same folder. Native `.docx` and `.pdf`, **no Google Docs conversion**. Names from
`templates/_shull_name.py`, not changed.
gws auth: `drive.file` only (plus identity scopes), token valid.

## Destination (verified by lookup before upload)

| Level | Name | ID | Parent |
|---|---|---|---|
| Unit | Unit 02 - Geologic Time | 1yB-RasB1BOXgMmsKK77v6v2cKC9qu-_C | 1lqHHql9cSqOZDGej2ff_121bITWOKZvr (Geology) |

Routing: unit study guide, loose in Unit (DRIVE_ARCHITECTURE §1 "What goes where", last row).
Existing direct children before filing: folders only (Homework, Quiz, Presentations, Guided Notes,
Section 02.1 to 02.5). No file with any of the four names below. No collision.

## Intended operations (new objects)

Each file: (1) gws create in Upload Inbox (1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy), no conversion;
(2) `update_file` parentId 1yB-RasB1BOXgMmsKK77v6v2cKC9qu-_C, title = same final name;
(3) verify by `parentId` search. Prior name: none (new object). Prior parent: Upload Inbox.

| # | Local file (scratchpad out/u2sg11/) | Final name | Object ID | Status |
|---|---|---|---|---|
| 1 | Unit 2 Study Guide - Geologic Time.docx | same | (pending) | pending |
| 2 | Unit 2 Study Guide - Geologic Time.pdf | same | (pending) | pending |
| 3 | Unit 2 Study Guide Key - Geologic Time.docx | same | (pending) | pending |
| 4 | Unit 2 Study Guide Key - Geologic Time.pdf | same | (pending) | pending |

Rollback: `update_file` parentId back to the Upload Inbox, or trash with user approval.

## Intended trash (only after all four verified)

| Object ID | Prior name | Prior parent | Intended change |
|---|---|---|---|
| 1L2ZBoLoYvSI47R28YlFYAmEPPimzGdLN | Unit 2 Study Guide - Geologic Time Student Guide.pdf | 1W9L10dhOpAt4IPg0zhHQiQPl59cIy9DI (Unit 02 / Homework) | Move to trash (recoverable). Never permanent delete. |

Confirmed by metadata lookup 2026-11-10: application/pdf, 43135 bytes, owner mshull, created
2026-09-17 (not by gws), not trashed.

## Results

(pending)
