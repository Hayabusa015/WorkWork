# Weekly System Review — 2026-W38 (2026-09-18)

**Report-only. Nothing outside this file and `governance/proposals/` was changed by this run.**

First run of `weekly-system-review` — Phase 13 was not started until today, so there is no prior
week's report to check for repeats.

## Validators

| Validator | Result |
|---|---|
| `validate_layers.py` | OK — 105 files checked |
| `validate_codes.py` | OK — 116 files checked (89 CHEM, 48 PHYS, 54 GEO codes) |
| `validate_tokens.py` | **FAIL — 13 problems**, see row 1 |
| `measure_tokens.py --check` | OK — tokens current; 1 note (Geology display pair 6 grey levels apart, needs border/label differentiation on categorical use — already a known constraint, not new) |
| `validate_agents.py` | OK — 7/7 agents match the authority matrix |
| `validate_references.py` | OK — 102 files checked |
| `validate_schemas.py` | OK — 12/12 cases |
| `validate_profiles.py` | OK — 21/21 cases |

## Findings

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| 1 | `CLAUDE.md`, `README.md` | **Duplicated, stale phase-status.** `CLAUDE.md` says "Phase 7 of 14... Standards, agents, and skills do not yet [exist]" (unedited since the Phase 7 commit, 09-08). `README.md` independently says "Phase 8 of 14... Skills do not yet [exist]." Both are wrong and disagree with each other — `standards/`, `.claude/agents/`, and `.claude/skills/` are all populated (6 standards, 7 agents, 13 skills), and `docs/SHULLOS_IMPLEMENTATION_PLAN.md` §23 already records Phases 1–12 done, T-7/T-10 passed. This is the exact failure the system's own rule 1 names: the same fact (build phase) written twice, and both copies went stale. See SHULL-CHG-0023. | Approve SHULL-CHG-0023 to correct both files from the one source (`docs/SHULLOS_IMPLEMENTATION_PLAN.md` §23) | 5 min |
| 2 | `app/`, `desktop/`, `api/`, `installer/`, `package.json` | **Undocumented addition.** Commits `0a22513`, `1c7d8f7`, `8bb46d2`, `31b4c37` (2026-09-11) added a working Electron desktop app + local orchestrator + Vercel API entrypoint ("SHULL OS local app") that runs the seven agent roles outside Claude Code. It isn't in `docs/SHULLOS_IMPLEMENTATION_PLAN.md` §9's architecture tree, isn't mentioned in `CLAUDE.md` or `README.md`, has no change-control record, and no `CHANGELOG.md` entry. Not flagged as a defect in the app itself — it looks deliberate and functional — but as it stands it's an orphaned tree from the documentation's point of view. See SHULL-CHG-0023. | Decide: is this part of SHULL OS proper (document it) or a separate product (say so explicitly, e.g. a note in `README.md`)? | 10 min |
| 3 | `scripts/validate_tokens.py` | **False-positive FAIL**, caused by #2: 13 raw hex values in `app/public/style.css` (the desktop app's own UI chrome) trip the "no hex outside `tokens.json`" rule. The rule was written for teaching deliverables and the design system, not for this app's UI, which was never in scope when the validator was built. See SHULL-CHG-0024. | Approve SHULL-CHG-0024 (exclude `app/public/` from `validate_tokens.py`, same treatment as `legacy/`) or reject it (require the desktop app to consume `brand/tokens.json` instead) | 10 min |

## Course open questions

Checked `courses/*/DECISIONS.md`. All open questions (Chemistry gradebook framing/CONFLICT-24;
Geology Gizmos/CONFLICT, U5 near-duplicate titles, grading and late-work PROVISIONAL items; Physics
Unit Map PDF location/CONFLICT-05, practice-set ramp) are unchanged since last recorded — no new
evidence surfaced this run that would let any of them be proposed as answered. Nothing to add.

## Legacy and archive

`legacy/` and `brand/palette-archive/` not flagged, per policy.
