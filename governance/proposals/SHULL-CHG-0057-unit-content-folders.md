# SHULL-CHG-0057 — Four unit-level content folders in every unit: Quiz, Test, Presentations + Guided Notes, Worksheets

> **ID note.** `SHULL-CHG-0056` is taken on another branch (`overseer-as-subagent-routing-brief`), so
> this record is 0057. The Secretary that drafted it had no shell and could not run
> `git fetch origin main` (`governance/CHANGE_CONTROL.md` §2, "Allocating a new Change ID"). The ID
> came from the main session. Under that rule the ID is not allocated until this file is pushed to
> `origin/main`. The main session must check the fetched `origin/main` before it commits.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0057 |
| **Date** | 2026-11-05 |
| **Source** | User, 2026-11-05, in the main session. The Secretary did not hear him directly. His words, as relayed: **(1)** *"I added them but can you just make them for me. Quiz's / Test / Presentations + Guided Notes / Worksheets"*, about the four folders he had made by hand in Chemistry Unit 04, asking for the same set in Unit 05. **(2)** He agreed to *"draft a change proposal making your four folders the standard for every unit"*, then said *"yes draft the proposal"*. **Neither answer approves the rule text below.** Evidence: `reports/drive-operations/2026-11-05_chem-u04-u05-content-folders.md` and `reports/drive-operations/2026-11-05_chem-u04-u05-notes-filing.md`. |
| **Current Rule** | See §1. Verbatim, from `standards/DRIVE_ARCHITECTURE.md`, `config/drive.json`, `.claude/skills/shelve-drive-file/SKILL.md`, `.claude/agents/librarian.md`, and records SHULL-CHG-0029, 0030 and 0035. |
| **Proposed Rule** | See §2. **The main session's reading of his words, written by the Secretary. Not his words.** Six open questions (§5) change the text. |
| **Supersedes** | **In part, and in conflict (§3):** SHULL-CHG-0035 (APPROVED), its rule that the system never creates a content folder, for these four names. SHULL-CHG-0030 (IMPLEMENTED), the unit-level `Quiz` holding unit tests, and its "never create `Tests` beside `Quiz`" clause. SHULL-CHG-0029 (IMPLEMENTED), the separate unit-level `Guided Notes` and `Presentations` folders. Text: `DRIVE_ARCHITECTURE.md` header lines 3–14, §1 tree (lines 30–41), Grammar (lines 50–64), What goes where (lines 66–79), §2 rules 2–3 (lines 84–88), §3 Create row (line 100). `config/drive.json` `$comment`, `folderGrammar.recognisedUnitFolders`, `contentFolderRule`, `homeworkFiling`, `operations.createFolder`. `shelve-drive-file/SKILL.md` lines 3, 24–26, 35–39, 50. `librarian.md` lines 33–36, 43, 72–73, 81–83. |
| **Reason** | (1) Matt has now made, or asked for, the same four unit-level folders in two Chemistry units. That is his layout, and the rule does not describe it. `recognisedUnitFolders` lists `Guided Notes`, `Presentations` and `Quiz`, so the Librarian would not recognise `Test`, `Worksheets` or `Presentations + Guided Notes`. Under SHULL-CHG-0035 it would file the next U04 or U05 worksheet loose in the section, beside a `Worksheets` folder it ignores. (2) The main session created the U05 folders on his direct instruction (CLAUDE.md §2, precedence 1), against SHULL-CHG-0035. That override covered two units only. Without a record, the next session falls back to the old rule and the two units become exceptions nobody wrote down. (3) He asked for it: "making your four folders the standard for every unit". |
| **Affected Agents** | Librarian (routing, and it gains authority to create these four content folders). Auditor and Janitor (they check filing against the rule; the Janitor's sweep must look for near-duplicates). Overseer (fills `reports/filing-queue.md` destinations). Secretary (this record). |
| **Affected Skills** | `shelve-drive-file` (lines 3, 24–26, 35–39, 50). `retrieve-drive-file` (lines 15, 23: "Search the section's content folder first" assumes section-level folders). `naming` is not changed: the types `Quiz`, `Test`, `Slides`, `Guided_Notes`, `Practice_Set`, `Activity`, `Organizer` in `standards/NAMING.md` line 47 already exist. |
| **Affected Courses** | **Chemistry for certain. Physics and Geology depend on §5 question 4.** As drafted ("every unit, in every course"), all three, which makes it a standard under CLAUDE.md §2. If he says Chemistry only, it becomes a Chemistry course decision (Path A, `courses/chemistry/DECISIONS.md`), and this record is rewritten or withdrawn. |
| **Risk** | **Medium.** It changes routing in up to three courses. It reverses part of an APPROVED rule (0035) and an IMPLEMENTED rule (0030). It gives the Librarian back an authority 0035 removed. Any retrofit of existing units means many Drive moves. The repository edit itself is low risk and one revertible commit. |
| **Recommendation** | Approve after §5 questions 1, 2 and 4 are answered; they change the rule text. Questions 3, 5 and 6 can take the defaults in §2 unless he says otherwise. Do **not** approve any retrofit (§2e) in the same decision. A retrofit is a Librarian move plan with its own approval. |
| **Decision** | *(pending, awaiting the user)* |
| **Status** | **PENDING** |
| **Implemented By** | — |
| **Verified** | No. Not implemented. Plan in §7. |

---

## 1. Current Rule — verbatim

### 1a. `standards/DRIVE_ARCHITECTURE.md`

§1 tree, lines 30–38:

> ```
> └── [Course]/                        Chemistry · Physics · Geology
>     └── Unit ## - Unit Name/
>         ├── Guided Notes/                  if the user made it
>         ├── Presentations/                 if the user made it
>         ├── Quiz/                          if the user made it
>         └── Section ##.# - Section Name/
>             ├── (homework and activities loose here — no Homework folder)
>             └── Labs-Case Studies-Projects/    if the user made it
> ```

Grammar, lines 50–64:

> - **Unit-level content folders recognised:** `Guided Notes`, `Presentations`, `Quiz` — **exactly**
>   those three names, same spelling, siblings of the Section folders, one copy per unit. **Not**
>   duplicated into each section. Match them case-insensitively. […]
> - **Section-level content folder recognised:** `Labs-Case Studies-Projects` — the only one. […]
> - **No `Homework` folder exists at any level.** Homework files — practice sets, worksheets,
>   take-home work, keys — are filed as loose files directly inside the Section folder itself.
>   (**SHULL-CHG-0030**.)
> - **The system never creates a content folder** (SHULL-CHG-0035). The user adds those himself, and a
>   unit that lacks one stays without it. If the matching folder is not there, the file goes **loose
>   in its parent**. This covers content subfolders only: a missing `Section ##.#` folder may still be
>   created (§2 rule 3).

What goes where, lines 73–79 (rows):

> | Guided Notes | Unit | Cornell and guided packets — student copy **and** filled teacher key. […] |
> | Presentations | Unit | Decks built on the slide template, plus exported PDFs. […] |
> | Quiz | Unit | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys. […] |
> | Labs-Case Studies-Projects | Section | Lab handouts, case studies, project instructions, rubrics |
> | *(no folder — loose in Section)* | Section | Homework: practice sets, worksheets, take-home work, keys. […] **SHULL-CHG-0030.** |
> | *(no folder — loose in Section)* | Section | Activities and any other file for a single section with no matching folder, including `Reference` and `Organizer` files (SHULL-CHG-0035). |
> | *(no folder — loose in Unit)* | Unit | Unit reviews, study guides, homework or files spanning several sections, and unit-scope files with no matching folder (SHULL-CHG-0035). |

§2 rules 2–3, lines 84–88:

> 2. **Reuse existing folders exactly**, matching case-insensitively. **Never create a content
>    folder** (SHULL-CHG-0035). If the matching one does not exist, file loose in the parent. `Quiz` is
>    the current name for the unit-level quiz folder (**SHULL-CHG-0030**).
> 3. Create missing Unit and Section folders using the grammar above. This is the only folder creation
>    the system does (SHULL-CHG-0035, decision D: it does not cover content subfolders).

§3 Create row, line 100:

> | Create | Files: allowed in authorised teaching locations. Folders: `Unit ##` and `Section ##.#` folders only (§2 rule 3). **Never a content folder** (SHULL-CHG-0035). |

### 1b. `config/drive.json`

Lines 42–51, `folderGrammar`:

> ```
> "recognisedUnitFolders": ["Guided Notes", "Presentations", "Quiz"],
> "recognisedSectionFolders": ["Labs-Case Studies-Projects"],
> "contentFolderRule": "SHULL-CHG-0035 (2026-10-15) governs, […] the system never creates a content folder; if the matching one is absent the file goes loose in its parent. […] Never create 'Tests' or 'Tests-Quizizz' beside 'Quiz'. […]",
> "homeworkFiling": "No Homework folder exists at any level as of SHULL-CHG-0030. Homework files are loose files directly inside 'Section ##.# - Section Name/', not inside any subfolder."
> ```

Line 55, `operations.createFolder`:

> "Not used for content folders (SHULL-CHG-0035). Only a missing Unit ## or Section ##.# folder may be created, with create_file and mimeType application/vnd.google-apps.folder."

Line 2, `$comment` (excerpt): "Structure: SHULL-CHG-0005 as amended by SHULL-CHG-0035 (2026-10-15); the system creates no content folders; do not restructure without a Secretary change record."

### 1c. `.claude/skills/shelve-drive-file/SKILL.md`

Line 3 (description): "File a finished deliverable into the correct Google Drive location (loose in the parent when the matching content folder is absent) and verify the destination."

Lines 24–26:

> 3. **Look for existing folders** and reuse them exactly, matching case-insensitively. If the
>    matching content folder is absent, file loose in its parent. Never create a content folder. Rules:
>    `standards/DRIVE_ARCHITECTURE.md` §2.

Lines 37–39:

> Content folders are never created. The only folders you may create are a missing Unit or Section
> folder, under `standards/DRIVE_ARCHITECTURE.md` §2 rule 3. […]

Line 50:

> | Create, upload | Files: yes, in authorised teaching locations. Folders: Unit and Section only, never a content folder. […] |

### 1d. `.claude/agents/librarian.md`

Lines 33–36: "Reuse existing folders exactly, matching case-insensitively. Folder rules, including which
folders you may create, are in `standards/DRIVE_ARCHITECTURE.md` §2 (SHULL-CHG-0035)."

Line 43:

> | Create | Files: yes, in authorised teaching locations. Folders: only as `standards/DRIVE_ARCHITECTURE.md` §3 allows. **Never a content folder.** |

Lines 72–73: "Resolve and verify the destination folder (Course, Unit, Section, content type), or the
parent the file goes loose in when the matching content folder does not exist."

Lines 81–83: "Confirm the destination folder, or the parent the file will go loose in, log the
operation, and hand the file back with the folder link."

### 1e. The records

- **SHULL-CHG-0029** (IMPLEMENTED, `3ef3ce8`), Proposed Rule: "Each **Unit** folder […] gets exactly
  two folders directly inside it […]: `Guided Notes` and `Presentations`."
- **SHULL-CHG-0030** (IMPLEMENTED, `07fc509`), Proposed Rule: "`Quiz` is the renamed, unit-level
  successor to the old Section-level `Tests-Quizizz` — same contents (quizzes, unit tests, exit
  tickets, bell ringers, A–D versions, keys) […]. `Homework` is removed as a folder at **any**
  level; homework files (worksheets, practice sets, take-home work, keys) are filed as loose files
  directly inside the Section folder itself."
- **SHULL-CHG-0035** (APPROVED, `c0c21f4`, not yet IMPLEMENTED), §2a rule 1 as narrowed by decision
  D: the system never creates a content folder; "Units without the unit-level folders stay without
  them." Its §2e Q6, the main session's reading of his 2026-09-23 answer: "Every unit gets the three
  unit-level folders? **No.**" His words then: *"no keep my folders the way they are, i do not need
  breakdown within each folder. its too much to click through, in the future if i need it I will add
  it."*

---

## 2. Proposed Rule

> **The main session's reading of the user's 2026-11-05 words, written by the Secretary. Not his
> words.** Approving this record confirms the reading. Text in [square brackets] depends on a §5
> question, and the default shown applies only if he does not answer otherwise.

### 2a. The rule

1. **Every unit folder [in every course: §5 Q4] has four unit-level content folders, with exactly
   these names:** `Quiz`, `Test`, `Presentations + Guided Notes`, `Worksheets`. They sit beside the
   unit's Section folders, one copy per unit, and are not duplicated into sections.
2. **The system creates them when missing.** This amends SHULL-CHG-0035 for these four names only.
   No other content folder is ever created. 0035's other rules stay: Unit and Section folders may
   be created, and nothing else.
3. **Reuse before create.** Before creating, list the unit folder's children (`parentId` search) and
   match each of the four names case-insensitively. If a match exists, use it. **Never create a
   near-duplicate**: not `Tests` beside `Test`, not `Quizzes` or `Quiz's` beside `Quiz`, not
   `Worksheet` beside `Worksheets`, not `Presentations & Guided Notes` or `Presentations and Guided
   Notes` beside `Presentations + Guided Notes`. A folder that looks like a variant but does not
   match exactly is **reported, not used and not renamed** (§5 Q6).
4. **Folder creation is logged** to `reports/drive-operations/` before it happens (unit folder ID,
   names to create), then verified by `parentId` lookup, the same as any other mutation.
5. **Routing by content type:**

| Content | Folder |
|---|---|
| Slides (decks and exported PDFs) and guided notes (student copy, key, PDF) | `Presentations + Guided Notes` |
| Quizzes, exit tickets, bell ringers, quiz banks (+ keys, A–D versions) | `Quiz` |
| Unit tests: Day 1 / Day 2, A–D versions, keys | `Test` **[conflicts with 0030: §5 Q1]** |
| Practice sets, worksheets, organizers, homework, activities (+ keys) | `Worksheets` **[section-level placement: §5 Q2]** |
| Labs, case studies, projects, rubrics | **[unchanged by default: `Section ##.#/Labs-Case Studies-Projects/` if present, else loose in the section. §5 Q3]** |
| Unit reviews, study guides, `Reference` files, anything with no row above | **[unchanged by default: loose in the unit folder. See note below]** |

6. A file spanning two units is filed once, in the first unit's folder, and not duplicated. (This is
   what was done with the U4–U5 deck and notes. It restates existing practice; it is not new.)

**Secretary's note on gaps in the reading.** Matt's list did not name `Study_Guide`, `Reference` or
`Rubric` (types in `standards/NAMING.md` line 47), unit reviews, or labs. The default above keeps
them where they go today. If he wants study guides in `Test` or `Quiz`, that is his call, not an
inference. Not one of the six questions; raise it only if he wants to.

### 2b. Text for `standards/DRIVE_ARCHITECTURE.md`

- **Header (lines 3–14):** add "**Amended by SHULL-CHG-0057** (2026-11-05): four unit-level content
  folders, created when missing. Supersedes in part 0029, 0030 and 0035." Leave the existing lines;
  history is appended.
- **§1 tree (lines 30–38):**

```
└── [Course]/                        Chemistry · Physics · Geology
    └── Unit ## - Unit Name/
        ├── Presentations + Guided Notes/      created if missing (SHULL-CHG-0057)
        ├── Quiz/                              created if missing
        ├── Test/                              created if missing
        ├── Worksheets/                        created if missing
        └── Section ##.# - Section Name/
            ├── [section files loose here: §5 Q2]
            └── Labs-Case Studies-Projects/    if the user made it [§5 Q3]
```

- **Lines 40–41:** "recognises when present" becomes: the four unit folders are required and are
  created if missing; the section folder is recognised when present.
- **Grammar (lines 50–64):** replace the unit-level bullet with the four names and rule 2a.3
  (case-insensitive reuse, the named near-duplicates). Replace the "No `Homework` folder" bullet per
  §5 Q2. Narrow the "never creates a content folder" bullet: "except the four unit-level folders
  (SHULL-CHG-0057)".
- **What goes where (lines 66–79):** replace the `Guided Notes`, `Presentations` and `Quiz` rows with
  the §2a table. Change the "loose in Section" homework row per §5 Q2.
- **§2 rule 2 (lines 84–86):** "Never create a content folder, **except** the four unit-level folders,
  which are created when missing after a case-insensitive check." Drop "`Quiz` is the current name
  for the unit-level quiz folder".
- **§2 rule 3 (lines 87–88):** "This is the only folder creation" becomes "Together with rule 2's
  four unit folders, this is the only folder creation".
- **§3 Create row (line 100):** "Folders: `Unit ##`, `Section ##.#`, and the four unit-level content
  folders (SHULL-CHG-0057). No other content folder."

### 2c. `config/drive.json`

- `folderGrammar.recognisedUnitFolders` → `["Presentations + Guided Notes", "Quiz", "Test",
  "Worksheets"]`. Rename the key to `requiredUnitFolders` **or** keep the name and add a
  `unitFoldersCreatedWhenMissing: true` flag. **Implementer: grep `scripts/` for the key first.**
  0035's implementation note says no script reads it; check again on the day.
- `folderGrammar.recognisedSectionFolders`: unchanged unless §5 Q3 changes it.
- `contentFolderRule`: one sentence pointing to `DRIVE_ARCHITECTURE.md` §1–§2 and citing 0057. Delete
  "Never create 'Tests' or 'Tests-Quizizz' beside 'Quiz'": `Test` is now a sibling of `Quiz` on
  purpose. Keep the history sentences, or move them to a pointer to 0029, 0030 and 0035.
- `homeworkFiling`: rewritten per §5 Q2.
- `operations.createFolder`: "Used for the four unit-level content folders (SHULL-CHG-0057) and a
  missing Unit or Section folder. Nothing else."
- `$comment`: "SHULL-CHG-0005 as amended by SHULL-CHG-0035 and SHULL-CHG-0057", plus the date.
- Per-unit IDs for CHEM U04 and U05 (eight folder IDs, from the 2026-11-05 content-folders log)
  are **not** added unless config gets a per-unit map. 0035 §4 left that open, and this record does
  not open it again.
- `courses.geology.state`: no edit. Its Geology U02 `Homework` exception stays as the user decided on
  2026-10-15.

### 2d. `shelve-drive-file/SKILL.md` and `librarian.md`

Both **point to** `DRIVE_ARCHITECTURE.md` §2 and restate no folder names. This is how 0035 left them,
and it is kept.

- `SKILL.md` line 3, description: "…into the correct Google Drive location (creating the four
  unit-level content folders when missing; otherwise loose in the parent)…".
- `SKILL.md` lines 24–26, step 3: "If a required unit folder is absent, create it (log first, check
  case-insensitively, never a near-duplicate). Any other absent content folder: file loose in its
  parent. Rules: `DRIVE_ARCHITECTURE.md` §2."
- `SKILL.md` lines 37–39, "Folders": "You may create the four unit-level content folders and a
  missing Unit or Section folder, under `DRIVE_ARCHITECTURE.md` §2 rules 2–3. Nothing else."
- `SKILL.md` line 50: Create row as in §2b §3.
- `librarian.md` lines 33–36: replace "(SHULL-CHG-0035)" with "(SHULL-CHG-0035, as amended by
  SHULL-CHG-0057)".
- `librarian.md` line 43: "**Never a content folder.**" becomes "Content folders: only the four
  unit-level folders, when missing."
- `librarian.md` lines 72–73 and 81–83: "or the parent the file goes loose in" stays, for files with
  no matching folder (labs, reviews).

### 2e. Existing units: retrofit, only if §5 Q4 says so

**Not part of approving this record.** If Matt wants existing units retrofitted, the Librarian first
walks each in-scope unit read-only and writes a move plan to `reports/drive-operations/`. The plan
lists every folder to create, every file to reparent (ID, name, prior parent, new parent), and every
old folder that would be left empty. **Moves are reparents by `update_file`, IDs kept. No file is
trashed. Empty old folders are left in place** unless he separately approves trashing them. The plan
needs his own approval before any mutation.

### 2f. The three records

0029, 0030 and 0035 are **not edited**. History is appended, never rewritten. Optional, his choice:
a one-line pointer at the top of each, "Superseded in part by SHULL-CHG-0057", as was done for the
renumbering banners. `change-log/CHANGELOG.md` gets a row naming 0029, 0030 and 0035 as partly
superseded. That row belongs to the main session.

---

## 3. Supersedes — and the conflicts

> **CONFLICT, not resolved here.** This record reverses parts of two in-force rules. SHULL-CHG-0035
> is APPROVED and was decided by Matt on 2026-10-15. Its reading of his 2026-09-23 words was "Units
> without the unit-level folders stay without them" and "do not need breakdown within each folder".
> SHULL-CHG-0030 is IMPLEMENTED and puts unit tests in `Quiz`. His 2026-11-05 words point the other
> way. The newer instruction is the likely intent (CLAUDE.md §2, precedence 1 and 5), but the
> Secretary does not pick a side. **He decides, through §5.**

| Rule | Status | What 0057 does to it |
|---|---|---|
| 0005: root, `_Brand/`, Unit/Section grammar, hyphen separators | APPROVED, LOCKED | **Kept** |
| 0029: separate unit-level `Guided Notes` and `Presentations` | IMPLEMENTED | **Superseded.** Merged into one folder, `Presentations + Guided Notes` |
| 0030: unit-level `Quiz` holds quizzes **and unit tests** | IMPLEMENTED | **Superseded in part.** `Quiz` kept; unit tests move to `Test` (§5 Q1) |
| 0030: "Never create 'Tests' or 'Tests-Quizizz' beside 'Quiz'" | IMPLEMENTED | **Superseded in part.** `Test` sits beside `Quiz` by design. `Tests-Quizizz` stays prohibited |
| 0030: no `Homework` folder; practice files loose in the section | IMPLEMENTED | **Superseded or kept, depending on §5 Q2.** No folder named `Homework` is created either way |
| 0030: `Labs-Case Studies-Projects` the only section folder | IMPLEMENTED | **Kept by default** (§5 Q3) |
| 0035: the system never creates a content folder | APPROVED | **Superseded for the four unit names only.** Kept for everything else |
| 0035: "Units without the unit-level folders stay without them" | APPROVED | **Superseded** for units in §5 Q4 scope |
| 0035 decision D: Unit and Section folders may be created | APPROVED | **Kept** |

**Already done on Drive, outside this record (2026-11-05):** U04's four folders (Matt, by hand), U05's
four (main session, on his instruction), and four files reparented into U04 / `Presentations + Guided
Notes`. All logged. Approving or rejecting 0057 does not undo or ratify those operations; they stand
on his direct instruction.

---

## 4. What each file would have to change

| # | File | Change on implementation |
|---|---|---|
| 1 | `standards/DRIVE_ARCHITECTURE.md` | Header lines 3–14 (append 0057). §1 tree lines 30–38 and note 40–41. Grammar lines 50–64. What goes where lines 66–79. §2 rules 2–3 lines 84–88. §3 Create row line 100. Per §2b |
| 2 | `config/drive.json` | `$comment`; `folderGrammar.recognisedUnitFolders` (rename or flag); `contentFolderRule` (drop "never create 'Tests' beside 'Quiz'"); `homeworkFiling`; `operations.createFolder`. Per §2c |
| 3 | `.claude/skills/shelve-drive-file/SKILL.md` | Lines 3, 24–26, 37–39, 50. Per §2d |
| 4 | `.claude/agents/librarian.md` | Lines 33–36, 43. Lines 72–73 and 81–83 checked, likely unchanged. Per §2d |
| 5 | `.claude/skills/retrieve-drive-file/SKILL.md` | Line 23, "Search the section's content folder first, then the whole unit": reorder to unit content folder first, then section, then course. Line 15 walk unchanged |
| 6 | `README.md:71` | Drive row: "filed into the folders you made; … the system creates no content folder" becomes a pointer to `DRIVE_ARCHITECTURE.md` with no restated rule |
| 7 | `governance/proposals/SHULL-CHG-0029`, `-0030`, `-0035` | **No edit to their fields.** Optional one-line pointer banner (§2f) |
| 8 | `change-log/CHANGELOG.md` | Row for 0057, naming 0029, 0030, 0035 as partly superseded. Main session |
| 9 | `courses/*/DECISIONS.md` | **None** if all three courses (it is a standard). If Chemistry only (§5 Q4), the rule goes here instead, and items 1–6 change much less |

**Checked and not changed:** `standards/NAMING.md` (types already cover these names; folder names are
not restated). `scripts/validate_schemas.py:19` uses `.../Guided Notes/` as a test-fixture path only,
not a rule. `courses/physics/DECISIONS.md:207` is a dated history note about Physics S01.1 folders
and is not edited.

Items 3, 4 and 5 are under `.claude/`. As 0035 noted, the user may need to approve those tool calls
himself when prompted.

---

## 5. For Matt — open questions (not decided here)

Asked one at a time. Q1, Q2 and Q4 change the rule text. The others have defaults.

| # | Question | Default if unanswered | Why it matters |
|---|---|---|---|
| **1** | **SHULL-CHG-0030 put unit tests inside `Quiz`. This splits them into `Test`. Confirm: unit tests (Day 1 / Day 2, A–D, keys) go in `Test`, and `Quiz` keeps quizzes, exit tickets, bell ringers and quiz banks?** | None. Needs an answer | Reverses part of an IMPLEMENTED rule |
| **2** | **0030 says practice and homework files go loose in the Section folder, with no Homework folder. Does `Worksheets` replace that, so every worksheet goes to the unit's `Worksheets`? Or do section folders still hold section-level worksheets, with `Worksheets` only for unit-wide ones?** | None. Needs an answer | Decides the `homeworkFiling` key and the tree |
| 3 | Do `Section ##.#` folders and the per-section `Labs-Case Studies-Projects` folder stay as they are? Where do labs go? | Sections and `Labs-Case Studies-Projects` unchanged; labs go there if present, else loose in the section | Labs are not in his four |
| **4** | **Scope: all three courses (Chemistry, Physics, Geology), or Chemistry only? And should existing units be retrofitted (a Librarian move plan, logged reparents, no files trashed, his approval first), or only new units going forward?** | None. Needs an answer | Decides whether this is a standard or a Chemistry course decision, and how much Drive work follows |
| 5 | Exact spelling. He typed "Quiz's", but the folder he made is `Quiz`; this record uses the Drive names. `Presentations + Guided Notes` contains a "+". Keep the names exactly as on Drive? | Drive names, as he made them in U04, including the "+" | The "+" is legal in Drive and has caused no failure in the U04/U05 operations. A search by name needs it quoted exactly |
| 6 | Units that already have `Guided Notes`, `Presentations`, `Quiz` or older folders (CHEM U00, U01; PHYS U01, U02; GEO U01, U02, U04, per 0035 §4a and `config/drive.json`): merge their contents into the new four, or leave them? | Leave them. Report them; create the missing new folders beside them only if Q4 says retrofit | Creating `Presentations + Guided Notes` beside `Presentations` and `Guided Notes` splits a unit across two places, the defect CLAUDE.md §1 names |

---

## 6. Rollback

- **Repository.** Implementation is one commit carrying `SHULL-CHG-0057`. `git revert <sha>` restores
  0035's rule exactly. 0029, 0030 and 0035 are not edited, so nothing in them needs restoring.
- **Folders the system creates under this rule.** Each creation is logged before it happens. To roll
  back, first move any files out (reparent to the logged prior parent), then the empty folder may be
  **trashed with the user's approval**. Trash is recoverable; nothing is permanently deleted.
- **Retrofit moves (if approved under §5 Q4).** Every move is an `update_file` reparent with the ID
  kept and the prior parent logged. Rollback is reparenting each file back to its logged prior
  parent. Links survive. Never copy-and-trash.
- **The 2026-11-05 U04/U05 operations** are outside this record and are not rolled back by rejecting
  it. If Matt wants them undone, the logs hold every ID and prior parent: the four files go back to
  the U04 root `1kc9YcPBNIev4ibE5_B0oFic99XxahqAC`. The U05 folders could be trashed only with his
  approval. The U04 folders are his own.

---

## 7. Implementation plan and checks — only after APPROVED, with §5 Q1, Q2 and Q4 answered

**Nothing is edited now.**

1. Edit files 1–6 in §4 per §2b–§2d, with the §5 answers applied. One commit, `SHULL-CHG-0057` in the
   message.
2. Main session: CHANGELOG row (§4 item 8).
3. No Drive mutation is part of this commit. Any retrofit is a separate, logged, approved Librarian
   plan (§2e).

Checks:

- [ ] `json.load` of `config/drive.json` succeeds
- [ ] `validate_layers`, `validate_references`, `validate_agents`, `validate_schemas`,
      `validate_codes.py` pass, counts unchanged
- [ ] Grep (outside `legacy/`, `docs/`, `reports/`, `governance/proposals/`): no live text says
      "never creates a content folder" without the 0057 exception; no live "beside 'Quiz'" clause
      prohibits `Test`; no live rule still lists `Guided Notes` and `Presentations` as separate unit
      folders
- [ ] `librarian.md` and both Drive skills point to `DRIVE_ARCHITECTURE.md` §2 and restate none of the
      four names
- [ ] Dry run, read-only: the Librarian resolves the destination for one of each type (deck, quiz,
      unit test, worksheet) in CHEM U04 and lands on the existing four folders, creating nothing
- [ ] Dry run, read-only: for a unit in scope without the folders, the Librarian's plan says "create
      four", lists the case-insensitive check, and logs before creating
- [ ] `legacy/` and `docs/` untouched; 0029, 0030, 0035 fields untouched
- [ ] `Implemented By` and `Verified` filled in here
