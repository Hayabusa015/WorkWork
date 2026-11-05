# SHULL-CHG-0057 — Four unit-level content folders for new units: Quiz, Test, Presentations + Guided Notes, Worksheets

> **ID note.** `SHULL-CHG-0056` is taken on another branch (`overseer-as-subagent-routing-brief`), so
> this record is 0057. The Secretary that drafted it had no shell and could not run
> `git fetch origin main` (`governance/CHANGE_CONTROL.md` §2, "Allocating a new Change ID"). The ID
> came from the main session. Under that rule the ID is not allocated until this file is pushed to
> `origin/main`. The main session must check the fetched `origin/main` before it commits.

> **Answers recorded, 2026-11-05. Not an approval.** Matt answered the open questions in the main
> session. The Secretary did not hear him directly; his words below are as the main session relayed
> them. They are recorded in §5 and applied to §2. **Status stays PENDING.** Answering questions is not
> approving the rule text. The main session asks him for an explicit approval next, and records it
> under `governance/CHANGE_CONTROL.md` §4.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0057 |
| **Date** | 2026-11-05 (drafted); answers to §5 recorded 2026-11-05 |
| **Source** | User, 2026-11-05, in the main session. The Secretary did not hear him directly. His words, as relayed: **(1)** *"I added them but can you just make them for me. Quiz's / Test / Presentations + Guided Notes / Worksheets"*, about the four folders he had made by hand in Chemistry Unit 04, asking for the same set in Unit 05. **(2)** He agreed to *"draft a change proposal making your four folders the standard for every unit"*, then said *"yes draft the proposal"*. **(3)** His answers to the open questions: *"1 yes, 2 Worksheets, 3 all courses, new units only"* (§5). **None of these approves the rule text below.** Evidence: `reports/drive-operations/2026-11-05_chem-u04-u05-content-folders.md` and `reports/drive-operations/2026-11-05_chem-u04-u05-notes-filing.md`. |
| **Current Rule** | See §1. Verbatim, from `standards/DRIVE_ARCHITECTURE.md`, `config/drive.json`, `.claude/skills/shelve-drive-file/SKILL.md`, `.claude/agents/librarian.md`, and records SHULL-CHG-0029, 0030 and 0035. |
| **Proposed Rule** | See §2. **Final text, with his 2026-11-05 answers applied.** It is still the main session's reading of his words, written by the Secretary. Approving this record confirms it. One definition (§2a, "new-layout unit") is the Secretary's mechanical form of the main session's wording; §2a.1 shows both. |
| **Supersedes** | **In part, for new-layout units only (§2a.1), and in conflict (§3):** SHULL-CHG-0035 (APPROVED), its rule that the system never creates a content folder, for these four names in new-layout units. SHULL-CHG-0030 (IMPLEMENTED), the unit-level `Quiz` holding unit tests, its "never create `Tests` beside `Quiz`" clause, and its "homework loose in the Section folder", all for new-layout units. SHULL-CHG-0029 (IMPLEMENTED), the separate unit-level `Guided Notes` and `Presentations` folders, for new-layout units. **Existing (legacy-layout) units keep 0029, 0030 and 0035 unchanged.** Text: `DRIVE_ARCHITECTURE.md` header lines 3–14, §1 tree (lines 30–41), Grammar (lines 50–64), What goes where (lines 66–79), §2 rules 2–3 (lines 84–88), §3 Create row (line 100). `config/drive.json` `$comment`, `folderGrammar.recognisedUnitFolders`, `contentFolderRule`, `homeworkFiling`, `operations.createFolder`. `shelve-drive-file/SKILL.md` lines 3, 24–26, 35–39, 50. `librarian.md` lines 33–36, 43, 72–73, 81–83. |
| **Reason** | (1) Matt has now made, or asked for, the same four unit-level folders in two Chemistry units. That is his layout, and the rule does not describe it. `recognisedUnitFolders` lists `Guided Notes`, `Presentations` and `Quiz`, so the Librarian would not recognise `Test`, `Worksheets` or `Presentations + Guided Notes`. Under SHULL-CHG-0035 it would file the next U04 or U05 worksheet loose in the section, beside a `Worksheets` folder it ignores. (2) The main session created the U05 folders on his direct instruction (CLAUDE.md §2, precedence 1), against SHULL-CHG-0035. That override covered two units only. Without a record, the next session falls back to the old rule and the two units become exceptions nobody wrote down. (3) He asked for it ("making your four folders the standard for every unit") and on 2026-11-05 scoped it: all courses, new units only. |
| **Affected Agents** | Librarian (routing; it classifies each unit's layout, and gains authority to create these four content folders in new-layout units). Auditor and Janitor (they check filing against the rule, per layout; the Janitor's sweep must look for near-duplicates and mixed units). Overseer (fills `reports/filing-queue.md` destinations). Secretary (this record). |
| **Affected Skills** | `shelve-drive-file` (lines 3, 24–26, 35–39, 50). `retrieve-drive-file` (lines 15, 23: "Search the section's content folder first" assumes section-level folders). `naming` is not changed: the types `Quiz`, `Test`, `Slides`, `Guided_Notes`, `Practice_Set`, `Activity`, `Organizer` in `standards/NAMING.md` line 47 already exist. |
| **Affected Courses** | **All three: Chemistry, Physics, Geology** (his answer, §5 Q4). It changes all three courses, so it is a standard under CLAUDE.md §2 (Path B), not a course decision. No `courses/*/DECISIONS.md` edit. |
| **Risk** | **Medium.** It changes routing in all three courses and introduces two layouts that coexist (new and legacy), which the Librarian must tell apart per unit. It reverses part of an APPROVED rule (0035) and an IMPLEMENTED rule (0030) for new units. It gives the Librarian back an authority 0035 removed, for four names only. No retrofit, so no bulk Drive moves. The repository edit is one revertible commit. |
| **Recommendation** | Approve. §5 is fully answered: Q1, Q2 and Q4 in his words, Q3, Q5 and Q6 by the stated defaults, which he did not object to. Before approving, the main session should put two points to him (§2a.1 definition wording; §2a.5 activities and organizers), since both go slightly beyond his literal words. No retrofit is part of this record (§2e). |
| **Decision** | Approved by the user, 2026-11-05: "approve 0057" |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | Secretary, 2026-11-05, against the APPROVED record at commit `113ca6f`. Files: `standards/DRIVE_ARCHITECTURE.md`, `config/drive.json`, `.claude/skills/shelve-drive-file/SKILL.md`, `.claude/skills/retrieve-drive-file/SKILL.md`, `.claude/agents/librarian.md`, `README.md`, and one-line pointer banners at the top of SHULL-CHG-0029, 0030 and 0035 (no field edits). Implementation commit: **`c5e64a0`** ("Implement SHULL-CHG-0057: four unit content folders for new units"; parent `113ca6f`, confirmed in the reflog by the Secretary). |
| **Verified** | **Partly.** Done by the Secretary: grep outside `legacy/`, `docs/`, `reports/`, `governance/proposals/` finds no live "never creates a content folder" without the 0057 exception, no live "beside 'Quiz'" clause unqualified by legacy layout, and the layout test stated only in `DRIVE_ARCHITECTURE.md` §1 Grammar. `librarian.md` and both Drive skills point to it and do not restate it or the four names. `scripts/` reads none of the changed `folderGrammar` keys. Reported by the main session after commit `c5e64a0` (run in its shell, not by the Secretary): `json.load(config/drive.json)` OK, and `folderGrammar.newLayoutUnitFolders` = `['Presentations + Guided Notes', 'Quiz', 'Test', 'Worksheets']`. `validate_agents`, `validate_codes`, `validate_layers`, `validate_notes`, `validate_profiles`, `validate_references`, `validate_schemas` all OK; counts were not reported. `validate_tokens` FAILS, only on `templates/slide/decks/chem_u04_u05/motion_polarity.html` (raw hex). That file comes from an earlier, unrelated commit, not from 0057, and the main session is fixing it separately. **Not yet done:** the three read-only Librarian dry runs in §7. |

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

> **Final text, with Matt's 2026-11-05 answers (§5) applied.** It is still the main session's reading
> of his words, written by the Secretary, and it becomes the rule only when he approves this record.

### 2a. The rule

1. **Two layouts. Each unit folder is one or the other, decided mechanically.** The four new folders
   apply to **new-layout units** only. **Legacy-layout units** keep their current layout, and filing
   into them follows the rule that applied before this record (0029, 0030, 0035, as in §1). Applies in
   all three courses.

   **The test.** Run it on the unit folder before filing anything into it. Read the unit folder's
   direct children and each Section folder's direct children by `parentId` listing. Folder names match
   case-insensitively and otherwise exactly. A file's type is the `Type` word in its name, per
   `standards/NAMING.md` (written with spaces, e.g. `Practice Set`). **First match wins:**

   | Step | If the unit… | Layout |
   |---|---|---|
   | 1 | does not exist yet (it is being created now) | **New** |
   | 2 | has a direct child folder named `Test`, `Worksheets` or `Presentations + Guided Notes` | **New** (CHEM U04 and U05 today) |
   | 3 | has a direct child folder named `Guided Notes`, `Presentations`, `Tests-Quizizz` or `Homework`, or any of its Section folders has a direct child folder named `Tests-Quizizz` or `Homework` | **Legacy** |
   | 4 | holds, anywhere inside it, a file whose type is one that the two layouts file differently: `Slides`, `Guided Notes`, `Quiz`, `Test`, `Practice Set`, `Activity`, `Organizer` | **Legacy** |
   | 5 | holds a file whose type cannot be read from its name, in a place step 4 would care about | **Stop.** Report the file and ask; do not guess |
   | 6 | none of the above (empty, only Section folders, or only labs, rubrics, study guides, reviews, references) | **New** |

   A unit's layout is stable. A new unit gets one of the four folders at its first step-4-type filing,
   and from then on step 2 keeps it new. A legacy unit keeps its legacy files, so step 3 or 4 keeps it
   legacy. Only a separate, approved retrofit (§2e) changes a legacy unit.

   **Mixed unit** (step 2 matches, and a step-3 folder or step-4 file is also present, e.g. a
   `Presentations` folder beside `Worksheets`): it is new-layout. New files go to the four folders.
   The legacy folders and files are **left alone and reported** (§5 Q6), never merged, moved or
   renamed.

   *Definition provenance.* The main session offered this wording on 2026-11-05: "a unit folder that
   has none of the legacy content folders (`Guided Notes`, `Presentations`, `Quiz` as a tests holder)
   and no existing filing under the old layout gets the four folders, created on demand. Existing
   units keep their current layout […]. Chemistry U04 and U05 already have the four folders and count
   as new-layout units." The table above is the Secretary's mechanical form of it. **It differs in
   three places, for Matt to accept or reject on approval:**
   - *"`Quiz` as a tests holder"* cannot be checked by name, because `Quiz` is also one of the new
     four. Step 4 replaces it: any `Quiz` or `Test` file already in the unit makes it legacy, so a
     lone empty `Quiz` folder (which he may have made by hand) does not.
   - *"No existing filing under the old layout"* is read as step 4: only files whose type the two
     layouts route differently count. Without that, a brand-new unit whose first file is a lab
     (filed in the section under both layouts) would flip to legacy, and the four folders would never
     appear.
   - `Tests-Quizizz` and `Homework` (pre-0030 names, still present in some units, e.g. Geology U02's
     `Homework` exception) are added as legacy markers.

2. **In a new-layout unit, the four folders are created on demand**, with exactly these names:
   `Quiz`, `Test`, `Presentations + Guided Notes`, `Worksheets`. A folder is created only when a file
   is about to be filed into it; the four are not created together in advance. They sit beside the
   unit's Section folders, one copy per unit, and are never duplicated into sections. This amends
   SHULL-CHG-0035 for these four names in new-layout units only. No other content folder is ever
   created. 0035's other rules stay: Unit and Section folders may be created, and nothing else. **In a
   legacy-layout unit nothing new is created**; 0035 applies unchanged.
3. **Reuse before create.** Before creating, list the unit folder's children (`parentId` search) and
   match the name case-insensitively. If a match exists, use it. **Never create a near-duplicate**:
   not `Tests` beside `Test`, not `Quizzes` or `Quiz's` beside `Quiz`, not `Worksheet` beside
   `Worksheets`, not `Presentations & Guided Notes` or `Presentations and Guided Notes` beside
   `Presentations + Guided Notes`. A folder that looks like a variant but does not match exactly is
   **reported, not used and not renamed** (§5 Q6).
4. **Folder creation is logged** to `reports/drive-operations/` before it happens (unit folder ID,
   layout-test step that classified the unit, name to create), then verified by `parentId` lookup,
   the same as any other mutation.
5. **Routing in a new-layout unit, by content type:**

| Content | Folder |
|---|---|
| Slides (decks and exported PDFs) and guided notes (student copy, key, PDF) | `Presentations + Guided Notes` |
| Quizzes, exit tickets, bell ringers, quiz banks (+ keys, A–D versions) | `Quiz` |
| Unit tests: Day 1 / Day 2, A–D versions, keys | `Test` (§5 Q1) |
| Worksheets, practice sets, homework, take-home work, activities, organizers (+ keys), for one section or several | `Worksheets` (§5 Q2). Replaces SHULL-CHG-0030's "loose in the Section folder" for new-layout units. Still no folder named `Homework` |
| Labs, case studies, projects, rubrics | Unchanged: `Section ##.#/Labs-Case Studies-Projects/` if present, else loose in the section (§5 Q3) |
| Unit reviews, study guides, `Reference` files, anything with no row above | Unchanged: loose in the unit folder, or loose in the section if single-section, as today |

   **Routing in a legacy-layout unit:** exactly as before this record (§1a "What goes where"). Unit
   tests stay in `Quiz` if present; homework stays loose in the Section folder; no folder is created.

   *Activities and organizers.* His Q2 answer named worksheets, practice sets and homework. The draft
   row he was answering also listed activities and organizers, which 0035 files loose in the section.
   They are kept in `Worksheets` here because they are worksheet-type student work and "loose in the
   section" is the rule Q2 replaced. **Confirm on approval;** if he says otherwise, they stay loose in
   the section and step 4 of the test is unaffected.

6. A file spanning two units is filed once, in the first unit's folder, and not duplicated. (This is
   what was done with the U4–U5 deck and notes. It restates existing practice; it is not new.)

**Not in his list, kept where they go today** (as the caller confirmed): study guides, unit reviews,
reference sheets, rubrics. If he wants study guides in `Test` or `Quiz`, that is his call in a later
record, not an inference.

### 2b. Text for `standards/DRIVE_ARCHITECTURE.md`

- **Header (lines 3–14):** add "**Amended by SHULL-CHG-0057** (2026-11-05): four unit-level content
  folders for new-layout units, created on demand. Supersedes in part 0029, 0030 and 0035, for
  new-layout units only." Leave the existing lines; history is appended.
- **§1 tree (lines 30–38):** two trees, labelled.

```
New-layout unit (SHULL-CHG-0057; layout test in §2)
└── [Course]/                        Chemistry · Physics · Geology
    └── Unit ## - Unit Name/
        ├── Presentations + Guided Notes/      created on demand
        ├── Quiz/                              created on demand
        ├── Test/                              created on demand
        ├── Worksheets/                        created on demand
        └── Section ##.# - Section Name/
            ├── (only files with no unit folder: single-section reviews, references)
            └── Labs-Case Studies-Projects/    if the user made it

Legacy-layout unit (existing units; unchanged)
└── [Course]/
    └── Unit ## - Unit Name/
        ├── Guided Notes/                  if the user made it
        ├── Presentations/                 if the user made it
        ├── Quiz/                          if the user made it
        └── Section ##.# - Section Name/
            ├── (homework and activities loose here — no Homework folder)
            └── Labs-Case Studies-Projects/    if the user made it
```

- **Lines 40–41:** "recognises when present" becomes: in a new-layout unit the four folders are
  created on demand; in a legacy-layout unit folders are recognised when present; the section folder
  is recognised when present in both.
- **Grammar (lines 50–64):** add a bullet stating the layout test (§2a.1 table, verbatim). Add a
  new-layout bullet with the four names and rule 2a.3 (case-insensitive reuse, the named
  near-duplicates). Label the existing unit-level bullet "Legacy-layout units". Label the "No
  `Homework` folder" bullet: homework is loose in the Section in legacy-layout units and in
  `Worksheets` in new-layout units; no `Homework` folder in either. Narrow the "never creates a
  content folder" bullet: "except the four unit-level folders in a new-layout unit (SHULL-CHG-0057)".
- **What goes where (lines 66–79):** add the §2a.5 table as "New-layout units". Keep the existing
  rows, headed "Legacy-layout units".
- **§2 rule 2 (lines 84–86):** "Never create a content folder, **except** the four unit-level folders
  in a new-layout unit, created on demand after a case-insensitive check." Keep "`Quiz` is the
  current name for the unit-level quiz folder" for legacy-layout units.
- **§2 rule 3 (lines 87–88):** "This is the only folder creation" becomes "Together with rule 2's
  four unit folders, this is the only folder creation".
- **§3 Create row (line 100):** "Folders: `Unit ##`, `Section ##.#`, and, in a new-layout unit only,
  the four unit-level content folders (SHULL-CHG-0057). No other content folder."

### 2c. `config/drive.json`

- `folderGrammar.recognisedUnitFolders`: **kept** as `["Guided Notes", "Presentations", "Quiz"]`,
  now meaning legacy-layout units. Add `newLayoutUnitFolders: ["Presentations + Guided Notes",
  "Quiz", "Test", "Worksheets"]` with a one-line pointer to `DRIVE_ARCHITECTURE.md` §1–§2 for the
  layout test. The test itself is **not** restated in config. **Implementer: grep `scripts/` for
  both keys first.** 0035's implementation note says no script reads them; check again on the day.
- `folderGrammar.recognisedSectionFolders`: unchanged.
- `contentFolderRule`: one sentence pointing to `DRIVE_ARCHITECTURE.md` §1–§2 and citing 0057. Narrow
  "Never create 'Tests' or 'Tests-Quizizz' beside 'Quiz'" to legacy-layout units: in a new-layout
  unit `Test` is a sibling of `Quiz` on purpose. `Tests-Quizizz` stays prohibited everywhere. Keep
  the history sentences, or move them to a pointer to 0029, 0030 and 0035.
- `homeworkFiling`: "No Homework folder at any level. Legacy-layout units: homework loose in the
  Section folder (SHULL-CHG-0030). New-layout units: in the unit's `Worksheets` folder
  (SHULL-CHG-0057). Layout test: `DRIVE_ARCHITECTURE.md` §2."
- `operations.createFolder`: "Used for the four unit-level content folders in a new-layout unit
  (SHULL-CHG-0057), on demand, and for a missing Unit or Section folder. Nothing else."
- `$comment`: "SHULL-CHG-0005 as amended by SHULL-CHG-0035 and SHULL-CHG-0057", plus the date.
- Per-unit IDs for CHEM U04 and U05 (eight folder IDs, from the 2026-11-05 content-folders log)
  are **not** added unless config gets a per-unit map. 0035 §4 left that open, and this record does
  not open it again.
- `courses.geology.state`: no edit. Its Geology U02 `Homework` exception stays as the user decided on
  2026-10-15 (that unit is legacy-layout by step 3).

### 2d. `shelve-drive-file/SKILL.md` and `librarian.md`

Both **point to** `DRIVE_ARCHITECTURE.md` §2 and restate no folder names and not the layout test.
This is how 0035 left them, and it is kept.

- `SKILL.md` line 3, description: "…into the correct Google Drive location (in a new-layout unit,
  creating the unit-level content folder on demand; otherwise loose in the parent)…".
- `SKILL.md` lines 24–26, step 3: "Classify the unit's layout (`DRIVE_ARCHITECTURE.md` §2). New
  layout: if the destination unit folder is absent, create it (log first, check
  case-insensitively, never a near-duplicate). Legacy layout, or any other absent content folder:
  file loose in its parent. If the test says stop, report and ask."
- `SKILL.md` lines 37–39, "Folders": "You may create the four unit-level content folders in a
  new-layout unit, and a missing Unit or Section folder, under `DRIVE_ARCHITECTURE.md` §2 rules 2–3.
  Nothing else."
- `SKILL.md` line 50: Create row as in §2b §3.
- `librarian.md` lines 33–36: replace "(SHULL-CHG-0035)" with "(SHULL-CHG-0035, as amended by
  SHULL-CHG-0057)".
- `librarian.md` line 43: "**Never a content folder.**" becomes "Content folders: only the four
  unit-level folders in a new-layout unit, on demand."
- `librarian.md` lines 72–73: add "and the unit's layout" after "content type". Lines 81–83:
  "or the parent the file goes loose in" stays, for files with no matching folder.

### 2e. Existing units: no retrofit

**Matt answered "new units only" (§5 Q4).** No existing unit is retrofitted, and no file in an
existing unit is moved under this record. If he later wants a retrofit, it is a **new record** plus a
Librarian move plan with its own approval: read-only walk, every folder to create and every file to
reparent (ID, name, prior parent, new parent) listed first; moves by `update_file`, IDs kept; nothing
trashed; empty old folders left in place unless he separately approves trashing them.

### 2f. The three records

0029, 0030 and 0035 are **not edited**. History is appended, never rewritten. Optional, his choice:
a one-line pointer at the top of each, "Superseded in part by SHULL-CHG-0057 (new-layout units
only)", as was done for the renumbering banners. `change-log/CHANGELOG.md` gets a row naming 0029,
0030 and 0035 as partly superseded. That row belongs to the main session.

---

## 3. Supersedes — and the conflicts

> **CONFLICT, still open until approval.** This record reverses parts of two in-force rules, for
> new-layout units. SHULL-CHG-0035 is APPROVED and was decided by Matt on 2026-10-15. Its reading of
> his 2026-09-23 words was "Units without the unit-level folders stay without them" and "do not need
> breakdown within each folder". SHULL-CHG-0030 is IMPLEMENTED and puts unit tests in `Quiz` and
> homework loose in the section. His 2026-11-05 answers (§5) point the other way for new units and
> leave existing units under the old rules. The Secretary records his answers and does not resolve
> the conflict; **his approval of this record does.**

| Rule | Status | What 0057 does to it |
|---|---|---|
| 0005: root, `_Brand/`, Unit/Section grammar, hyphen separators | APPROVED, LOCKED | **Kept** |
| 0029: separate unit-level `Guided Notes` and `Presentations` | IMPLEMENTED | **Superseded for new-layout units** (one folder, `Presentations + Guided Notes`). Kept for legacy-layout units |
| 0030: unit-level `Quiz` holds quizzes **and unit tests** | IMPLEMENTED | **Superseded in part for new-layout units:** `Quiz` kept, unit tests go to `Test` (§5 Q1). Kept for legacy-layout units |
| 0030: "Never create 'Tests' or 'Tests-Quizizz' beside 'Quiz'" | IMPLEMENTED | **Superseded in part:** `Test` sits beside `Quiz` by design in new-layout units. `Tests-Quizizz` stays prohibited everywhere |
| 0030: no `Homework` folder; practice files loose in the section | IMPLEMENTED | **Superseded for new-layout units:** practice and homework go to `Worksheets` (§5 Q2). Kept for legacy-layout units. No folder named `Homework` anywhere |
| 0030: `Labs-Case Studies-Projects` the only section folder | IMPLEMENTED | **Kept** (§5 Q3) |
| 0035: the system never creates a content folder | APPROVED | **Superseded for the four unit names in new-layout units only.** Kept for everything else |
| 0035: "Units without the unit-level folders stay without them" | APPROVED | **Kept for existing (legacy-layout) units.** Superseded for new-layout units |
| 0035 decision D: Unit and Section folders may be created | APPROVED | **Kept** |

**Already done on Drive, outside this record (2026-11-05):** U04's four folders (Matt, by hand), U05's
four (main session, on his instruction), and four files reparented into U04 / `Presentations + Guided
Notes`. All logged. Approving or rejecting 0057 does not undo or ratify those operations; they stand
on his direct instruction. Under §2a.1 both units are new-layout by step 2.

---

## 4. What each file would have to change

| # | File | Change on implementation |
|---|---|---|
| 1 | `standards/DRIVE_ARCHITECTURE.md` | Header lines 3–14 (append 0057). §1 tree lines 30–38 (two labelled trees) and note 40–41. Grammar lines 50–64 (layout test, new-layout bullet). What goes where lines 66–79 (two tables). §2 rules 2–3 lines 84–88. §3 Create row line 100. Per §2b |
| 2 | `config/drive.json` | `$comment`; `folderGrammar.newLayoutUnitFolders` (new key; `recognisedUnitFolders` kept); `contentFolderRule`; `homeworkFiling`; `operations.createFolder`. Per §2c |
| 3 | `.claude/skills/shelve-drive-file/SKILL.md` | Lines 3, 24–26, 37–39, 50. Per §2d |
| 4 | `.claude/agents/librarian.md` | Lines 33–36, 43, 72–73. Lines 81–83 checked, likely unchanged. Per §2d |
| 5 | `.claude/skills/retrieve-drive-file/SKILL.md` | Line 23, "Search the section's content folder first, then the whole unit": search the whole unit (unit content folders and sections), then course. Works for both layouts. Line 15 walk unchanged |
| 6 | `README.md:71` | Drive row: "filed into the folders you made; … the system creates no content folder" becomes a pointer to `DRIVE_ARCHITECTURE.md` with no restated rule |
| 7 | `governance/proposals/SHULL-CHG-0029`, `-0030`, `-0035` | **No edit to their fields.** Optional one-line pointer banner (§2f) |
| 8 | `change-log/CHANGELOG.md` | Row for 0057, naming 0029, 0030, 0035 as partly superseded. Main session |
| 9 | `courses/*/DECISIONS.md` | **None.** All three courses, so it is a standard |

**Checked and not changed:** `standards/NAMING.md` (types already cover these names; folder names are
not restated). `scripts/validate_schemas.py:19` uses `.../Guided Notes/` as a test-fixture path only,
not a rule. `courses/physics/DECISIONS.md:207` is a dated history note about Physics S01.1 folders
and is not edited.

Items 3, 4 and 5 are under `.claude/`. As 0035 noted, the user may need to approve those tool calls
himself when prompted.

---

## 5. Matt's answers, 2026-11-05

**His words**, in the main session, 2026-11-05, as relayed to the Secretary: *"1 yes, 2 Worksheets, 3
all courses, new units only"*. He was also told that the remaining questions take this record's
defaults unless he says otherwise, and he said nothing against them.

**Numbering.** The main session put the questions to him in a different order from the draft of this
table. His "3" is this table's **Q4** (scope). This table's Q3, Q5 and Q6 were the defaults he was told
about. The questions he was shown are quoted in each row.

| # | Question (draft text) | As put to him | Answer, 2026-11-05 | Effect |
|---|---|---|---|---|
| **1** | SHULL-CHG-0030 put unit tests inside `Quiz`. This splits them into `Test`. Confirm: unit tests (Day 1 / Day 2, A–D, keys) go in `Test`, and `Quiz` keeps quizzes, exit tickets, bell ringers and quiz banks? | "Should unit tests move from Quiz to Test from now on?" (his Q1) | **"yes"** (his words, *"1 yes"*) | Unit tests → `Test` in new-layout units (§2a.5) |
| **2** | 0030 says practice and homework files go loose in the Section folder, with no Homework folder. Does `Worksheets` replace that? Or do section folders still hold section-level worksheets? | "Should practice sets and homework go in the unit's Worksheets folder instead of loose in each section folder?" (his Q2) | **"Worksheets"** (his words, *"2 Worksheets"*) | Worksheets, practice sets, homework → unit `Worksheets`, replacing 0030's "loose in the Section folder" for new-layout units (§2a.5) |
| 3 | Do `Section ##.#` folders and the per-section `Labs-Case Studies-Projects` folder stay as they are? Where do labs go? | Not asked; he was told it takes the default | **Default, no objection.** No words of his on this point | Section folders and `Labs-Case Studies-Projects` unchanged; labs there if present, else loose in the section |
| **4** | Scope: all three courses, or Chemistry only? Existing units retrofitted, or only new units going forward? | "Chemistry only, or Physics and Geology too? Existing units get the new folders and their files moved, or only new units?" (his Q3) | **"all courses, new units only"** (his words, *"3 all courses, new units only"*) | A standard, all three courses. No retrofit (§2e). "New units" defined mechanically in §2a.1 |
| 5 | Exact spelling: keep the Drive names (`Quiz`, not "Quiz's"; `Presentations + Guided Notes` with the "+")? | Not asked; he was told it takes the default | **Default, no objection.** No words of his on this point | Names exactly as on Drive in U04, including the "+" |
| 6 | Units that already have `Guided Notes`, `Presentations`, `Quiz` or older folders: merge their contents into the new four, or leave them? | Not asked; he was told it takes the default | **Default, no objection.** No words of his on this point | Left alone and reported, never merged. Under "new units only" those units are legacy-layout and get no new folders at all; a mixed unit (§2a.1) is reported |

**Q3, Q5 and Q6 rest on silence after being told the default.** That is enough to settle open
questions in a draft. It is not approval. The approval the main session asks for next covers the
whole of §2, defaults included.

**Two points for the approval message** (both go slightly past his literal words; neither blocks):
1. The mechanical "new unit" test in §2a.1, and its three differences from the main session's wording.
2. Activities and organizers in `Worksheets` (§2a.5).

---

## 6. Rollback

- **Repository.** Implementation is one commit carrying `SHULL-CHG-0057`. `git revert <sha>` restores
  0035's rule exactly. 0029, 0030 and 0035 are not edited, so nothing in them needs restoring.
- **Folders the system creates under this rule.** Each creation is logged before it happens. To roll
  back, first move any files out (reparent to the logged prior parent, or to where the legacy rule
  would have put them), then the empty folder may be **trashed with the user's approval**. Trash is
  recoverable; nothing is permanently deleted.
- **No retrofit**, so no bulk moves to roll back.
- **The 2026-11-05 U04/U05 operations** are outside this record and are not rolled back by rejecting
  it. If Matt wants them undone, the logs hold every ID and prior parent: the four files go back to
  the U04 root `1kc9YcPBNIev4ibE5_B0oFic99XxahqAC`. The U05 folders could be trashed only with his
  approval. The U04 folders are his own.

---

## 7. Implementation plan and checks — only after APPROVED

**Nothing is edited now.** §5 is answered; approval is still required.

1. Edit files 1–6 in §4 per §2b–§2d. One commit, `SHULL-CHG-0057` in the message.
2. Main session: CHANGELOG row (§4 item 8).
3. No Drive mutation is part of this commit. No retrofit (§2e).

Checks:

- [x] `json.load` of `config/drive.json` succeeds (main session, after `c5e64a0`)
- [x] `validate_layers`, `validate_references`, `validate_agents`, `validate_schemas`,
      `validate_codes.py` pass, counts unchanged (pass per the main session; counts not reported.
      `validate_tokens` fails on an unrelated pre-existing file; see `Verified`)
- [x] Grep (outside `legacy/`, `docs/`, `reports/`, `governance/proposals/`): no live text says
      "never creates a content folder" without the 0057 new-layout exception; no live "beside 'Quiz'"
      clause prohibits `Test` in a new-layout unit; no live text states the layout test outside
      `DRIVE_ARCHITECTURE.md`
- [x] `librarian.md` and both Drive skills point to `DRIVE_ARCHITECTURE.md` §2 and restate neither
      the four names nor the layout test
- [ ] Dry run, read-only: the Librarian classifies CHEM U04 and U05 as new-layout (step 2), resolves
      one of each type (deck, quiz, unit test, worksheet) to the existing four folders, and creates
      nothing
- [ ] Dry run, read-only: the Librarian classifies one existing unit per course (e.g. CHEM U01,
      PHYS U01, GEO U02) as legacy-layout, names the step, and routes a unit test to `Quiz` (or
      loose) and a practice set loose in the section, creating nothing
- [ ] Dry run, read-only: for a new unit with no folders, the Librarian's plan for a worksheet says
      "create `Worksheets` only", lists the case-insensitive check, and logs before creating
- [x] `legacy/` and `docs/` untouched; 0029, 0030, 0035 fields untouched (Secretary's edits only:
      one banner line each on 0029, 0030, 0035; the commit diff itself not inspected)
- [x] `Implemented By` and `Verified` filled in here
