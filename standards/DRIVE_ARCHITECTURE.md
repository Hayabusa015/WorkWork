# Drive Architecture

**Authority:** SHULL-CHG-0005 — the structure stays exactly as built, **except** where superseded.
**Superseded in part by SHULL-CHG-0023** (2026-09-16): Guided Notes and Presentations moved from the
Section level to the Unit level. See `governance/proposals/SHULL-CHG-0023-unit-level-guided-notes-presentations.md`.
**Superseded in part again by SHULL-CHG-0024** (2026-09-16): `Tests-Quizizz` is renamed `Quiz` and
moves from the Section level to the Unit level; `Homework` is removed as a folder at any level —
homework files are filed loose directly inside the Section folder. `Labs-Case Studies-Projects`
is unchanged. See
`governance/proposals/SHULL-CHG-0024-quiz-unit-level-no-homework-folder.md`.
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
        ├── Guided Notes/
        ├── Presentations/
        ├── Quiz/
        └── Section ##.# - Section Name/
            ├── (homework files loose here — no Homework folder)
            └── Labs-Case Studies-Projects/
```

`_Brand/` holds anything used by more than one course — **one copy, not three drifting copies.**

### Grammar

- Units: `Unit ##` zero-padded plus a short title — `Unit 08 - <Unit Name>`
- Sections: `Section ##.#` plus a short title — `Section 08.4 - <Section Name>`
- **Separator is a hyphen-minus, never an en dash.** An en dash creates a near-duplicate folder.
- **Unit-level content folders:** `Guided Notes`, `Presentations`, `Quiz` — **exactly** those three,
  same spelling, same order, siblings of the Section folders, one copy per unit. **Not** duplicated
  into each section. (`Guided Notes` and `Presentations`: **SHULL-CHG-0023**. `Quiz`: **SHULL-CHG-0024**,
  which renamed the old `Tests-Quizizz` and moved it up from the Section level — a unit's quiz bank
  and tests aren't necessarily one per section, the same reasoning as the other two unit-level
  folders.)
- **Section-level content folders:** `Labs-Case Studies-Projects` — the only one. (**SHULL-CHG-0024**,
  superseding the prior three-item section list.)
- **No `Homework` folder exists at any level.** Homework files — practice sets, worksheets,
  take-home work, keys — are filed as loose files directly inside the Section folder itself.
  (**SHULL-CHG-0024**.)
- Section subfolders are created on demand, when first needed.

### What goes where

| Folder | Level | Contents |
|---|---|---|
| Guided Notes | Unit | Cornell and guided packets — student copy **and** filled teacher key. A packet or deck spans a unit, not one section — this is why it lives one level up. |
| Presentations | Unit | Decks built on the slide template, plus exported PDFs. Same reasoning as Guided Notes. |
| Quiz | Unit | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys. Formerly `Tests-Quizizz` at the Section level; renamed and moved up by **SHULL-CHG-0024** for the same reason as Guided Notes and Presentations. |
| Labs-Case Studies-Projects | Section | Lab handouts, case studies, project instructions, rubrics |
| *(no folder — loose in Section)* | Section | Homework: practice sets, worksheets, take-home work, keys. Filed directly in `Section ##.# - Section Name/`, not in a subfolder. **SHULL-CHG-0024.** |

## 2. Routing rules

1. Resolve **Course → Unit → Section → content type before saving.** Not after.
2. **Reuse existing folders exactly**, matching case-insensitively. Never create `Tests` or
   `Tests-Quizizz` beside `Quiz` — `Quiz` is the current name (**SHULL-CHG-0024**); `Tests-Quizizz`
   is the retired one.
3. Create missing Unit and Section folders using the grammar above.
4. **If the unit or section is unclear, ask.** Never default to a misc folder.
5. The code on the document, in the filename, and in the folder path must all agree.
6. **Never copy a template into a course folder.** Course decks reference `_Brand/Templates/`. One
   template, one place to fix it.
7. An image used by two courses moves to `Image Library/Shared/`.

## 3. Librarian authority

| Operation | Permission |
|---|---|
| Read, search, retrieve | Allowed |
| Create | Allowed in authorised teaching locations |
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
