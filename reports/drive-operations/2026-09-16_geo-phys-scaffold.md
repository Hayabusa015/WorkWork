# Drive operation log — Geology & Physics full folder scaffold

**Logged:** 2026-09-16 · **Agent:** Librarian
**Task:** Create missing Unit → Section → 5 content-folder scaffold for Geology (full course, empty)
and Physics (9 missing units of 11; Unit 01 already exists and is explicitly out of scope).
**Authorisation:** Matt approved "full scaffold" (Unit + Section + 5 content folders) after scope
confirmation, per task instructions. Live-Drive write task — not gated by Secretary/proposal
workflow (does not touch brand/standards/governance/courses in the repo).
**Chemistry:** explicitly out of scope, not touched.
**Physics Unit 01:** explicitly out of scope, not opened, not modified.

Logged **before** execution per `standards/DRIVE_ARCHITECTURE.md` §3 / SHULL OS §4.

## Prior state (verified against `config/drive.json`, itself verified 2026-09-07)

| Course | Parent ID | Prior state |
|---|---|---|
| Geology | `1lqHHql9cSqOZDGej2ff_121bITWOKZvr` | Empty — 0 unit folders |
| Physics | `1NOjl2nEZ1bjcjm32G55V265uGUoTErlk` | 1 of 11 unit folders — `Unit 01 - Motion in One Dimension` (with existing sections/content — untouched) |

## Intended change

Create, for Geology: 10 unit folders, 54 section folders, 270 content folders (54 x 5).
Create, for Physics: 10 missing unit folders (00, 02–10 — the task brief's "9" undercounts by one
against its own listed units; all 10 listed units are built and this is flagged in the closing
report), their sections (44 total), and content folders (44 x 5 = 220).

Grammar per `standards/DRIVE_ARCHITECTURE.md` / `config/drive.json.folderGrammar`:
- Unit: `Unit ## - Unit Name`, hyphen-minus
- Section: `Section ##.# - Section Name`, hyphen-minus
- Content folders, exact order every time: `Homework`, `Presentations`, `Guided Notes`,
  `Tests-Quizizz`, `Labs-Case Studies-Projects`

Section titles cross-checked against `courses/geology/DECISIONS.md` (10 units, 54 sections,
CONFIRMED SHULL-CHG-0009) and `courses/physics/DECISIONS.md` (Units 0–10, 48 sections, CONFIRMED
SHULL-CHG-0012). Folder titles use the short form given in the task brief where DECISIONS.md
carries a parenthetical elaboration (e.g. brief: "Multi-Body Systems" vs DECISIONS.md "Multi-Body
Systems (Atwood Machines)") — same section, shorter folder label, not a numbering conflict.

## Verification method

Every folder creation is followed by an independent `search_files` (`parentId = '<parent ID>'`)
lookup confirming the created object is present under the intended parent, per the rule that a
create call returning success is not verification. Full results in the closing report,
`2026-09-16_geo-phys-scaffold-RESULTS.md`, once all creates and lookups are complete.
