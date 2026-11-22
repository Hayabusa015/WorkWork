# SHULL-CHG-0079 — Approved records whose status has not moved

Repeat of: SHULL-CHG-0064 (second raise for SHULL-CHG-0034, -0035, -0038, -0039)

> **Aging.** This is not a request to re-approve anything. It changes no existing record's status.
> No conflict with a LOCKED rule (none known).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0079 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` rows 9-12) |
| **Current Rule** | `governance/CHANGE_CONTROL.md` §2: "**`Verified:`** — **a change is not done until it has been checked.** APPROVED is not IMPLEMENTED, and IMPLEMENTED is not verified." |
| **Proposed Rule** | For each record below: backfill `Implemented By`, run its verification, then move Status to IMPLEMENTED (or keep it APPROVED with a note saying what remains); or Matt defers it. |
| **Supersedes** | Nothing. |
| **Reason** | 19 APPROVED records are open. Nine are implemented with blank or false notes. Two are partly implemented. Four have no implementing commit after 14 days. Four were already raised by SHULL-CHG-0064, which was approved on 2026-11-08 to finish them; none has moved in 14 days. |
| **Affected Agents** | Secretary (backfill), Auditor (verification), main session (asks the open questions). |
| **Affected Skills** | None. |
| **Affected Courses** | Chemistry, Physics, Geology (per record). |
| **Risk** | Medium. The record says "not committed" where commits exist, so it misstates the audit trail. |
| **Recommendation** | Backfill the A and B rows in one Secretary pass. Ask Matt about C and D. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

SHAs below are as the Janitor reported them. The Secretary did not re-check them against `git log`
this run.

## A. Implemented, Status never advanced (row 9)

| Record | Implementing commit(s) | Note on record |
|---|---|---|
| SHULL-CHG-0066-study-guide-unit-span | e6fa5c7 | blank |
| SHULL-CHG-0068-physics-u3-six-sections | f716dcf | "SHA … pending, add it here" |
| SHULL-CHG-0069-notes-no-inline-blanks | 18d3d46 | blank |
| SHULL-CHG-0070-physics-sum-of-forces-notation | f716dcf | blank |
| SHULL-CHG-0071 | f9d9f41, d3edc84, 2aa8251 | banner says "CHANGELOG has no row yet"; row exists (line 44) |
| SHULL-CHG-0072 | d1cad19 | says "not committed", which is false |
| SHULL-CHG-0073 | 258a32f | says "did not commit", which is false |
| SHULL-CHG-0058 | 84d4eb1 | blank |
| SHULL-CHG-0059 | 38de3fe | blank |

## B. Partly implemented (row 10)

| Record | Commit(s) | Remaining |
|---|---|---|
| SHULL-CHG-0060 | b4e5110 (item 3), f92c179 (item 4) | Open questions to Matt unanswered |
| SHULL-CHG-0061 | f92c179 (NAMING example) | Open questions to Matt unanswered |

## C. Approved 2026-11-08, no implementing commit (row 11, first age flag)

SHULL-CHG-0062, -0063, -0064, -0065. (0065 has its own follow-ups in SHULL-CHG-0082 and -0083.)

## D. Second raise (row 12)

| Record | APPROVED since | State |
|---|---|---|
| SHULL-CHG-0034 | 2026-09-23 | Unchanged since SHULL-CHG-0064 |
| SHULL-CHG-0038 | 2026-09-23 | Unchanged |
| SHULL-CHG-0039 | 2026-09-28 | Likely already shipped (per SHULL-CHG-0064) |
| SHULL-CHG-0035 | 2026-10-15 | Item (a) needs Drive; not checked this run |

## Open question

1. For D: finish SHULL-CHG-0034 and -0038 now, or defer them? This repeats SHULL-CHG-0064's
   unanswered question 1.

## Researcher corroboration (2026-W47)

The Researcher reported the same aging independently (`reports/2026-W47/researcher.md` row 8). It
adds these specifics for part B, confirmed by grep on 2026-11-22:

- **SHULL-CHG-0061's chosen fix ("Mark it 'retired'") is not applied.** `courses/chemistry/DECISIONS.md`
  Short titles (line 403) still reads `| 1.4 | Isotopes |`, with no "retired".
- **SHULL-CHG-0060 (remove stale Drive-state prose) is not applied.**
  - `courses/physics/DECISIONS.md` "Drive status" (line 235) still says `Physics/` holds "**1 of 11**"
    unit folders. That contradicts the same file's 2026-11-11 log: "Drive still holds seven U3
    section folders".
  - `courses/geology/DECISIONS.md` (line 229) still says "`Geology/` is an empty placeholder".
- **Inferred cause (Researcher):** SHAs are not written back after commits. The Secretary has no git
  tool in these sessions, and the main session is not backfilling. Suggested: a one-line step in the
  commit procedure, "write the SHA back into the record", owned by the main session. That would be a
  governance change needing its own approval.
