# SHULL-CHG-0065 — Weekly Routine fire time after DST, and the legacy-skill retirement condition

> No conflict with a LOCKED rule (none known). Part 2 is a decision, not a defect.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0065 |
| **Date** | 2026-11-08 |
| **Source** | Janitor finding, weekly sweep 2026-11-08 |
| **Current Rule** | `workflows/weekly-system-review.md`, Schedule section: revisit the cron at the DST change on 2026-11-01. `CLAUDE.md` line 6: legacy skill retirement is withheld "until the system has been exercised on real work". |
| **Proposed Rule** | Part 1: Matt confirms the intended Ohio fire time. The Secretary then replaces the Schedule wording with the confirmed time and a winter/summer rule. Part 2: Matt either schedules retirement or restates the condition. Neither is adopted. |
| **Supersedes** | `workflows/weekly-system-review.md` Schedule wording, in part, once Matt confirms. `CLAUDE.md` line 6, in part, only if Matt restates the retirement condition. |
| **Reason** | Part 1: today is 2026-11-08 and no re-check is recorded. The Routine fires Sundays at 21:56 UTC, which was 17:56 EDT before 2026-11-01 and is 16:56 EST now. Part 2: real work has shipped since the condition was written (S2.3 Dinosaur Poster filed; snow-day builders). |
| **Affected Agents** | Secretary (wording). Janitor and Researcher (the Routine runs them). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Ask both questions. If a time change is wanted, the Routine's cron is outside the repo and is changed by Matt, not by an agent. |
| **Decision** | Approved by the user via the Secretary's Desk, 2026-11-08T22:43:14.477Z. Still open — Questions for Matt, not answered by the click: (1) What Ohio local time do you want the Sunday sweep to fire? If it should stay at 17:56, the Routine cron moves to 22:56 UTC. (2) Do you want to schedule legacy skill retirement now, or restate the condition for it? Answered in chat 2026-11-08 (Q1): "Keep 4:56 PM". Q2 (legacy retirement) still open. |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is not needed. The Routine's current cron was not read this run; its value above is
from the workflow file and the finding. Verification of the live Routine is deferred to Matt.
