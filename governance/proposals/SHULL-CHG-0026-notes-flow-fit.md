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

---

## Amendment — 2026-09-25, same day

Appended, not rewritten. The sections above stay as they were written. Where this amendment
contradicts them, **this amendment wins** — see "What this amendment supersedes in the record
above" below.

### What happened

Matthew reviewed the first flowed and fitted build (the 11-page build in "Verification" above) and
said, verbatim: **"well shit theres way too much spacing now"**.

Cause: the unconditional page break before every section (original item 1) freed whole
page-bottoms, and the fitter (original item 3) poured all of that room into the writing slots. Each
prompt got up to 6–7 ruled lines and the unit review became a full page of lines. The build went
from 8 pages to 11.

### What changed

Code commit **`9b83b8d`** on `claude/elegant-bohr-8hkbpj`. The coordinator made and verified it.
Four files: `templates/notes/build_notes_docx.py`, `templates/notes/fit_notes.py`,
`templates/notes/README.md`, `templates/notes/specs/geo_u02_s02.1-s02.5.json`. All four are in
`templates/`, outside the Secretary's authority. **The Secretary did not touch any of them.**

1. **Sections no longer page-break unconditionally under flow.** A section starts a new page only
   when it carries `"breakBefore": true`. The fitter sets that only when the section's head would
   otherwise be stranded, meaning its title is on one page and none of its rows are on that page.
   Otherwise a section flows on directly after the previous one. Keep-with-next on the head and
   learning target, `cantSplit` rows and summary, row-level `breakBefore`, and the close starting
   its own page are all unchanged.
2. **Narrower orphan test for summary boxes.** A summary box counts as orphaned only when it sits
   on a page with no rows at all. If a summary tops a page that the next section's notes also use,
   it is left alone, because it sits directly after what it summarises. For a true orphan the
   original fix still applies: the section's last row gets `breakBefore` and travels with the
   summary.
   *Tried and dropped:* one intermediate attempt also moved a section's last row down with its
   summary on a shared page. That left big gaps (one page a third empty) and pushed the build back
   to 11 pages, so it is not in `9b83b8d`.
3. **Growth is capped** by the `CAP` constant in `fit_notes.py`, measured over each slot's natural
   count:

   | Slot | Natural | Cap | Maximum |
   |---|---|---|---|
   | Label line (`lines`) | see item 4 | +1 | natural + 1 |
   | Section summary (`summaryLines`) | 4 | +2 | 6 |
   | Close, big picture (`bigPictureLines`) | 3 | +3 | 6 |
   | Close, still fuzzy on (`fuzzyLines`) | 3 | +3 | 6 |

   Room past the caps stays white at the foot of the page.
4. **A label line's natural count is now the larger of two numbers:** the recall rule's count
   (`recall.ruled_lines()`; 2 for a line ending in `:`), and the number of lines the key answer
   wraps to (`wrap_to()` on Archivo's glyph widths at the notes width). The key writes on the
   student's lines, so a student needs at least that much room. Without this rule the capped key
   overflowed to 11 pages against the student's 10.
5. **Result for Geology U2:** 10 pages for the student copy and 10 for the key. The key matches the
   student copy page for page, checked on the first text of each page. Both use Archivo only and
   are within the ink budget. These figures are from the coordinator.

### What this amendment supersedes in the record above

These lines stay in the record unedited. They are **no longer accurate**:

| Where in this record | Stale text | Now |
|---|---|---|
| Front matter `title:` | "sections start a page" | A section starts a page only when its head would otherwise be stranded (item 1). |
| "New behavior" item 1, first bullet | "every section after the first starts a new page — via a pinned 1pt paragraph carrying `pageBreakBefore`" | Only a section marked `"breakBefore": true`. The fitter sets it only for a stranded head (item 1). |
| "New behavior" item 3 | "grows … until no room is left" | Growth stops at the caps. Room past them stays white (item 3). |
| "New behavior" item 3 | orphan = "a summary box alone at the top of a page, cut off from its notes" | Orphan = a summary on a page with **no rows at all** (item 2). |
| "New behavior" item 3 | "resets them to natural counts" | Still true, but a label's natural count now includes the key's wrapped length (item 4). |
| "Supersedes", last paragraph | "Item 1 lets the renderer meet `build-document` SKILL.md's existing 'Every section starts a new page' — for flowed specs only." | **No longer true.** See "Flagged" below. |
| "Affected", Auditor | "a flowed packet should have every section at a page top" | A flowed packet should have **no stranded section head** and no summary alone on a page with no rows. Key page-for-page with the student copy still applies. |
| "Verification", first two bullets | "11 pages student, 11 pages key", "Every section starts at a page top", "all 11 key pages" | 10 student, 10 key, key page-for-page (item 5). Sections are not all at a page top by design. |

These are unchanged by this amendment: original items 2, 4, 5, and 6. Opt-in `"flow": true`. The
fitter refusing an unflowed spec. The 16pt safety margin. Growth never changing the page count or
row placement. The fitter owning `lines`, `summaryLines`, `bigPictureLines`, `fuzzyLines`, and
`breakBefore`. Option B out of scope.

### Flagged, not resolved

- **The skill and the flowed renderer now disagree.** `.claude/skills/build-document/SKILL.md`
  line 106 says: "Every section starts a new page and ends with a summary box plus self-check." The
  original record said flow brought the renderer into line with that for flowed specs. After this
  amendment it no longer does. Under flow a section starts a new page only when its head would be
  stranded. Matthew's original instruction ("its ok if you end sections and move the next section
  to the next page") reads as a permission, not a requirement. His follow-up ("way too much spacing
  now") pushed away from unconditional breaks. **Which behavior is the rule is Matthew's decision,
  and it is not made here.** The two ways out are:
  - amend the skill so a section starts a new page only when its head would otherwise be stranded,
    which needs its own change record; or
  - restore unconditional breaks and keep the growth caps.

  This joins the existing open item "The skill and the default renderer still disagree" above.
- **The cap values were chosen by the coordinator, not named by Matthew.** The +1 / +2 / +3 caps
  and the stranded-head break rule came from the coordinator's reading of "way too much spacing
  now". Matthew's words direct a reduction but do not name the numbers. They are recorded here
  under this record's existing approval as a correction to its own over-growth. **Matthew should
  see the cap table in item 3 stated plainly**, because it sets how much writing room students get.
- **`templates/notes/README.md` §"QA"**: the stale sentence flagged above ("Neither builder checks
  page breaks…") is still not covered by this amendment. It is outside the Secretary's authority.

### Implemented By / Verified (amendment)

**Implemented By:** `9b83b8d` on `claude/elegant-bohr-8hkbpj`, committed by the coordinator. This
amendment will land in a follow-up commit by the coordinator. The Secretary session has no git
access.

**Verified:** yes, by the coordinator: the commit, and the 10/10 page counts, page-for-page key
match, font audit, and ink audit in item 5.
The Secretary could not run `git show --stat 9b83b8d`. Its own check was a read-only spot-check of
the working tree. It confirms the code matches this description. It is not a re-run of the builds.
- `fit_notes.py`: `CAP = {"label": 1, "summary": 2, "close": 3}` is present with a comment citing
  "Way too much spacing".
- `fit_notes.py`: `normalise()` sets a label's natural count to
  `max(recall.ruled_lines(...), len(wrap_to(key, ...)))`.
- `fit_notes.py`: the stranded-head test ("title on the page, none of its rows") sets the
  section's `breakBefore`. The orphan test is `not p["rows"]`.
- `build_notes_docx.py`: page-breaks a section only when `FLOW and si > 0 and
  sec.get("breakBefore")`.
- `README.md`: the "Flow and fit" subsection states the stranded-head rule and the caps, and
  quotes "way too much spacing now".
- Geology U2 spec: carries `"flow": true` and no `breakBefore`, so in the committed fit no section
  or row is forced to a new page. All five `summaryLines` are 4, and the close has
  `bigPictureLines` 6 and `fuzzyLines` 6 (at cap).

`change-log/CHANGELOG.md` is unchanged. The status stays CONFIRMED and the record path is the same.

### Decision (amendment)

Matthew Shull, in conversation, 2026-09-25, reviewing the first flowed build: **"well shit theres
way too much spacing now"**. The quote reached this record through the coordinator session. The
Secretary did not hear it directly.

---

## Amendment 2 — 2026-09-25

This amendment is appended. Nothing above has been rewritten: the original record and the first
amendment stay as they were written. Where this amendment contradicts either one, **this amendment
wins**. See "What this amendment supersedes" below.

### What happened

Matthew sent a screenshot of the build from the first amendment (`9b83b8d`) open in Word. Some pages
were half empty in the middle of a section. A Cornell row could not split, so it jumped whole to the
next page and left a gap. He said, verbatim:
**"na see, this is what i mean. keep each section together, if a section ends just head to a new
page!"**

### Decision recorded: each section starts a new page

**This is Matthew's decision.** Under flow, each section starts a new page. That matches
`.claude/skills/build-document/SKILL.md` line 106: "Every section starts a new page and ends with a
summary box plus self-check." It settles the first amendment's flagged question ("Which behavior is
the rule is Matthew's decision, and it is not made here"). He chose the second way out: restore the
unconditional breaks and keep the growth caps. The skill is not amended, and no separate change
record is needed.

The decision covers **flowed** specs. The original record's open item, "The skill and the default
renderer still disagree", is **not** settled by it. Unflowed specs (GEO U1, PHYS U1, and any new spec
that leaves out `"flow": true`) still do not start each section on a new page. Whether `flow` should
become the default for new specs is still Matthew's decision.

### What changed

Code commit **`d0ad4e3`** on `claude/elegant-bohr-8hkbpj`. The coordinator made and verified it. Five
files:

- `templates/_shull_docx.py`
- `templates/notes/build_notes_docx.py`
- `templates/notes/fit_notes.py`
- `templates/notes/README.md`
- `templates/notes/specs/geo_u02_s02.1-s02.5.json`

All five are in `templates/`, which is outside the Secretary's authority. **The Secretary did not
touch any of them.**

1. **Each section starts a new page again.** Under flow, every section after the first starts a new
   page, every time. The close is still on its own page. The fitter no longer sets `breakBefore` on
   sections or rows. The builder no longer supports `breakBefore` on rows.
2. **One table row per prompt.** A prompt is its label, its ruled lines, and any must-write line
   under it. Each prompt is now its own table row, and that row cannot split. The cue cell is
   vertically merged down beside the prompts. Horizontal borders are drawn only at the top of the
   first prompt and the bottom of the last, so the prompts still look like one Cornell row. A page
   can now break between prompts but never through one, so a section runs on without gaps.
   *Tried and dropped:* an intermediate attempt put keep-with-next on the paragraphs inside a row
   that was allowed to split. LibreOffice ignores keep-with-next inside table cells. Word reads it as
   "keep this row with the next row", which chains the whole table into one block. It is not in
   `d0ad4e3`.
3. **Exact line spacing in `rule_lines()`.** Each ruled line is now exactly 14pt with 5pt after it,
   plus the 1pt spacer, so each line takes 20pt. Before, the spacing was "single", which takes its
   height from the font's own metrics. Word set those rules about a third further apart than
   LibreOffice did. So every page ran long in Word but not in the LibreOffice previews. Also,
   `w:pBdr` is now inserted in OOXML schema order, before `w:spacing`, by a new `add_pbdr()` helper,
   because Word is stricter about element order. *This is the shared helper, so like original item
   4 it affects every notes packet and worksheet built with it, in all three courses, and it is not
   opt-in.*
4. **How the fitter gives back room.** For each section, the fitter measures the room left on the
   page that holds the section's summary, which is the page where the section ends.
   - It adds one line to every prompt in the section, but only if all of them fit ("never some and
     not others").
   - The rest of the room goes to the summary, which can grow by up to 6 lines over its natural 4.
   - The close is capped at 4 extra lines for each box, over a natural 3.
   - Room past a cap stays white.
   - Each box still starts at least as tall as its key answer wraps, as in the first amendment's
     item 4.
   - The fitter backs off if the page count changes, or if any summary moves to a different page.
   - If a summary box ends up alone on a page, the fitter prints a warning. It does not fix it.

   | Slot | Natural | Cap | Maximum |
   |---|---|---|---|
   | Label line (`lines`) | the larger of the recall count and the key's wrapped length (first amendment, item 4) | +1 | natural + 1 |
   | Section summary (`summaryLines`) | 4 | +6 | 10 |
   | Close, big picture (`bigPictureLines`) | 3 | +4 | 7 |
   | Close, still fuzzy on (`fuzzyLines`) | 3 | +4 | 7 |

5. **Result for Geology U2:** 10 pages for the student copy and 10 for the key. The key matches the
   student copy page for page, checked on the first text of each page. Both use Archivo only. The
   heaviest page uses 3.84% toner on the student copy and 4.25% on the key. The GEO U1 and PHYS U1
   specs, which do not use flow, still build. These figures are from the coordinator.

### What this amendment supersedes

These lines stay unedited in the record above, but they are **no longer accurate**.

From the first amendment:

| Where | Stale text | Now |
|---|---|---|
| First amendment, item 1 | A section starts a new page "only when it carries `"breakBefore": true`", set "only when the section's head would otherwise be stranded" | Every section after the first starts a new page, every time. The fitter sets no `breakBefore`. The builder does not read a row `breakBefore`. |
| First amendment, item 2 | Narrower orphan test, where the fix is "the section's last row gets `breakBefore`". Also the tried-and-dropped approach of moving the last row down. | The fitter only warns about a summary alone on a page and does not fix it. There is no `breakBefore` in either direction. The tried-and-dropped note no longer applies. |
| First amendment, item 3, cap table | Summary +2 (maximum 6). Close +3 each (maximum 6). | The label cap of +1 **still stands**. Summary is now +6 (maximum 10). Close is now +4 each (maximum 7). See the table in item 4 above. |

Knock-on effects on lines elsewhere in the record:

| Where | Stale text | Now |
|---|---|---|
| The first amendment's own "supersedes" table, rows for the front-matter `title:`, "Supersedes, last paragraph", and "Verification" | "A section starts a page only when…", "**No longer true**", "Sections are not all at a page top by design" | The original wording is accurate again for flowed specs. The title's "sections start a page" holds. Flow meets the skill's "Every section starts a new page". Every section after the first is at the top of a page. |
| The first amendment's own "supersedes" table, Auditor row, and the original "Affected", Auditor | "no stranded section head" / "every section at a page top" | Every section after the first starts at the top of a page. The close is on its own page. No prompt is split across a page. The fitter warns about a summary alone on a page. The key still matches the student copy page for page. |
| Original "New behavior" item 1 | "every Cornell row is `cantSplit`", and "a row may carry `"breakBefore": true`" | Every **prompt** is a `cantSplit` row. A Cornell row, meaning a cue and its prompts, may break between prompts. Row `breakBefore` is gone. |
| Original item 3, and the first amendment's "unchanged" paragraph | "The fitter owns … `breakBefore`". Growth never changes "page count or row placement". | The fitter owns `lines`, `summaryLines`, `bigPictureLines`, and `fuzzyLines`. It removes `breakBefore` and never sets it. It backs off if the page count changes or any summary moves to a different page. Where a row sits is no longer checked on its own. |
| Original item 3 | "hands it back … to the writing slots on that page" | Room is given back per section, measured on the page with that section's summary. Every prompt gets a line or none does. |

These are unchanged by this amendment:

- original items 2, 5, and 6
- original item 4's spacer paragraph (the line pitch is now exact, as in item 3 above)
- `"flow": true` stays opt-in, and the fitter still refuses a spec without it
- the 16pt safety margin
- the first amendment's item 4 (each box starts at least as tall as its key answer)
- Option B is still out of scope

### Resolved

- **The first amendment's flag "The skill and the flowed renderer now disagree"** is resolved by
  Matthew's decision above. Under flow, every section starts a new page, as the skill says.
- **`templates/notes/README.md` §"QA"** is covered by both earlier flags. In the working tree it now
  reads: "A flowed spec run through `fit_notes.py` has its page breaks checked for you — sections
  start pages and no prompt splits; it warns if a summary sits alone. Option B and unflowed specs do
  not, and a summary box orphaned at the top of a page is the defect to watch for there." That is the
  qualification the original record asked for. The Secretary read the text but did not check which
  commit introduced it.

### Flagged, not resolved

- **Matthew did not choose the cap values or the all-or-none rule; the coordinator did.** The +1 /
  +6 / +4 caps and the rule that every prompt in a section gets a line or none does are the
  coordinator's reading of the three quotes from Matthew. Matthew's words say to give back the space,
  that there was too much, and that each section should start a new page. They do not give any
  numbers. The caps are recorded under this record's existing approval. **Matthew should see the cap
  table in item 4**, because it sets how much writing room students get. The summary can now grow to
  10 lines. The first amendment capped it at 6.
- **The default for unflowed specs is still open.** See "Decision recorded" above.
- **`add_pbdr()` is not used everywhere a paragraph border is built.** Item 3 says `w:pBdr` is now
  inserted in schema order, and that is true inside `rule_lines()`. But in
  `templates/notes/build_notes_docx.py`, the left bar on a must-write line (lines 311–315) still uses
  `pPr.append(bd)`. That happens after `para()` has already set paragraph spacing, so the bar's
  `w:pBdr` comes after `w:spacing`, which is out of schema order. `templates/practice/build_practice.py`
  line 315 also builds a `w:pBdr` by hand, and the Secretary did not check its order. Word opened the
  build, according to the coordinator's report, so this may be harmless. It is recorded because it
  contradicts the claim as stated. This is outside the Secretary's authority.
- **Code left over from the dropped keep-with-next attempt.** `rule_lines()` in
  `templates/_shull_docx.py` still accepts `keep=False` and sets `keep_with_next` from it. Its
  docstring still describes holding a prompt's lines together "when the row itself is allowed to
  break", which is the approach dropped in item 2. `build_notes_docx.py` never passes `keep`, so
  nothing is built with it. It is dead code with a stale docstring. This is outside the Secretary's
  authority.

### Implemented By / Verified (amendment 2)

**Implemented By:** `d0ad4e3` on `claude/elegant-bohr-8hkbpj`, committed by the coordinator. This
amendment will land in a follow-up commit by the coordinator. The Secretary session has no git
access.

**Verified:** yes, by the coordinator. The coordinator checked the commit and produced the 10/10 page
counts, the page-for-page key match, the font audit, and the ink figures in item 5. The Secretary
could not run `git show --stat d0ad4e3`.

The Secretary's own check was a read-only look at the working tree. It confirms that the code
matches this description, apart from the two flags above. It is not a re-run of the builds.

- `fit_notes.py`
  - It contains `CAP = {"label": 1, "summary": 6, "close": 4}`.
  - Its docstring quotes all three of Matthew's instructions.
  - `normalise()` removes `breakBefore` from sections and rows.
  - `grow()` adds a line to every prompt only when `extra >= len(labels)`, then adds up to the cap
    to the summary.
  - The back-off test is `len(new) != n_pages or section_ends(new) != home`.
  - A summary alone on a page only produces a warning on stderr.
- `build_notes_docx.py`
  - It calls `page_break(doc)` for every section when `FLOW and si > 0`, and before the close when
    `FLOW`.
  - It does not refer to `breakBefore` anywhere.
  - `blocks_of()` makes one row per prompt, with a must-write line folded into the prompt above it.
  - Each prompt row gets `no_split(tr)`. The cue cell uses `vMerge` "restart" and then "continue".
  - Top and bottom borders are drawn only on the first and last prompt.
- `_shull_docx.py`
  - `RULE_LINE_PT = 14` and `RULE_AFTER_PT = 5` are set with exact line spacing.
  - `add_pbdr()` exists, and `rule_lines()` uses it.
- Geology U2 spec
  - It carries `"flow": true` and no `breakBefore`.
  - The five `summaryLines` values are 4, 7, 8, 10, 7. The 10 is at the new cap.
  - The close has `bigPictureLines` 7 and `fuzzyLines` 7, both at the new cap.

The record path is the same. `change-log/CHANGELOG.md` is not touched by this amendment. The index
row still reads CONFIRMED.

### Decision (amendment 2)

Matthew Shull, in conversation, 2026-09-25, looking at a screenshot of the `9b83b8d` build in Word:
**"na see, this is what i mean. keep each section together, if a section ends just head to a new
page!"**

This decides that each section starts a new page for flowed specs. It also approves the one-row-per-
prompt change, which is how a section runs on without gaps. The exact line spacing in item 3 is not
named in the quote. It is recorded under this approval as the fix for pages running long in Word,
which is what his screenshot showed. The cap values are the coordinator's; see "Flagged" above.

The quote reached this record through the coordinator session. The Secretary did not hear it
directly.
