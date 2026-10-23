# SHULL-CHG-0054 — Guided notes follow the slides: every block names its slide

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0054 |
| **Date** | 2026-10-23 |
| **Source** | User, 2026-10-23. Students told the user that the guided notes do not follow the slides well enough. He asked for improvements. The main session proposed four rules and three later items. He chose to *"start with 1-4"* for Chemistry Unit 1, was shown a rendered mockup (Chem U1 S1.3: slides 11-14 and the two notes pages), and said, verbatim: *"Yeah 1-4 looks correct now finish writing the rest."* Earlier in the same conversation he answered *"3. Yes"* to building the next Chemistry unit the same way. The main session relayed these words, so the Secretary did not hear them directly. **None of these statements approves this record.** They are the finding it is written from. |
| **Current Rule** | See section 1, verbatim, with file and section. |
| **Proposed Rule** | See section 2. The authoritative statement lives in `templates/notes/README.md` and `templates/slide/README.md`. |
| **Supersedes** | Nothing is removed. See section 3. In short: it makes the `build-document` SKILL "one object" sentence enforceable; it extends the `templates/slide/README.md` must-write rule; and it partly reverses **SHULL-CHG-0038** choice (d) in spirit only. No block numbers return. It also covers rebuilding the Chemistry U1 notes, which SHULL-CHG-0038 recorded the user declining on 2026-09-23. |
| **Reason** | The rule that the notes and the deck are one object existed but nothing enforced it. An audit of the Chemistry U1 notes against their deck (section 4) found titles that did not match, no slide named anywhere in the notes, a worked example split across a page turn, missing blanks and must-write lines, a key that disagreed with the slide, and lime "write this" blocks on the wrong slides. The students' complaint is the result. |
| **Affected Agents** | Designer (builds to it). Auditor (checks it). |
| **Affected Skills** | `build-document` (`.claude/skills/build-document/SKILL.md`, "Guided and Cornell notes"). `build-presentation` (`.claude/skills/build-presentation/SKILL.md`). Both point at the template READMEs and do not restate the rules. |
| **Affected Courses** | All three: Chemistry, Physics and Geology (the rules are in shared templates). Chemistry U1 is rebuilt now. Existing Physics and Geology specs have no `"deck"` field and build unchanged. |
| **Risk** | Low-medium. Existing specs are unaffected unless they opt in with `"deck"` (notes) or `"notesPacket"` (slides). The slide template's `MUST WRITE` label became a placeholder (`mwlabel`) that `build_deck.js` always fills, so every deck build now passes through new code. |
| **Recommendation** | Approve as written. The user has already seen and accepted the rendered result of rules 1-4. |
| **Decision** | (blank) |
| **Status** | **PENDING** |
| **Implemented By** | (blank) |
| **Verified** | (blank) |

---

## 1. Current Rule, verbatim

`.claude/skills/build-document/SKILL.md`, "## Guided and Cornell notes", first paragraph:

> **The notes and the deck are one object.** A student should look at a slide and know exactly which
> blank it fills. **Locate the section deck first.** If it does not exist, build it first or say the
> notes are provisional.

Nothing in the notes builder or the slide builder enforced it.

`templates/slide/README.md`, "The rules the layouts encode", first bullet (kept unchanged, and
extended by rule 3 below):

> - **One must-write bar per slide, never two.** Two write-this cues means students copy neither.

## 2. Proposed Rule

The four items the user chose. **The authoritative statement is `templates/notes/README.md`, "The
notes and the deck are one object", with the slide half in `templates/slide/README.md`, "The rules
the layouts encode".** The two skills point there. The summary below is what was proposed; where it
and the READMEs differ, the READMEs win and the difference is a defect in this record.

1. **Every notes block names its slide(s).** Spec field `"slides"` (`12` or `[13, 14]`) prints
   `SLIDE 12` / `SLIDES 13–14` under the cue label. RECALL prints `NO SLIDE · CLOSE YOUR NOTES`;
   RECAP and REVIEW print `NO SLIDE` unless given slides. Switched on by a top-level spec field
   `"deck"`; with it, a fill-in block without `"slides"` is refused.
2. **A block's title is its slide's headline, word for word; blocks follow slide order; one
   slide's blocks are never split across a page turn.** The build refuses out-of-order slides and a
   slide split across pages. The headline match is checked by eye: the build has slide numbers, not
   slide text.
3. **A must-write (lime) block appears only on a slide with a matching notes blank, and names that
   block** (`✎ IN YOUR NOTES: <block title>`). A slide with nothing new to write gets `CHECK YOUR
   WORK · nothing new to write` instead. In the twelve-layout template: slide field `"notes":
   "<title>"` or `"notes": false`; the bar's label reads `CHECK ONLY` for `false`; a deck spec with
   `"notesPacket"` must give one or the other on every bar slide; only masters 03, 07, 09 and 10
   have a bar.
4. **A fill-in is the slide's own sentence with its key words blanked** (generator helper
   `F("…{word}…")`). The key prints the finished sentence in the same place.

### Not in scope (the user chose 1-4 only)

- Generating the notes outline from the deck file.
- An automated slide-text match check.

## 3. Supersedes

| Rule | From | Effect |
|---|---|---|
| "The notes and the deck are one object…" | `.claude/skills/build-document/SKILL.md`, "Guided and Cornell notes" | Kept. Made enforceable; the skill now points at `templates/notes/README.md`. |
| "One must-write bar per slide, never two." | `templates/slide/README.md`, "The rules the layouts encode" | Kept. Extended: the bar names the notes block it fills, or reads check-only. |
| Choice (d): drop the `01`, `02` block numbers | SHULL-CHG-0038, Decision | **Reversed in spirit only.** The cue column again carries a locator, but it is the slide label, not a block number. **No block numbers return.** |
| *"no dont rebuild"* (the Chem U1 notes, 2026-09-23) | SHULL-CHG-0038, Decision | The user's 2026-10-23 instruction *"finish writing the rest"* covers rebuilding Chem U1 now. 0038's record is not edited. |

## 4. The audit that motivated it

Chemistry U1 notes spec `templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py` against the
Drive deck *Unit 1 - Matter and Atomic Theory Notes.pptx* (22 slides, Drive ID
`1_U_6sqdSUQbAW3RA8C2x8I9uvqm_XEpi`). Verified by the main session, 2026-10-23.

| # | Finding |
|---|---|
| 1 | Sections and their order matched. |
| 2 | 8 block titles did not match their slide headlines. |
| 3 | Nothing in the notes named a slide. |
| 4 | Part A (iron-56) and Part B (calcium-40) of the slide 13 worked example were split across a page turn. |
| 5 | Slide 17's formula had no blank in the notes; it appeared only in the cover toolbox. |
| 6 | The must-write lines on slides 12 and 17 were missing from the notes. |
| 7 | The key said "Mixture — homogeneous" where slide 9 says "Solution". |
| 8 | Lime "write this" blocks were on nearly every slide, including the solution slides 14, 19 and 21; the work slides 13, 18 and 20 had none. |

## 5. Two defects fixed in the same change

Both enforce an already-approved rule, **SHULL-CHG-0023** (notes are recall; no questions). They are
fixes, not new rules.

| # | Defect | Fix |
|---|---|---|
| a | `templates/notes/recall.py` read rows only from old flat specs (`section["rows"]`), never from paged specs (`pages[].rows`). The paged Chem U1 packet shipped with question cues such as "Why is O₂ not a compound?". | Reads paged specs. The rebuilt U1 cues name the thing to record. |
| b | `templates/notes/build_notes_docx.py` `validate()` returned `1` (truthy) when `recall.check` found questions, so `main()` treated it as a pass and built anyway. | A recall failure now stops the build. |

## 6. Affected files

Implementation is by the main session acting as Designer. **None of these is a Secretary-only path.**
No `brand/`, `standards/` or `courses/` file changes.

- `templates/notes/build_notes_docx.py`
- `templates/notes/recall.py`
- `templates/notes/README.md`
- `templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py`, and its `_student` / `_key` JSON
- `templates/slide/build.js`
- `templates/slide/build_deck.js`
- `templates/slide/README.md`
- `.claude/skills/build-document/SKILL.md`
- `.claude/skills/build-presentation/SKILL.md`

## 7. Known limitations

1. **The Chem U1 deck predates the twelve-layout template** (Poppins/Lato, lime blocks). Its
   `IN YOUR NOTES` / `CHECK YOUR WORK` tabs were added to the built `.pptx` by a one-off patch, not
   by `build_deck.js`. Rule 3 is enforced by the build only for decks built from the template.
2. **Pre-existing defect noticed, not fixed.** Slides 19 and 21 of the original deck clip the last
   line of their bottom block text. Fixing it is a content change to the user's deck and is outside
   this record.

## 8. Verification required before this is IMPLEMENTED

- [ ] The Chem U1 notes (student and key) rebuild with `"deck"` set and every fill-in block carrying
      `"slides"`; the build passes.
- [ ] A spec with `"deck"` and a fill-in block missing `"slides"` is refused.
- [ ] A spec with out-of-order slides is refused, and so is one slide's blocks split across pages.
- [ ] A paged spec with a question cue is refused (defect a), and the refusal stops the build
      (defect b).
- [ ] Existing Physics and Geology specs (no `"deck"`) build unchanged.
- [ ] A deck spec with `"notesPacket"` and a bar slide giving neither `"notes": "<title>"` nor
      `"notes": false` is refused; a deck without `"notesPacket"` still builds, with the bar label
      filled.
- [ ] Block titles match slide headlines, checked by eye against the deck, slide by slide.
- [ ] `build-document` and `build-presentation` point at the template READMEs and do not restate the
      four rules.
- [ ] The commit message carries `SHULL-CHG-0054`, and `Implemented By` and `Verified` are filled in
      here.
