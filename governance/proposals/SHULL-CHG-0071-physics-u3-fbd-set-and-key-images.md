# SHULL-CHG-0071 — Key-image support in the worksheet key builder, plus one-time exceptions for the Physics U3 free-body-diagram practice set

> **Change ID is provisional.** Taken as the next integer after `SHULL-CHG-0070`, the highest ID in
> the local `governance/proposals/` on 2026-11-11. The Secretary session that wrote this record has
> no git tool. It could not `git fetch origin main` and cannot push. Under
> `governance/CHANGE_CONTROL.md` §2 this ID is **not allocated** until someone checks it against a
> freshly fetched `origin/main` and pushes the record there. If `SHULL-CHG-0071` already exists on
> `origin/main`, renumber this file before pushing it. `change-log/CHANGELOG.md` has no row for it
> yet.
>
> **Conflicts with CONFIRMED course rules, marked and not resolved here.** Part B sets aside four
> rules in `courses/physics/DECISIONS.md` for one deliverable. All four are labelled **CONFIRMED**.
> None is labelled LOCKED (section 4). Matt chose each exception in chat on 2026-11-11 (section 1).
> That is precedence 1 in CLAUDE.md §2 for this deliverable. It does not change the rules. This
> record exists so the exceptions are written down and are not read as precedent.
>
> **Two layers, labelled separately (CHANGE_CONTROL §1).** Part A is Path B, a build change for all
> courses. Parts B and C are Path A, Physics only, one deliverable. They can be approved separately.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0071 (provisional, see banner) |
| **Date** | 2026-11-11 |
| **Source** | User. Matt asked for the set in chat on 2026-11-11. The designer found the blockers while planning it, and Matt answered four questions in chat that day (section 1). |
| **Current Rule** | Part A: `templates/worksheet/build_worksheet_key_docx.py` `answer_block()` (lines 63-99) prints either a typed `solution` or, if the item carries `steps`, a PNG from `scripts/key_solution.solution_image()`. `solution_image()` (lines 172-182) needs `q["steps"]` and draws a sketch only from `SCENES = {"linear": linear_scene}` (line 169). `standards/ANSWER_KEYS.md` §1: "A question opts in by carrying `"steps"` in its spec." §6.3: "Where the scene builder would misrepresent the story ... the sketch is **omitted**." Part B: `courses/physics/DECISIONS.md` lines 112-115, 133-134 and 436-442, and the ramp `RAMP["physics"]` (2/2/1/1, SHULL-CHG-0019) in `templates/worksheet/build_worksheet_docx.py`, all quoted in section 4. Part C: `standards/NAMING.md` §2 lines 38 and 41-42, quoted in section 5. |
| **Proposed Rule** | Section 2 (Part A), section 3 (Part B), section 5 (Part C). |
| **Supersedes** | Part A: `standards/ANSWER_KEYS.md` §1 opt-in sentence and §6.3 omission rule (amended, not removed). Also the `steps`-only branch of `answer_block()` and the `linear`-only `SCENES` table. Part B: **nothing.** The four course rules and the 2/2/1/1 ramp stay in force for every other Physics document. Part C: nothing. |
| **Reason** | Matt wants students to read a scenario and draw a labelled free-body diagram for each one. The key for that set has to show the drawn diagram, and today the key builder can only print typed text or a `linear` motion sketch next to algebra steps. Matt chose to add the capability to the builder so later FBD sets and quizzes can use it (choice 1). The course rules in section 4 were written for calculation sets. Matt set them aside for this set (choices 2 and 3). |
| **Affected Agents** | Designer (builds the set and the key). Auditor (visual key inspection, `audit_fonts.py --key`). Secretary (implements Part A). |
| **Affected Skills** | Worksheet and practice-set build skills that call `build_worksheet_key_docx.py`. Any skill that restates the `steps`/`sketch` schema is already meant to point at the `scripts/key_solution.py` docstring instead (`standards/ANSWER_KEYS.md` header). Not exhaustively checked. |
| **Affected Courses** | Part A: all three. It is a builder capability, and it is opt-in per item, so existing specs are unchanged. Parts B and C: Physics, one deliverable. |
| **Risk** | Part A: medium. It changes a shared builder and a standard. It is additive and opt-in, but the key builder has **no tests today** (section 2.3). Part B: low, if the scope stays one file pair. Part C: low. |
| **Recommendation** | Approve A, B and C as written. Matt has already made each choice in chat. These approvals cover only this record. Approving it does not approve SHULL-CHG-0068 or SHULL-CHG-0070. |
| **Decision** | Approved by the user in chat, 2026-11-11, choosing from four offered options: Key drawings: "Add image support (Recommended)"; Structure: "One set of 12 (Recommended)"; Scenarios: "Everyday objects (Recommended)"; File name: "Practice Set - Free-Body Diagrams (Recommended)". Approves Parts A, B and C. Footer default: no section code (U03 only). Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | `f9d9f41` (branch `claude/focused-mendel-cefeca`): code, tests and the deliverable build script. Documentation (`standards/ANSWER_KEYS.md` header, §1 and §6.3; `templates/worksheet/README.md` pointer; `change-log/CHANGELOG.md` row; this record) written by the Secretary on 2026-11-11, to be committed by the main session. **SHA of that commit: pending, add it here.** Later grid-layout commits on the same branch: see section 10. |
| **Verified** | **Partially, pending QA.** Done: (1) `scripts/test_key_solution.py` and `templates/worksheet/test_build_worksheet_key_docx.py` pass; (2) regression: existing committed keys rebuild byte-identical with `PYTHONHASHSEED=0`; (3) deliverable built: `output/physics/u03/Unit 3 Practice Set - Free-Body Diagrams` (.docx/.pdf) and its Key. As reported by the implementing session; not re-run by the Secretary, which has no shell. Outstanding: page-by-page visual inspection of the rendered FBD key (`standards/ANSWER_KEYS.md` §9), `scripts/audit_fonts.py --key` on it, and the main session's documentation commit. See section 9 for follow-ups, and section 10 for the 2026-11-11 amendment (2-page grid layout, its checks, and its open items). |

---

## 1. Matt's request and his four choices (verbatim)

The request, 2026-11-11:

> "problem set 1: ... student to read a scenario and label free body diagrams ... give them labels
> ... like gravity, applied force, friction, tension etc. I just want them to thoroughly draw the
> boxes and situations."

His answers in chat on 2026-11-11. Each line gives the option he picked, then what he was told it meant.

| # | Question | Matt's choice (verbatim) | As described to him |
|---|---|---|---|
| 1 | Key drawings | "Add image support (Recommended)" | Change the key builder so it can place a drawn diagram in each box. This is a builder change, logged as a proposal, and future FBD sets and quizzes get it too. |
| 2 | Structure | "One set of 12 (Recommended)" | One list of scenarios, easy to hard, with no section breaks, as a one-time exception to the 6-item ramp. |
| 3 | Scenarios | "Everyday objects (Recommended)" | (Everyday objects as scenario subjects, in place of characters.) |
| 4 | File name | "Practice Set - Free-Body Diagrams (Recommended)" | Files "Unit 3 Practice Set - Free-Body Diagrams.docx" and its Key. He was told that adding a descriptor needs his approval and that this answer counts as that approval. |

Those chat answers are the source of Parts A to C. They are **not** the approval of this record.
Under CHANGE_CONTROL §4.1, an approval is a `Decision:` line, written by the main session, quoting
Matt's words about this ID.

## 2. Part A: standing change, all courses (Path B). Key-image capability.

### 2.1 Proposed rule (verbatim, not adopted)

1. **A per-item key image field.** A spec item may carry `"keyImage"`. Its value is a scene object,
   `{"scene": "<name>", ...}`, rendered by a scene in `scripts/key_solution.SCENES`. When an item
   carries `keyImage`, `answer_block()` embeds the rendered PNG in that item's answer box. If the
   item also carries `steps`, the steps are drawn below the image, as for a `sketch` today. If it
   carries no `steps`, the image stands alone. An item without `keyImage` is unchanged.
2. **A generic scene registry, with an FBD scene as the first new entry.** `SCENES` gains `"fbd"`.
   It draws the object as a box or a dot, with one arrow per force. Each arrow is labelled from
   the spec and scaled to the relative magnitude the spec gives. The scene refuses any force
   labelled as motion. That enforces the Physics FBD rule in `courses/physics/DECISIONS.md`
   lines 108-110 ("Object as a dot or box · one labelled arrow per force · arrows scaled to
   relative magnitude · **no arrow for 'motion.'**"). Its spec shape is documented in the
   `scripts/key_solution.py` docstring, which is the one place that schema lives
   (`standards/ANSWER_KEYS.md` header). It is not restated anywhere else. The existing `linear`
   scene becomes reachable through `keyImage` as well as `sketch`.
3. **Look.** Key images follow `standards/ANSWER_KEYS.md` §2 and §6. They use the key-handwriting
   face (`typography.keyHandwriting`). Lines, the object outline and every label are drawn in
   `keyInk.pencil`. **Force arrows are vectors, so they keep `keyInk.arrow`** (§2 row
   `keyInk.arrow`, §6.2 "vectors keep the arrow ink"). Labels that the face cannot render clearly
   fall back under §7. If the face cannot be used at all for some element, the implementation
   reports that element in `Verified:`. It does not substitute silently.
4. **The typed solution stays mandatory.** An item with `keyImage` still carries `"solution"`. For
   an FBD item that is the typed list of forces with directions. The key builder's existing
   refusal ("Every question in a spec must carry a `"solution"` field", file docstring line 19) is
   unchanged. The typed list is what `verify-content` checks the drawing against
   (`standards/ANSWER_KEYS.md` §8). It is also the fallback in item 5.
5. **Amendment to `standards/ANSWER_KEYS.md` §6.3 for drawing items.** Where the drawing **is**
   the answer, it cannot simply be omitted. If the scene cannot model the item correctly, the key
   prints the typed `solution` for that item instead of the image. "No sketch is better than a
   wrong one" still holds.
6. **Amendment to `standards/ANSWER_KEYS.md` §1.** "A question opts in by carrying `"steps"`, or a
   `"keyImage"` (SHULL-CHG-0071), in its spec."
7. **§6.4 ("Physics only, for now").** The `fbd` scene is a physics scene, so §6.4 is not affected
   by it. The `keyImage` mechanism itself is course-neutral. A Chemistry or Geology scene would
   need its own record before it is added.

### 2.2 Files it touches

| File | Change |
|---|---|
| `scripts/key_solution.py` | Add `fbd_scene` to `SCENES`. Let `solution_image()` draw a scene with no `steps`, since it currently reads `q["steps"]` unconditionally at line 179. Document the `keyImage` and `fbd` shapes in the module docstring. |
| `templates/worksheet/build_worksheet_key_docx.py` | In `answer_block()` (lines 63-99), add a `keyImage` branch alongside the `steps` branch, plus the fallback from 2.1 item 5. Update the file docstring. |
| `scripts/key_ink.py` | Only if the `fbd` scene needs a drawing primitive (an arrowhead at an angle, or a box outline) that `Page` lacks. Not yet checked. |
| `standards/ANSWER_KEYS.md` | §1 and §6 amendments (2.1 items 5 and 6). Add `SHULL-CHG-0071` to the Authority line. |
| `templates/worksheet/README.md` | A one-line pointer to the `key_solution.py` docstring for `keyImage`, if the README lists key fields. It must not restate the schema. |

### 2.3 Tests

**Neither `build_worksheet_key_docx.py` nor `scripts/key_solution.py` has a test today.** A glob for
`test_*`/`*.test.*` finds only `templates/practice/test_practice.py` and the `app/` and `desktop/`
tests. The proposal is to add:

| New test file | Checks |
|---|---|
| `scripts/test_key_solution.py` | (a) An `fbd` scene with N forces draws N arrows and N labels, and the labels match the spec. (b) A force named as motion is refused. (c) A scene with no `steps` renders. (d) The existing `linear` + `steps` path renders as before (regression). |
| `templates/worksheet/test_build_worksheet_key_docx.py` | (a) An item with `keyImage` gets exactly one picture in its answer cell. (b) An item with `steps` behaves as before. (c) An item with neither keeps its typed solution and `ANSWER:` line. (d) An item with `keyImage` and no `solution` is refused. (e) Rebuilding an existing committed spec, for example `templates/worksheet/specs/phys_u01_s01.2_10q.json`, still succeeds. |

Verification for `Verified:` should also cover a page-by-page visual inspection of one rendered FBD
key (`standards/ANSWER_KEYS.md` §9) and `scripts/audit_fonts.py --key` passing on it.

## 3. Part B: one-time exceptions for one deliverable (Path A, Physics)

**Scope:** `Unit 3 Practice Set - Free-Body Diagrams.docx` and its Key, and nothing else.
**Not a precedent.** A later document that needs any of these exceptions needs its own request
and its own record, and may not cite this one. That is the same wording as the 2026-09-14 one-off
entries in `courses/physics/DECISIONS.md` (lines 291-294, 348-349). The shared student builder
`templates/worksheet/build_worksheet_docx.py` is **not** edited for Part B. The ramp is applied
through a one-time override at build time, the same mechanism those entries record (lines 317-323).

| # | Exception | Rule set aside (section 4) | How it is built |
|---|---|---|---|
| B1 | **12 items, one list, easy to hard, no section breaks, and no equations.** The force-label bank (gravity, normal force, applied force, friction, tension, and so on) goes in the equation bar under the heading **"FORCE LABEL BANK"**. | `RAMP["physics"]` 2/2/1/1 (SHULL-CHG-0019). The order check that requires the last item to be `multi-topic` (`build_worksheet_docx.py` lines 918-920). | A one-time in-memory ramp override, as in the U1 precedents. The equation bar needs **no** override. `check_profile()` requires `equations` to be non-empty (lines 867-869), and the label bank goes in as that list with `"equationLabel": "FORCE LABEL BANK"`, which the builder already reads (line 1086). `priorKnowledge` is still required (lines 863-866) and is kept. |
| B2 | **A drawing box on each item**, despite "no work areas" | `DECISIONS.md` lines 133-134 | A per-item `draw` panel (`draw_block`, line 230). See the note below the table. |
| B3 | **No graph-reading item** | `DECISIONS.md` lines 113-115 | Content choice. No builder change. |
| B4 | **Everyday objects as scenario subjects**, not superheroes or cartoon characters | `DECISIONS.md` lines 436-442 | Content choice. The variety rule still applies: vary the object from item to item. |

**Not waived:** the FBD rule (lines 108-110), which governs both the student task and the key
drawings. Sign conventions (lines 117-118) apply if any item uses one. The self-check rules apply
as written: there are no calculations, so there are no brackets.

**Separate finding, not bundled into this record.** The Physics no-work-area check in
`check_profile()` (lines 858-862) refuses only `math` and `answerLines`. A per-question `draw`
panel passes it without any warning, even though a drawing box is a work area under the course
rule. B2 therefore needs no builder override, which is why it has to be written down here. Whether
the check should also refuse `draw` on Physics is a separate proposal if Matt wants one.

## 4. The course rules Part B sets aside (verified, with line numbers)

All quoted from `courses/physics/DECISIONS.md` as of 2026-11-11.

| Rule | Lines | Label | Verbatim |
|---|---|---|---|
| No work areas | 133-134 | "Worksheets — CONFIRMED" (line 131) | "**No work areas on Physics worksheets.** Practice sets, homework worksheets, and study guides carry problems and prompts only — no ruled lines, no work boxes." |
| Graph-reading item | 112-115 | "Physics-specific build rules — CONFIRMED as discipline standards" (line 98) | "**Build at least one graph-reading item into every practice set** where kinematics, forces, or energy are in play." Forces are in play here, so the rule applies to this set. |
| Character scenarios | 436-442 (decision-log entry dated 2026-09-14) | "Status: CONFIRMED — Path A" (line 468) | "Physics practice-set questions default to **recognizable characters** as the scenario subject — Marvel and DC superheroes (Spider-Man, Batman, Iron Man, The Flash, Aquaman, etc.) and cartoon characters (SpongeBob, Patrick, etc.) ..." |
| 2/2/1/1 ramp | 491-494 (restated in the decision log) | SHULL-CHG-0019 | "`templates/worksheet/build_worksheet_docx.py` enforces an exact Physics ramp of 2 warm-up / 2 practice / 1 challenge / 1 multi-topic (6 questions per section) via `RAMP["physics"]`, confirmed under SHULL-CHG-0019." |

None of the four is labelled LOCKED. Matt's direct instruction outranks the course file for this
one deliverable (CLAUDE.md §2, precedence 1). The rules themselves stay as written.

## 5. Part C: naming descriptor "Free-Body Diagrams" (Path A, one deliverable)

**What the standard says.** `standards/NAMING.md` §2, line 38: the topic is "the **short title** ...
from the 'Short titles' table ... **No row, no topic**." Lines 41-42: "A **descriptor** (`Longhand`,
`Day 2`, `Extended`) follows the short title when it tells two files apart."

**What exists.** `courses/physics/DECISIONS.md` "Short titles" (lines 221-234) has no `U3` row and
no `3.x` rows. So today the builder names the file "Unit 3 Practice Set.docx" for a multi-section
spec, or "3.2 Practice Set.docx" for a single-section one.

**Can it be done without changing the standard? Mechanically yes. By the letter of the text, only
as a one-off.**
- `templates/_shull_name.py` `document_name()` already takes `descriptor=`. With no topic it
  writes ` - <descriptor>` (lines 67-73), and descriptors have no length limit. "Free-Body
  Diagrams" is 18 characters in any case, under the 20-character topic limit, and contains no
  banned characters. `document_name("Practice_Set", [...], 3, descriptor="Free-Body Diagrams")`
  gives `Unit 3 Practice Set - Free-Body Diagrams.docx`.
- **Neither builder passes `descriptor`.** See `build_worksheet_docx.py` lines 962-965 and
  `build_worksheet_key_docx.py` lines 139-142. Both accept an explicit output path as `argv[2]`, so
  the name can be produced that way with **no code change**.
- The standard describes a descriptor as something that *follows a short title* and *tells two
  files apart*. This one stands in for a missing topic. That is outside what lines 41-42 describe,
  so it is recorded here as a one-time naming exception with Matt's approval (choice 4). **No
  change to `standards/NAMING.md` is proposed.** If Matt wants descriptors-without-a-topic
  allowed generally, that needs its own record.
- Not recommended: adding `U3 | Free-Body Diagrams` to the Short titles table. U3 is "Forces and
  Motion", so that row would put the wrong topic on every other U3 file.

**The exact Key name.** The grammar puts `Key` after the type: **`Unit 3 Practice Set Key -
Free-Body Diagrams.docx`** (NAMING.md line 28, and examples such as "1.3 Lab Key - Motion
Graphs.pdf"). Matt was shown "and its Key", not this exact string. The main session may want to
show it to him when it records the decision.

## 6. Interaction with SHULL-CHG-0068 (PENDING): section codes

Both builders refuse any code in `spec["sections"]` that does not appear in
`courses/physics/DECISIONS.md` (`build_worksheet_docx.py` lines 940-945, key builder lines
112-115). Both print a section span in the footer: `SHULL SCIENCE   U03 · S<first>[-S<last>]`
(lines 956-960 and 1156; key builder line 184). SHULL-CHG-0068 would renumber U3 from seven
sections to six. 3.1 and 3.2 mean the same in both lists. 3.4 to 3.6 change meaning, and 3.7
disappears.

**Recommendation:**
1. **Print no section code on the student page or the key.** Use the unit-level form only. The
   footer reads `U03` with no `S` span, and the filename is the unit-level name from Part C. This
   needs the footer string changed in the same one-time build override as B1. It is part of Part B
   and changes no builder.
2. Internally, the spec declares **one** section, `"3.2"`. That passes the known-code check today
   and stays valid with the same meaning if SHULL-CHG-0068 is approved. A one-section spec also
   matches choice 2 (no section breaks). A two-section spec would force a section break.
3. Do not declare 3.4 to 3.7 in the spec while SHULL-CHG-0068 is PENDING.
4. **To check at build time:** whether the section heading block on the student page prints
   "3.2" or the 3.2 title. If it does, suppress it under the same one-time override, so no code
   is printed anywhere.

## 7. Questions for Matt (one at a time, in this order)

1. Approve Part A, the `keyImage` field, the `fbd` scene and the `ANSWER_KEYS.md` §1/§6
   amendments, as written in section 2?
2. Approve Parts B and C, the one-time exceptions and the naming descriptor for this one file
   pair, including the exact Key name `Unit 3 Practice Set Key - Free-Body Diagrams.docx`?
3. (Only if it matters to him.) Should the footer print no section code at all (recommended), or
   `U03 · S3.2`?

## 8. What this does not do

- It does not edit any file other than this record. Nothing is implemented and nothing is
  committed.
- It does not change `courses/physics/DECISIONS.md`, `standards/NAMING.md`, or the 2/2/1/1 ramp.
- It does not approve or depend on SHULL-CHG-0068 or SHULL-CHG-0070.
- It does not propose closing the `draw` gap in the no-work-area check (section 3 note).

(Section 8 describes the record as proposed. Implementation is in the `Implemented By` field.)

## 9. Follow-ups found during implementation (recorded, not acted on)

Each needs its own record if Matt wants it. None is part of this change.

| # | Finding | Where | What a fix would need |
|---|---|---|---|
| F1 | `draw_block()` always prints a panel number ("1", "2") in each drawing box. The FBD set cannot suppress it. | `templates/worksheet/build_worksheet_docx.py` `draw_block()` | A spec field to suppress the number. That is a builder change, so a Path B record. |
| F2 | The Physics no-work-area check does not refuse `draw` panels. It refuses only `math` and `answerLines`. (Already noted in section 3.) | `build_worksheet_docx.py` `check_profile()` | A decision from Matt on whether a `draw` panel on Physics should be refused, then a builder change. |
| F3 | The key builder seeds handwriting jitter from `hash(prompt)`. Python salts string hashes per process, so a build is reproducible only with a fixed `PYTHONHASHSEED`. The byte-identical regression check in `Verified` depended on `PYTHONHASHSEED=0`. | `templates/worksheet/build_worksheet_key_docx.py` / `scripts/key_solution.py` | A stable seed (for example a digest of the prompt) in place of `hash()`. Would change every key's rendered jitter once. |
| F4 | A `ResourceWarning` for a file left open. | `scripts/key_ink.py` | Close the file (a `with` block). Low risk. |

## 10. Amendment, 2026-11-11: two-page grid layout for the same deliverable

Recorded here rather than in a new record because these changes serve the same file pair. This
section is an audit record of work already committed. **It is not an approval and it widens no
approval** (see 10.4).

### 10.1 Source (verbatim)

Matt, in chat, 2026-11-11, after seeing the first build:

> "na make it 2 pages, move the problems around so they are square boxes and you can move them
> around in, you do not need that much room to draw these, 2, maybe even 3 boxes acrossed a row to
> draw the FBD's"

### 10.2 What changed

All of it is opt-in. A spec that does not name the new keys builds as before (10.3). The keys'
schema is documented once, in `templates/worksheet/README.md` ("Opt-in: a grid of square drawing
boxes"). It is not restated here.

| File | Change |
|---|---|
| `templates/worksheet/build_worksheet_docx.py` | `"layout": "grid"`, with `columns`, `squareIn`, `gridPromptPt` and `gridRowGapPt`. |
| `templates/worksheet/build_worksheet_docx.py` | `draw_block` options `"numbered": false` and `"captionStrip": false`, on a `draw` block or a question's own `draw`. **These close follow-up F1** (section 9), and also the caption-strip item labelled F9 by the implementing session. F9 does not appear in section 9 of this record. |
| `templates/worksheet/build_worksheet_docx.py` | An inline label bank: `"equationStyle": "inline"` and `"equationColumns"`. In that bank `_{...}` sets a subscript run. |
| `templates/worksheet/build_worksheet_docx.py` | `"compactTop": true`. |
| `templates/_shull_docx.py` | `equation_bar(cols=2)`. |
| `templates/worksheet/build_worksheet_key_docx.py` | `render_key_grid`, which draws the key in the same grid. Also a fix so that grid notes no longer clip. |
| `templates/worksheet/test_build_worksheet_docx.py` | New student-builder tests (17). |

**Commits.** These are on branch `claude/focused-mendel-cefeca`. The latest is titled "U3 FBD
practice set: page-1 slack and subscripted label bank". **SHA: pending, add it here.** This
Secretary session has no git tool, so it could not read the SHA.

### 10.3 Verification, as reported by the implementing session

The Secretary has not re-run any of this. It has no shell.

| Check | Result |
|---|---|
| Regression: existing specs rebuild identical, member by member, under `PYTHONHASHSEED=0` | 22 builds compared, all identical |
| `templates/worksheet/test_build_worksheet_docx.py` | 17 tests, pass |
| `templates/worksheet/test_build_worksheet_key_docx.py` | 8/8 |
| `scripts/test_key_solution.py` | 8/8 |
| Page count | Student copy 2 pages, key 3 pages |

**The page budget is met.** `standards/QA_GATE.md` §2: "Practice set is exactly 2 pages." The
student copy is 2 pages. The key is not a practice set, so "whatever was specified" applies to it.
The page-budget concern no longer applies.

Still outstanding from the `Verified` field: the page-by-page visual inspection of the key
(`standards/ANSWER_KEYS.md` §9), `scripts/audit_fonts.py --key`, and the documentation commit.
The `change-log/CHANGELOG.md` row for 0071 stays **PARTIAL** until the deliverable is filed.

### 10.4 Scope of approval: marked, not resolved

Part A (section 2) approved the `keyImage` field and the `fbd` scene. It did not cover a grid
layout, the `draw_block` options, the inline label bank, `compactTop`, or `equation_bar(cols=2)`.
These are **shared-builder capabilities, available to all three courses**. Under the test in
CLAUDE.md §2, that makes them Path B. Section 9 said F1 "needs its own record".

Matt's words in 10.1 are a direct instruction about this deliverable (precedence 1). They are not
a `Decision:` on a builder change under CHANGE_CONTROL §4.1. **No one has recorded a decision on
the 10.2 builder capabilities as standing features.** The main session should ask Matt whether to
keep them as standing, opt-in builder features. If he says yes, the main session records that
under §4.1, either here or in a new record. Until then, this amendment is a record of what was
built. It is not authority to build more against these keys.

### 10.5 Open items

| # | Item | Rule involved | Who decides |
|---|---|---|---|
| A1 | **Label-bank subscripts render at about 6 pt on a student page.** This is below the print floor. | `brand/tokens.json` `typography.floors.printBody` = 8 pt, status **INHERITED** (not LOCKED). `brand/SHULL_DESIGN_SYSTEM.md`: "no student-page text below this except the running footer." | **Matt.** The options are to raise the subscript size, to approve a one-time exception for this file pair, or to amend the floor (which needs its own record). Not resolved here. |
| A2 | `scripts/key_solution.solution_image` may have the same handwriting edge-clipping risk on full-width lines that the grid-notes fix addressed in `render_key_grid`. | `standards/ANSWER_KEYS.md` §9 (visual inspection) | Check needed, by the designer or auditor. Not yet checked. |
| A3 | Drive destination: `Unit 03` or `Section 03.2`. | `standards/DRIVE_ARCHITECTURE.md`. Section 6 of this record puts no section code on the page and declares `3.2` internally. | **Matt.** Pending. The CHANGELOG row stays PARTIAL until filing. |
| A4 | 10.4: should the grid, `draw_block` options, inline bank and `compactTop` stay as standing builder features? | CHANGE_CONTROL §1 Path B, §4.1 | **Matt**, recorded by the main session. |
