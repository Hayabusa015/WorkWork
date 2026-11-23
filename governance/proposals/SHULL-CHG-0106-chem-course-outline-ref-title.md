# SHULL-CHG-0106 — Chemistry Course Outline: a `REF` short title, filed as a Reference

> **ID note.** The main session supplied 0106. The Secretary that drafted this record had no shell
> and could not run `git fetch origin main` (`governance/CHANGE_CONTROL.md` §2, "Allocating a new
> Change ID"). The local checkout's highest record is SHULL-CHG-0105, and nothing outside `legacy/`
> mentions 0106. Under that rule the ID is not allocated until this file is pushed to `origin/main`.
> The main session must check the fetched `origin/main` again before it commits.

> **No conflict with a LOCKED rule.** This record adds one row to a table. It changes no curriculum
> code, no packet sheet, and no naming grammar. The outline is **not** a thirteenth reference-packet
> sheet (§2).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0106 |
| **Date** | 2026-11-23 (drafted) |
| **Source** | User. Matt chose option (a) in the main session on 2026-11-23. His words, as the main session relayed them: *"a, file it as Reference - Course Outline"*. The Secretary did not hear him directly. **This record is not the approval.** The main session records his decision under `governance/CHANGE_CONTROL.md` §4 once this record exists. The question came from an Overseer routing brief for a one-page Chemistry Course Outline. The brief found no legal course-level name for it: `Roadmap` is unit-level only (`standards/NAMING.md` §2, SHULL-CHG-0100), and a course-level name needs a `REF` row (SHULL-CHG-0069). Option (b), a new course-level Roadmap type, was declined. |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, "Short titles": *"The topic in a filename (`standards/NAMING.md` §2, SHULL-CHG-0041). **At most 20 characters.** … A section or unit with no row here gets no topic in its filename. Never shorten a title automatically; add a row when the user approves one."* The table has thirteen `REF` rows: the twelve packet sheets plus `Full Packet`. It has **no row for a course outline**. `standards/NAMING.md` §2: *"a course-level name always has a topic, so with no `REF` row there is no course-level name (SHULL-CHG-0069)."* So no legal filename exists for the outline today. |
| **Proposed Rule** | Add one row to the "Short titles" table in `courses/chemistry/DECISIONS.md`, after `REF \| Full Packet`: **`\| REF \| Course Outline \|`** (14 characters, within the 20-character limit). Add a dated decision-log entry (§3) stating what the document is and that it is **not** one of the twelve reference-packet sheets and **not** part of `Reference - Full Packet.pdf`. Resulting filename: `Reference - Course Outline.pdf`, filed in Drive `Chemistry/Reference/`. |
| **Supersedes** | **No rule.** This adds a row; it replaces nothing. It does **not** supersede "Reference packet contents" (twelve sheets, SHULL-CHG-0068, as amended by SHULL-CHG-0070) or the 2026-11-06 decision-log entry. Both stand unchanged. |
| **Reason** | (1) Matt asked for a one-page Chemistry Course Outline at the front of the class binder. It lists all 16 units (U0–U15) by phase, with each unit's section list taken from the curriculum map in `courses/chemistry/DECISIONS.md`. It has no dates and no pacing. (2) It spans the whole year, so it is course-level (`standards/NAMING.md` §2). Course-level is allowed only for type `Reference` and needs a `REF` row. Without the row the document cannot be named, and the Overseer must not invent a name. (3) Matt picked this route, (a), over a new course-level Roadmap type, (b). (a) needs no change to the naming standard. |
| **Affected Agents** | Overseer (routes the build; checks the name). Designer (builds the outline). Auditor (QA; checks the filename against the row, and that the outline is kept out of the Full Packet). Librarian (files it to `Chemistry/Reference/`). Secretary (this record and the decisions-file edit). No responsibilities change. No agent file is edited. |
| **Affected Skills** | None edited. Skills that name files read the "Short titles" table; none of them restates it. |
| **Affected Courses** | **Chemistry only.** A course fact, so it belongs in `courses/chemistry/DECISIONS.md` (CLAUDE.md §2). It is filed as a record, as SHULL-CHG-0099 was, because the decisions file changes only against an approved record. Physics and Geology are untouched. |
| **Risk** | **Low.** One table row and one log entry. The one real risk: "Reference packet contents" says *"each file's topic is its `REF` row in 'Short titles'"*. A builder could read every `REF` row as a packet sheet and put the outline into `Reference - Full Packet.pdf`. The decision-log entry rules this out. `REF \| Full Packet` already shows that not every `REF` row is a sheet (§4, open point). |
| **Recommendation** | Approve as written. The approval should cover the row and the decision-log entry only. A clarifying sentence in "Reference packet contents" is a separate question (§4). Leave it out unless Matt names it. |
| **Decision** | Approved by the user, 2026-11-23: "a, file it as Reference - Course Outline" |
| **Status** | **IMPLEMENTED** (commit pending; see Implemented By) |
| **Implemented By** | Secretary, 2026-11-23, against the APPROVED record committed by the main session in `b05a8bb`. That SHA was relayed by the main session; the Secretary has no shell and did not check it in git history. `courses/chemistry/DECISIONS.md`: (i) the §3 row `\| REF \| Course Outline \|` was inserted after `\| REF \| Full Packet \|`; (ii) the §3 decision-log entry was put at the top of the log, with one amendment the main session asked for: after `Chemistry/Reference/` it adds "(folder to be created on Matt's approval)", because the Librarian found on 2026-11-23 that the Drive folder does not exist yet. The amendment states a fact about Drive and adds no rule. Nothing else was edited. **Implementation commit SHA: _pending_.** The main session commits and fills it in here. |
| **Verified** | **Partial**, 2026-11-23, Secretary. (1) Grep: `Course Outline` is in `courses/chemistry/DECISIONS.md` only in the table row (line 419) and the new log entry (lines 423–430). Outside `legacy/` it is otherwise only in this record and `change-log/CHANGELOG.md`, and no standard or skill restates it. (2) "Reference packet contents" still lists twelve sheets and was not edited. (3) **Not run:** `python3 scripts/validate_codes.py` (§6 item 1), because the Secretary has no shell. The main session runs it before committing, records the result here, and then sets the CHANGELOG row to CONFIRMED. |

---

## 1. What the document is

Stated here so the build has one reference point. It is **not** a rule. Content facts come from
`courses/chemistry/DECISIONS.md`, never from this record.

| Property | Value |
|---|---|
| Purpose | One-page Chemistry Course Outline for the front of the class binder |
| Content | All 16 units (U0–U15) grouped by the four phases, each with its section list as the curriculum map gives it. Retired codes (1.4, 3.5, 6.5, 6.6) follow the map as written; the builder does not decide how they appear |
| Excluded | Dates, pacing, calendar, quarter mapping |
| Name | `Reference - Course Outline.pdf` (`standards/NAMING.md` §2, course-level) |
| Drive folder | `Chemistry/Reference/` |
| In the reference packet? | **No.** Not one of the twelve sheets. Not in `Reference - Full Packet.pdf` |

## 2. Relation to the reference packet

The 2026-11-06 decision-log entry (SHULL-CHG-0068) and "Reference packet contents" fix the packet at
**twelve sheets**. Students use the packet on tests. The Course Outline is a binder front page, not
a packet sheet. It shares the `REF` code only because `REF` is the only course-level topic code
`standards/NAMING.md` §2 allows. It does not change the packet's count, order, or contents. It is
never combined into the Full Packet.

## 3. Text to insert on implementation

**(i) "Short titles" table, `courses/chemistry/DECISIONS.md`.** One new row, immediately after
`| REF | Full Packet |`:

```markdown
| REF | Course Outline |
```

**(ii) Decision log, at the top, above the 2026-11-23 "U6 reworked to four sections" entry:**

```markdown
### 2026-11-23 — Course Outline filed as a Reference
A one-page Chemistry Course Outline sits at the front of the class binder. It lists all 16 units by
phase, with each unit's sections from the curriculum map, and has no dates or pacing. It spans the
year, so it is course-level: `Reference - Course Outline.pdf` in `Chemistry/Reference/`
(`standards/NAMING.md` §2), short title `Course Outline` in "Short titles". It is **not** one of the
twelve reference-packet sheets and is not combined into `Reference - Full Packet.pdf`. "Reference
packet contents" and the 2026-11-06 entry are unchanged. Decided by Matt 2026-11-23 ("a, file it as
Reference - Course Outline"), choosing a `REF` title over a new course-level Roadmap type.
Supersedes: None (new short-title row; no rule replaced).
Status: CONFIRMED · SHULL-CHG-0106
```

Nothing else in `courses/chemistry/DECISIONS.md` is edited. The "Last updated" line already reads
2026-11-23; if the implementation date differs, it is updated to match.

## 4. Open point (not part of this record unless Matt names it)

"Reference packet contents" says *"each file's topic is its `REF` row in 'Short titles'"*. One
added sentence there, such as *"Not every `REF` row is a sheet: `Full Packet` and `Course Outline`
are not,"* would close the risk at its source. It would also make that section restate a fact the
decision-log entry already holds. It is outside option (a) as Matt stated it, so it is **not
bundled**. Ask him only if the Auditor flags the ambiguity.

## 5. Rollback

One commit carrying `SHULL-CHG-0106` that touches only `courses/chemistry/DECISIONS.md`.
`git revert <sha>` removes the row and the log entry. No Drive mutation is part of this change. If an
outline has already been filed under this name by then, the Librarian trashes it as a separate
logged operation (`reports/drive-operations/`).

## 6. Verification plan (only after APPROVED and implemented)

1. `python3 scripts/validate_codes.py` passes, with no new warnings. Chemistry's valid-section
   count is unchanged, because a `REF` row is not a section.
2. Grep: `Course Outline` appears in `courses/chemistry/DECISIONS.md` exactly twice, in the table
   row and the log entry, plus this record and `change-log/CHANGELOG.md`. No skill or standard
   restates it.
3. "Reference packet contents" still lists twelve sheets and is byte-identical to before the
   commit.
4. Fill in `Implemented By` (SHA) and `Verified` here. Update the CHANGELOG row's status.
