# Drive survey: Physics Unit 04 (read-only)

**Date:** 2026-11-26 · **Agent:** Librarian · **Skill:** retrieve-drive-file
**Scope:** READ-ONLY. Nothing was created, moved, renamed or trashed. No mutation, so no rollback
entry is needed.
**Purpose:** Groundwork for the Physics U4 unit reading (`workflows/unit-textbook.md`).

## 1. Unit folder, verified by parentId lookup

Query: `parentId = '1NOjl2nEZ1bjcjm32G55V265uGUoTErlk'` (Physics, from `config/drive.json`).

| Field | Value |
|---|---|
| Name (live) | `Unit 04 - Work, Energy & Power` |
| ID | `1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE` |
| Parent | `1NOjl2nEZ1bjcjm32G55V265uGUoTErlk` (Physics), confirmed |
| Created | 2026-09-16 |
| Matches `courses/physics/DECISIONS.md` | Yes. "U4 · Work, Energy & Power", 4 sections (4.1 to 4.4). Hyphen-minus separator, no en dash |

Physics course root, other direct children: Unit 00 to Unit 10 (11 unit folders) and `Snow Day`
(`141OLqJPb-Q0ITxhIXiM0t5E03P7WSQNU`). No `Reference` folder in Physics.

## 2. Unit 04 direct children (`parentId = '1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE'`)

| Name | Type | ID | Children |
|---|---|---|---|
| Guided Notes | folder | `1BwOV44D9vchmIawAqn_zKjerCcegL10b` | empty |
| Presentations | folder | `1a2Ev4ixVHuElg-JqfoJtplk6zbOz4nZ_` | empty |
| Quiz | folder | `1Nj69K4SK6cR0s57uwIW3CzKxPlarDssU` | empty |
| Section 04.1 - Work & Power | folder | `1wpbhd3W9qJOrccHPvo9ONeG3gEPP1Vtz` | see §3 |
| Section 04.2 - Kinetic Energy & Work-Energy Theorem | folder | `1rMlfWOZUthDz6axNcmmpWyz3-GJsPdwt` | see §3 |
| Section 04.3 - Potential Energy | folder | `12uHrpqK7j4d674zGB9uCnbquwXaxFepm` | see §3 |
| Section 04.4 - Conservation of Energy | folder | `1SFXAvD-hqPPM3MnY0Lu_hiNJ1g2NwnJO` | see §3 |

No loose files in the unit folder. No `Test`, `Worksheets` or `Presentations + Guided Notes` folder.

## 3. Section folders and their children

| Section | Section ID | Direct children | Labs folder contents |
|---|---|---|---|
| 04.1 - Work & Power | `1wpbhd3W9qJOrccHPvo9ONeG3gEPP1Vtz` | `Labs-Case Studies-Projects` `1g03UzIBQCYZ1NVZL0_AYpiTzF0AodCuw` | empty |
| 04.2 - Kinetic Energy & Work-Energy Theorem | `1rMlfWOZUthDz6axNcmmpWyz3-GJsPdwt` | `Labs-Case Studies-Projects` `1GH2ImzIqgss1EFjjG-7MLIowKanHzDmw` | empty |
| 04.3 - Potential Energy | `12uHrpqK7j4d674zGB9uCnbquwXaxFepm` | `Labs-Case Studies-Projects` `17IWAPJhz5rWskGn4YzQVpiTId0yAryTC` | empty |
| 04.4 - Conservation of Energy | `1SFXAvD-hqPPM3MnY0Lu_hiNJ1g2NwnJO` | `Labs-Case Studies-Projects` `1NfvwXLED8g5RZmVBgpi-NhTEifrcl-HT` | empty |

Cross-check: an `ancestors` search on the unit returned the same 11 folders and **no files**
anywhere inside Unit 04.

## 4. Section-level Homework / Tests-Quizizz folders (2026-09-16 retrofit log)

`2026-09-16d_geo-phys-retrofit-shull-chg-0024.md` lists eight Physics U04 folders as confirmed empty,
"for trash, not yet trashed". None is present now.

| Section | Logged Homework ID | Logged Tests-Quizizz ID | Live state 2026-11-26 |
|---|---|---|---|
| 04.1 | `1e6VXsEEvA_Fe8hsmjvE5pyO0KFAVjXss` | `1JNd6JtOTQ9HpldBBc559IP9Z2W5J9bb0` | Both absent from the section listing; `get_file_metadata` returns "not found" |
| 04.2 | `1950OW8AS8l790yIR71Zdw6bChChB3CZ_` | `1w0W-2NSM1oTw5_c_V3rTRbOm9YJkC8oJ` | Same |
| 04.3 | `1TIpETW6HOp8GSZpLFJZeF-nN9QbMgLG-` | `17krE821AorWF_GQ8zza9SpKh3YyKlPwJ` | Same |
| 04.4 | `1dm7WonHvX1tNuWrkz_VDv6J4l_GGDXvH` | `14QFknqP4Kof4lLBA7y3LFAm4llvT3NqN` | Same |

A `trashed = true` search on the unit and section parents also returned nothing. The folders are gone
from the live Drive, probably trashed and then purged by the user. This survey found no log of their
trashing, and does not claim one exists. They do not affect the layout test.

(The same log's lines 162-166 list a second U04 table with five sections, 04.1 to 04.5. That is the
**Geology** U04 table: Geology Unit 04 - Plate Tectonics. It is not Physics.)

## 5. Existing U4 teaching files

| Location | Result |
|---|---|
| Inside `Unit 04 - Work, Energy & Power` (all depths) | **None.** No deck, notes, lab, quiz or test |
| Elsewhere under `SHULL Science` (title search: U04 / U4_ / S04 / Energy) | No Physics U4 file. Hits were PHYS U01, GEO U1 and image-library PNGs only |
| Outside the library (legacy/pre-migration Drive) | Older U4-topic material exists, none of it SHULL-built. Notable items: `Work - Energy - Power (Updated).pptx` `1FIpPVuz54krA_KqOZbY9CSHv814IAshF` (2023-01-09), `Work, Energy and Power.pptx` `1jrtDob2QB4hDxNp5Dts9X8rdfxdpLA8L` (2023-01-06), `kinetic Energy Theorm.pptx` `1ydbUCNMRcW8-R-_RywwVSIhEGh_L5PFv`, `Mechanical Energy.pptx` `1dRKO7gko3ceJV3lG2KCI32VvPxELQwoJ`, all in folder `Chapter 5` `1LOldNh4QfGrKVoXCFNg-5-XnONnEYufk`; `Work power and Energy Test A.docx` `1YboNeiumHlvWQUo6Qw-6rd_nonMGZguL` and `Test B.docx` `1FS4FWaFnTNWa-l2CCDtuVrAoNYSh2WBe` (2026-03-11); `Unit V Mechanical Energy Notes.pdf` `1Xyn2WsXiSoMzn_PY6UFHFj64UAaUyFNf` (+ Filled In `11wCvJkbmL1JbjTq6qK-7cBvveKYas7TY`); `Work and Energy.docx` `1JfzB9Y5QYIER8ikJyCwu813MBTHbfR87`; `Work and Energy Review.docx` `1XFqMt6LGJQUie5r0Q58aH0EBMZQqXKMh` |

**No SHULL U4 deck exists, so no deck extract was written.** The legacy decks are pre-system, outside
the library, and not authoritative for notation or section order. They are listed only as possible
source material if the user wants them used.

## 6. Layout test (`standards/DRIVE_ARCHITECTURE.md` §1 Grammar)

| Step | Check | Result |
|---|---|---|
| 1 | Unit does not exist yet | No. It exists |
| 2 | Direct child `Test`, `Worksheets` or `Presentations + Guided Notes` | No |
| 3 | Direct child `Guided Notes`, `Presentations`, `Tests-Quizizz` or `Homework`, or a section child `Tests-Quizizz` / `Homework` | **Yes.** `Guided Notes` (`1BwOV44D9vchmIawAqn_zKjerCcegL10b`) and `Presentations` (`1a2Ev4ixVHuElg-JqfoJtplk6zbOz4nZ_`) |

**Resolves at step 3: LEGACY layout.** Not a mixed unit, because step 2 did not match.

**Step-5 stop:** none. The unit holds no files, so no file has an unreadable type. (For the record,
step 4 would not match either: there are no files.)

## 7. Where a unit-level Reading would be filed

`Reading` is always unit-level (`standards/NAMING.md`, SHULL-CHG-0114). The legacy-layout table has
no Reading folder, so it falls under "unit-scope files with no matching folder" and is filed **loose
in the unit folder**. No folder is created.

| Item | Value |
|---|---|
| Destination | `SHULL Science / Physics / Unit 04 - Work, Energy & Power` |
| Parent ID | `1EmZU9RfEl0pIj6Y6sXwCnurOO0iKFgGE` |
| Student file name | `Unit 4 Reading - Work, Energy & Power.[ext]` |
| Key file name | `Unit 4 Reading Key - Work, Energy & Power.[ext]` |
| Precedent | Same route as the Chemistry U07 and U06 readings (`2026-11-25_chem-u07-reading-filing.md`, `2026-11-26_chem-u06-reading-filing.md`) |

Filing still needs an approved row in `reports/filing-queue.md` (SHULL-CHG-0027).

## 8. Findings

| Item | Issue | Recommended action |
|---|---|---|
| Unit 04 | Empty scaffold: no teaching files at any level | None for Drive. The reading has no SHULL deck to match. Ask the user which source sets notation and section order |
| Physics U04 Homework / Tests-Quizizz (8 IDs) | Logged "for trash, not yet trashed" in 2026-09-16d; now absent and not found | Annotate the retrofit log as resolved (Secretary or user). This survey found no record of the trashing |
| Physics `Reference` folder | Absent | Only matters if a course-level Reference file is filed. Not needed for a unit Reading |
| Legacy U4 decks outside the library | Pre-system material. Not authoritative | Use as source only if the user says so |
