# SHULL-CHG-0118 — Tear-off vocabulary: students write the definitions

> **No conflict with a LOCKED rule.** It replaces the printed-reference part of item 5 of the reading
> format set by SHULL-CHG-0107 (IMPLEMENTED) and the matching audit sentence. The ten-term limit, the
> duplex tear-off, the front page and the SHULL-CHG-0117 Key Refreshers block are unchanged. Nothing
> CONFLICT, PROVISIONAL or UNKNOWN is converted.
>
> **One layer: Path B, a build rule** (`governance/CHANGE_CONTROL.md` §1). It applies to unit
> readings in all three courses, so it belongs in the workflow (CLAUDE.md §2 test). No course fact
> changes, and no `DECISIONS.md` entry is needed.
>
> **ID allocation.** No `SHULL-CHG-0118` exists in the local checkout's `governance/proposals/`. The
> main session confirms the ID is free on a freshly fetched `origin/main` before this record is
> committed. Until it is pushed, the ID is not allocated (`governance/CHANGE_CONTROL.md` §2).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0118 |
| **Date** | 2026-11-25 |
| **Source** | User. Matt, main session, 2026-11-25, while working on the Chemistry U6 reading: "Also for the vocabulary. I want the students to write the definitions" and "I don't want them prefilled in" (typed as "refilled"). He was then asked: "For the tear-off back, students would see the 10 terms with blank lines and write each definition themselves, finding it bolded in the reading. Should this apply only to Unit 6, or become the rule for every unit reading?" He chose "Rule for all readings (Recommended)", whose option text read: "Change the textbook rule (SHULL-CHG-0107) so every reading's tear-off back lists the terms with write-in lines. Unit 6 follows now. Unit 7 is filed with printed definitions and changes only if you ask." |
| **Current Rule** | `workflows/unit-textbook.md`, "Prepare the unit reading and its detachable submission", item 5: "**Reverse — vocabulary.** On the last even-numbered page, print each selected term alongside its student-friendly definition. Match each word and its meaning to its bold first definition in the reading. This side is a printed vocabulary reference. Assign vocabulary writing only when the teacher requests it. Supply expected comprehension responses in the separate teacher key." And in "Independent accuracy and print review", the bullet beginning "Audit the **exported student PDF** for the detachable leaf", the sentence: "Confirm at most ten printed term–definition pairs and trace each to its bold in-text definition." |
| **Proposed Rule** | Two replacements in `workflows/unit-textbook.md`, quoted in full under "Exact text" below: (A) item 5 (Reverse — vocabulary) is replaced, and (B) the vocabulary sentence in the "Audit the **exported student PDF**" bullet is replaced. |
| **Supersedes** | The printed-reference part of SHULL-CHG-0107 item 5 (`governance/proposals/SHULL-CHG-0107-textbook-reading-and-tear-off.md`: "print up to ten terms with their student-friendly definitions on the reverse"), as written in `workflows/unit-textbook.md` item 5 ("print each selected term alongside its student-friendly definition … This side is a printed vocabulary reference. Assign vocabulary writing only when the teacher requests it.") and in the audit sentence "Confirm at most ten printed term–definition pairs…". The rest of SHULL-CHG-0107 stands. |
| **Reason** | Matt wants students to write the definitions themselves rather than receive them pre-filled. Writing each definition makes students locate the bold term in the reading and read its defining sentence, which the printed reference did not require. He chose to make this the rule for every unit reading. |
| **Affected Agents** | Textbook Page Designer (builds the reverse and the key). Auditor (revised check). Overseer (routes the U6 revision as classroom work). Secretary (implementation only, and only on approval). `.claude/agents/textbook-page-designer.md` defers to the workflow and needs no change. |
| **Affected Skills** | None. `.claude/skills/verify-content/SKILL.md` and `standards/QA_GATE.md` do not list the reading format. `standards/NAMING.md` §2 mentions the tear-off leaf only to describe a Reading and needs no change. |
| **Affected Courses** | Chemistry, Physics and Geology (all unit readings). No course fact changes. Chemistry U6 follows the new rule now (classroom work, via the Overseer). Chemistry U7 is filed with printed definitions and is unchanged unless Matt asks. |
| **Risk** | Low. (1) **Writing space.** Ten terms with handwriting lines take more room than ten printed pairs. The reverse is one page, so the builder must fit ten terms with enough lines, or the term count or line count has to be resolved with the teacher (the same fit rule as the front). (2) **Builder.** `templates/reading/build_reading_docx.py` currently prints the definitions on the reverse; until it changes, a reading cannot follow the rule. (3) **Students keep no printed glossary on the leaf.** The definitions stay in the reading pages that students keep (bold term plus the set-off definition line), so the retained packet is still a complete reference. |
| **Recommendation** | Approve. Matt's choice above named this exact change; the text below is the wording for it. |
| **Decision** | 2026-11-25, user, in the main session, answering "For the tear-off back, students would see the 10 terms with blank lines and write each definition themselves, finding it bolded in the reading. Should this apply only to Unit 6, or become the rule for every unit reading?": "Rule for all readings (Recommended)" (option text: "Change the textbook rule (SHULL-CHG-0107) so every reading's tear-off back lists the terms with write-in lines. Unit 6 follows now. Unit 7 is filed with printed definitions and changes only if you ask."). |
| **Status** | **APPROVED** |
| **Implemented By** | pending commit; builder side by the U6 rebuild |
| **Verified** | |

---

## Exact text for `workflows/unit-textbook.md`

**(A) Replaces item 5** of "Prepare the unit reading and its detachable submission" in full. It keeps
the number 5, because `templates/reading/build_reading_docx.py` cites "workflows/unit-textbook.md
steps 3-5".

> 5. **Reverse — vocabulary.** On the last even-numbered page, list each selected term (up to ten)
>    with ruled write-in space for the student's own definition. Do not print the definitions.
>    Students find each definition where the term is bolded in the reading. Allow enough handwriting
>    space for a one- or two-sentence definition; if the page crowds, simplify the layout before
>    reducing the lines, and resolve a genuine fit problem with the teacher. Supply the expected
>    comprehension responses and the expected definitions in the separate teacher key, with each
>    definition worded as in the reading.

**(B) Replaces one sentence** in the "Independent accuracy and print review" bullet that begins
"Audit the **exported student PDF** for the detachable leaf". The sentence "Confirm at most ten
printed term–definition pairs and trace each to its bold in-text definition." becomes:

> On the reverse, confirm that at most ten terms are listed, that no definition is printed, and that
> each term traces to its bold in-text definition. Check that each term has adequate ruled space for
> a handwritten definition, and that each definition in the teacher key matches the reading's
> wording.

The rest of that bullet is unchanged.

## The choices this record makes

| Question | Answer in the rule | Why |
|---|---|---|
| Scope | Every unit reading, all three courses | Matt chose "Rule for all readings (Recommended)". |
| What the reverse shows | Each selected term, up to ten, with ruled write-in space; no printed definitions | "I want the students to write the definitions"; "I don't want them prefilled in". |
| Where students find the definition | Where the term is bolded in the reading | The option Matt answered: "finding it bolded in the reading". Item 2 already requires the meaning in the bolding sentence or the next. |
| Key | Expected definitions, worded as in the reading, alongside the comprehension responses | The key checks student work against the reading's own definition, so the reading stays the single source of the wording. |
| "Assign vocabulary writing only when the teacher requests it" | Removed | Writing the definitions is now the default on every reading. |
| Fit | Same approach as the front: simplify layout first, then resolve with the teacher | Keeps one fit rule for both sides of the leaf. |
| Chemistry U6 / U7 | U6 follows now; U7 unchanged unless Matt asks | The option text Matt chose. Recorded only here, so the course-specific case lives in one place; the workflow states the general rule. |
| Workflow line "The tear-off is the short reading-comprehension assignment." | Left as written | Outside the scope Matt answered. If it should also name the vocabulary, that is a separate wording question. |

## Affected files and implementation (after approval, in this order)

| File | Change |
|---|---|
| `workflows/unit-textbook.md` | Text (A) and (B), verbatim |
| `templates/reading/build_reading_docx.py` | Reverse renders write-in lines instead of definitions; key heading and docstrings updated (step 2) |
| `templates/reading/specs/chem_u06_reading.json` | `tearOff.vocabNote` reworded for write-in use (step 3, classroom work) |

1. **Secretary:** replace item 5 with text (A) and the audit sentence with text (B) in
   `workflows/unit-textbook.md`, in one commit that carries SHULL-CHG-0118.
2. **Builder** (build tooling, not a protected rule directory; do it under this record's ID): in
   `templates/reading/build_reading_docx.py`, `tear_off()` reverse, replace the definition column
   (`definition_text(v)`) with ruled handwriting lines (e.g. `write_lines`, as the front uses), keeping
   the term and its section code. Add a fit check that fails the build when ten terms with the
   minimum lines do not fit on the one reverse page. In `build_key`, rename the heading
   "Vocabulary (page N) — the ten printed definitions" to name them as expected definitions. Update
   the module docstring (lines describing the reverse as "the ten terms and definitions") and the
   `tear_off()` docstring. The set-off definition lines in the reading body are unchanged.
3. **Not part of this record:** revising the Chemistry U6 reading (`tearOff.vocabNote` currently
   reads "These are the ten bold terms from the reading, defined the same way.") and rebuilding it.
   That is classroom work and routes through the Overseer (CLAUDE.md §6). Chemistry U7
   (`templates/reading/specs/chem_u07_reading.json`) is not touched unless Matt asks.

## Verification plan (for a checker other than the implementer)

1. The implementing commit's diff to `workflows/unit-textbook.md` replaces exactly item 5 with text
   (A) and the one audit sentence with text (B); items 1–5 keep their numbering and the SHULL-CHG-0117
   text is untouched.
2. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
3. After step 2: build a reading spec with ten terms. The student PDF's last even page lists the ten
   terms with ruled lines and no definition text; the key lists the ten definitions in the reading's
   wording. A spec whose reverse cannot fit ten terms with the minimum lines fails the build.
4. Fill in `Implemented By` with the commit SHA(s) and `Verified` with the results.
