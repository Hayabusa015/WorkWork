# Drive Architecture

**Authority:** SHULL-CHG-0005 — the structure stays exactly as built.
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
        └── Section ##.# - Section Name/
            ├── Homework/
            ├── Presentations/
            ├── Guided Notes/
            ├── Tests-Quizizz/
            └── Labs-Case Studies-Projects/
```

`_Brand/` holds anything used by more than one course — **one copy, not three drifting copies.**

### Grammar

- Units: `Unit ##` zero-padded plus a short title — `Unit 08 - <Unit Name>`
- Sections: `Section ##.#` plus a short title — `Section 08.4 - <Section Name>`
- **Separator is a hyphen-minus, never an en dash.** An en dash creates a near-duplicate folder.
- The five content folders are **exactly** those five, same spelling, same order, every time.
- Section subfolders are created on demand, when first needed.

### What goes where

| Folder | Contents |
|---|---|
| Homework | Practice sets, worksheets, take-home work, homework keys |
| Presentations | Decks built on the slide template, plus exported PDFs |
| Guided Notes | Cornell and guided packets — student copy **and** filled teacher key |
| Tests-Quizizz | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys |
| Labs-Case Studies-Projects | Lab handouts, case studies, project instructions, rubrics |

## 2. Routing rules

1. Resolve **Course → Unit → Section → content type before saving.** Not after.
2. **Reuse existing folders exactly**, matching case-insensitively. Never create `Tests` beside
   `Tests-Quizizz`.
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
