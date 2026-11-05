# Drive Architecture

**Authority:** SHULL-CHG-0005 — the structure stays exactly as built, **except** where superseded.
**Superseded in part by SHULL-CHG-0029** (2026-09-16): Guided Notes and Presentations moved from the
Section level to the Unit level. See `governance/proposals/SHULL-CHG-0029-unit-level-guided-notes-presentations.md`.
**Superseded in part again by SHULL-CHG-0030** (2026-09-16): `Tests-Quizizz` is renamed `Quiz` and
moves from the Section level to the Unit level; `Homework` is removed as a folder at any level —
homework files are filed loose directly inside the Section folder. `Labs-Case Studies-Projects`
is unchanged. See
`governance/proposals/SHULL-CHG-0030-quiz-unit-level-no-homework-folder.md`.
**Amended by SHULL-CHG-0035** (2026-10-15), which supersedes SHULL-CHG-0005 for the content folders:
the system creates no content folders. The user adds them himself, and the folders named below are
the ones it recognises when present. See
`governance/proposals/SHULL-CHG-0035-drive-unit-folders.md`.
**Amended by SHULL-CHG-0057** (2026-11-05): four unit-level content folders for new-layout units,
created on demand. Supersedes in part 0029, 0030 and 0035, for new-layout units only. See
`governance/proposals/SHULL-CHG-0057-unit-content-folders.md`.
**Folder IDs and operational notes:** `config/drive.json`. This file does not repeat them.
**Google Drive is the canonical location for finished teaching documents.** The repository is
canonical for the system. Claude Projects are working context, never storage.

---

## 1. The tree

```
SHULL Science/
├── _Brand/                          shared; sorts to the top on the underscore
│   ├── Templates/
│   ├── Standards/
│   └── Image Library/
│       ├── Chemistry/  Physics/  Geology/  Shared/
└── [Course]/                        Chemistry · Physics · Geology
    └── Unit ## - Unit Name/         new-layout or legacy-layout (below)
```

Each unit folder is one of two layouts, decided by the layout test in the Grammar below.

```
New-layout unit (SHULL-CHG-0057; layout test in Grammar)
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

In a new-layout unit the four unit-level content folders are **created on demand**, one at a time,
when a file is about to be filed into it. In a legacy-layout unit the content folders are
**recognised when present**; they are not folders that must exist, and none is created. The
section-level `Labs-Case Studies-Projects` folder is recognised when present in both layouts.

`_Brand/` holds anything used by more than one course — **one copy, not three drifting copies.**

### Grammar

- Units: `Unit ##` zero-padded plus a short title — `Unit 08 - <Unit Name>`
- Sections: `Section ##.#` plus a short title — `Section 08.4 - <Section Name>`
- **Separator is a hyphen-minus, never an en dash.** An en dash creates a near-duplicate folder.
- **Layout test (SHULL-CHG-0057). This is the only statement of it; other files point here.** Each
  unit folder is new-layout or legacy-layout, decided mechanically, in all three courses. Run the
  test on the unit folder before filing anything into it. Read the unit folder's direct children and
  each Section folder's direct children by `parentId` listing. Folder names match case-insensitively
  and otherwise exactly. A file's type is the `Type` word in its name, per `standards/NAMING.md`
  (written with spaces, e.g. `Practice Set`). **First match wins:**

  | Step | If the unit… | Layout |
  |---|---|---|
  | 1 | does not exist yet (it is being created now) | **New** |
  | 2 | has a direct child folder named `Test`, `Worksheets` or `Presentations + Guided Notes` | **New** (CHEM U04 and U05 today) |
  | 3 | has a direct child folder named `Guided Notes`, `Presentations`, `Tests-Quizizz` or `Homework`, or any of its Section folders has a direct child folder named `Tests-Quizizz` or `Homework` | **Legacy** |
  | 4 | holds, anywhere inside it, a file whose type is one that the two layouts file differently: `Slides`, `Guided Notes`, `Quiz`, `Test`, `Practice Set`, `Activity`, `Organizer` | **Legacy** |
  | 5 | holds a file whose type cannot be read from its name, in a place step 4 would care about | **Stop.** Report the file and ask; do not guess |
  | 6 | none of the above (empty, only Section folders, or only labs, rubrics, study guides, reviews, references) | **New** |

  A unit's layout is stable. A new unit gets one of the four folders at its first step-4-type
  filing, and from then on step 2 keeps it new. A legacy unit keeps its legacy files, so step 3 or 4
  keeps it legacy. Only a separate, approved retrofit changes a legacy unit; none is part of
  SHULL-CHG-0057.

  **Mixed unit** (step 2 matches, and a step-3 folder or step-4 file is also present, e.g. a
  `Presentations` folder beside `Worksheets`): it is new-layout. New files go to the four folders.
  The legacy folders and files are **left alone and reported**, never merged, moved or renamed.
- **New-layout units — unit-level content folders (SHULL-CHG-0057):** `Presentations + Guided
  Notes`, `Quiz`, `Test`, `Worksheets` — **exactly** those four names, including the `+`. Siblings
  of the Section folders, one copy per unit, never duplicated into sections. Each is created on
  demand, only when a file is about to be filed into it; the four are not created together in
  advance. **Reuse before create:** list the unit folder's children by `parentId` and match the name
  case-insensitively; if a match exists, use it. **Never create a near-duplicate**: not `Tests`
  beside `Test`, not `Quizzes` or `Quiz's` beside `Quiz`, not `Worksheet` beside `Worksheets`, not
  `Presentations & Guided Notes` or `Presentations and Guided Notes` beside `Presentations + Guided
  Notes`. A folder that looks like a variant but does not match exactly is **reported, not used and
  not renamed**. Each creation is logged to `reports/drive-operations/` before it happens (unit
  folder ID, the layout-test step that classified the unit, name to create), then verified by
  `parentId` lookup.
- **Legacy-layout units — unit-level content folders recognised:** `Guided Notes`, `Presentations`, `Quiz` — **exactly**
  those three names, same spelling, siblings of the Section folders, one copy per unit. **Not**
  duplicated into each section. Match them case-insensitively. (`Guided Notes` and `Presentations`: **SHULL-CHG-0029**. `Quiz`: **SHULL-CHG-0030**,
  which renamed the old `Tests-Quizizz` and moved it up from the Section level — a unit's quiz bank
  and tests aren't necessarily one per section, the same reasoning as the other two unit-level
  folders.)
- **Section-level content folder recognised:** `Labs-Case Studies-Projects` — the only one. (**SHULL-CHG-0030**,
  superseding the prior three-item section list.)
- **No `Homework` folder exists at any level, in either layout.** Homework files — practice sets,
  worksheets, take-home work, keys — are filed as loose files directly inside the Section folder
  itself in **legacy-layout units** (**SHULL-CHG-0030**), and in the unit's `Worksheets` folder in
  **new-layout units** (**SHULL-CHG-0057**).
- **The system never creates a content folder** (SHULL-CHG-0035), **except the four unit-level
  folders in a new-layout unit (SHULL-CHG-0057)**. Otherwise the user adds content folders himself,
  and a legacy-layout unit that lacks one stays without it. If the matching folder is not there and
  may not be created, the file goes **loose in its parent**. This covers content subfolders only: a
  missing `Section ##.#` folder may still be created (§2 rule 3).

### What goes where

#### New-layout units (SHULL-CHG-0057)

The four unit-level folders are created on demand (Grammar above). A file spanning two units is
filed once, in the first unit's folder, and not duplicated.

| Content | Folder |
|---|---|
| Slides (decks and exported PDFs) and guided notes (student copy, key, PDF) | `Presentations + Guided Notes` |
| Quizzes, exit tickets, bell ringers, quiz banks (+ keys, A–D versions) | `Quiz` |
| Unit tests: Day 1 / Day 2, A–D versions, keys | `Test` |
| Worksheets, practice sets, homework, take-home work, activities, organizers (+ keys), for one section or several | `Worksheets`. Still no folder named `Homework` |
| Labs, case studies, projects, rubrics | `Section ##.#/Labs-Case Studies-Projects/` if present, else loose in the section |
| Unit reviews, study guides, `Reference` files, anything with no row above | Loose in the unit folder, or loose in the section if single-section |

#### Legacy-layout units

Each row names where the document goes **if the folder exists**; otherwise it goes loose in the
parent given in the Level column. Nothing is created.

| Folder | Level | Contents |
|---|---|---|
| Guided Notes | Unit | Cornell and guided packets — student copy **and** filled teacher key. A packet or deck spans a unit, not one section — this is why it lives one level up. |
| Presentations | Unit | Decks built on the slide template, plus exported PDFs. Same reasoning as Guided Notes. |
| Quiz | Unit | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys. Formerly `Tests-Quizizz` at the Section level; renamed and moved up by **SHULL-CHG-0030** for the same reason as Guided Notes and Presentations. |
| Labs-Case Studies-Projects | Section | Lab handouts, case studies, project instructions, rubrics |
| *(no folder — loose in Section)* | Section | Homework: practice sets, worksheets, take-home work, keys. Filed directly in `Section ##.# - Section Name/`, not in a subfolder. **SHULL-CHG-0030.** |
| *(no folder — loose in Section)* | Section | Activities and any other file for a single section with no matching folder, including `Reference` and `Organizer` files (SHULL-CHG-0035). |
| *(no folder — loose in Unit)* | Unit | Unit reviews, study guides, homework or files spanning several sections, and unit-scope files with no matching folder (SHULL-CHG-0035). |

## 2. Routing rules

1. Resolve **Course → Unit → Section → content type before saving.** Not after.
2. **Classify the unit's layout** (layout test, Grammar above), then **reuse existing folders
   exactly**, matching case-insensitively. **Never create a content folder** (SHULL-CHG-0035),
   **except** the four unit-level folders in a new-layout unit, created on demand after a
   case-insensitive check (SHULL-CHG-0057). If the matching one does not exist and may not be
   created, file loose in the parent. In legacy-layout units, `Quiz` is the current name for the
   unit-level quiz folder (**SHULL-CHG-0030**). If the layout test says stop, report and ask.
3. Create missing Unit and Section folders using the grammar above. Together with rule 2's four unit
   folders, this is the only folder creation the system does (SHULL-CHG-0035, decision D;
   SHULL-CHG-0057).
4. **If the unit or section is unclear, ask.** Never default to a misc folder.
5. The code on the document, in the filename, and in the folder path must all agree.
6. **Never copy a template into a course folder.** Course decks reference `_Brand/Templates/`. One
   template, one place to fix it.
7. An image used by two courses moves to `Image Library/Shared/`.

## 3. Librarian authority

| Operation | Permission |
|---|---|
| Read, search, retrieve | Allowed |
| Create | Files: allowed in authorised teaching locations. Folders: `Unit ##`, `Section ##.#` (§2 rule 3), and, in a new-layout unit only, the four unit-level content folders (§2 rule 2, SHULL-CHG-0057). No other content folder (SHULL-CHG-0035). |
| Rename | Allowed when deterministic — **log the prior name first** |
| Move | **Allowed when deterministic.** `update_file` accepts `parentId` and replaces the existing parent — a true reparent that **preserves the file ID**, so links survive and rollback is exact. Log the prior parent first. |
| Overwrite | Requires explicit workflow authorisation |
| Trash | **Requires user approval.** Recoverable. |
| Permanent delete | **Not possible.** No tool exists. Emptying the trash is the user's action alone. |

> **The Librarian must verify every important file operation, and must never claim a file has been
> shelved until the destination has been independently confirmed** by a `parentId` search.

Every mutation is logged to `reports/drive-operations/` **before** it happens: object ID, prior
name, prior parent. A mutation that was not logged cannot be rolled back.

## 4. Saving markdown

Drive converts uploaded markdown into a Google Doc unless told not to. Use
`disableConversionToGoogleType: true` with `contentMimeType: text/plain`. Verified working — every
`.md` in `_Brand/Standards/` is stored as `text/plain`.

## 5. Moving a file

`update_file` with `fileId` and the new `parentId`. The file ID does not change.

> **Never move by `copy_file` + `trash_file`.** That produces a new ID, breaks every existing link,
> and leaves the original in the trash. The reparent is the only correct move.

Before: log object ID, prior name, **prior parent**. After: verify by `parentId` search on the
destination. Rollback is reparenting back to the logged prior parent.

## 6. Known filing defects

Found during inspection, **not yet corrected** — these are the Librarian's and Janitor's first work
order, and each needs approval before action. The current list is in `config/drive.json` under
`knownDefects`.

The blocking one: a Geology guided-notes `.docx` is sitting in `_Brand/Templates/`, both misfiled
and misnamed.

## 7. Publishing standards to Drive

`scripts/publish_standards.py` renders `standards/` and `brand/` into `_Brand/Standards/` so Claude
Projects can read them. **One direction only.** Projects never write back, and nothing in
`_Brand/Standards/` is authoritative — the repository is.

## 8. When to file

**Authority:** SHULL-CHG-0027. How a file is filed is in section 3 and
`.claude/agents/librarian.md` (SHULL-CHG-0026); this section says *when*.

1. **Iteration never reaches Drive.** Drafts and revisions stay on the session's disk. Drive only
   receives a version the user has approved.
2. **A document is ready when the QA gate has passed.** The Overseer adds one unticked row to
   `reports/filing-queue.md` (document, course, unit, section, spec path, files, status) and
   commits the final spec, so the document can be rebuilt if the session ends first. A document
   that cannot be rebuilt from a spec, for example a hand-edited `.docx`, is flagged as such.
3. **The user approves in either of two ways.** In chat: "file it" for one document, or "file
   everything built this session". Or by ticking the box on its row in the queue. No agent ticks a
   box or files on its own judgement.
4. **On approval the Librarian files the set**: the student file, its separate key where one
   exists, and the print PDF, into the same folder. If a ticked row's file is gone, rebuild it from
   the committed spec and run the QA gate again first.
5. **If the destination is unclear, stop and ask.** Never default to a misc folder, and never leave
   a file in the Upload Inbox without telling the user.
6. **After filing**, the Overseer marks the row Filed with the confirmed Drive path, the file ID
   and the date. A failed step leaves the row Not filed with the reason.
7. **A revision after filing needs a new approval.** The Librarian never overwrites a filed file.
   The revision is filed as `Version N` (`standards/NAMING.md`) unless the user asks to replace
   the old one. Trashing the old one needs the user's approval.
