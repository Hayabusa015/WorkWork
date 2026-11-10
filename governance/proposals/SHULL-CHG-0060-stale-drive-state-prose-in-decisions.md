# SHULL-CHG-0060 — Drive-state and status prose in decisions files restates facts kept elsewhere

> **Pattern repeat.** Same defect as SHULL-CHG-0046, 0047, 0048, 0050, 0051 and 0052 (six small
> records on 2026-10-22): status or "Last updated" prose restating a fact that lives in another file.
> Violates CLAUDE.md section 1 (a fact lives in one place). No conflict with a LOCKED rule (none known).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0060 |
| **Date** | 2026-11-08 |
| **Source** | Janitor finding, weekly sweep 2026-11-08 |
| **Current Rule** | See section 1 (the stale lines). |
| **Proposed Rule** | See section 2. Not adopted until approved. |
| **Supersedes** | The Drive-state sections of `courses/physics/DECISIONS.md` (lines 204-217) and `courses/geology/DECISIONS.md` (lines 227-231), in part; `standards/NAMING.md` lines 112-114 (the restated section count), in part. |
| **Reason** | Each restated fact has gone stale; see section 1. |
| **Affected Agents** | Secretary (edits); Janitor (new validator check). |
| **Affected Skills** | None found this run. |
| **Affected Courses** | Physics, Geology, Chemistry. |
| **Risk** | Low for the prose deletions. Medium for the validator check, which is new tooling. |
| **Recommendation** | Approve the deletions. Treat the standing rule and validator check as separate decisions. |
| **Decision** | Approved by the user via the Secretary's Desk, 2026-11-08T22:43:27.892Z. Still open — Questions for Matt, not answered by the click: (1) Delete the Drive-state sections and point at `config/drive.json`? (2) Make "course DECISIONS files carry no Drive-state prose" a standing rule? (3) Add a validator check that `Last updated` is at or after the newest log date? (4) Is the misfiled-Geology-notes defect still blocking, once Drive is re-checked? Answered in chat 2026-11-08 (Q1): "Yes, delete (Recommended)" |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is deferred: no Drive access this run. Item 6 in section 1 needs a Drive re-check
before the blocking wording is removed.

---

## 1. Current state — evidence

| # | Where | Says | Actual (source) |
|---|---|---|---|
| 1 | `courses/physics/DECISIONS.md` 204-217 | 1 of 11 unit folders exist | `config/drive.json` 28-32: 11 present |
| 2 | `courses/geology/DECISIONS.md` 227-231 | `Geology/` is an empty placeholder | `config/drive.json` 34-37: 10 unit folders, S2.3 filed (`reports/drive-operations/2026-11-04_geo-s02.3-dinosaur-poster-filing.md`) |
| 3 | `courses/geology/DECISIONS.md` Last updated | 2026-09-08 | Newer log entries exist |
| 4 | `courses/physics/DECISIONS.md` Last updated | 2026-09-14 | Newer log entries exist |
| 5 | `courses/chemistry/DECISIONS.md` line 4 | Last updated 2026-10-15 | CONFIRMED entry 2026-10-28 (SHULL-CHG-0054) at line 358 |
| 6 | `standards/DRIVE_ARCHITECTURE.md` 140-141 and `config/drive.json` 65 | Misfiled Geology notes in `_Brand/Templates` are a blocking defect | 2026-09-23 survey F6 (line 24): `GEO_U1_S1.2-S1.4_Guided_Cornell_Notes.docx` is now in Geology U01 Guided Notes. The naming half may still hold (SHULL-CHG-0037). |
| 7 | `standards/NAMING.md` 112-114 | Restates the Geology 54-section count | Belongs in `courses/geology/DECISIONS.md` |

## 2. Proposed Rule (not adopted)

1. Delete the Drive-state sections in rows 1 and 2; point at `config/drive.json`.
2. Standing rule: course `DECISIONS.md` files carry no Drive-state prose.
3. Update the Last updated dates (rows 3-5) to match their newest log entry.
4. Replace the section count in `standards/NAMING.md` with a pointer to the Geology decisions file.
5. After a Drive re-check, correct or remove the blocking wording in row 6, keeping any part that still holds.
6. Janitor validator check: `Last updated` is at or after the newest log date in each decisions file.

## 3. What this does not do

- It does not change any course fact, section code, or Drive object.
- It does not decide the row 6 question without a Drive re-check.
