# Drive operation log — CHEM U01 filing (guided notes + S01.5 practice set)

**Logged:** 2026-09-23 · **Agent:** Librarian (sub-agent, Claude Code) · **Task:** file the CHEM U01
deliverables that passed independent QA on 2026-09-23
**Status:** **Destinations confirmed, duplicate check clean, operations logged. Upload NOT executed
for all 8 files — blocked by the Claude Code binary-transport limit, not by a Drive permission.
Nothing is filed.**

Logged before any mutation, per `standards/DRIVE_ARCHITECTURE.md` §3.

## Routing authority

- Routing is the user's direct instruction, "file these away", relayed by the main session. The
  layout is recorded in `governance/proposals/SHULL-CHG-0027-drive-unit-folders.md` (**PENDING**).
  That layout conflicts with LOCKED SHULL-CHG-0005, whose section-level five folders no longer
  exist on Drive. Precedence rule 1 (the user's direct instruction) governs this filing. The record
  itself is not approved by this log.
- The user said, verbatim, 2026-09-23: "no keep my folders the way they are, i do not need breakdown
  within each folder. its too much to click through, in the future if i need it I will add it."
  **No folders created. Nothing renamed, moved or trashed.**
- Not touched: `SHULL_CHEM_Slides_U01_S01.4.pptx` in `Unit 01 / Presentations`.

## Destination lookups (independent, 2026-09-23, starting from CHEM Unit 01)

| Step | Query | Result |
|---|---|---|
| 1 | `get_file_metadata 1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | `Unit 01 - Matter & Atomic Structure`, folder, parent `1dA5kKA9vQxaWX0CZMhXIoBMYGfDhMxH6` (Chemistry, matches `config/drive.json`) |
| 2 | `parentId = '1vYISUV443AAVTmODSnUIwxSUgxCc5i8b'` | 8 children, all folders: Section 01.1, 01.2, 01.3, 01.4, 01.5, Quiz, Presentations, Guided Notes. No loose files |
| 3 | `get_file_metadata 1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | `Guided Notes`, folder, parent = Unit 01 |
| 4 | `get_file_metadata 1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` | `Section 01.5 - Average Atomic Mass`, folder, parent = Unit 01 |
| 5 | `parentId = '1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG'` | **empty**. No same-name file |
| 6 | `parentId = '1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D'` | one child: folder `Labs-Case Studies-Projects` `1QV9m7jqso5CKhkZNWDW8TjAcquLGv14n`. No same-name file |
| 7 | Drive-wide `title contains 'SHULL_CHEM_Guided_Notes_U01' or title contains 'SHULL_CHEM_Practice_Set_U01_S01.5'` | 5 hits, **none an exact name match** to the 8 files below (see Flags) |

These IDs match SHULL-CHG-0027 §4a/§4b, but they were looked up here, not copied from it.

## Intended operations — logged before execution

All are new-object creates. There is no prior name or prior parent because no object exists yet.
Conversion is to be disabled (`.docx` stays `.docx`).

| # | Source (scratchpad) | Intended Drive name | Intended mimeType | Destination parent | Status |
|---|---|---|---|---|---|
| 1 | `chem_u01_build/SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5.docx` | same | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | Guided Notes `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | **NOT EXECUTED** |
| 2 | `chem_u01_build/SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5.pdf` | same | `application/pdf` | Guided Notes `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | **NOT EXECUTED** |
| 3 | `chem_u01_build/SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5_Key.docx` | same | docx (as above) | Guided Notes `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | **NOT EXECUTED** |
| 4 | `chem_u01_build/SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5_Key.pdf` | same | `application/pdf` | Guided Notes `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | **NOT EXECUTED** |
| 5 | `chem_u01/SHULL_CHEM_Practice_Set_U01_S01.5_AverageAtomicMass.docx` | same | docx (as above) | Section 01.5 `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` (loose) | **NOT EXECUTED** |
| 6 | `chem_u01/SHULL_CHEM_Practice_Set_U01_S01.5_AverageAtomicMass.pdf` | same | `application/pdf` | Section 01.5 `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` (loose) | **NOT EXECUTED** |
| 7 | `chem_u01/SHULL_CHEM_Practice_Set_U01_S01.5_AverageAtomicMass_Key.docx` | same | docx (as above) | Section 01.5 `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` (loose) | **NOT EXECUTED** |
| 8 | `chem_u01/SHULL_CHEM_Practice_Set_U01_S01.5_AverageAtomicMass_Key.pdf` | same | `application/pdf` | Section 01.5 `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` (loose) | **NOT EXECUTED** |

Scratchpad root: `/tmp/claude-0/-home-user-WorkWork/26f8099c-89f2-51d6-8b84-531faeb169a3/scratchpad/`.
All 8 source files were confirmed present by glob. Byte sizes were **not** measured: this agent has
no shell.

Excluded, as instructed: the `BallAndStickStations` rubric (it waits for its activity); every
`_S01.1_S01.3_S01.5` file; the unit review, Day 2 tests, the `BallAndStickStations` practice set,
and everything else in the scratchpad.

## Naming check

| File(s) | Grammar (`standards/NAMING.md` §2) | Code in `courses/chemistry/DECISIONS.md` |
|---|---|---|
| `SHULL_CHEM_Practice_Set_U01_S01.5_AverageAtomicMass[_Key]` | **Conforms.** Type `Practice_Set`, zero-padded, `_Descriptor`, `_Key` last | 1.5 Average Atomic Mass: present |
| `SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5[_Key]` | **Not in the current grammar.** The range form is defined only in **PENDING** SHULL-CHG-0029 §2a. `validate_codes.py` would match on the first code only | 1.1 through 1.5: present |

The range name is filed as instructed, and the flag stays open until SHULL-CHG-0029 is approved.

## Why the upload was not executed

`create_file` takes content only inline (`textContent` / `base64Content`). There is no path-based
upload. Built binaries do not survive that round trip intact (measured in
`2026-09-08_chem-u01-s01.4-slides.md`, where a 15 KB PNG was corrupted). This agent also has no
shell to produce the base64 at all. A corrupt file that looks filed is worse than one that is
plainly not filed.

**This is a limit of the transport between Claude Code and the connector.** It is not a Drive
permission and not a limit on Librarian authority.

## Where it gets filed from

**The Claude Project running the official Google Drive connector** hands the connector the file by
reference. The user confirmed this route from his own working setup on 2026-09-08. After filing,
the Project should verify each file by an independent `parentId` lookup: exact name, parent,
mimeType (`.docx` not converted to a Google Doc), and non-zero size.

- Guided Notes: https://drive.google.com/drive/folders/1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG
- Section 01.5 - Average Atomic Mass (loose, **not** in its Labs subfolder):
  https://drive.google.com/drive/folders/1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D

## Flags — not actioned

| Item | Issue | Recommended action |
|---|---|---|
| `SHULL_CHEM_U01_Guided_Notes_Cover_and_Review.pdf` `1encHae0mOs59snonuLG4rdCQPxWLhwIy`, in `Chapter 4 - Atomic Structure` `1zY61_LkoPe7YKARMCfl6E2B3MZAIpHW5` | Created today, outside the governed Unit 01 tree. The name does not follow the grammar | The user decides whether it belongs in `Unit 01 / Guided Notes`. A move would be a logged reparent |
| `SHULL_CHEM_U01_Guided_Notes_Cover_and_Review.pdf` `1pI-xb1s9OgODYXNVOLG_-Bp3I86jKJZD`, in folder `pdf` `13bjAwZfmIxrt0g0W1ozt8lBFfIojWpra` | Same name and same size (1,419,721 B) as the file above. Probably a duplicate | Needs a user decision. Trashing requires approval |
| `SHULL_CHEM_Guided_Notes_U01_Ink_Saver.pdf` / `_Ink_Saver_Condensed.pdf` / `_Redesigned.pdf`, in `pdf` `13bjAwZfmIxrt0g0W1ozt8lBFfIojWpra` | Other U01 guided-notes variants uploaded today, outside the Unit 01 tree. No section code | The user confirms which version is canonical next to the QA-passed files |
| Guided-notes range filename | Legal only under PENDING SHULL-CHG-0029 | Approve 0029, or rename before filing |
