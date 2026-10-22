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
    └── Unit ## - Unit Name/
        ├── Guided Notes/                  if the user made it
        ├── Presentations/                 if the user made it
        ├── Quiz/                          if the user made it
        └── Section ##.# - Section Name/
            ├── (homework and activities loose here — no Homework folder)
            └── Labs-Case Studies-Projects/    if the user made it
```

The tree shows the content folders the system **recognises when present**. They are not folders
that must exist.

`_Brand/` holds anything used by more than one course — **one copy, not three drifting copies.**

### Grammar

- Units: `Unit ##` zero-padded plus a short title — `Unit 08 - <Unit Name>`
- Sections: `Section ##.#` plus a short title — `Section 08.4 - <Section Name>`
- **Separator is a hyphen-minus, never an en dash.** An en dash creates a near-duplicate folder.
- **Unit-level content folders recognised:** `Guided Notes`, `Presentations`, `Quiz` — **exactly**
  those three names, same spelling, siblings of the Section folders, one copy per unit. **Not**
  duplicated into each section. Match them case-insensitively. (`Guided Notes` and `Presentations`: **SHULL-CHG-0029**. `Quiz`: **SHULL-CHG-0030**,
  which renamed the old `Tests-Quizizz` and moved it up from the Section level — a unit's quiz bank
  and tests aren't necessarily one per section, the same reasoning as the other two unit-level
  folders.)
- **Section-level content folder recognised:** `Labs-Case Studies-Projects` — the only one. (**SHULL-CHG-0030**,
  superseding the prior three-item section list.)
- **No `Homework` folder exists at any level.** Homework files — practice sets, worksheets,
  take-home work, keys — are filed as loose files directly inside the Section folder itself.
  (**SHULL-CHG-0030**.)
- **The system never creates a content folder** (SHULL-CHG-0035). The user adds those himself, and a
  unit that lacks one stays without it. If the matching folder is not there, the file goes **loose
  in its parent**. This covers content subfolders only: a missing `Section ##.#` folder may still be
  created (§2 rule 3).

### What goes where

Each row names where the document goes **if the folder exists**; otherwise it goes loose in the
parent given in the Level column.

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
2. **Reuse existing folders exactly**, matching case-insensitively. **Never create a content
   folder** (SHULL-CHG-0035). If the matching one does not exist, file loose in the parent. `Quiz` is
   the current name for the unit-level quiz folder (**SHULL-CHG-0030**).
3. Create missing Unit and Section folders using the grammar above. This is the only folder creation
   the system does (SHULL-CHG-0035, decision D: it does not cover content subfolders).
4. **If the unit or section is unclear, ask.** Never default to a misc folder.
5. The code on the document, in the filename, and in the folder path must all agree.
6. **Never copy a template into a course folder.** Course decks reference `_Brand/Templates/`. One
   template, one place to fix it.
7. An image used by two courses moves to `Image Library/Shared/`.

## 3. Librarian authority

| Operation | Permission |
|---|---|
| Read, search, retrieve | Allowed |
| Create | Files: allowed in authorised teaching locations. Folders: `Unit ##` and `Section ##.#` folders only (§2 rule 3). **Never a content folder** (SHULL-CHG-0035). |
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
