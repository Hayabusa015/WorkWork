# SHULL-CHG-0027 — Drive: the system creates no folders; file into a matching folder if it exists, else loose in the parent

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0027 |
| **Date** | 2026-09-23 |
| **Source** | User, 2026-09-23, two answers, both relayed by the main session. The Secretary did not hear either directly. **(1)** Asked whether the unit-level `Presentations` / `Guided Notes` / `Quiz` folders should be added to the rules, he answered, verbatim: *"We changed them i assumed they were added to the rules, update that"*. **(2)** Then he was asked five questions (§1g), and answered, verbatim: *"no keep my folders the way they are, i do not need breakdown within each folder. its too much to click through, in the future if i need it I will add it."* **Neither answer approves the rule text below.** §2 is the main session's reading of answer (2), written after he gave it. Finding: the Librarian's read-only survey, `reports/drive-operations/2026-09-23_chem-u01-folder-survey.md`. Corroborated by Auditor item 35 in `reports/2026-09-23_chem-u01-qa-audit.md`. |
| **Current Rule** | See §1. Verbatim, from SHULL-CHG-0005, `standards/DRIVE_ARCHITECTURE.md`, `config/drive.json`, `.claude/agents/librarian.md` and `.claude/skills/shelve-drive-file/SKILL.md` |
| **Proposed Rule** | See §2. **The main session's reading of his answer. Not his words.** |
| **Supersedes** | **SHULL-CHG-0005, in part (a LOCKED record). See §3.** Also `DRIVE_ARCHITECTURE.md`: §1 tree, Grammar lines 36–37 and "What goes where"; §2 rules 2 and 3; the §3 Create row. `config/drive.json` `$comment` and `folderGrammar.contentFolders` / `contentFolderRule`. `librarian.md` lines 24, 32 and 64–72. `shelve-drive-file/SKILL.md` lines 22, 26, 29–35 and 46 |
| **Reason** | On 2026-09-16 the user restructured Drive himself in all three courses. He added unit-level `Presentations`, `Guided Notes` and `Quiz` folders in some units. He removed `Homework`, `Presentations`, `Guided Notes` and `Tests-Quizizz` from the sections, so only `Labs-Case Studies-Projects` is left there. The rules still describe the five-folder section tree and let the Librarian create folders. So the Librarian routes to folders that no longer exist, and the Auditor has blocked filing three Unit 1 deliverables (audit item 35). He has now said he wants the tree left as he made it, with no further breakdown. |
| **Affected Agents** | Librarian (routing, and it loses folder creation). Auditor and Janitor (check filing against the rule). Designer and builders (only through the separate naming record in §6) |
| **Affected Skills** | `shelve-drive-file` (lines 22, 26, 29–35, 46). `retrieve-drive-file` reads the same tree. `naming`, only through the separate record in §6 |
| **Affected Courses** | All three: Chemistry, Physics and Geology. Under `CLAUDE.md` §2 this makes it a standard, not a course decision |
| **Risk** | **Medium.** It changes routing for all three courses, removes an agent authority (folder creation), and supersedes a LOCKED record (0005). The live Drive already differs from the rule, so leaving the rule as it is carries risk too. |
| **Recommendation** | Approve §2. Answer §5 item C first. Item D only settles how far "never creates a folder" reaches. The naming gap (§6) is now its own record, SHULL-CHG-0029. |
| **Decision** | *Pending.* |
| **Status** | **PENDING** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. Nothing has been implemented. The required checks are in §8. |

---

## 1. Current Rule — verbatim

### 1a. SHULL-CHG-0005, `docs/DECISIONS_2026-09-07.md` line 123 (APPROVED, CHANGELOG status CONFIRMED)

> | **Confirmed structure** | `SHULL Science/` → `_Brand/{Templates, Standards, Image Library}` and `[Course]/Unit ## - Name/Section ##.# - Name/{Homework, Presentations, Guided Notes, Tests-Quizizz, Labs-Case Studies-Projects}`. Hyphen separators. Section level preserved. |

### 1b. `standards/DRIVE_ARCHITECTURE.md`

Header, line 3:

> **Authority:** SHULL-CHG-0005 — the structure stays exactly as built.

§1 tree, lines 19–26:

> ```
> └── [Course]/                        Chemistry · Physics · Geology
>     └── Unit ## - Unit Name/
>         └── Section ##.# - Section Name/
>             ├── Homework/
>             ├── Presentations/
>             ├── Guided Notes/
>             ├── Tests-Quizizz/
>             └── Labs-Case Studies-Projects/
> ```

§1 Grammar, lines 36–37:

> - The five content folders are **exactly** those five, same spelling, same order, every time.
> - Section subfolders are created on demand, when first needed.

§1 What goes where, lines 41–47:

> | Folder | Contents |
> |---|---|
> | Homework | Practice sets, worksheets, take-home work, homework keys |
> | Presentations | Decks built on the slide template, plus exported PDFs |
> | Guided Notes | Cornell and guided packets — student copy **and** filled teacher key |
> | Tests-Quizizz | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys |
> | Labs-Case Studies-Projects | Lab handouts, case studies, project instructions, rubrics |

§2 rules 2 and 3, lines 52–54:

> 2. **Reuse existing folders exactly**, matching case-insensitively. Never create `Tests` beside
>    `Tests-Quizizz`.
> 3. Create missing Unit and Section folders using the grammar above.

§3 Librarian authority, line 66:

> | Create | Allowed in authorised teaching locations |

### 1c. `config/drive.json`

Line 2, `$comment`:

> "Verified read-only against the live Drive on 2026-09-07. Owner: mshull@jagschools.org. Structure locked by SHULL-CHG-0005; do not restructure without a Secretary change record."

Lines 42–49, `folderGrammar`:

> ```
> "contentFolders": [
>   "Homework",
>   "Presentations",
>   "Guided Notes",
>   "Tests-Quizizz",
>   "Labs-Case Studies-Projects"
> ],
> "contentFolderRule": "Exactly these five, same spelling, same order, every time. Reuse existing folders case-insensitively. Never create 'Tests' beside 'Tests-Quizizz'. Section subfolders are created on demand."
> ```

### 1d. `.claude/agents/librarian.md`

Line 24 (within lines 23–25):

> Resolve **Course → Unit → Section → content type before saving.** Reuse existing folders exactly,
> matching case-insensitively — never create `Tests` beside `Tests-Quizizz`. **If the unit or section
> is unclear, ask.** Never default to a misc folder.

Line 32:

> | Create | Yes, in authorised teaching locations |

Lines 64–65 and 70:

> So when you are running in Claude Code and a built binary needs filing: create and verify the
> destination folders, check the naming grammar, log the operation, and hand the file back naming

> What you CAN do, and should: create and verify the destination folders, check the naming grammar

### 1e. `.claude/skills/shelve-drive-file/SKILL.md`

Line 22 (step 3, lines 21–22):

> 3. **Look for existing folders** and reuse them exactly, matching case-insensitively.
>    **Never create `Tests` beside `Tests-Quizizz`.**

Line 26:

> 6. Create or upload.

Lines 29–35:

> ## Creating folders
>
> `create_file` with the folder mimeType. Follow the grammar exactly — zero-padded unit, hyphen
> separator, **never an en dash**. An en dash creates a near-duplicate folder that sorts beside the
> real one and splits the unit in half.
>
> Section subfolders are created on demand, when first needed.

Line 46:

> | Create, upload | Yes, in authorised teaching locations |

### 1f. Also stale, not named in the brief

| Where | Text |
|---|---|
| `README.md:71` | Drive row: "Unchanged — `SHULL Science/`, Unit → Section → five content folders" |
| `config/drive.json:62`, `knownDefects[3]` | "Chemistry Unit 00 has a bare Labs/ folder instead of a Section folder with the five content folders" |
| `config/drive.json:28–35` | Physics `unitFolders: 1`, Geology `unitFolders: 0`. The live counts are 11 and 10 (survey F8) |

### 1g. The five questions answer (2) replied to (as relayed by the main session)

- practice sets/homework: loose in the section folder, or recreate Homework/?
- unit tests: into Unit/Quiz/?
- activities: into Labs-Case Studies-Projects/ or loose?
- unit review: into Quiz/ or a new folder?
- should every unit in all three courses get the three unit-level folders?

---

## 2. Proposed Rule

> **This is the main session's reading of the user's 2026-09-23 answer (2). It is not his words.** His
> words are in the Source row. Approving this record confirms that the reading is right.

### 2a. The rule

1. **The system never creates a Drive folder.** The tree as it stands is the layout. The user adds
   folders himself. Units without the unit-level folders stay without them. (How far this reaches
   is §5 item D.)
2. **File into a matching folder only if it already exists. Otherwise, file loose in its parent.**

| Document | Destination if the folder exists | Otherwise |
|---|---|---|
| Slides | `Unit ##/Presentations/` | loose in the unit folder |
| Guided notes + key | `Unit ##/Guided Notes/` | loose in the unit folder |
| Quizzes and tests + keys | `Unit ##/Quiz/` | loose in the unit folder |
| Labs, case studies, projects and their rubrics | `Section ##.#/Labs-Case Studies-Projects/` | loose in the section folder |
| Practice sets, homework and activities for one section | none (no matching folder) | loose in the section folder |
| Unit reviews, study guides, and multi-section files with no matching folder | none | loose in the unit folder |

**Secretary's note on a gap in the reading.** `Reference` and `Organizer` files are not named. Rule 2
covers them anyway: no matching folder exists, so they go loose in the section folder (one section)
or the unit folder (unit-scope). The note is here so an implementer does not have to guess.

### 2b. Text for `DRIVE_ARCHITECTURE.md`

§1 tree (replaces lines 19–26). It shows the folders the system **recognises when present**, not
folders that must exist:

```
└── [Course]/                        Chemistry · Physics · Geology
    └── Unit ## - Unit Name/
        ├── Presentations/                 if the user made it
        ├── Guided Notes/                  if the user made it
        ├── Quiz/                          if the user made it
        └── Section ##.# - Section Name/
            └── Labs-Case Studies-Projects/    if the user made it
```

§1 Grammar, replacing lines 36–37:

> - The recognised content folders are `Presentations`, `Guided Notes` and `Quiz` at unit level, and
>   `Labs-Case Studies-Projects` at section level. Match them case-insensitively.
> - **The system never creates a folder.** The user adds folders himself. If the matching folder is
>   not there, the file goes loose in its parent.

"What goes where" (lines 39–47) is replaced by the §2a table.

§2 rule 2 (replaces lines 52–53):

> 2. **Reuse existing folders exactly**, matching case-insensitively. **Never create a folder.**

§2 rule 3 (line 54) is **removed**, or narrowed, depending on §5 item D.

§3 Create row (line 66): "Files: allowed in authorised teaching locations. **Folders: never.**"

§2 rule 4 ("If the unit or section is unclear, ask. Never default to a misc folder.") **stays**. A
file loose in its correct unit or section folder is not a misc folder.

### 2c. `librarian.md` and `shelve-drive-file/SKILL.md`

Both **point to** `DRIVE_ARCHITECTURE.md` §2 and stop restating folder names. Restating them is how
both went stale.

- `librarian.md:24`: replace the `Tests-Quizizz` clause with the pointer.
- `librarian.md:32`: Create row as in §2b.
- `librarian.md:64–65, 70`: "create and verify the destination folders" becomes "confirm the
  destination folder, or the parent the file will go loose in".
- `SKILL.md:22`: the pointer.
- `SKILL.md:26`: "Upload." (not "Create or upload.")
- `SKILL.md:29–35`, "Creating folders": removed, replaced by one line pointing to §2 rule 2.
- `SKILL.md:46`: Create row as in §2b.

### 2d. `config/drive.json`

- `$comment`: "Structure: SHULL-CHG-0005 as amended by SHULL-CHG-0027. The system creates no
  folders." Plus the new verification date.
- `folderGrammar.contentFolders` → `recognisedUnitFolders: ["Presentations", "Guided Notes", "Quiz"]`
  and `recognisedSectionFolders: ["Labs-Case Studies-Projects"]`. `contentFolderRule` is rewritten to
  §2b. These are names to match, **not** folders that must exist.
- `courses.physics`: `unitFolders: 11`, Unit 00–10. `courses.geology`: `unitFolders: 10`, Unit 01–10.
  Both verified (survey F8).
- `operations.createFolder`: marked "not used. The system creates no folders (SHULL-CHG-0027)".
- `knownDefects[3]`: reworded so it no longer cites "the five content folders". The bare `Labs/`
  folder in CHEM U00 still exists (survey §5). Under this rule it is his folder, so whether it is a
  defect at all is his call.
- Per-unit IDs: **§4, and only §4.** Config has no per-unit map today, so adding one is a schema
  addition.

### 2e. Q1–Q6 from the survey: resolved by this reading, no longer open

| # | Survey question | Resolved as (the main session's reading) |
|---|---|---|
| Q1 | Section homework: loose, or a recreated `Homework/`? | Loose in the section folder. No `Homework/` is created |
| Q2 | Does `Quiz/` hold everything `Tests-Quizizz` held? | Quizzes and tests + keys go in `Unit ##/Quiz/` if present, else loose in the unit folder |
| Q3 | Activities: in Labs, or loose? | Loose in the section folder |
| Q4 | Unit review / study guide? | `Quiz/` is not used for them, and no new folder is made. Loose in the unit folder |
| Q5 | Homework spanning several sections? | Loose in the unit folder |
| Q6 | Every unit gets the three unit-level folders? | **No.** Units without them stay without them. CHEM U02 stays as it is |

Survey §6 action "The user must create `Labs-Case Studies-Projects`, then reparent" (PHYS S01.4 lab)
**falls away.** Under rule 2 the lab is already correctly filed, loose in the section.

---

## 3. Supersedes — and the conflict with a LOCKED record

> **CONFLICT, not resolved here.** SHULL-CHG-0005 is APPROVED and CONFIRMED. It locks the five
> content folders **inside each section**, and `config/drive.json` says "do not restructure without a
> Secretary change record". The user restructured Drive on 2026-09-16 without one, and the Auditor
> found no operation log for it (audit item 35). The live Drive now contradicts a LOCKED rule. Both
> of his answers plainly favour his own layout, but the rule text came later. The Secretary does not
> pick a side. **The user decides (§5 item C).**

| Part of 0005 | What 0027 does to it |
|---|---|
| Root `SHULL Science/`, `_Brand/{Templates, Standards, Image Library}` | **Kept** |
| `[Course]/Unit ## - Name/Section ##.# - Name/` and hyphen separators | **Kept** as the naming grammar for folders the user makes |
| "Section level preserved" | **Kept.** Sections still exist and hold labs and section files |
| `Section …/{Homework, Presentations, Guided Notes, Tests-Quizizz, Labs-Case Studies-Projects}` | **Superseded.** No required content folders. The system recognises the four named in §2b when present |
| `DRIVE_ARCHITECTURE.md` line 3, "the structure stays exactly as built" | **Superseded.** Becomes "SHULL-CHG-0005 as amended by SHULL-CHG-0027" |

Also superseded, and **not** part of 0005: the Librarian's authority to create folders
(`DRIVE_ARCHITECTURE.md` §2 rule 3 and the §3 Create row, `librarian.md:32`, `SKILL.md:46`). That
authority came from the architecture standard, not from a separate change record.

0005 stays on file and is **not** edited. `docs/` is the decision record, and history is appended,
never rewritten. The new CHANGELOG row for 0027 names 0005 as partly superseded.

---

## 4. `config/drive.json` IDs — verified, existing folders only (2026-09-23)

Verified by independent `parentId` search from the `SHULL Science` root (survey §2, §4, §7). **No
entry is added for a folder that does not exist.** No key, no `null`, no placeholder.

### 4a. Unit folders and their unit-level content folders

| Course / unit | Unit folder | Presentations | Guided Notes | Quiz |
|---|---|---|---|---|
| CHEM U00 | `1QknMfGJdISiBVIINQm724R6_X7EtxfuT` | `1sfhd0zfsQGxQ6ktYM79rxReqVLqYIU8-` | `1o_oF3Xqu-oMsPfdNeb8yyoJZCOw7icRl` | `1bx_3T_eruQ-LeQnhC8RP3SOGV4DzxuX-` |
| CHEM U01 | `1vYISUV443AAVTmODSnUIwxSUgxCc5i8b` | `1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx` | `1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG` | `1cwiX68GJE4OGxsI_wC8IGE-g8Ejz2sO7` |
| CHEM U02 | `1caxbGbuk4m-18ERTvk5Le_NNsMLmQ3Xp` | *(none exist. No entries)* | | |
| PHYS U01 | `1_ykbQae1GAKi0hWFn-OWIdvVAWXwc_6D` | `1a2yvOkD19Heypn4RdXrZMBykvhgSJ_JT` | `1Kof55nqkDQo6rMoy5JYagNxNXl-FsRt7` | `1aYZtAI2rKprtJIFOjJMKDnTOBteAjqVI` |
| PHYS U02 | `1rB4t-tF-PygDHIFFQBleIpHV4GHJYBve` | `193RS23zSyfdOJF3s7b9Yd9xzmpV6dPFv` | `1EkaGgN5rCqWC0tmCQutdjwY6eM9_8FaN` | `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW` |
| GEO U01 | `1vdta_fO_QPLqzwt7rD76VyKZOGZOnXI_` | `1RIpXtC2JvyVvFI4rHbNF_hHvhFVWL_2f` | `13or8vDciecTyueJRQ7xKQ6TllyAkr7hC` | `1NUPLYgUeRNgt6NL9cUL_6r02YpJ54jAF` |
| GEO U04 | `1xnMcAw0yAOqDWAMuTm9A8b915XGwvHM8` | `1IoDRLvp3_V1gJaziZNbzJDdc4T4n1pD5` | `1wJEc8Nj-KZdzAOcbqSWY3yOWIvqdwd3O` | `1QHXv5XFcchSDD4oRaumMi4f6oQNBH8Xr` |

### 4b. CHEM U01 sections

| Section | Section folder | `Labs-Case Studies-Projects` |
|---|---|---|
| S01.1 | `1XS4PboqJFcbDmtQWdArK7H54KFGlA0_s` | `12jktWfOEEUPTqvDAdFCAB9B9XY0jOfNl` |
| S01.2 | `15FUjBMNe9elG0Cod5eNqUTSn9d1cEDWe` | `1EMp9Vi12n39sLv-r2WV_tM7R73Rrdwp5` |
| S01.3 | `1t_3db6VNrkCYuP73LgQx-sWEVHvz7GIK` | `1IE9wqFT8iXkFkY3Py2OAe-o4brVFlqjS` |
| S01.4 | `1WU_Mx3hYEDdNR8ADffg_bI16kPZ0GQDK` | *(none exists. No entry.)* The folder is empty. See SHULL-CHG-0028 (the fold) |
| S01.5 | `1WoVqoIbq7nC10gXGM4GC4U8IctJywa5D` | `1QV9m7jqso5CKhkZNWDW8TjAcquLGv14n` |

### 4c. Other section-level Labs folders the survey verified

The survey saw these by `parentId` search (§4) but did not log their parent **section** folder IDs.
The Labs IDs may be listed. The section IDs are **not** listed and are not guessed.

| Course / section | `Labs-Case Studies-Projects` |
|---|---|
| CHEM S00.4 | `199f-dW2ZxIk99mqmK96HGQGbVHWWqTf6` |
| PHYS S01.3 | `1MFa1jLRkYaQPrGoXeHpkdnPFfnlOUuAm` |
| PHYS S02.1 | `10aGiNXh8Y--NBzGzXcruAdglgJIaw3ck` |
| GEO S01.1 | `1KGS9wtbINi5LlzAkmob1CKeej1THK9f8` |
| GEO S04.1 | `1CupEoLfy7DHoTskPNlke99HnxXRlaob6` |

PHYS S01.2 `1syvqWt83E0ReKfLvVqF34FAcH2ZkG7i6` is also verified (survey §6), as a section folder. The
CHEM U00 bare `Labs` folder `1otXTZSKkPAwasC4uX8NyjhpT3-eBFaNk` exists but is not a recognised name.
It stays under `knownDefects` and is not listed as a content folder.

### 4d. Not yet walked — a full walk is needed before config lists them

| Course | Units not walked |
|---|---|
| Chemistry | U03 to U15 |
| Physics | **U00**, U03 to U10. The survey's "not sampled" list leaves out PHYS U00, but U00 was not sampled either |
| Geology | U02, U03, U05 to U10 |

**Do not add IDs for these units** from config, old logs or inference. The Librarian walks them
read-only first. The walk lists what exists and creates nothing.

---

## 5. For the user — decide before approving

| # | Question | Why it matters |
|---|---|---|
| **C** | **Your 2026-09-16 layout replaces the section folders that SHULL-CHG-0005 locked. Should 0027 supersede 0005 for the content folders, as §3 sets out?** Both your answers point this way, but they were given before this text existed. | Nothing else in this record can be applied until the LOCKED conflict is decided |
| **D** | Flagged, not resolved. **Does "never creates a folder" also cover Unit and Section folders?** Your words were about "breakdown within each folder". The reading says "never creates a Drive folder", which goes further. Today every unit folder exists, but many sections do not: CHEM U02 is empty. **If D is yes:** a U02 section's lab goes loose in `Unit 02`. **If D is no:** the Librarian may still create a missing `Section ##.#` folder, and only content subfolders are off limits. | Decides whether `DRIVE_ARCHITECTURE.md` §2 rule 3 is removed or narrowed |

Q1–Q6 are **closed** by the reading in §2e.

---

## 6. Split out: the NAMING gap. Now SHULL-CHG-0029

**Raised as its own record: `governance/proposals/SHULL-CHG-0029-multi-section-filenames.md`
(PENDING).** That record is authoritative for the naming gap. It carries the user's delegation, the
range form the main session chose, and the validator findings. The notes below are what this record
said before 0029 existed. They are kept for the audit trail and **superseded by 0029** wherever they
differ.

**Not part of 0027's rule.**

- `standards/NAMING.md` §2 grammar is `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]`.
  Every file must carry `S##.#`. A unit quiz, a unit deck, a unit review or a multi-section file
  filed loose in the unit folder has no single section, so **it has no legal name today.**
- The unit-level files already on Drive use four different ad-hoc forms (survey F9):
  `SHULL_PHYS_Quiz_U01_Fall2026_A`, `GEO_U1_S1.2-S1.4_…`, `Unit 1 - Matter and Atomic Theory Notes`,
  `Physics Unit 1 - Motion in 1D Pres`.
- **A question is already with the user:** for multi-section files, `_S01.1_S01.3_S01.5` or
  `_S01.1-S01.5`? **His answer is not in yet.** Neither form is assumed here.
- Whole-unit files (no section at all) need their own form too. The survey offers
  `SHULL_[COURSE]_[Type]_U##[_Descriptor][_Version]` as **an option only**.
- **Recommendation:** raise it as its own record once he answers, number allocated then. It changes
  `standards/NAMING.md` and the `naming` skill, and may change `scripts/validate_codes.py`. None of
  those are Drive-architecture files. It should not wait on 0027, and 0027 should not wait on it.
  File renames stay blocked until it lands (survey §6).

### `scripts/validate_codes.py`: not checked for filenames with no section code

The Librarian did not check it. **Nobody has run it against a unit-scope or range filename.** The
Secretary read the pattern at line 16 but did not run it:
`SHULL_(CHEM|PHYS|GEO)_[A-Za-z_]+_U(\d{1,2})_S(\d{1,2}\.\d)`. Reading it suggests that:

- a filename with **no** `S##.#` does not match, so it is **skipped silently**. It is neither passed
  nor failed.
- a range such as `_S01.1-S01.5` or `_S01.1_S01.3_S01.5` matches on its **first** code only.

That reading has not been tested. The naming record must test it and fix the validator.

---

## 7. Flags

### 7a. Dead folder IDs. The user can check Drive Trash

These IDs are cited in repo logs and no longer resolve (survey F4, §3). **From the connector the
Librarian cannot tell whether they were trashed or permanently deleted.** If they were trashed, the
user can see them, and restore them, in **Drive Trash**. No agent can empty the trash.

| Item | Cited in | ID | Result |
|---|---|---|---|
| `Unit PPT` | 2026-09-15 log | `1htdFwk1O71Z4WBUmPIeRG0Mit_pVUGp3` | not found |
| `New folder` | 2026-09-15 log | `1CagpVXjDdxIje-bGHHqYy5Dnw2Rt_o67` | not found |
| S01.4 `Presentations` | 2026-09-08 log, and its "drag it in" link | `1bK07FKOdrW3JUw5-2jre5zm1VZ1itJU-` | not found. **The filing link in that log is dead** |
| S01.1 `Homework` | 2026-09-14 log | `1NphcrpeHSmBNIVUkYU9vvWCOyH9o8AjL` | not found |
| S01.1 `Presentations` | 2026-09-14 log | `1pOywcnz66gxAZ2Mr9SMldX9226U9u6wp` | not found |
| S01.1 `Guided Notes` | 2026-09-14 log | `1LwWvGHxrYA_YYGNon9x3a_fbYUwdniMT` | not found |
| S01.1 `Tests-Quizizz` | 2026-09-14 log | `1EHD67dKmv9DBuF8M4kXqVZH40H3OxliJ` | not found |
| S01.2 / S01.3 / S01.5 `Homework`, `Presentations`, `Guided Notes`, `Tests-Quizizz` (12 IDs) | 2026-09-15 log | see that log | absent from each section's listing. **Not checked one by one by metadata** |
| PHYS S01.1 `Homework` | 2026-09-14 PHYS log | `1CVfke4Axe8jGk9b6pm7WmzPvLKwug78u` | absent from the S01.1 listing |

### 7b. The 2026-09-16 changes have no operation log

`CHANGE_CONTROL.md` §7 says a mutation that was not logged cannot be rolled back. He made these
changes himself, so no pre-mutation log exists. The Auditor recommends a retroactive log (audit
item 35). Recording that is Librarian work, outside this record.

### 7c. Related, not part of this record

- The CHANGELOG "Open" row (2026-09-08) asking whether to file the U01 S1.4 deck is overtaken. The
  deck is on Drive, in unit-level `Presentations` (survey F5). It needs retiring when the index is
  next updated.
- Survey §6 file-level issues (duplicates, PHYS S01.2 files misfiled in S01.1, the second GEO notes
  copy) are Librarian/Janitor work orders. Each trash or move needs its own approval.

---

## 8. Implementation plan and checks — only after APPROVED and §5 C and D answered

**Nothing is edited now.**

| # | File | Change |
|---|---|---|
| 1 | `standards/DRIVE_ARCHITECTURE.md` | Line 3 authority, §1 tree, Grammar, What goes where, §2 rules 2 and 3, the §3 Create row, per §2b |
| 2 | `config/drive.json` | Per §2d and §4. Only the IDs in §4a–§4c |
| 3 | `.claude/agents/librarian.md` | Lines 24, 32 and 64–72, per §2c |
| 4 | `.claude/skills/shelve-drive-file/SKILL.md` | Lines 22, 26, 29–35 and 46, per §2c |
| 5 | `README.md:71` | "Unit → Section → five content folders" → a pointer to `standards/DRIVE_ARCHITECTURE.md` |
| 6 | `change-log/CHANGELOG.md` | Row for 0027, naming 0005 as partly superseded |

Items 3 and 4 are under `.claude/`. As SHULL-CHG-0026 §5 item 2 notes, a sub-agent may not be able to
edit those on a relayed approval. The user may need to approve those tool calls himself when prompted.

Checks:

- [ ] `grep -rn "Tests-Quizizz"` outside `legacy/`, `docs/`, `reports/` and `governance/proposals/`
      finds nothing
- [ ] `grep -rn "five content folders\|Exactly these five\|Creating folders\|created on demand"`
      returns nothing live
- [ ] Every ID in `config/drive.json` matches §4 and resolves by `get_file_metadata` on the day of the
      commit. No key exists for a folder that does not exist
- [ ] No ID from §4d appears in config
- [ ] `librarian.md` and `SKILL.md` point to `DRIVE_ARCHITECTURE.md` §2 and restate no folder names
- [ ] `legacy/` and `docs/DECISIONS_2026-09-07.md` untouched
- [ ] Commit carries `SHULL-CHG-0027`. `Implemented By` and `Verified` filled in here
