# SHULL-CHG-0023 — Guided Notes and Presentations move to the Unit level

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0023 |
| **Date** | 2026-09-16 |
| **Source** | User — Matt's direct instruction, live conversation, 2026-09-16 |
| **Current Rule** | `standards/DRIVE_ARCHITECTURE.md` §1 — every `Section ##.# - Name` folder gets exactly five content folders: `Homework`, `Presentations`, `Guided Notes`, `Tests-Quizizz`, `Labs-Case Studies-Projects`. Same list restated in `config/drive.json` → `folderGrammar.contentFolders` (five items) and `folderGrammar.contentFolderRule`. Locked under **SHULL-CHG-0005** ("the structure stays exactly as built"). |
| **Proposed Rule** | Two of the five move up one level. Each **Unit** folder (`Unit ## - Unit Name`) gets exactly two folders directly inside it, as siblings of its Section folders: `Guided Notes` and `Presentations`. Each **Section** folder (`Section ##.# - Section Name`) keeps exactly three: `Homework`, `Tests-Quizizz`, `Labs-Case Studies-Projects`. Spelling and relative order are unchanged — this re-levels two of the five, it does not rename or add a folder. |
| **Supersedes** | `standards/DRIVE_ARCHITECTURE.md` §1 (folder tree diagram and the "five content folders" grammar rule) and `config/drive.json` → `folderGrammar.contentFolders` / `contentFolderRule`, both previously locked by **SHULL-CHG-0005**. This record is the one that makes that supersession visible; SHULL-CHG-0005 itself is not deleted or rewritten. |
| **Reason** | Matt's stated rationale: Guided Notes and Presentations are unit-wide materials. A single slide deck or guided-notes packet typically spans an entire unit, not one section, so filing an empty (or duplicated) `Guided Notes` and `Presentations` folder into every section misrepresents their actual scope and invites the same document, or fragments of it, being duplicated across several section folders — the exact defect the one rule in `CLAUDE.md` §1 exists to prevent. |
| **Affected Agents** | Librarian (folder creation/routing), Secretary (this record), Auditor, Janitor (future sweeps for stray section-level `Guided Notes`/`Presentations` folders) |
| **Affected Skills** | None yet built — Phase 7 of 14, standards/agents/skills for routing do not exist yet per `CLAUDE.md`. This record is the standard any future folder-routing skill must build against. |
| **Affected Courses** | Chemistry, Physics, Geology — all three. Per `CLAUDE.md`'s own test ("changing it affects all three courses → it belongs in a standard"), this is a standards-level change. No course `DECISIONS.md` is touched; none of the three describes content-folder placement, which is standards-level, not a course fact. |
| **Risk** | **Medium.** Not the edit itself (low) — the timing. `reports/drive-operations/2026-09-16_geo-phys-scaffold.md`, logged the same day as this record, shows the Librarian mid-execution on a **live Drive** scaffold for Geology (54 sections) and Physics (44 sections) built against the **old** five-per-section grammar (`54×5 = 270` and `44×5 = 220` content folders), with no closing RESULTS file yet confirming completion. If that operation completes, or has completed, under the old rule, live Drive and this repository's standard will disagree the moment this record is implemented. **Flagged for the user; not resolved here** — this record only changes the repository's system of record, per the task instruction that a separate Librarian task is handling the live rebuild in parallel. Whether the in-flight scaffold needs to be corrected, redone, or left and reconciled later is the user's call. |
| **Recommendation** | Adopt — already instructed directly by the user in the current conversation, which is top precedence per `CLAUDE.md` §2 and `governance/GOVERNANCE.md` §3. |
| **Decision** | Approved. Matt, direct instruction, live conversation, 2026-09-16. |
| **Status** | **IMPLEMENTED** (repository record only — see "What this does and does not do" below) |
| **Implemented By** | commit — see repository log for the commit carrying `SHULL-CHG-0023` in its message (filled at commit time; this file is written and committed in the same commit) |
| **Verified** | Yes, by diff review: `standards/DRIVE_ARCHITECTURE.md` §1 tree and grammar table updated; `config/drive.json.folderGrammar` split into `unitContentFolders` (2) and `sectionContentFolders` (3) with `$comment` citing this ID; `standards/NAMING.md` checked and requires no edit (it documents document/image code grammar only, points to `DRIVE_ARCHITECTURE.md` for folder names, and never restated the five-folder list — no duplication existed there to fix); `change-log/CHANGELOG.md` carries a new row. **Not verified against live Drive** — that is explicitly out of scope for this record (see Risk, above). |

## What this does and does not do

**Does:** update the repository's standards and config so the *system of record* states the new
rule — two unit-level folders, three section-level folders — going forward, for all three courses.

**Does not:** touch any actual Google Drive folder. Does not touch `courses/*/DECISIONS.md` — none
of the three files describes folder content-folder placement; that fact lives in `standards/`, and
restating it in a course file would itself be the duplication this system exists to prevent. Does
not touch `brand/`. Does not resolve the live-Drive timing conflict flagged in Risk, above — that is
the user's decision, to be made with the Librarian's own report once
`2026-09-16_geo-phys-scaffold-RESULTS.md` (or its equivalent) exists.

## Old vs. new, stated plainly

**Old (SHULL-CHG-0005, locked):**

```
Section ##.# - Section Name/
├── Homework/
├── Presentations/
├── Guided Notes/
├── Tests-Quizizz/
└── Labs-Case Studies-Projects/
```

**New (this record):**

```
Unit ## - Unit Name/
├── Guided Notes/
├── Presentations/
└── Section ##.# - Section Name/
    ├── Homework/
    ├── Tests-Quizizz/
    └── Labs-Case Studies-Projects/
```
