# Execution plan — consolidate SHULL OS and ship documents (2026-11-13)

**Decisions are in §10; the legacy-skill work is §11.**
**Written for:** an executing Claude session with no memory of the review that produced this.
**Owner:** Matt. **Repository:** `Hayabusa015/WorkWork`.
**Read first:** `CLAUDE.md`. Its rules override anything here that seems to conflict.

## 1. Why this plan exists

**Correction, 2026-11-13.** The first review read `main` only and concluded the system had
produced almost nothing. That was wrong. A second look at every remote branch found the real
work, and a different problem.

| Measure | Finding on 2026-11-13 |
|---|---|
| `main` | 200 commits; last change 2026-11-09; 18 document specs; change records up to SHULL-CHG-0067 |
| Branches with commits not on `main` | 27, holding roughly 365 commits (not checked for work that reached `main` another way) |
| Work that exists only on branches | Chemistry Units 2, 3, 4 and 5; Physics Units 2 and 3; Geology Units 2 and 3; the Chemistry reference packet; question banks and tests; an `assessment` and an `activity` template family |
| Rule changes that exist only on branches | Change records up to at least SHULL-CHG-0071, with edits to `brand/`, `standards/`, the builders and `config/drive.json` |
| Desktop app | No feature work since 2026-09-20; only the worksheet builder is wired to its build button |
| Health of `main` | 37 of 37 app tests pass; 7 of 8 validators pass (see Phase 0) |

**The real defect:** the repository's one rule is that a fact lives in one place, and `main` is
supposed to be that place. It is not. Every session branches from a stale `main`, so each one
starts without the others' builder fixes, standards changes and Change IDs. Change IDs are
allocated from `origin/main`, so sessions on separate branches can take the same number.

**Goal:** get everything onto `main` and keep it there; one runtime (Claude Code); one command
that reaches every builder; less ceremony per document.

**What stays untouched:** the course `DECISIONS.md` files, the validators, CI, and `legacy/`.

## 2. Rules for the executing session

1. Work on the branch your session assigns. Do not push to `main`. Open the pull requests named
   in §10 row 4 and no others. Do not merge them; Matt merges.
2. You may not edit `brand/`, `standards/`, `governance/` (other than adding new proposal files)
   or `courses/`. Phases 3 and 4 produce **PENDING proposals only**.
3. Delete nothing beyond the files named in Phase 1. Delete no branch. Do not touch Drive in
   Phases 0–4.
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

## 4b. Phase 0b — bring the branches home (do this before anything else changes)

Phases 1 and 2 edit the builders and scripts. Doing that on a stale `main` would add a 28th
divergent copy. So the branches come first.

**Step 1 — inventory, report only.** `git fetch origin`, then for every remote branch with commits
not on `main`, one table row: branch, last commit date, commits ahead, what it holds (documents,
builder changes, rule changes, Change IDs), whether its content already reached `main` another
way (compare trees, not just history), and whether it merges cleanly. Flag:

- every Change ID that appears on more than one branch with different content;
- every file changed on more than one branch (the builders and `templates/_shull_docx.py` will be);
- branches that look abandoned or superseded.

Show Matt the table. **Merge nothing until he says yes.**

**Step 2 — ask which sessions are still live.** Matt has at least one other session open on
Chemistry Units 4 and 5 (`claude/funny-heisenberg-vu0q4r`). Do not rewrite, rebase or delete any
branch. A live branch is merged into `main` like the others and the live session then updates
from `main`; Matt decides the timing.

**Step 3 — merge, oldest first.** One pull request per branch, or per small group Matt agrees to.
Resolve conflicts by reading both sides; where two branches changed the same rule or builder
behaviour differently, stop and ask rather than choosing. Rule-file conflicts (`brand/`,
`standards/`, `governance/`, `courses/`) are resolved only in favour of an APPROVED or IMPLEMENTED
change record; if the records themselves disagree, ask. Run §3 after each merge. Matt merges.

**Step 4 — renumber only if Matt approves.** If two different records share a Change ID, propose
which keeps the number; do not renumber on your own.

**Step 5 — prevent the recurrence.** Propose (as a PENDING record, with the two in §7) a rule
that a session's work reaches `main` by pull request before the session ends, and that the
SessionStart setup warns when the branch is behind `origin/main`.

Never delete a branch. List the ones that are fully merged and let Matt delete them.

**Done when:** every branch is either merged, or listed with the reason it is not; `main` passes
§3; the table in the final report shows no unexplained branch.

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

There are more families on the branches than this table shows (`assessment`, `activity`); after
Phase 0b, list what is actually in `templates/` and cover all of it.

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
| First real upload through the Upload Inbox not yet checked | `docs/TODO_DESKTOP_2026-10-15.md` |
| Duplicate Physics practice-set filename; group D files with no unit or section; three duplicates in the `pdf` staging folder | `docs/TODO_DESKTOP_2026-10-15.md` |
| CONFLICT-24, Chemistry grading framing | `courses/chemistry/DECISIONS.md` |
| CONFLICT-26 (Gizmos exception) and Q-13 (archive folder) | `docs/DECISIONS_2026-09-07.md` |

## 9. Phase 6 — the proof: ship one full unit

Start only after Phases 0–2 are merged, including Phase 0b.

1. Ask Matt for the unit (§10 row 2). It must be one no other session is working on.
2. Run the unit plan. Show the table. Get a yes.
3. For rows with no spec, write the spec from the course decisions file and Matt's source
   material. Anything not given is asked for or marked PROVISIONAL in teacher notes only.
4. Build with `scripts/build.py`, one section at a time, in the workflow's build order.
5. Record for every document: start time, end time, number of commits, number of audit rounds.
6. File through the existing queue (`reports/filing-queue.md`) after Matt approves each row.

**Done when:** every document in the unit is verified in Drive, and the final report states the
time and commits per document next to a baseline taken from the branch history of a comparable
unit built before this plan (measure it; do not assume one).
If the numbers are not clearly better, say so; that result decides what gets cut next.

**Freeze:** until this phase is done, no new agents, skills, standards, dashboards or app
features. Bug fixes that block a build are allowed.

## 10. Decisions — answered by Matt, 2026-11-13

| # | Decision | Answer |
|---|---|---|
| 1 | Park the desktop app and remove Vercel (Phase 1)? | **Yes.** Verbatim: "Lets park the app and remove vercel" |
| 2 | Proof unit (Phase 6)? | **Open again.** Matt first said Chemistry Unit 4, then on 2026-11-13: "I have files in the drive I have been working on unit 4 and 5 in tandem in another session." That work is on `claude/funny-heisenberg-vu0q4r` (combined deck, guided notes, and practice sets filed to Drive). Do not build or rebuild anything for Chemistry Units 4 or 5. After Phase 0b, ask Matt which unit is next and unbuilt. |
| 3 | Legacy skills? | **Retire them.** Verbatim: "Legacy skills, retire them". See §11. |
| 4 | Delivery of Phases 0–2? | Matt asked for a recommendation. Recommended and adopted unless he says otherwise: **pull requests as Phase 0b describes for the branches, then one pull request for Phases 1–2**, so CI runs on it and the work reaches `main` in one reviewed step. The two proposals (Phases 3 and 4) go in a second pull request so their IDs become real on `main`. |

## 11. Legacy skill retirement

Matt's answer in §10 row 3 answers question 2 of SHULL-CHG-0065. Claude cannot uninstall an
installed skill; only Matt can, in the Claude app.

1. Record the decision in
   `governance/proposals/SHULL-CHG-0065-dst-cron-recheck-and-legacy-retirement.md`, verbatim and
   dated, following `governance/CHANGE_CONTROL.md` §4. Change nothing else in that record.
2. Any edit this requires in `CLAUDE.md`, `README.md` or the implementation plan (they say the
   legacy skills stay installed) goes through the Secretary against SHULL-CHG-0065.
3. Give Matt the uninstall list. The ten snapshotted in `legacy/skills/` are: `anti-ai`,
   `shull-chemistry-guidelines`, `shull-course-librarian`, `shull-geology-guidelines`,
   `shull-guided-notes-builder`, `shull-physics-guidelines`, `shull-slide-deck-builder`,
   `shull-student`, `shull-studio`, `test-quiz-generator`. Confirm the list against what the
   record says before sending it.
4. Before Matt uninstalls, tell him plainly: the repository's skills only load in a Claude Code
   session on this repository. A Claude Project or phone chat that relied on a legacy skill will
   lose it. Read `docs/MOBILE_AND_PROJECT_WORKFLOW.md` and say what, if anything, stops working.
5. `legacy/` stays as it is. It is the snapshot, not the installed copy.

**Done when:** the decision is recorded, Matt has the list and the warning, and Matt confirms the
uninstall. Do not report the skills as retired until he confirms.
