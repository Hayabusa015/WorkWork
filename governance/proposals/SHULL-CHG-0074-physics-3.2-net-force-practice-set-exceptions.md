# SHULL-CHG-0074 — Physics: one-time exceptions for "3.2 Practice Set - Net Force"

> **Change ID is provisional.** It is the next integer after `SHULL-CHG-0073`, the highest ID in the
> local `governance/proposals/` on 2026-11-18. The Secretary session that wrote this record has no
> git tool. It could not `git fetch origin main` and cannot push. Under
> `governance/CHANGE_CONTROL.md` §2 this ID is **not allocated** until someone checks it against a
> freshly fetched `origin/main` and pushes the record there. If `SHULL-CHG-0074` already exists on
> `origin/main`, renumber this file before pushing it. `change-log/CHANGELOG.md` has no row for it
> yet.
>
> **Path A (course change), one deliverable.** Every edit proposed here is to
> `courses/physics/DECISIONS.md`. No builder, template, standard or skill is changed.
>
> **Conflicts with CONFIRMED course rules, marked and not resolved here.** Items 1, 2 and 4 set aside
> CONFIRMED Physics rules for this one deliverable (section 3). None of them is labelled LOCKED. Matt
> chose each exception in chat on 2026-11-18 (CLAUDE.md §2, precedence 1). That does not change the
> rules, and this record is **not a precedent**.
>
> **Two items are pending Matt's confirmation** (items 5 and 6). The Secretary also found that the
> committed build path appears to **show** tier tags on both copies, which contradicts item 5 as
> reported (section 4). Both are open, and neither is settled by this record.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0074 (provisional, see banner) |
| **Date** | 2026-11-18 |
| **Source** | User. Matt chose from offered options in chat on 2026-11-18, while the Physics 3.2 net-force set was being built. His choices are quoted verbatim in section 1, as relayed to the Secretary by the main session. |
| **Current Rule** | (1) Ramp: `RAMP["physics"]` 2 warm-up / 2 practice / 1 challenge / 1 multi-topic per section (SHULL-CHG-0019), restated in `courses/physics/DECISIONS.md` lines 575-577. (2) `courses/physics/DECISIONS.md` lines 119-121: "**Build at least one graph-reading item into every practice set** where kinematics, forces, or energy are in play." (3) `standards/NAMING.md` line 38: "**No row, no topic**". Physics "Short titles" (lines 234-242) has no `3.2` row. (4) `courses/physics/DECISIONS.md` lines 520-552, 2026-09-14 "Standing convention: character-based scenarios in Physics practice sets": "Physics practice-set questions default to **recognizable characters** as the scenario subject". (5) Tier tags are drawn on every card of the student page (`build_worksheet_docx.py` `question_card()`, lines 759-765, grey under SHULL-CHG-0055) and on every key entry (`build_worksheet_key_docx.py` `answer_block()`, lines 86-87). (6) No written rule on whether g = 9.8 m/s² counts toward significant figures. |
| **Proposed Rule** | Section 2 (one-time exceptions, items 1-6), and section 5 (draft decision-log entries). |
| **Supersedes** | **Nothing.** Items 1-5 are a one-time exception for one file pair, like the 2026-09-14 S1.2 entry. The ramp, the graph-reading rule, the naming rule, the character convention and the tier-tag rendering all stay in force for every other Physics document. Item 6, if Matt confirms it as a standing convention: no written rule (it fills a gap in "Sequencing" / sig figs, `courses/physics/DECISIONS.md` lines 83-93). |
| **Reason** | Matt wanted the set on 2 pages (`standards/QA_GATE.md` line 37: "Practice set is exactly 2 pages."), with everyday objects as subjects and no graph item this time. He chose a name with a descriptor because 3.2 has no short title. These choices need writing down so they are not read as precedent, and so the two unconfirmed items are not presented as settled. |
| **Affected Agents** | Designer (built the set). Auditor (checks it). Secretary (implements the decision-log entry). |
| **Affected Skills** | Worksheet and practice-set build skills that call `build_worksheet_docx.py` / `build_worksheet_key_docx.py`. Not edited. |
| **Affected Courses** | Physics only. |
| **Risk** | Low for items 1-4, provided the scope stays one file pair. Low to medium for item 5, because the build may not match what is reported (section 4). Low for item 6 as a one-time note. If it is recorded as a standing convention, it affects every future Physics key that uses g. |
| **Recommendation** | Approve items 1-4 as written. Hold items 5 and 6 until Matt has answered the questions in section 6. Resolve the section 4 discrepancy before the set is filed. If Matt confirms item 6 as standing, approve the separate convention entry in section 5.2. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Matt's choices (verbatim, chat, 2026-11-18)

Relayed to the Secretary by the main session. The Secretary did not see the chat. Each line gives
the option he picked, then what he was told it meant.

| # | Question | Matt's choice (verbatim) | As offered to him |
|---|---|---|---|
| 1 | Length | "Cut to 2 pages" | Fewer problems, about 4 per part instead of 6, with the parts running together. |
| 2 | Graph item | "Skip it this time (Recommended)" | (A one-time waiver of the graph-reading rule.) |
| 3 | Name | "3.2 Practice Set - Net Force (Recommended)" | The descriptor "Net Force". 3.2 has no short-title row. |
| 4 | Scenarios | (From his request, not an option) "use something someone might use in an every day scenario" | Everyday objects, not characters. |

Item 5 rests on an earlier instruction about a different set, the FBD set: "remove this on the
text boxes". Item 6 has no instruction from Matt yet.

These chat answers are the source of this record. They are **not** its approval. Under
CHANGE_CONTROL §4.1, an approval is a `Decision:` line, written by the main session, quoting Matt's
words about this ID.

## 2. The one-time exceptions

**Scope:** `output/physics/u03/3.2 Practice Set - Net Force.docx`/`.pdf` and
`3.2 Practice Set Key - Net Force.docx`/`.pdf`. These are built from
`templates/worksheet/specs/phys_u03_s03.2_net_force.json` by
`templates/worksheet/specs/build_phys_u03_s03.2_net_force.py`. **Nothing else is in scope.**

| # | Exception | Rule set aside | Label | How it is built | Status |
|---|---|---|---|---|---|
| 1 | **Ramp override: one section of 12, 2 warm-up / 4 practice / 5 challenge / 1 multi-topic**, three parts running together, continuous numbering 1-12, with a part sub-heading before each part. | `RAMP["physics"]` 2/2/1/1 (SHULL-CHG-0019); `DECISIONS.md` lines 575-577 | CONFIRMED (SHULL-CHG-0019). Not labelled LOCKED. | Build script line 50: `b.RAMP["physics"] = {"warm-up": 2, "practice": 4, "challenge": 5, "multi-topic": 1}`, in memory, for this call only. It swaps in `render_questions()` (student) and `answer_block()` (key) to draw the `partHeading` sub-headings. The key starts each part on a new page. No builder file is edited. | **The main session's implementation of Matt's "Cut to 2 pages" choice. Matt did not ask for the ramp override separately**, and the 2/4/5/1 shape was not put to him. |
| 2 | **No graph-reading item.** | `DECISIONS.md` lines 119-121, "Physics-specific build rules — CONFIRMED as discipline standards" (line 97) | CONFIRMED. Not labelled LOCKED. | Content choice. No builder change. | Matt: "Skip it this time (Recommended)". |
| 3 | **Name with the descriptor "Net Force"** with no short title. | `standards/NAMING.md` line 38 ("No row, no topic") and line 41 (a descriptor "follows the short title") | Standard. | `document_name("Practice_Set", ["3.2"], 3, descriptor="Net Force")`, build script lines 18-19. The same one-time naming route as SHULL-CHG-0071 Part C. **No `3.2` short-title row is added, and `standards/NAMING.md` is not changed.** | Matt: "3.2 Practice Set - Net Force (Recommended)". |
| 4 | **Everyday objects as scenario subjects**, not characters. | `DECISIONS.md` lines 520-552, the 2026-09-14 character-scenario convention | CONFIRMED — Path A (line 552). Not labelled LOCKED. | Content choice. The variety rule still applies. | Matt: "use something someone might use in an every day scenario". |
| 5 | **Tier tags hidden on both the student copy and the key.** | Tier-tag rendering in both builders (Current Rule 5) | Builder behaviour. See also SHULL-CHG-0062 below. | **See section 4: the committed build path appears not to do this.** | **PENDING Matt's confirmation for this set.** It follows his "remove this on the text boxes" for the FBD set. He has not said it for this set. |
| 6 | **g = 9.8 m/s² treated as exact for significant figures**, so key answers keep the other givens' precision. Example, spec item 9: "Fg = 15.0 × 9.8 = 147 N down". Strict sig figs, with 9.8 at two figures, would give 150 N. | No written rule | None. | Content choice in the key and the self-check brackets (spec line 675: "[  147 N  ·  95.4 N  ·  23.7 N  ]"). | **PENDING Matt's confirmation.** If he confirms, the proposal is to record it as a standing Physics convention (section 5.2). |

**Not waived:** units and direction on every answer (lines 102-105), the FBD rule (lines 113-116),
sign conventions stated explicitly (lines 123-124), ∑F notation (lines 107-111, SHULL-CHG-0070),
no work areas (lines 139-140), and the separate answer-key file (2026-09-14 entry, line 486).

**Overlap with SHULL-CHG-0062 (APPROVED, not implemented). Marked, not resolved.** SHULL-CHG-0062's
Decision records Matt's "Yes, make it the rule". That makes "no tier label on the student page" and
"a larger default ramp (about 9-10 questions)" the standing Physics rule, and retires the one-off
overrides. Its `Implemented By` is blank, so the builder still enforces 2/2/1/1 and draws tags.
Items 1 and 5 here are one-off overrides of exactly that kind. Implementing 0062 would make item 5
(student page) standard and might cover a 12-question set. It says nothing about the key. This
record does not implement 0062, and it does not decide how the two interact.

## 3. Course rules set aside (verified, with line numbers)

All quoted from `courses/physics/DECISIONS.md` as read on 2026-11-18. Line numbers have moved since
SHULL-CHG-0071 quoted some of these rules.

| Rule | Lines | Verbatim |
|---|---|---|
| Graph-reading item | 118-121 | "**Graph interpretation is a first-class skill, not a garnish.** ... **Build at least one graph-reading item into every practice set** where kinematics, forces, or energy are in play." Forces are in play, so the rule applies. |
| Character scenarios | 520-552 (entry dated 2026-09-14) | "Physics practice-set questions default to **recognizable characters** as the scenario subject — Marvel and DC superheroes ... and cartoon characters ..." |
| 2/2/1/1 ramp | 575-577 | "`templates/worksheet/build_worksheet_docx.py` enforces an exact Physics ramp of 2 warm-up / 2 practice / 1 challenge / 1 multi-topic (6 questions per section) via `RAMP["physics"]`, confirmed under SHULL-CHG-0019." |

## 4. Finding: item 5 is not what the committed build does

Read from the working tree on 2026-11-18. The Secretary has no shell, did not run the build, and
cannot open the `.docx` files.

- `phys_u03_s03.2_net_force.json` uses the default card layout. It has no `"layout": "grid"` and no
  `"tierTags": false`. (The FBD spec, `phys_u03_fbd_problem_set_1.json` line 23, does carry
  `"tierTags": false`.)
- `"tierTags"` is read only by `grid_opts()` (`build_worksheet_docx.py` lines 869-886), which
  returns None for a card layout. It has no effect on cards.
- On the card path, `question_card()` draws the tag whenever the item has a `tier`
  (`build_worksheet_docx.py` lines 759-765). The key's `answer_block()` does the same
  (`build_worksheet_key_docx.py` lines 86-87). All 12 items carry a `tier`, which the ramp check
  needs.
- `build_phys_u03_s03.2_net_force.py` overrides `render_questions()` and `answer_block()`. Its
  `render_questions()` calls the stock `b.question_card()`, and its `answer_block()` calls the stock
  `_answer_block()`. Neither override suppresses the tag.

**Result:** rebuilt from the committed spec and script, both copies would show tier tags. Either the
files in `output/physics/u03/` came from a version that is not committed, or the tags are showing.
The designer or auditor should open both PDFs and look before item 5 is approved or the set is
filed. Fixing it would mean one more in-memory override in the build script, like the S1.2
precedent (`DECISIONS.md` lines 414-420). This record does not make that change.

## 5. Draft decision-log entries (not applied)

### 5.1 Top of the Physics decision log

Items 5 and 6 are in square brackets. Keep each one only if Matt confirms it, and delete it
otherwise. The `Status:` line must then match.

```markdown
### 2026-11-18 — One-time exceptions: "3.2 Practice Set - Net Force"
Matt asked for a net-force practice set on Section 3.2 and chose from offered options in chat.
Departures from the standing Physics rules, for this one set only:

1. **One section of 12 in three parts, ramp 2 warm-up / 4 practice / 5 challenge / 1 multi-topic.**
   Matt chose "Cut to 2 pages", offered as fewer problems, about 4 per part instead of 6, with the
   parts running together. The ramp override is how that choice was built. Matt did not ask for it
   separately. Built with a one-time in-memory override of `RAMP["physics"]` and of the
   question/key renderers (part sub-headings) in
   `templates/worksheet/specs/build_phys_u03_s03.2_net_force.py`. The 2/2/1/1 ramp
   (SHULL-CHG-0019) is unchanged.
2. **No graph-reading item.** Matt: "Skip it this time (Recommended)". This waives the
   graph-reading rule under "Physics-specific build rules" for this set only.
3. **Named "3.2 Practice Set - Net Force".** Matt: "3.2 Practice Set - Net Force (Recommended)".
   "Net Force" is a descriptor. 3.2 has no short-title row and none is added.
4. **Everyday objects, not characters.** Matt: "use something someone might use in an every day
   scenario". This departs from the 2026-09-14 character-scenario convention for this set only.
[5. **No tier tags on the student copy or the key.** Matt confirmed this for this set on <date>:
   "<his words>". It follows his "remove this on the text boxes" for the FBD set.]
[6. **g = 9.8 m/s² is treated as exact for significant figures** (for example 15.0 kg × 9.8 m/s²
   = 147 N). Confirmed by Matt on <date>: "<his words>". See the standing entry above, if recorded.]

**Scope, stated plainly:**
1. Scoped to this one set: `3.2 Practice Set - Net Force.docx`/`.pdf` and its `3.2 Practice Set Key
   - Net Force` files, built from `templates/worksheet/specs/phys_u03_s03.2_net_force.json`.
2. **Not a precedent.** A future set needing any of these exceptions needs its own explicit request
   and its own record. It may not cite this one.
3. `templates/worksheet/build_worksheet_docx.py`, `templates/worksheet/build_worksheet_key_docx.py`,
   `standards/NAMING.md` and the worksheet skills are **not** modified.

Supersedes: None.
Status: CONFIRMED · SHULL-CHG-0074 — Path A (course-specific; shared builders untouched, only used via a documented one-time override).
```

### 5.2 Separate standing entry, only if Matt confirms item 6 as a standing convention

This is a course-wide convention, not a one-off, so it is a separate entry. It needs its own quoted
answer in `Decision:`.

```markdown
### 2026-11-18 — g = 9.8 m/s² is exact for significant figures
In Physics answer keys and self-check brackets, g = 9.8 m/s² is treated as an exact constant. It
does not limit significant figures, and answers keep the precision of the measured givens (15.0 kg ×
9.8 m/s² = 147 N, not 150 N). Matt, <date>: "<his words>".
Supersedes: No written rule.
Status: CONFIRMED · SHULL-CHG-0074
```

**Placement question.** The entry's rule could instead be one sentence under "Sequencing —
CONFIRMED" (sig figs, lines 83-93), with the log entry pointing at it, as the ∑F entry points at its
rule paragraph. Either way the rule lives in one place.

## 6. Questions for Matt (one at a time, in this order)

1. **Tier tags, this set.** "Hide the difficulty tags on the 3.2 Net Force set, on both the student
   copy and the key, as on the FBD set?" Ask after the section 4 check, so he is told whether they
   currently show.
2. **g and sig figs.** "Treat g = 9.8 m/s² as exact, so 15.0 kg gives 147 N rather than 150 N?" If
   yes: "Make that the standing Physics rule?"
3. (Optional, not blocking.) The ramp override was not put to him as such. The main session may want
   to tell him that "Cut to 2 pages" was built as 2/4/5/1.

## 7. What this record does not do

- It does not edit `courses/`, `templates/`, `standards/`, any skill or any output. Nothing is
  implemented and nothing is committed.
- It does not add a `3.2` short-title row.
- It does not implement or interpret SHULL-CHG-0062.
- It does not add a `change-log/CHANGELOG.md` row. The main session adds that when it commits this
  record.
