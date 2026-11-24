# SHULL-CHG-0113 — Renumber the branch-side 0106 and 0107 records to 0111 and 0112

> **ID note.** The Secretary that drafted this record has no shell and could not run
> `git fetch origin main` (`governance/CHANGE_CONTROL.md` §2, "Allocating a new Change ID"). The local
> branch `merge-0110` holds a merge of `origin/main` with `origin/claude/amazing-ritchie-hql8dw`. Its
> highest record is SHULL-CHG-0110, and nothing outside `legacy/` mentions 0111, 0112 or 0113. Under
> §2 none of 0111, 0112 or 0113 is allocated until pushed to `origin/main`. The main session must check
> a freshly fetched `origin/main` before it commits.

> **Why this record exists.** The main session relayed Matt's answer and asked the Secretary to apply
> it. Under `governance/CHANGE_CONTROL.md` §4 item 3 the Secretary acts only on a committed record
> whose `Status:` reads APPROVED and whose `Decision:` quotes Matt. No existing record covers a
> renumber (SHULL-CHG-0110 is the U7 course change; SHULL-CHG-0078 chose "no renumbering" for the
> duplicates that existed on 2026-11-23). This record gives the main session a place to record his
> words. **This record is not the approval.**

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0113 |
| **Date** | 2026-11-24 (drafted) |
| **Source** | User. Merging branch `claude/amazing-ritchie-hql8dw` (the U7 five-section work, SHULL-CHG-0110) into `main`. Matt's answer, as the main session relayed it: *"Merge everything, fix IDs (Recommended)"*. The option text he chose: merge the whole branch to main, and renumber its colliding 0106 and 0107 records to the next free IDs. The Secretary did not hear him directly. |
| **Current Rule** | `governance/CHANGE_CONTROL.md` §2: Change IDs are "Never reused, never guessed." `scripts/validate_change_ids.py` fails on any new reuse of a number; adding to its allow-list "is a governance change and needs its own APPROVED record." After the merge, two numbers each name two different records: `governance/proposals/SHULL-CHG-0106-textbook-page-designer.md` (main, IMPLEMENTED) and `governance/proposals/SHULL-CHG-0106-chem-course-outline-ref-title.md` (branch, IMPLEMENTED); `governance/proposals/SHULL-CHG-0107-textbook-reading-and-tear-off.md` (main, IMPLEMENTED) and `governance/proposals/SHULL-CHG-0107-chem-ohio-standards-list.md` (branch, PENDING). |
| **Proposed Rule** | No rule changes. The main-side records keep 0106 and 0107. The branch-side records are renumbered: `SHULL-CHG-0106-chem-course-outline-ref-title.md` becomes `SHULL-CHG-0111-chem-course-outline-ref-title.md`, and `SHULL-CHG-0107-chem-ohio-standards-list.md` becomes `SHULL-CHG-0112-chem-ohio-standards-list.md`. Every live reference to those two records is updated (§1 inventory). Logs get a bracketed pointer, not a rewrite. The allow-list in `scripts/validate_change_ids.py` is **not** extended. |
| **Supersedes** | The IDs SHULL-CHG-0106 and SHULL-CHG-0107 **as they apply to the two branch-side records only**. Precedent: `docs/CHANGE_ID_RENUMBERING_2026-10-15.md`, and SHULL-CHG-0056 (renumbered from 0054 on 2026-10-28). It does not supersede SHULL-CHG-0078 option 1: that covered the duplicates existing on 2026-11-23, which stay as they are. |
| **Reason** | (1) Matt chose to fix the IDs rather than keep the duplicates. (2) Without the renumber, `scripts/validate_change_ids.py` fails on the merged tree, and the only other fix is an allow-list addition, which needs its own record. (3) Bare-ID citations of 0106/0107 would stay ambiguous, which is the problem SHULL-CHG-0078 describes. |
| **Affected Agents** | Secretary (applies it). Main session (records the decision, commits, pushes). No responsibilities change. |
| **Affected Skills** | None. |
| **Affected Courses** | Chemistry, citation only: one `Status:` line in `courses/chemistry/DECISIONS.md`. No course fact changes. |
| **Risk** | **Low.** The edits are identifier text only. One risk: changing a reference that means the main-side 0106/0107. Inventory §1 classifies each occurrence. Commit subjects made before the renumber cannot change and will still cite the old IDs. |
| **Recommendation** | Approve as written. The main session records Matt's verbatim words already given, if it judges they answer this record. They name the renumber and its targets ("the next free IDs"). |
| **Decision** | 2026-11-24, user, in the main session, answering the question "How should I get the U7 change onto main?" (which named the colliding 0106 and 0107 records): "Merge everything, fix IDs (Recommended)". |
| **Status** | **APPROVED** |
| **Implemented By** | Pending commit. Secretary, 2026-11-24, against this record as APPROVED on disk on `merge-0110` (the main session's recording commit was relayed; the Secretary has no shell and did not check it in git history). Renames by `git mv`, done by the main session. Text edits by the Secretary, as listed in §1, with three changes: the old ID notes in 0111/0112 got a bracketed "[History, kept as written ...]" prefix; 0112's own ID note got "[now SHULL-CHG-0111]" after its citation of 0106; and the Change ID fields read the new ID only (the renumber note carries the old one). |
| **Verified** | |

## 1. Inventory of occurrences (grep `0106\|0107`, repo minus `legacy/`, 2026-11-24)

**Main-side, not touched:**

| File:line | Means |
|---|---|
| `change-log/CHANGELOG.md:33` | main 0107, textbook reading |
| `change-log/CHANGELOG.md:34` | main 0106, textbook page designer |
| `governance/proposals/SHULL-CHG-0106-textbook-page-designer.md:1,5` | main 0106 itself |
| `governance/proposals/SHULL-CHG-0107-textbook-reading-and-tear-off.md:1,5` | main 0107 itself |

**Branch-side, to change:**

| File:line | Edit |
|---|---|
| `governance/proposals/SHULL-CHG-0106-chem-course-outline-ref-title.md` | `git mv` to `SHULL-CHG-0111-chem-course-outline-ref-title.md`. Line 1 title and line 15 Change ID become 0111. Add the renumber note (§2) under the title. Lines 77 and 93 are the planned log text and the planned commit, both now history: leave them, and the note covers them. Lines 3–6 (old ID note) stay as history. |
| `governance/proposals/SHULL-CHG-0107-chem-ohio-standards-list.md` | `git mv` to `SHULL-CHG-0112-chem-ohio-standards-list.md`. Line 1 title and line 15 Change ID become 0112. Add the renumber note. The record is PENDING, so the planned text at line 127 (`Status: CONFIRMED · SHULL-CHG-0107`) and line 179 (commit carrying `SHULL-CHG-0107`) **become 0112**, since they are not yet history. Line 21 cites SHULL-CHG-0106 meaning the Course Outline record (branch-side): becomes `SHULL-CHG-0111`. Lines 3–7 (old ID note) stay as history, plus one bracketed pointer. |
| `change-log/CHANGELOG.md:42` | ID cell becomes `SHULL-CHG-0112`, path becomes the new filename. |
| `change-log/CHANGELOG.md:43` | ID cell becomes `SHULL-CHG-0111`, path becomes the new filename. |
| `change-log/CHANGELOG.md` | New row at the top of 2026-11-24 for this record (SHULL-CHG-0113). |
| `courses/chemistry/DECISIONS.md:487` | `Status: CONFIRMED · SHULL-CHG-0111 (committed as SHULL-CHG-0106; renumbered 2026-11-24, SHULL-CHG-0113)` |
| `templates/unit-roadmap/build_course_outline.py:2` | `(SHULL-CHG-0111)` |
| `templates/unit-roadmap/course_outline.css:1` | `(SHULL-CHG-0111)` |
| `templates/unit-roadmap/README.md:11` | `(SHULL-CHG-0111)` |
| `reports/drive-operations/2026-11-23_chem-reference-folder.md:6` | Log, so append ` [now SHULL-CHG-0111]` after `SHULL-CHG-0106`. |
| `governance/proposals/SHULL-CHG-0108-chem-ice-blue-deep.md:4,6` | ID note, history: append ` [now SHULL-CHG-0112]` after each `SHULL-CHG-0107`. |
| `governance/proposals/SHULL-CHG-0108-chem-ice-blue-deep.md:175` | Branch 0107 (Ohio list, its decision-log entry): becomes `SHULL-CHG-0112`. |
| `governance/proposals/SHULL-CHG-0108-chem-ice-blue-deep.md:245` | Branch 0106 (Course Outline): becomes `SHULL-CHG-0111`. |

`docs/CHANGE_ID_RENUMBERING_2026-10-15.md` is a dated note about an earlier renumber. A row for this
one could go there or in a new dated note; this record is the record, so neither is required.

## 2. Note added to both renamed records

> Originally committed as SHULL-CHG-0106 [0107] on branch claude/amazing-ritchie-hql8dw; renumbered
> 2026-11-24 because the ID collided with a different record merged to main first. Commit messages
> before the renumber still cite the old ID. (SHULL-CHG-0113)

## 3. Verification plan

1. `python3 scripts/validate_change_ids.py`: passes with the allow-list unchanged.
2. `python3 scripts/validate_references.py`: OK (no path points at a removed filename).
3. `scripts/hook-validate.sh`: OK.
4. Grep `0106|0107` (repo minus `legacy/`): only the main-side rows above, the history lines kept
   on purpose, and the renumber notes remain.
