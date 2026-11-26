# 2026-11-26 — Physics Unit 4 Reading (Work & Energy) filing

Approval relayed by the coordinator: Matt, in the main session 2026-11-26, "File it".
Filing-queue row: Unit 4 Reading - Work & Energy (Physics), approved in chat, Status Ready (textbook
audit PASS, Round 2). Logged before any mutation.

## Pre-flight

| Check | Result |
|---|---|
| Unit code | U4 Work, Energy & Power, 4.1–4.4 (courses/physics/DECISIONS.md). Short title "Work & Energy" (DECISIONS.md, Short titles table, and the 2026-11-26 entry "U4 short title") |
| Names | `Unit 4 Reading - Work & Energy` / `Unit 4 Reading Key - Work & Energy` match standards/NAMING.md (Reading type, short title). Note: the 2026-11-26 survey §7 predicted "Work, Energy & Power". The later short-title decision supersedes it |
| Hash, student PDF | 30dd0218d2a55790ad3dd66b186f2c959330731262ff51b5d0339e24028d18c0, 466558 bytes (matches 30dd0218…) |
| Hash, key PDF | 04eb69760fd2778a5afcebf923d0d492f1013910c43d64ddde31df0a26d03848, 185013 bytes (matches 04eb6976…) |
| Hash, student DOCX | 5e48ff0438539879240805be638c8558988f33d775debc12351c2526e9523eff, 443775 bytes |
| Hash, key DOCX | 354dd2b653b6908b720112b7054533d9508918dc025d04fa817027a07b93a053, 51536 bytes |
| Unit folder | `Physics / Unit 04 - Work, Energy & Power`, 1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE. Found by a parentId listing of Physics (1NOjl2nEZ1bjcjm32G55V265uGUoTErlk): Unit 00–10 plus Snow Day. It is the only Unit 04 folder and is not trashed |
| Unit direct children | Guided Notes (1BwOV44D9vchmIawAqn_zKjerCcegL10b), Presentations (1a2Ev4ixVHuElg-JqfoJtplk6zbOz4nZ_), Quiz (1Nj69K4SK6cR0s57uwIW3CzKxPlarDssU), Section 04.1–04.4. No loose files |
| Files anywhere in the unit | None (ancestors search, non-folder, returned nothing) |
| Earlier edition | None. Title searches for "Unit 4 Reading", "Unit 04 Reading", Reading + Work, "Work & Energy" and "Reading Key" return no Physics U4 reading. Only legacy pre-system material outside the library, plus the Chem U6/U7 reading keys |
| Layout test (re-run) | Step 1 no (exists). Step 2 no (no Test, Worksheets, Presentations + Guided Notes). **Step 3 yes**: Guided Notes and Presentations are direct children. **LEGACY layout.** Not mixed. No files, so no step-5 stop |
| Destination | A Reading is unit-scope with no matching legacy folder, so it goes **loose in the unit folder** (DRIVE_ARCHITECTURE §1, legacy table, last row). No folder is created |

## Intended operations

These are new objects, so they have no prior name or prior parent. Route: Drive connector
`create_file` with a file reference (`sha256:<hex>:<path>`), `disableConversionToGoogleType: true`,
and parentId 1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE (loose in the unit). This is the same route as the
Chem U6 and U7 readings. Rollback: trash the new files, which needs user approval.

| # | Final name | contentMimeType | Bytes | New ID | Result |
|---|---|---|---|---|---|
| 1 | Unit 4 Reading - Work & Energy.docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | 443775 | 1fige9rnDc2MLI2V0eTVYzyECVxJ8Zyg8 | Filed, verified |
| 2 | Unit 4 Reading - Work & Energy.pdf | application/pdf | 466558 | 104YUMVM_a1kJdRrZuzrYENh9qUnqDoo1 | Filed, verified |
| 3 | Unit 4 Reading Key - Work & Energy.docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | 51536 | 1tGdV0dwYjqEjzskdi3NqNHHF-tax2vdk | Filed, verified |
| 4 | Unit 4 Reading Key - Work & Energy.pdf | application/pdf | 185013 | 1js95qnXg_W9Au3MP_Lz8QI6v8fTQckUI | Filed, verified |

## Result: FILED

After creation, each file was checked with its own `get_file_metadata` call, and Unit 04 was then
listed by parentId:

| ID | parentId = Unit 04 | Title exact | Size = local | mimeType (not converted) |
|---|---|---|---|---|
| 1fige9rnDc2MLI2V0eTVYzyECVxJ8Zyg8 | yes | Unit 4 Reading - Work & Energy.docx | 443775 = 443775 | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| 104YUMVM_a1kJdRrZuzrYENh9qUnqDoo1 | yes | Unit 4 Reading - Work & Energy.pdf | 466558 = 466558 | application/pdf |
| 1tGdV0dwYjqEjzskdi3NqNHHF-tax2vdk | yes | Unit 4 Reading Key - Work & Energy.docx | 51536 = 51536 | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| 1js95qnXg_W9Au3MP_Lz8QI6v8fTQckUI | yes | Unit 4 Reading Key - Work & Energy.pdf | 185013 = 185013 | application/pdf |

All four are not trashed. The connector reports canEdit, canMoveItemWithinDrive and canTrash as true
on all four.

**Unit 04 listing** (parentId 1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE): the four files above, plus Guided
Notes, Presentations, Quiz and Section 04.1–04.4. Nothing else.

Filing-queue row updated: Status Filed, path, folder ID, four file IDs, date 2026-11-26. Box not
ticked. Nothing committed.
