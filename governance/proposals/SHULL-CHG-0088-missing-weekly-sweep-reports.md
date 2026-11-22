# SHULL-CHG-0088 — Weekly sweeps have not been writing their reports

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0088 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 26) |
| **Current Rule** | `.claude/skills/weekly-system-review/SKILL.md` step 5: "**5. Write it up.** Findings to `reports/YYYY-WW/`. Proposals to `governance/proposals/` ..." |
| **Proposed Rule** | No change. Every sweep writes its `reports/YYYY-WW/` file, including a sweep that finds nothing. |
| **Supersedes** | Nothing. |
| **Reason** | Only `reports/2026-W38/` and this week's `reports/2026-W47/` exist (glob, 2026-11-22). The 2026-10-22 and 2026-11-08 sweeps produced proposals but no report. There is no W46 (2026-11-15) sweep commit. That would be allowed if the sweep found nothing, but without a report it cannot be confirmed that the Routine fired. |
| **Affected Agents** | Janitor, Researcher. |
| **Affected Skills** | weekly-system-review. |
| **Affected Courses** | None. |
| **Risk** | Low. Without reports there is no record that a sweep ran. |
| **Recommendation** | Enforce step 5 as written. Matt confirms the Routine is still firing. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Did the Routine fire on 2026-11-15? The Routine's run history is outside the repo, so only Matt
   can check it.
2. Should step 5 say explicitly that an empty sweep still writes a one-line report? It is ambiguous
   now.
