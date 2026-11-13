# Execution plan — consolidate SHULL OS and ship documents (2026-11-13)

**Written for:** an executing Claude session with no memory of the review that produced this.
**Owner:** Matt. **Repository:** `Hayabusa015/WorkWork`.
**Read first:** `CLAUDE.md`. Its rules override anything here that seems to conflict.

## 1. Why this plan exists

A review on 2026-11-13 found the system has had far more work put into it than documents taken
out of it.

| Measure | Finding on 2026-11-13 |
|---|---|
| Effort | 200 commits since early September; 67 change proposals |
| Rules and docs | About 70,000 words |
| Output visible in the repository | 18 document specs, 1 slide deck, 1 task report, 1 filing-queue row |
| Cost of one document | The Geology Dinosaur Poster took about 12 commits over 9 days |
| Desktop app | No feature work since 2026-09-20; only the worksheet builder is wired to its build button |
| Health | 37 of 37 app tests pass; 7 of 8 validators pass (see Phase 0) |

**Goal:** one runtime (Claude Code), one command that reaches every builder, less ceremony per
document, and a full unit shipped through the system as the proof.

**What stays untouched:** the builders in `templates/`, the course `DECISIONS.md` files, the
validators, CI, and `legacy/`.

## 2. Rules for the executing session

1. Work on the branch your session assigns. Do not push to `main`. Do not open a pull request
   unless Matt asks.
2. You may not edit `brand/`, `standards/`, `governance/` (other than adding new proposal files)
   or `courses/`. Phases 3 and 4 produce **PENDING proposals only**.
3. Delete nothing beyond the files named in Phase 1. Do not touch Drive in Phases 0–4.
4. One commit per phase at minimum, each with a plain message. Run the checks in §3 before every
   commit; do not commit on a new failure.
5. Never invent a unit title, section code, date or policy. If a code is not in the course
   `DECISIONS.md`, stop and ask.
6. Stop and ask Matt (one question) when: a step would need a rule you may not edit, a check
   fails for a reason you cannot explain, or a decision in §9 is needed and unanswered.
7. Report at the end as a table: phase, what changed, how it was verified, what is still open.
   A phase is done when its verification passed, not when the edit was made.

## 3. Checks to run before every commit

```bash
npm test
for v in validate_layers validate_codes validate_tokens validate_agents validate_schemas \
         validate_references validate_profiles validate_notes; do python3 scripts/$v.py || echo "FAIL $v"; done
for c in measure_tokens build_slide_tokens build_app_css; do python3 scripts/$c.py --check || echo "FAIL $c"; done
```

`validate_references.py` fails on any repository path written in a file that does not exist. When
you document a file, create it in the same commit.

## 4. Phase 0 — baseline

1. Run `bash scripts/setup-environment.sh`, then the checks in §3.
2. On 2026-11-13 `validate_profiles.py` failed in a container where the PyMuPDF module (`fitz`)
   was missing and the setup script had not run. The cause was **not confirmed**. If it still
   fails after setup, find the real cause and fix it before anything else; if the fix would touch
   a protected folder, stop and ask.
3. Record the baseline results in your final report.

**Done when:** all checks pass, or each failure has a stated cause.

## 5. Phase 1 — one runtime

The desktop app is a second orchestrator. It cannot build notes, labs or slides, cannot file to
Drive, does not run the repository hooks, and needs a separate paid API key. Claude Code does all
of that already. Park the app; do not delete it.

1. Remove the Vercel deployment path: delete `vercel.json` and `api/index.mjs` (and the then-empty
   `api/` folder). Remove the `VERCEL` branches from `app/server.mjs` and `app/runtime.mjs`, update
   `app/runtime.test.mjs` to match, and check `desktop/main.cjs` and `.gitignore` for leftovers.
   Leave the historical mention in `docs/SHULLOS_IMPLEMENTATION_PLAN.md` alone.
2. Add a short "Parked 2026-11-13" notice at the top of `app/README.md`, `desktop/README.md` and
   `installer/README.md`: what the app can and cannot do, that Claude Code is the working runtime,
   and that no new features go in until Matt reopens it.
3. Keep the app tests and the preview/theme generators running in CI. They are cheap and
   `validate_tokens.py` depends on the generated theme.
4. Leave `.github/workflows/` unchanged except to remove anything that only served Vercel.

**Done when:** `grep -ri vercel` finds nothing outside `docs/` and `legacy/`, and §3 passes.

## 6. Phase 2 — one build command, and a batch mode

Today each builder has its own calling convention:

| Family | Entry point | Arguments today |
|---|---|---|
| Worksheet / activity | `templates/worksheet/build_worksheet_docx.py` | spec, output file; `--rubric-sheet` |
| Worksheet key | `templates/worksheet/build_worksheet_key_docx.py` | spec, optional output file |
| Guided notes | `templates/notes/build_notes_docx.py` | spec, output file; `--verify` |
| Practice set | `templates/practice/build_practice.py` | spec or `--all`, `--out` directory |
| Lab | `templates/lab/build_lab.py` | HTML source, optional page count |
| Snow day | `templates/snow_day/build_snow_day_docx.py` | spec, output directory |
| Slides | `templates/slide/build_deck.js` | `SHULL_COURSE` env, spec, optional output file |

Read each builder and the matching skill in `.claude/skills/` before designing anything. Spec
filenames are not consistent across families, so identify a spec by the course, unit and section
fields **inside** it, not by its name. Do not rename existing specs.

Build `scripts/build.py` with two modes:

**Single build** — `python3 scripts/build.py <course> <section> <type> [--spec PATH] [--out DIR]`

1. Check the section code against `courses/<course>/DECISIONS.md`. Reuse the existing lookup in
   `scripts/_shullos.py` / `scripts/validate_codes.py`; do not write a second parser. Refuse a code
   that is not there.
2. Find the spec (or take `--spec`). If none exists, say so and exit non-zero; never generate
   content.
3. Call the family's builder unchanged, including its key builder where one exists.
4. Take the filename from the existing naming helpers (`templates/_shull_name.py`,
   `templates/shull_name.cjs`). Do not restate the naming grammar.
5. Render to PDF with LibreOffice when present, then run the family's existing audit
   (`scripts/audit_worksheet.py`, `scripts/audit_print_ink.py`, `scripts/audit_fonts.py`,
   `scripts/audit_slide_geometry.py`).
6. Print one table: file, pages, audit result, path. Exit non-zero on a build or audit failure.

**Unit plan** — `python3 scripts/build.py <course> --unit <N> --plan`

Print the table `workflows/build-deliverable.md` asks for: section, document type, filename, spec
exists (yes/no), status. Nothing is built in plan mode. `--unit <N> --build` builds every row that
has a spec, in the build order that workflow file defines, and stops at the first failure.

Also:

- Add `scripts/test_build.py` (or extend an existing test) covering: a code not in the decisions
  file is refused; a missing spec exits non-zero; one existing spec per family builds; plan mode
  builds nothing. Add it to `.github/workflows/` validation and to `scripts/hook-validate.sh`
  together, since the CI file says the two lists must match.
- Add one row for the new script to `scripts/README.md`.
- Do **not** edit the skills to point at the new command here. That is a skill change and goes in
  the Phase 4 proposal.

**Done when:** every existing spec in `templates/*/specs/` builds through `scripts/build.py`, or is
listed with the reason it does not; the new tests pass; §3 passes.

## 7. Phases 3 and 4 — two proposals, drafted and left PENDING

Follow `governance/CHANGE_CONTROL.md` exactly, including the ID allocation rule: `git fetch origin
main` first and take the next integer after the highest ID on `origin/main`. Your session cannot
push to `main`, so mark each ID provisional the way the most recent records do. Use the newest
file in `governance/proposals/` as the format model, and quote current rules verbatim. Implement
neither.

**Phase 3 — a fast lane in change control.**
Problem: a cosmetic template fix costs a proposal, a recorded decision, an implementation and a
close-out. Propose a third path for changes that alter no course fact, no agent authority and no
standard's meaning (typos, a label, a spacing fix in a template, a broken reference): one commit
carrying a Change ID and a one-line changelog entry, with no proposal file. Offer at least two
options for where the line is drawn and say which you recommend. State what stays on the full
path. State the risk honestly: the fast lane is where an unreviewed rule change could hide.

**Phase 4 — a light path for routine documents.**
Problem: the seven-agent chain in `workflows/build-deliverable.md` runs for every document.
Propose: for a document type that has already shipped once through the full chain, the path is
`scripts/build.py`, its automated audits, `verify-content` where the document contains science,
then Matt's review and filing. The full chain stays for a new document type, a new template, or
anything Matt flags. Include the skill and workflow edits this would need (pointing the build
skills at `scripts/build.py`), listed file by file.

**Done when:** both proposal files exist, pass `validate_schemas.py` and `validate_references.py`,
and are listed in the final report with their questions for Matt.

## 8. Phase 5 — close the open items (needs Matt)

Do not act on these. Collect them into one table in the final report with the question, the
options and your recommendation, so Matt can answer them in one message.

| Item | Where it is recorded |
|---|---|
| Legacy skill retirement: schedule it now or restate the condition (question 2 of SHULL-CHG-0065) | `governance/proposals/SHULL-CHG-0065-dst-cron-recheck-and-legacy-retirement.md` |
| First real upload through the Upload Inbox not yet checked | `docs/TODO_DESKTOP_2026-10-15.md` |
| Duplicate Physics practice-set filename; group D files with no unit or section; three duplicates in the `pdf` staging folder | `docs/TODO_DESKTOP_2026-10-15.md` |
| CONFLICT-24, Chemistry grading framing | `courses/chemistry/DECISIONS.md` |
| CONFLICT-26 (Gizmos exception) and Q-13 (archive folder) | `docs/DECISIONS_2026-09-07.md` |

## 9. Phase 6 — the proof: ship one full unit

Start only after Matt has answered §10 and Phases 0–2 are merged.

1. Matt names the course and unit.
2. Run the unit plan. Show the table. Get a yes.
3. For rows with no spec, write the spec from the course decisions file and Matt's source
   material. Anything not given is asked for or marked PROVISIONAL in teacher notes only.
4. Build with `scripts/build.py`, one section at a time, in the workflow's build order.
5. Record for every document: start time, end time, number of commits, number of audit rounds.
6. File through the existing queue (`reports/filing-queue.md`) after Matt approves each row.

**Done when:** every document in the unit is verified in Drive, and the final report states the
time and commits per document next to the Dinosaur Poster baseline (about 12 commits, 9 days).
If the numbers are not clearly better, say so; that result decides what gets cut next.

**Freeze:** until this phase is done, no new agents, skills, standards, dashboards or app
features. Bug fixes that block a build are allowed.

## 10. Decisions Matt should give before sending this

| # | Decision | Default if unanswered |
|---|---|---|
| 1 | Park the desktop app and remove Vercel (Phase 1)? | Stop before Phase 1 and ask |
| 2 | Which course and unit is the proof unit (Phase 6)? | Stop before Phase 6 and ask |
| 3 | Legacy skills: retire after the proof unit ships, or now? | Leave installed |
| 4 | Should Phases 0–2 arrive as one pull request or stay on a branch? | Branch only |
