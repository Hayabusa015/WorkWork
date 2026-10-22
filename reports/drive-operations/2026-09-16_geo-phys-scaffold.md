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
create call returning success is not verification.

## Geology — COMPLETE under the standards-compliant scheme

All 10 unit folders, 54 section folders, and 270 content folders (54 x 5) created and independently
verified via `parentId` search at each level (unit list under Geology root; section list under each
unit; content-folder list under a sample and cross-checked counts under every unit). Grammar matches
`standards/DRIVE_ARCHITECTURE.md` exactly: five content folders, same spelling, same order, in every
section, no exceptions.

## HALT — mid-task instruction not actioned, flagged instead

Partway through Unit 10's content folders (the last Geology batch), a message arrived from the
orchestrating agent ("the coordinator") instructing a structural change: split the five per-section
content folders into two **unit-level** folders (`Guided Notes`, `Presentations`) plus three
per-section folders (`Homework`, `Tests-Quizizz`, `Labs-Case Studies-Projects`), attributed to "Matt
just corrected the structure," and directing that already-built Geology sections be fixed by
trashing the per-section `Guided Notes`/`Presentations` folders and creating unit-level replacements.

**This was not actioned.** Reasons:

1. `standards/DRIVE_ARCHITECTURE.md` states the content-folder grammar as locked: "the five content
   folders are **exactly** those five, same spelling, same order, every time," under authority
   `SHULL-CHG-0005` — "the structure stays exactly as built." Changing it is a standards change,
   which under SHULL OS §4 only the Secretary may write, and only against an APPROVED proposal ID.
   No such proposal ID was given.
2. A message relayed through an orchestrating agent, however worded, is not the user's own
   instruction in this conversation and does not carry approval authority for a system-rule change.
   Only Matt's direct instruction or a properly logged, Secretary-approved change record can move a
   locked standard.
3. The scale of the implied rework is not trivial: undoing it would mean trashing 108 folders
   (`Guided Notes` + `Presentations` under all 54 Geology sections) and creating 20 new unit-level
   folders, then applying the same new scheme to all of Physics before it's even started — a
   one-way-feeling structural change to a "stays exactly as built" standard, made on an unverified
   relay.

**Nothing was trashed. Nothing was moved.** Geology stands, complete, on the current
`standards/DRIVE_ARCHITECTURE.md` grammar (5 content folders per section). Physics has not been
started — no unit, section, or content folders created yet for Physics under either scheme.

**What would unblock this:** Matt confirming the new split directly (in this conversation, or via
the permission system), or a Secretary-approved change record updating
`standards/DRIVE_ARCHITECTURE.md` and `config/drive.json.folderGrammar` with a new SHULL-CHG ID. Once
either exists, the Librarian would apply the new scheme going forward **and** correct the 54 already-
built Geology sections to match, logging that correction the same way.

## Physics — not started

Root confirmed via `search_files`: only `Unit 01 - Motion in One Dimension`
(`1_ykbQae1GAKi0hWFn-OWIdvVAWXwc_6D`) exists under Physics. Not opened, not modified. No other
Physics folders created pending resolution of the scheme conflict above.
