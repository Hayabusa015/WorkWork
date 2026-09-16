# SHULL-CHG-0024 — Quiz moves to the Unit level; Homework folder eliminated

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0024 |
| **Date** | 2026-09-16 |
| **Source** | User — Matt's direct instruction, live conversation, 2026-09-16, following his own live demonstration in Google Drive (he manually built `Guided Notes`, `Presentations`, `Quiz` inside Physics Unit 01 as an example before instructing the orchestrating session to build this everywhere) |
| **Current Rule** | `standards/DRIVE_ARCHITECTURE.md` §1, as left by **SHULL-CHG-0023**: each **Unit** folder (`Unit ## - Unit Name`) gets exactly two content folders — `Guided Notes`, `Presentations`. Each **Section** folder (`Section ##.# - Section Name`) keeps exactly three — `Homework`, `Tests-Quizizz`, `Labs-Case Studies-Projects`. Same list restated in `config/drive.json` → `folderGrammar.unitContentFolders` (2 items) / `folderGrammar.sectionContentFolders` (3 items) and `folderGrammar.contentFolderRule`. |
| **Proposed Rule** | One more folder moves up, one folder is renamed in the move, and one folder is eliminated entirely. Each **Unit** folder now gets exactly three content folders, as siblings of its Section folders: `Guided Notes`, `Presentations`, `Quiz`. `Quiz` is the renamed, unit-level successor to the old Section-level `Tests-Quizizz` — same contents (quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys), same reasoning as the other two unit-level folders: a unit's quiz bank and tests aren't necessarily one per section. Each **Section** folder now gets exactly one content folder — `Labs-Case Studies-Projects`, unchanged. `Homework` is removed as a folder at **any** level; homework files (worksheets, practice sets, take-home work, keys) are filed as loose files directly inside the Section folder itself. |
| **Supersedes** | `standards/DRIVE_ARCHITECTURE.md` §1 (folder tree diagram, the content-folder grammar rule, and the "What goes where" table) and `config/drive.json` → `folderGrammar.unitContentFolders` / `folderGrammar.sectionContentFolders` / `folderGrammar.contentFolderRule`, as most recently set by **SHULL-CHG-0023**, which itself superseded the **SHULL-CHG-0005**-locked five-per-section structure. Neither SHULL-CHG-0023 nor SHULL-CHG-0005 is deleted or rewritten — this record is what makes the second supersession visible. |
| **Reason** | Matt's stated rationale, and his own live example in Drive: a unit's quiz bank and tests are unit-wide materials in the same way Guided Notes and Presentations are — not naturally one-per-section — so `Tests-Quizizz` (renamed `Quiz`) belongs beside them at the Unit level, not duplicated or fragmented across every Section folder. Separately, a bare `Homework` folder holding a handful of files per section added a folder layer without organizing anything a loose file in the Section folder doesn't already do — Matt's direct instruction: "then in each homework just have the homework, it doesnt need a homework folder." |
| **Affected Agents** | Librarian (folder creation/routing), Secretary (this record), Auditor, Janitor (future sweeps for stray `Tests-Quizizz` or `Homework` folders) |
| **Affected Skills** | None yet built — Phase 7 of 14, standards/agents/skills for routing do not exist yet per `CLAUDE.md`. This record is the standard any future folder-routing skill must build against. |
| **Affected Courses** | Chemistry, Physics, Geology — all three. Per `CLAUDE.md`'s own test ("changing it affects all three courses → it belongs in a standard"), this is a standards-level change. No course `DECISIONS.md` is touched; none of the three describes content-folder placement, which is standards-level, not a course fact. |
| **Risk** | **Low for the repository edit itself; the live-Drive retrofit is separate and unresolved here.** Matt has already hand-built the new structure in Physics Unit 01 as a demonstration, so the intended end state is unambiguous and not a guess. But Chemistry (16 unit folders, built under SHULL-CHG-0005's original five-per-section grammar), the rest of Physics, and Geology (0 unit folders as of the last verified read) still need to be retrofitted or built fresh against this rule — that is a Librarian task, dispatched separately, not performed by this record. This record only updates the repository's system of record; it does not touch any actual Google Drive folder. There is also an open, unresolved timing question logged against SHULL-CHG-0023 (`change-log/CHANGELOG.md`, "Open, not yet a change record", 2026-09-16 row) about a Geology/Physics scaffold built under an even older grammar — this record does not resolve that either. |
| **Recommendation** | Adopt — already instructed directly by the user in the current conversation, and physically demonstrated by the user in live Drive, which is top precedence per `CLAUDE.md` §2 and `governance/GOVERNANCE.md` §3. |
| **Decision** | Approved. Matt, direct instruction, live conversation, 2026-09-16. |
| **Status** | **IMPLEMENTED** (repository record only — see "What this does and does not do" below). The Secretary session that edited these files had no shell/git tool and could not confirm the commit itself; the orchestrating session reviewed the diff and committed on its behalf immediately after. |
| **Implemented By** | Commit `07fc509` on `claude/gracious-galileo-drxzqh`, message citing `SHULL-CHG-0024`. |
| **Verified** | Yes, by diff review at commit time: `standards/DRIVE_ARCHITECTURE.md` §1 tree, grammar rule, "What goes where" table, and routing rule 2 updated to `Quiz` (unit-level) / `Labs-Case Studies-Projects` (section-level, only one) / no `Homework` folder at any level; `config/drive.json` → `folderGrammar.unitContentFolders` (3), `folderGrammar.sectionContentFolders` (1), `contentFolderRule` and new `homeworkFiling` key updated, `$comment` and the Chemistry Unit 00 `knownDefects` entry updated to match, all citing this ID; `standards/NAMING.md` re-checked, no edit needed; `change-log/CHANGELOG.md` carries the new row above SHULL-CHG-0023's, already marked IMPLEMENTED. **Not verified against live Drive** — that is explicitly out of scope for this record (see Risk, above), except Physics Unit 01, which Matt built by hand and is already known to match. Live-Drive retrofit across Geology, the rest of Physics, and Chemistry was separately dispatched to Librarian agents after this commit landed; that work is tracked in `reports/drive-operations/`, not here.|

## What this does and does not do

**Does:** update the repository's standards and config so the *system of record* states the new
rule — three unit-level folders (Guided Notes, Presentations, Quiz), one section-level folder
(Labs-Case Studies-Projects), homework filed loose in the Section folder — going forward, for all
three courses.

**Does not:** touch any actual Google Drive folder. Physics Unit 01 already reflects this structure
because Matt built it there by hand as the example; every other unit in every other course still
needs a Librarian retrofit pass, tracked separately in `reports/drive-operations/`, not here. Does
not touch `courses/*/DECISIONS.md` — none of the three files describes content-folder placement;
that fact lives in `standards/`, and restating it in a course file would itself be the duplication
this system exists to prevent. Does not touch `brand/`. Does not resolve the SHULL-CHG-0023 Drive
timing question already open in `change-log/CHANGELOG.md`.

## Old vs. new, stated plainly

**Old (SHULL-CHG-0023):**

```
Unit ## - Unit Name/
├── Guided Notes/
├── Presentations/
└── Section ##.# - Section Name/
    ├── Homework/
    ├── Tests-Quizizz/
    └── Labs-Case Studies-Projects/
```

**New (this record):**

```
Unit ## - Unit Name/
├── Guided Notes/
├── Presentations/
├── Quiz/
└── Section ##.# - Section Name/
    ├── (homework files loose here — no Homework folder)
    └── Labs-Case Studies-Projects/
```
