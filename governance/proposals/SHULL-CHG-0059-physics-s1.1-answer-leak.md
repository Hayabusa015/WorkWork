# SHULL-CHG-0059 — Physics S1.1 student copy prints an answer beside the blanks

> **REPEAT.** Flagged blocking in `reports/2026-09-24_chg0030-notes-headers-audit.md` row 1. Still
> present six weeks later. No conflict with a LOCKED rule (none known).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0059 |
| **Date** | 2026-11-08 |
| **Source** | Auditor finding, weekly sweep 2026-11-08 (repeat of the 2026-09-24 audit) |
| **Current Rule** | `templates/notes/specs/phys_u01_s01.1-s01.4.json` line 321: the student copy prints "meaning 29.7 m/s downward" beside blanks. The answer is visible to students. |
| **Proposed Rule** | Designer moves that text into the answer key's solution and removes it from the student copy. About 5 minutes. This is a build fix, not a rule change. |
| **Supersedes** | Nothing. The line in the spec is replaced; no rule changes. |
| **Reason** | Student copy gives away the answer to the blank. Blocking in the 2026-09-24 audit and never closed. |
| **Affected Agents** | Designer (the edit), Auditor (re-check). |
| **Affected Skills** | Notes build skill (reads the spec). |
| **Affected Courses** | Physics. |
| **Risk** | Low. |
| **Recommendation** | Approve; designer fixes the spec and rebuilds. Confirm no filed Drive copy carries the leak. |
| **Decision** | PENDING. Question for Matt, unadopted: if a filed Drive copy has the leak, rebuild and refile it, or leave the filed copy? |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Drive verification is deferred: no Drive access this run. Whether any filed S1.1 Guided Notes copy in
the Physics U01 folder carries "meaning 29.7 m/s downward" has not been checked. The Auditor checks it
once Drive is reachable.
