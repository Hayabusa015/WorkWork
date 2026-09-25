---
id: SHULL-CHG-0026
title: Guided-notes flow and fit — sections start a page, rows never split, writing space grows into the freed room; every ruled line actually ruled
status: IMPLEMENTED
opened: 2026-09-25
decided: 2026-09-25
source: Coordinator session (code, written and tested) + Matthew Shull (approval)
decided_by: Matthew Shull
---

# SHULL-CHG-0026 — Guided-notes flow and fit

## What happened

Matthew reviewed the built Geology U2 guided notes (`templates/notes/specs/geo_u02_s02.1-s02.5.json`,
rendered by `templates/notes/build_notes_docx.py`, the production "Option A" renderer governed by
`governance/proposals/SHULL-CHG-0014-guided-notes-template.md`) and attached screenshots of section
heads stranded at the foot of a page: the S2.3 head with only its first Cornell row under it, the
S2.4 head alone, and the Unit 2 close banner ("Pulling it together") alone at the foot of p8.

The renderer let Word and LibreOffice break pages wherever the content ran out. `templates/notes/README.md`
§"QA" says so in as many words — "Neither builder checks page breaks, and a summary box orphaned at
the top of a page is the defect to watch for" — which left it to a human looking at every page.
`.claude/skills/build-document/SKILL.md` §"Guided and Cornell notes" already required the opposite:
"Every section starts a new page and ends with a summary box plus self-check." The renderer never
did that either.

Growing the boxes into the freed space then exposed a second, older defect that every packet has
always had (item 4 below): multi-line ruled writing space printed as a single rule.

## Current behavior (before this change)

- No page control. A section head, learning target, Cornell row, summary box, or the unit close
  could land anywhere, including alone at a page foot, with its content on the next page.
- A Cornell row could split across a page.
- Writing-space line counts were fixed in code: a notes label line 2 (a line ending in `:`, per
  `templates/notes/README.md` §"Section rhythm": "A note line ending in `:` gets two ruled lines.
  Everything else gets one."), the section summary 4, the close's "big picture" 3 and "still fuzzy
  on" 3. A spec could not change any of them.
- **`templates/_shull_docx.py` `rule_lines()` drew N identical bottom-bordered paragraphs back to
  back.** Word and LibreOffice both merge adjacent paragraphs with identical borders into one
  bordered group and draw the bottom rule once, under the last paragraph. So "2 ruled lines" — every
  Define line in every packet, all three courses — has always printed as **one** rule with blank
  space above it; a 4-line summary printed as one rule under four lines of blank. Not noticed until
  boxes grew and the gap became obvious.
- Key mode (SHULL-CHG-0025) printed a filled answer as a free paragraph in place of the ruled lines,
  so the key's height differed from the student copy's, row by row. Once sections page-break, the
  key's pages came out half-empty and no longer lined up with the student's.
- `build_notes_docx.py` assembled the section span from the spec's unpadded strings (`"2.1"`), so the
  default filename and running footer did not carry the zero-padded range SHULL-CHG-0024 requires.

## New behavior (already written and tested by the coordinator)

1. **Opt-in `"flow": true` spec key** in `build_notes_docx.py`. When set:
   - every section after the first starts a new page — via a pinned 1pt paragraph carrying
     `pageBreakBefore`, placed outside any table;
   - the section head and learning target carry keep-with-next, so neither is stranded;
   - every Cornell row is `cantSplit` — a row never breaks across pages;
   - the section summary box is `cantSplit`;
   - the unit close ("Pulling it together") starts its own page;
   - a row may carry `"breakBefore": true`, which splits the Cornell table at that row and
     page-breaks between the two halves (Word will not break a page inside a table).

   **Opt-in on purpose.** Packets already in circulation (GEO U1 `geo_u01_s01.2-s01.4.json`, PHYS
   U1 `phys_u01_s01.1-s01.4.json`) do not reflow under anyone. Both were rebuilt unflowed and are
   unchanged apart from item 4.
2. **Per-slot line counts in the spec.** A notes-line dict may carry `"lines": n`; a section may
   carry `"summaryLines"`; the close may carry `"bigPictureLines"` and `"fuzzyLines"`. Absent, the
   defaults are exactly as before (label 2, summary 4, close 3 / 3).
3. **New `templates/notes/fit_notes.py specs/<spec>.json [--write]`.** Renders the student copy in
   LibreOffice, measures with PyMuPDF the room left at the foot of each page, and hands it back as
   extra ruled lines to the writing slots on that page (label lines, the section summary, the
   close). It re-renders until no room is left, and backs off if a row it grew got pushed to the next
   page — **page count and row placement never change.** It also fixes the one orphan flow can still
   make — a summary box alone at the top of a page, cut off from its notes — by setting
   `breakBefore` on that section's last row so the row travels with its summary. **The fitter owns
   `lines`, `summaryLines`, `bigPictureLines`, `fuzzyLines`, and `breakBefore`** and resets them to
   natural counts on every run; hand edits to those fields do not survive a fit. 16pt is left empty at
   every page foot as margin for Word setting the same Archivo slightly differently from LibreOffice.
   Refuses a spec without `"flow": true`.
4. **`rule_lines()` fixed in the shared helper `templates/_shull_docx.py`.** A 1pt unbordered spacer
   paragraph now sits between each pair of rules, which breaks the border group in both Word and
   LibreOffice, so **every line asked for is ruled.** This is a shared helper: **every notes packet
   and every worksheet built from it, in all three courses, now prints more rules than before** —
   the number of rules students were always meant to have. It is the one part of this change that is
   not opt-in.
5. **Key mode writes on the student's lines** (extends SHULL-CHG-0025). The answer is set onto the
   student copy's own ruled lines, word-wrapped on Archivo's real glyph widths by a new `wrap_to()`
   helper in `templates/_shull_docx.py`, instead of as a free paragraph. The key is the student copy
   filled in, and it paginates page-for-page with it. More wrapped lines than rules adds rules.
6. **`build_notes_docx.py` zero-pads the section span itself** (new `zpad()`), so the default filename
   and running footer read `S02.1-S02.5`, per SHULL-CHG-0024. This closes the Option A half of that
   record's open code follow-up. **The Option B half still stands:** `templates/notes/build_notes.py`
   was not touched and still emits an unpadded span (SHULL-CHG-0024 §"Not done here";
   `change-log/CHANGELOG.md` "Open" table).

**Option B is out of scope**, as in SHULL-CHG-0025: `templates/notes/build_notes.py` gets neither
flow nor the fitter.

## Supersedes

- `templates/notes/README.md` §"QA": "Neither builder checks page breaks, and a summary box orphaned
  at the top of a page is the defect to watch for." — **no longer true of Option A for a flowed
  spec.** It remains true of Option B and of an unflowed Option A spec. The sentence is still in
  the README unchanged; see "Not done here".
- The fixed, code-only line counts in `build_notes_docx.py` (label 2, summary 4, close 3 / 3) — they
  remain the defaults, but they are no longer the only possible values.
- The previous `rule_lines()` in `templates/_shull_docx.py`: N adjacent identically-bordered
  paragraphs, which printed as one rule. Named here because its output is what every packet and
  worksheet built to date actually looks like.
- SHULL-CHG-0025 item 3's rendering of a key answer "in place of the blank ruled lines" as a free
  bold paragraph — the answer is now written **on** the ruled lines. The bold / display-accent
  styling and the refuse-an-incomplete-key gate are unchanged.

No written *rule* in `standards/`, `brand/`, or any `courses/*/DECISIONS.md` is replaced. Items 4
and 6 bring the code into line with rules already written (two ruled lines under a `:` label;
SHULL-CHG-0024's padded range). Item 1 lets the renderer meet `build-document` SKILL.md's existing
"Every section starts a new page" — for flowed specs only.

## Where it's written

- `templates/notes/build_notes_docx.py` — `flow`, `breakBefore`, per-slot line counts, key-on-lines,
  `zpad()`.
- `templates/notes/fit_notes.py` — new.
- `templates/_shull_docx.py` — `rule_lines()` fix; new `wrap_to()`.
- `templates/notes/specs/geo_u02_s02.1-s02.5.json` — `"flow": true` and fitter-written counts; the
  first flowed spec.
- `templates/notes/README.md` — new subsection "Flow and fit — `"flow": true`, `fit_notes.py`"
  under "## Build", citing SHULL-CHG-0026, stating that the fitter owns the line-count and
  `breakBefore` fields and that it is opt-in.
- This record, and one index row in `change-log/CHANGELOG.md` (plus a note on the SHULL-CHG-0024 open
  row) — in a follow-up commit, not in `53278b5`.

The code, spec, and README edits were written and tested by the coordinator session; **not touched by
the Secretary** — `templates/` is outside the Secretary's authority (not `brand/`, `standards/`,
`governance/`, or `courses/`).

## Not done here — flagged, not fixed

- **`templates/notes/README.md` §"QA"** still says "Neither builder checks page breaks, and a
  summary box orphaned at the top of a page is the defect to watch for." That is now stale for a
  flowed, fitted Option A spec. It is still true of Option B and of unflowed specs, so the sentence
  needs a qualification, not deleting.
- **The skill and the default renderer still disagree.** `build-document` SKILL.md says every
  section starts a new page; an unflowed spec (GEO U1, PHYS U1, and any new spec that omits the key)
  still does not. Whether `flow` should become the default for new specs is a user decision and is
  not made here.
- **Option B** (`templates/notes/build_notes.py`): no flow, no fitter, still an unpadded span.

## Affected

- **Agents:** Designer (builds flowed specs and runs the fitter), Auditor (a flowed packet should
  have every section at a page top and no orphaned summary; a key should paginate page-for-page with
  its student copy; every packet and worksheet now shows every rule it asks for).
- **Skills:** `build-document` — flow is how the renderer meets the skill's "every section starts a
  new page"; the key-on-lines change strengthens "generated from the same source so they cannot
  drift" to page-for-page.
- **Courses:** all three, through the `rule_lines()` fix in the shared helper (notes and worksheets).
  Flow and fit are opt-in per spec; Geology U2 is the first and only flowed spec. No course
  `DECISIONS.md` is touched — this is build mechanics, not a course fact.

## Risk

**Low** for flow and the fitter: opt-in per spec, and the fitter is constrained never to change page
count or row placement. **The `rule_lines()` fix is a visible change to every document built with the
shared helper, in all three courses** — more rules printed, in the places students were always meant
to have them. Nothing already printed or already on Drive changes until it is rebuilt.

## Verification

Performed by the coordinator session prior to this record:

- Geology U2 spec, flowed and fitted: **11 pages student, 11 pages key.** Every section starts at a
  page top; no summary orphaned; every page ends within ~17–34pt of the body foot.
- Key paginates with the student copy: all 11 key pages start with the same content as the
  corresponding student page.
- `audit_fonts`: Archivo only.
- `audit_print_ink`: worst page 3.57% toner (student); key within budget; no fills.
- GEO U1 and PHYS U1 specs still build, unflowed, unchanged apart from the `rule_lines()` fix.

Secretary spot-check of the working tree (read-only): `build_notes_docx.py` carries `FLOW =
bool(spec.get("flow"))`, `breakBefore`, `summaryLines` / `bigPictureLines` / `fuzzyLines`, `zpad()`,
and cites SHULL-CHG-0026; `fit_notes.py` exists and refuses an unflowed spec; `_shull_docx.py`
`rule_lines()` has the spacer paragraph and `wrap_to()` exists; the Geology U2 spec has `"flow":
true`. This confirms the code matches the description. It is not a re-run of the builds.

**Implemented By:** `53278b5` on `claude/elegant-bohr-8hkbpj`, message carries `SHULL-CHG-0026`,
committed and pushed by the coordinator. Five files: `templates/_shull_docx.py`,
`templates/notes/build_notes_docx.py`, `templates/notes/fit_notes.py`, `templates/notes/README.md`,
`templates/notes/specs/geo_u02_s02.1-s02.5.json`. This record and the `change-log/CHANGELOG.md` row
land in a follow-up commit by the coordinator. The Secretary session holds no git access.

**Verified:** yes, by the coordinator, who checked the commit with git and reported the five-file
list above, which matches "Where it's written" for code. The build and audit results above are also
the coordinator's. This Secretary session has no git tool, so it could not run `git show --stat
53278b5` itself. Its own check is the read-only working-tree spot-check above. Same arrangement as
SHULL-CHG-0025.

## Decision

Matthew Shull, in conversation, 2026-09-25, reviewing the Geology U2 guided notes: **"can we do a
quick sweep and touch these up a bit. Ex: unit 2 review starts at the end of page 8, just move it to
page 9, then just make the review a bit bigger. its ok if you end sections and move the next section
to the next page. use the space available, if you move a section to the next page, just increase the
size of the boxes to use the new space available. just make it flow."**

Explicit approval of flow (items 1–3) and of growing the writing space. Items 4–6 are not named in
the quote. They are recorded under this approval as fixes that bring the code into line with rules
already approved: item 4 with the "two ruled lines" rule, item 5 with SHULL-CHG-0025's "cannot drift"
and needed for flowed keys to paginate, item 6 with SHULL-CHG-0024. **Item 4 is the one Matthew should
see stated plainly**, because it changes the look of every notes packet and worksheet in all three
courses the next time each is rebuilt.

The quote reached this record through the coordinator session; the Secretary did not hear it
directly.
