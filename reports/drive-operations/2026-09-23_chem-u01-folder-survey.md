# Drive survey: CHEM U01 folder reorganisation, plus Physics and Geology samples

**Logged:** 2026-09-23 · **Agent:** Librarian · **Mode:** READ-ONLY. Nothing on Drive was created, moved,
renamed or trashed. The only repo write is this file.
**Purpose:** give the Secretary verified facts for a proposal that adds the user's unit-level folders
(created 2026-09-16) to `standards/DRIVE_ARCHITECTURE.md`, `standards/NAMING.md` and `config/drive.json`.

**Method:** every folder below was found by an independent `parentId` search, walking down from the
`SHULL Science` root (`1FsFiaYfkwgSLnA62bpIHt2zGosFwcPec`, found by title search). IDs logged in
earlier operation logs were checked with `get_file_metadata`. None of these facts come from config or
old logs alone. All times are UTC.

---

## 1. Headline findings

| # | Finding | Evidence |
|---|---|---|
| F1 | The user added three **unit-level** folders, `Presentations`, `Guided Notes` and `Quiz`, on 2026-09-16. The same pattern appears in **all three courses**. | §2 and §4 |
| F2 | The section folders are no longer five-folder folders. Every section sampled holds **only `Labs-Case Studies-Projects`**, or no subfolders at all. `Homework`, `Presentations`, `Guided Notes` and `Tests-Quizizz` are gone from the section level. | §2 and §4 |
| F3 | No folder titled `Tests-Quizizz` exists anywhere in Drive search. The only `homework` folders are legacy ones outside `SHULL Science/`. | Drive-wide title search |
| F4 | `Unit PPT` and `New folder` (logged 2026-09-15) and every section-level content folder the Librarian created on 2026-09-08, 09-14 and 09-15 no longer resolve. `get_file_metadata` returns "not found". **From this connector I cannot tell whether they were trashed or permanently deleted.** The user can check Drive Trash. | §3 |
| F5 | `SHULL_CHEM_Slides_U01_S01.4.pptx` is now in **unit-level** `Presentations`, not in `Section 01.4/Presentations` where it was routed on 2026-09-08. So the user files section decks at unit level. | §2 |
| F6 | Geology's multi-section notes (`GEO_U1_S1.2-S1.4_…`) sit in Geology **U01 `Guided Notes`**. So the user files multi-section notes at unit level. | §4 |
| F7 | Physics U01 section folders hold practice sets and a lab **loose in the section root**, with no `Homework` or `Labs` subfolder. That is not the same as Chemistry and Geology, where sections have a `Labs-Case Studies-Projects` subfolder. | §4 |
| F8 | `config/drive.json` is stale on unit counts as well. Physics has **11** unit folders (config says 1). Geology has **10** (config says 0). All were created 2026-09-16. | §5 |
| F9 | NAMING has no grammar for unit-scope or multi-section files. Every filename must carry `S##.#`, but a unit quiz or a unit deck has no single section. The files already filed at unit level use four different ad-hoc forms. | §6 |

---

## 2. Chemistry, Unit 01: full listing to two levels, with Labs contents counted

`SHULL Science` → `Chemistry` (`1dA5kKA9vQxaWX0CZMhXIoBMYGfDhMxH6`) →
`Unit 01 - Matter & Atomic Structure` (`1vYISUV443AAVTmODSnUIwxSUgxCc5i8b`, created 2026-09-05)

### Level 1: children of Unit 01 (8)

| Name | Folder ID | Parent ID | Created | Contents |
|---|---|---|---|---|
| `Presentations` | `1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-16 15:51:46 | 2 files |
| `Guided Notes` | `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-16 15:51:45 | empty |
| `Quiz` | `1cwiX68GJE4OGxsI_wC8IGE-g8Ejz2sO7` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-16 15:51:47 | empty |
| `Section 01.1 - Matter & Changes` | `1XS4PboqJFcbDmtQWdArK7H54KFGlA0_s` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-14 15:28:55 | 1 folder |
| `Section 01.2 - History of the Atomic Model` | `15FUjBMNe9elG0Cod5eNqUTSn9d1cEDWe` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-15 15:20:10 | 1 folder, 1 loose file |
| `Section 01.3 - Atomic Structure` | `1t_3db6VNrkCYuP73LgQx-sWEVHvz7GIK` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-15 15:20:10 | 1 folder, 1 loose file |
| `Section 01.4 - Isotopes` | `1WU_Mx3hYEDdNR8ADffg_bI16kPZ0GQDK` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-08 14:54:50 | **empty** |
| `Section 01.5 - Average Atomic Mass` | `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | 2026-09-15 15:20:11 | 1 folder |

### Level 2

| Parent | Child | ID | Type | Created | Contents / size |
|---|---|---|---|---|---|
| Presentations | `Unit 1 - Matter and Atomic Theory Notes.pptx` | `1_U_6sqdSUQbAW3RA8C2x8I9uvqm_XEpi` | pptx | 2026-09-15 14:55 (before the folder existed, so it was moved in) | 110,117 B |
| Presentations | `SHULL_CHEM_Slides_U01_S01.4.pptx` | `1eSuicKHiQ7TzPj-7-Nwa64Vs8fIqj-AQ` | pptx | 2026-09-08 15:14 | 591,361 B (the un-repacked build, not the 109 KB repack) |
| Section 01.1 | `Labs-Case Studies-Projects` | `12jktWfOEEUPTqvDAdFCAB9B9XY0jOfNl` | folder | 2026-09-14 15:29:03 | 2 files: `SHULL_CHEM_Lab_U01_S01.1_Chromatography.pdf`, `…_Key.pdf` |
| Section 01.2 | `Labs-Case Studies-Projects` | `1EMp9Vi12n39sLv-r2WV_tM7R73Rrdwp5` | folder | 2026-09-15 15:20:19 | empty |
| Section 01.2 | `SHULL_CHEM_Atomic_Theory_Jigsaw_Original_Drawings.pdf` | `1R-O3_d3mBp1K0HgSE-z5KSWyQqWmLE3b` | pdf, loose | 2026-09-18 12:05 | 819,472 B |
| Section 01.3 | `Labs-Case Studies-Projects` | `1IE9wqFT8iXkFkY3Py2OAe-o4brVFlqjS` | folder | 2026-09-15 15:20:23 | 1 file: `SHULL_CHEM_Element_Builder_Designed.docx` (`1HJhPRu1eGBTmqGzku71GBJcXMCvsViYh`) |
| Section 01.3 | `SHULL_CHEM_Element_Builder_Designed.docx` | `1Q051gCAbpbqrTWhi8FL_WnpLwK9KUiRT` | docx, loose | 2026-09-22 17:00 | 64,941 B. **Duplicate** of the file in Labs (same size, same modified time) |
| Section 01.4 | none | | | | |
| Section 01.5 | `Labs-Case Studies-Projects` | `1QV9m7jqso5CKhkZNWDW8TjAcquLGv14n` | folder | 2026-09-15 15:20:28 | empty |

---

## 3. Classification against the current rules

### Described by the architecture today

| Folder | Status |
|---|---|
| `Unit 01 - Matter & Atomic Structure` | Matches unit grammar |
| `Section 01.1` through `Section 01.5` | Match section grammar and `courses/chemistry/DECISIONS.md` titles |
| `Labs-Case Studies-Projects` in each section | One of the five content folders. It is now the **only** one present |

### New: not in the rules

| Folder | ID | Note |
|---|---|---|
| Unit-level `Presentations` | `1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx` | The name is a legal content-folder name, but at the **wrong level** under the current tree |
| Unit-level `Guided Notes` | `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | Same as above |
| Unit-level `Quiz` | `1cwiX68GJE4OGxsI_wC8IGE-g8Ejz2sO7` | **Not one of the five names at all.** Appears to replace `Tests-Quizizz`. Current §2 rule 2 ("never create `Tests` beside `Tests-Quizizz`") has no referent now |

### Rules, config and log entries that no longer resolve

| Item | Where it is referenced | ID | Result |
|---|---|---|---|
| `Unit PPT` | 2026-09-15 log | `1htdFwk1O71Z4WBUmPIeRG0Mit_pVUGp3` | not found |
| `New folder` | 2026-09-15 log | `1CagpVXjDdxIje-bGHHqYy5Dnw2Rt_o67` | not found |
| S01.4 `Presentations` | 2026-09-08 log, including its "drag it in" link | `1bK07FKOdrW3JUw5-2jre5zm1VZ1itJU-` | not found. **The filing link in that log is dead** |
| S01.1 `Homework` | 2026-09-14 log | `1NphcrpeHSmBNIVUkYU9vvWCOyH9o8AjL` | not found |
| S01.1 `Presentations` | 2026-09-14 log | `1pOywcnz66gxAZ2Mr9SMldX9226U9u6wp` | not found |
| S01.1 `Guided Notes` | 2026-09-14 log | `1LwWvGHxrYA_YYGNon9x3a_fbYUwdniMT` | not found |
| S01.1 `Tests-Quizizz` | 2026-09-14 log | `1EHD67dKmv9DBuF8M4kXqVZH40H3OxliJ` | not found |
| S01.2, S01.3, S01.5 `Homework`, `Presentations`, `Guided Notes`, `Tests-Quizizz` (12 IDs) | 2026-09-15 log | see that log | Absent from each section's `parentId` listing. I did not check them individually by metadata |
| PHYS S01.1 `Homework` | 2026-09-14 PHYS log | `1CVfke4Axe8jGk9b6pm7WmzPvLKwug78u` | Absent from the S01.1 `parentId` listing. The S01.1 section has no subfolders |
| Five-folder section rule | `DRIVE_ARCHITECTURE.md` §1 tree, Grammar bullet "exactly those five", §1 "What goes where" | none | Contradicted by the live structure in all three courses |
| `folderGrammar.contentFolders` and `contentFolderRule` | `config/drive.json` | none | Same as above |
| "Never create `Tests` beside `Tests-Quizizz`" | `DRIVE_ARCHITECTURE.md` §2, `.claude/agents/librarian.md:24`, `.claude/skills/shelve-drive-file/SKILL.md:22` | none | `Tests-Quizizz` no longer exists |
| "Structure locked by SHULL-CHG-0005" | `DRIVE_ARCHITECTURE.md` header, `config/drive.json` `$comment` | none | The user has restructured. The proposal has to supersede CHG-0005's tree explicitly |

---

## 4. Physics and Geology samples

Four units sampled, plus Chemistry U00 and U02 for comparison.

| Course / unit | Unit-level folders (ID, created) | Section-level pattern |
|---|---|---|
| CHEM U00 `1QknMfGJdISiBVIINQm724R6_X7EtxfuT` | Presentations `1sfhd0zfsQGxQ6ktYM79rxReqVLqYIU8-` (09-16 15:51) · Guided Notes `1o_oF3Xqu-oMsPfdNeb8yyoJZCOw7icRl` (09-16 15:51) · Quiz `1bx_3T_eruQ-LeQnhC8RP3SOGV4DzxuX-` (09-16 15:51). All empty. There is also the bare `Labs` folder `1otXTZSKkPAwasC4uX8NyjhpT3-eBFaNk`, empty, which is a known defect | `Section 00.4` has `Labs-Case Studies-Projects` only (`199f-dW2ZxIk99mqmK96HGQGbVHWWqTf6`) |
| CHEM U02 `1caxbGbuk4m-18ERTvk5Le_NNsMLmQ3Xp` | **none**. The unit folder is empty | none |
| PHYS U01 `1_ykbQae1GAKi0hWFn-OWIdvVAWXwc_6D` | Presentations `1a2yvOkD19Heypn4RdXrZMBykvhgSJ_JT` (09-16 15:33), 1 file: `Physics Unit 1 - Motion in 1D Pres.pptx`, 7.6 MB · Guided Notes `1Kof55nqkDQo6rMoy5JYagNxNXl-FsRt7` (09-16 15:33), empty · Quiz `1aYZtAI2rKprtJIFOjJMKDnTOBteAjqVI` (09-16 15:33), 7 files: `SHULL_PHYS_Quiz_U01_Fall2026_{A,B,C} - Copy.docx`, `…_{A,B,C}_Key - Copy.docx`, `…_GradeSheet.pdf` | S01.1 has 11 loose files and no subfolders. S01.2 has 4 loose files and no subfolders. S01.3 has 4 loose files plus `Labs-Case Studies-Projects` (`1MFa1jLRkYaQPrGoXeHpkdnPFfnlOUuAm`, created 09-16 18:16). S01.4 has 5 loose files including `SHULL_PHYS_Lab_U01_S01.4_Reaction_Time.pdf`, with no Labs folder |
| PHYS U02 `1rB4t-tF-PygDHIFFQBleIpHV4GHJYBve` | Presentations `193RS23zSyfdOJF3s7b9Yd9xzmpV6dPFv` (09-16 14:38) · Guided Notes `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` (09-16 14:38) · Quiz `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW` (09-16 15:47) | `Section 02.1` has `Labs-Case Studies-Projects` only (`10aGiNXh8Y--NBzGzXcruAdglgJIaw3ck`) |
| GEO U01 `1vdta_fO_QPLqzwt7rD76VyKZOGZOnXI_` | Presentations `1RIpXtC2JvyVvFI4rHbNF_hHvhFVWL_2f` (09-16 14:36), 1 file: `Formation of the Universe and Solar System.pptx`, 21 MB · Guided Notes `13or8vDciecTyueJRQ7xKQ6TllyAkr7hC` (09-16 14:36), 1 file: `GEO_U1_S1.2-S1.4_Guided_Cornell_Notes.docx` (`1o9tibpojTp76ZGf0ltcljXSRE2JitQU9`) · Quiz `1NUPLYgUeRNgt6NL9cUL_6r02YpJ54jAF` (09-16 15:47), empty | `Section 01.1` has `Labs-Case Studies-Projects` only (`1KGS9wtbINi5LlzAkmob1CKeej1THK9f8`) |
| GEO U04 `1xnMcAw0yAOqDWAMuTm9A8b915XGwvHM8` | Presentations `1IoDRLvp3_V1gJaziZNbzJDdc4T4n1pD5` (09-16 14:36) · Guided Notes `1wJEc8Nj-KZdzAOcbqSWY3yOWIvqdwd3O` (09-16 14:36) · Quiz `1QHXv5XFcchSDD4oRaumMi4f6oQNBH8Xr` (09-16 15:47) | `Section 04.1` has `Labs-Case Studies-Projects` only (`1CupEoLfy7DHoTskPNlke99HnxXRlaob6`) |

**Conclusion.** The unit-level `Presentations / Guided Notes / Quiz` pattern is **cross-course**. Under
the CLAUDE.md §2 test, that makes it a standard, not a course decision. It is **not yet universal**:
CHEM U02 has no unit-level folders, and I did not sample CHEM U03 to U15, PHYS U03 to U10, or GEO
U02, U03 and U05 to U10.

---

## 5. `config/drive.json` corrections needed

| Key | Current | Live |
|---|---|---|
| `courses.physics.unitFolders` / `state` | `1`, "only Unit 01 exists" | **11** folders, Unit 00 to Unit 10. Unit 00 to 10 except 01 were created 2026-09-16 14:37 |
| `courses.geology.unitFolders` / `state` | `0`, "empty" | **10** folders, Unit 01 to Unit 10, created 2026-09-16 14:21 |
| `folderGrammar.contentFolders` | five section-level folders | see §7 routing |
| `knownDefects[0]` (GEO notes in `_Brand/Templates/`) | open | **Still open.** `1fo8LhjpYfcxep-Dvb4grtz3QzuOmIKc4` (16,689 B) is still in Templates. A **second, separate upload** (`1o9tibpojTp76ZGf0ltcljXSRE2JitQU9`, 16,477 B, created 09-16) is in GEO U01 Guided Notes. That is not a move. Two copies now exist |
| `knownDefects[3]` (CHEM U00 bare `Labs/`) | open | Still present and empty |

---

## 6. File-level issues seen during the survey (not actioned)

| File | Issue | Recommended action |
|---|---|---|
| `Unit 1 - Matter and Atomic Theory Notes.pptx` (`1_U_6sqdSUQbAW3RA8C2x8I9uvqm_XEpi`) | Off-grammar name. Unclear whether it duplicates the S01.4 deck | Ask the user. Rename only after the unit-scope grammar exists |
| `SHULL_CHEM_Element_Builder_Designed.docx`, 2 copies (`1Q051g…` in S01.3 root, `1HJhPR…` in S01.3 Labs) | Duplicate. Name has no `U##_S##.#` or valid Type | Trash one, with user approval. Rename to grammar |
| `SHULL_CHEM_Atomic_Theory_Jigsaw_Original_Drawings.pdf` (`1R-O3_…`) | Loose in the S01.2 root. No U/S code | Route once "Activity" has a home (§7 Q3) |
| `SHULL_CHEM_Slides_U01_S01.4.pptx` (`1eSuic…`) | The 591 KB un-repacked build is filed, not the 109 KB repack | Informational only |
| PHYS S01.1 root: `SHULL_PHYS_Practice_Set_U01_S01.2.pdf`, `…_Key.pdf` and both `- Copy` twins | **S01.2 files misfiled in S01.1** | Reparent to `Section 01.2` (`1syvqWt83E0ReKfLvVqF34FAcH2ZkG7i6`). Deterministic, but needs a pre-move log |
| PHYS S01.1 root: `SHULL_PHYS_Practice_Set_U01_S01.1 - Copy.docx` | Duplicate | Trash, with user approval |
| PHYS S01.1: `SHULL_PHYS_Practice_Set_U01_S01.1.docx` exists but has no `.pdf` | The 2026-09-14 log intended pdf+docx | Ask the user |
| PHYS U01 to U04 legacy `…_S1.x` files | Unpadded codes (CONFLICT-09 era) | Batch rename needs confirmation |
| PHYS U01 Quiz: 6 files ending ` - Copy` | Copy-suffix names. No S code | Rename after the unit-scope grammar exists |
| PHYS S01.4 `SHULL_PHYS_Lab_U01_S01.4_Reaction_Time.pdf` | Loose in the section root. No Labs folder | The user must create `Labs-Case Studies-Projects`, then reparent |
| `Physics Unit 1 - Motion in 1D Pres.pptx`, `Formation of the Universe and Solar System.pptx` | Legacy names | Rename after the unit-scope grammar exists |

---

## 7. Proposed routing rule, for the Secretary

Items marked **CONFIRM** are inferred from what the user did but not stated by him. Each needs one
answer from him before the Secretary treats it as LOCKED. Until then they are PROVISIONAL.

### Proposed tree

```
[Course]/
└── Unit ## - Unit Name/
    ├── Presentations/                 unit level
    ├── Guided Notes/                  unit level
    ├── Quiz/                          unit level
    └── Section ##.# - Section Name/
        └── Labs-Case Studies-Projects/    created on demand
        (homework files: see Q1)
```

### Routing table

| Document type (NAMING Type) | Scope | Destination | Basis |
|---|---|---|---|
| `Slides`, one section | S##.# | `Unit ##/Presentations/` | Observed: the user moved the S01.4 deck here |
| `Slides`, multi-section or whole unit | S01.1–S01.5 | `Unit ##/Presentations/` | Observed in CHEM, PHYS and GEO |
| `Guided_Notes`, student copy + teacher key, one section | S##.# | `Unit ##/Guided Notes/` | Inferred from the folder's existence. No section-level Guided Notes remains |
| `Guided_Notes`, multi-section | e.g. S1.2–S1.4 | `Unit ##/Guided Notes/` | Observed: the GEO U01 notes are filed here |
| `Quiz`, A–D versions, `_Key`, grade sheet | unit | `Unit ##/Quiz/` | Observed: PHYS U01 quiz set |
| `Quiz`, one section; exit ticket; bell ringer; Quizizz | S##.# | `Unit ##/Quiz/` | **CONFIRM (Q2)** |
| `Test`, unit test, A–D versions, keys, S01.1–S01.5 | unit | `Unit ##/Quiz/` | **CONFIRM (Q2).** No `Test` folder exists and `Tests-Quizizz` is gone |
| `Study_Guide` / unit review | unit | **No folder exists.** Candidates: `Unit ##/Quiz/`, or a new unit-level folder the user would create | **CONFIRM (Q4)** |
| `Practice_Set`, homework, worksheet, `_Key`, one section | S##.# | `Section ##.#/` root, or a `Section ##.#/Homework/` the user recreates | **CONFIRM (Q1).** PHYS shows loose files. No `Homework` folder exists anywhere |
| `Practice_Set`, multi-section | S01.1–S01.3 | **No rule.** Not safe to guess | **CONFIRM (Q5)** |
| `Lab`, case study, project, `Rubric` | S##.# | `Section ##.#/Labs-Case Studies-Projects/` | Observed in CHEM, PHYS S01.3, GEO and PHYS U02 |
| `Activity` (jigsaw, element builder) | S##.# | `Section ##.#/Labs-Case Studies-Projects/` or the section root | **CONFIRM (Q3).** CHEM S01.3 has one copy in each |
| `Reference`, `Organizer` | any | not observed | **CONFIRM** |

### Questions the user must answer (one line each)

| # | Question |
|---|---|
| Q1 | Section homework and practice sets: loose in the section folder, or in a section `Homework/` folder that you recreate? |
| Q2 | Does `Quiz/` hold **everything** `Tests-Quizizz` held (section quizzes, unit tests, exit tickets, bell ringers, Quizizz)? |
| Q3 | Activities such as the jigsaw and the element builder: in `Labs-Case Studies-Projects/`, or loose in the section? |
| Q4 | Unit review / study guide: in `Quiz/`, or in a folder you would create? Name it if so |
| Q5 | Homework that spans several sections: which folder? |
| Q6 | Should every unit in all three courses get the three unit-level folders? CHEM U02 has none today |

### Naming gap (a separate NAMING.md change)

NAMING §2 requires `S##.#` on every file. Unit-scope files have no legal name today. The live forms
disagree: `SHULL_PHYS_Quiz_U01_Fall2026_A`, `GEO_U1_S1.2-S1.4_…`, `Unit 1 - Matter and Atomic Theory
Notes`, `Physics Unit 1 - Motion in 1D Pres`. The Secretary needs a user decision on a grammar such as
`SHULL_[COURSE]_[Type]_U##[_Descriptor][_Version]` for whole-unit files and `…_U##_S##.#-S##.#` for
ranges. **This is an option to put to the user, not a decided rule.** I have not checked whether
`scripts/validate_codes.py` accepts a filename with no section code.

### New IDs for `config/drive.json` (verified 2026-09-23)

| Course / unit | Presentations | Guided Notes | Quiz |
|---|---|---|---|
| CHEM U00 | `1sfhd0zfsQGxQ6ktYM79rxReqVLqYIU8-` | `1o_oF3Xqu-oMsPfdNeb8yyoJZCOw7icRl` | `1bx_3T_eruQ-LeQnhC8RP3SOGV4DzxuX-` |
| CHEM U01 | `1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx` | `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | `1cwiX68GJE4OGxsI_wC8IGE-g8Ejz2sO7` |
| PHYS U01 | `1a2yvOkD19Heypn4RdXrZMBykvhgSJ_JT` | `1Kof55nqkDQo6rMoy5JYagNxNXl-FsRt7` | `1aYZtAI2rKprtJIFOjJMKDnTOBteAjqVI` |
| PHYS U02 | `193RS23zSyfdOJF3s7b9Yd9xzmpV6dPFv` | `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` | `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW` |
| GEO U01 | `1RIpXtC2JvyVvFI4rHbNF_hHvhFVWL_2f` | `13or8vDciecTyueJRQ7xKQ6TllyAkr7hC` | `1NUPLYgUeRNgt6NL9cUL_6r02YpJ54jAF` |
| GEO U04 | `1IoDRLvp3_V1gJaziZNbzJDdc4T4n1pD5` | `1wJEc8Nj-KZdzAOcbqSWY3yOWIvqdwd3O` | `1QHXv5XFcchSDD4oRaumMi4f6oQNBH8Xr` |

CHEM U01 section and Labs IDs for config: S01.1 `1XS4PboqJFcbDmtQWdArK7H54KFGlA0_s` / Labs
`12jktWfOEEUPTqvDAdFCAB9B9XY0jOfNl` · S01.2 `15FUjBMNe9elG0Cod5eNqUTSn9d1cEDWe` / Labs
`1EMp9Vi12n39sLv-r2WV_tM7R73Rrdwp5` · S01.3 `1t_3db6VNrkCYuP73LgQx-sWEVHvz7GIK` / Labs
`1IE9wqFT8iXkFkY3Py2OAe-o4brVFlqjS` · S01.4 `1WU_Mx3hYEDdNR8ADffg_bI16kPZ0GQDK` / no Labs ·
S01.5 `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` / Labs `1QV9m7jqso5CKhkZNWDW8TjAcquLGv14n`.

The other units were not surveyed, so their unit-level IDs are not verified. A full walk is needed
before config lists them.

### Other files the Secretary proposal must touch

`.claude/agents/librarian.md` line 24 and `.claude/skills/shelve-drive-file/SKILL.md` line 22 both cite
`Tests-Quizizz`. Once the rule changes, both are stale.
