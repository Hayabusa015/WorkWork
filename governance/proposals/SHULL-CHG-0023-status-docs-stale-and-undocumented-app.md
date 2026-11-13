Change ID:        SHULL-CHG-0023
Date:             2026-09-18
Source:           Janitor (weekly-system-review, 2026-W38)
Current Rule:     `CLAUDE.md` (top): "Status: Phase 7 of 14. The skeleton and governance exist.
                  Standards, agents, and skills do not yet." `README.md` (top): "Status: Phase 8 of
                  14 — governance, design system, standards, and agents exist. Skills do not yet."
Proposed Rule:    Both files' status line is rewritten from the single source of truth,
                  `docs/SHULLOS_IMPLEMENTATION_PLAN.md` §23, which already records Phases 1–12
                  complete and Phase 13 in progress (this review). `README.md`'s "What exists"
                  table is corrected to list `.claude/skills/` (13 skills) alongside agents and
                  standards. Additionally: `docs/SHULLOS_IMPLEMENTATION_PLAN.md` §9's architecture
                  tree and `README.md` gain one line each naming the `app/`, `desktop/`, `api/`,
                  `installer/` tree (the Electron/local-orchestrator "SHULL OS local app" added
                  2026-09-11, commits 0a22513/1c7d8f7/8bb46d2/31b4c37) and its relationship to the
                  rest of the system — pending the decision below.
Supersedes:       CLAUDE.md (Phase 7 status line, from commit 9c024fe); README.md (Phase 8 status
                  line, commit unrecorded — never carried a Change ID)
Reason:           Rule 1 of this system is "a fact lives in exactly one place." The build phase is
                  currently written in three places (CLAUDE.md, README.md, and the implementation
                  plan's §23 tracker) and two of the three are stale — neither has been touched
                  since 2026-09-08 despite six more days of real work (guided notes template,
                  worksheet template, course profiles, the local app). This is the exact failure
                  mode the repository exists to prevent, now demonstrated inside the repository
                  itself. Separately, the local app is real, working, committed code with no
                  change-control record and no mention in any architecture document — it is
                  orphaned from the documentation's point of view even though it is not orphaned
                  from the repository's.
Affected Agents:  none (documentation only)
Affected Skills:  none
Affected Courses: none
Risk:             low
Recommendation:   Approve. This is a correction to already-established fact (the phase tracker in
                  §23 is not in dispute), not a new decision — except for one open question this
                  proposal surfaces but does not resolve: whether the local app is part of SHULL OS
                  proper or a separate product that happens to share the repository. That question
                  is the user's, and this record does not answer it — see the Janitor's finding #2
                  in `reports/2026-W38/weekly-review.md`.
Decision:
Status:           PENDING
Implemented By:
Verified:
