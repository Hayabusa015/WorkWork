# SHULL-CHG-0083 — Weekly Routine schedule text still says "revisit at DST"

Repeat of: SHULL-CHG-0065 (part 1)

> No conflict with a LOCKED rule (none known). The Routine's cron lives outside the repo; Matt
> changes it, not an agent.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0083 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 21) |
| **Current Rule** | `workflows/weekly-system-review.md`, Schedule: "Ohio is UTC−4 until 2026-11-01, UTC−5 after — **the schedule needs revisiting at the DST change** (21:56 UTC will drift an hour relative to Ohio local time) ... Whoever is running the system after 2026-11-01 should re-check the fire time against local expectations." |
| **Proposed Rule** | Replace with the confirmed time and a winter/summer rule. For example: "Fires Sundays at 4:56 PM Ohio time: 21:56 UTC in EST (November–March), 20:56 UTC in EDT. Matt moves the cron at each DST change." Exact wording depends on the open question. |
| **Supersedes** | `workflows/weekly-system-review.md` Schedule, DST paragraph. |
| **Reason** | Matt answered SHULL-CHG-0065 Q1 on 2026-11-08: "Keep 4:56 PM" (recorded in that record's Decision field). The Schedule wording was not replaced and no winter/summer rule is recorded. At the 2027-03-14 DST change, 21:56 UTC becomes 5:56 PM EDT, which no longer matches "4:56 PM". |
| **Affected Agents** | Secretary (wording). Janitor and Researcher (the Routine runs them). |
| **Affected Skills** | weekly-system-review. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Implement under SHULL-CHG-0065, which is already APPROVED for this wording. This record is the reminder plus the March question. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Should the cron move to 20:56 UTC on 2027-03-14 to keep 4:56 PM local, or stay at 21:56 UTC and
   fire at 5:56 PM in summer?
