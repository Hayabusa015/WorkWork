# T-7 — Acceptance test

**Date:** 2026-09-08 · **Subject:** Chemistry U01 S1.4, Isotopes · **Deliverable:** section slide deck
**Verdict:** **PASS, with the Librarian step held for the user.**

The test is "build one real Chemistry deliverable through the chain." It found nine defects. Seven
were in the system, not the deck — including three in checks written the same day. That is the
result worth recording: the deck was the bait, the chain was what was under test.

---

## What the chain caught, in the order it caught it

| # | Found by | Severity | Defect |
|---|---|---|---|
| 1 | Overseer, reading standards | MAJOR | `standards/NAMING.md` stale in two places |
| 2 | `pdffonts` | MAJOR | a stray DejaVu Sans run in the first real deck |
| 3 | T-10 probe | **BLOCKER** | a deck built for a section that does not exist |
| 4 | T-10 probe | **BLOCKER** | the task report accepted WORK COMPLETE over a failed step |
| 5 | Auditor | **BLOCKER** | clipped text on slide 6 |
| 6 | Auditor | **BLOCKER** | a worked example with no solution slide |
| 7 | Auditor | MAJOR | a caption standing where a diagram belongs |
| 8 | Auditor | MAJOR | twelve empty image wells and no way to get prompts |
| 9 | Auditor | MAJOR + 10 minors | section numeral, voice, sequencing, grammar |

### 1 — the standard the build read was stale

`NAMING.md` still said Geology renaming was blocked pending CONFLICT-25, closed by CHG-0009 four
commits earlier, and still described the in-document chip as spanning slides, which CHG-0013
withdrew the previous day. The `naming` **skill** had been updated. The **standard** had not.

The two-place problem, in the system built to prevent it. Fixed.

### 2 — a font substitution nothing else could see

pptxgenjs turns `addText` aimed at a placeholder the master never declared into a plain text box in
a default font. Silently. `02_SECTION_TITLE` has no eyebrow; `build_deck` was adding one to every
slide. Geometry audit: clean. Contrast: clean. Only `pdffonts` saw it.

`build.js` now collects each master's placeholder names **as the masters are defined** — a registry,
not a list maintained beside them — and `build_deck` refuses any field the master does not declare.

### 3 — a deck for a section that does not exist

`build_deck` produced a finished deck footered `U01 • S01.4` for section **1.9**. U1 has five
sections. `validate_codes.py` did not catch it either, because a deck spec states its code in
structured fields rather than in a `SHULL_` filename.

This is the Geology numbering failure exactly — the one the naming standard was written to stop, and
the one that would print on a packet. Step 0 of the workflow says confirm the code in the decisions
file; that rule lived only in a document. **A rule in a document is not a mechanism.** Both sides
closed: the builder checks before building, and the validator understands deck specs.

### 4 — the report could claim a completion it had not earned

The schema accepted `WORK COMPLETE` with the auditor marked `fail` and a clipped slide named in its
own note. It enforced the verified-location half of its rule and not the no-failed-step half.

That is the precise dishonesty the file exists to make impossible, and it was possible. Tightened;
the cases are permanent in `validate_schemas.py`, which went from 9 to 12.

### 5 — clipped text, and the check that should have caught it

Two step-card bodies on slide 6 were sliced through the glyph bodies by the card's bottom edge.

`audit_slide_geometry.py` reported clean. It checked box-against-box and never text-against-its-own
container. `build_deck`'s cap counted explicit newlines, so it saw two lines where the renderer
wrapped three.

The audit now measures real wrapped extent using advance widths from the shipped Archivo files, and
compares against **the card behind the text, not the text box** — overflowing a text box is not the
defect, because PowerPoint lets text spill and nothing is lost; running past the card edge is,
because the edge slices it. First run of the corrected check reproduced both clips and nothing else.

### 6 — a worked example with no solution

`Your Turn: Potassium-40` shipped with an empty work area and no solution slide. The numbers 19 p,
21 n, 19 e appeared nowhere in the deck. It was also the deck's only formative check, so as built
the class would never have found out whether it got K-40 right.

Named as a bug in four separate places in this repository. Written anyway. **Every rule in this
system is one an author can walk past unless something checks it.**

### 7 and 8 — the deck could not actually be finished

Slide "Two Ways to Write the Same Isotope" showed neither way: the diagram slot held a *description*
of a figure. And twelve image slots were empty with no prompts anywhere, so there was no path from
the JSON to a usable deck.

- `scripts/build_diagram_nuclear_notation.py` builds the carbon-14 figure — hand-built, from
  `tokens.json` colours and the shipped Archivo files, because anything carrying a number or a label
  is built, never generated.
- `build_deck` gained image support that places into a **named slot**, never at coordinates. A deck
  that could place an image anywhere is a deck that can invent geometry.
- `scripts/image_prompts.py` is step one of the documented image loop, which had no mechanism.
  **It refuses to guess.** A slot with no declared subject gets no prompt — it gets a line telling
  the author to say what the picture is. A prompt derived from a headline produces an image that
  could belong to any slide in any deck, which is the standard's own definition of slop.

### 9 — the Auditor was right about the writing too

Section numeral reading `01` on section 1.4. A subhead explaining how the slide was built. A key
question arriving after slide 2 had already answered it. `does` for `do` in the one line students
are told to copy. A must-write carrying two unrelated ideas. And 1.5's conclusion handed to students
as 1.4's required note — the term-ordering rule, inverted.

All fixed. Two template-level findings fixed with them: three "parallel" cards had the third one
dark, putting the deck's strongest emphasis on tritium; and the `PROBLEM` panel competed with the
must-write bar as a second black block.

---

## Auditor independence — T-8, in passing

The Auditor ran as a separate agent with its own context. It was told what to audit and which
standards to read, and nothing about what I had chosen or already fixed.

It returned **FAIL** on work I had already self-reviewed and believed was clean. It found two
blockers I had missed, re-solved every number in the deck independently, and traced the clipping to
the exact line of `build_deck.js` responsible. It also declined to pad: it explicitly recorded what
it could not verify rather than scoring it.

**An auditor that shares the builder's context is not an auditor.** This is the step where the
separation earns its cost.

---

## What is NOT done

- **The deck is not filed to Drive.** The Librarian's log is written
  (`reports/drive-operations/2026-09-08_chem-u01-s01.4-slides.md`) and deliberately not executed. It
  writes into Matthew's live teaching Drive and he has not reviewed the deck.
- **Twelve images are outstanding.** The deck is not classroom-ready. `image_prompts.py` lists them.
- **Empty image wells still render** as dashed boxes. On the divider that is two-thirds of the frame.
  A deck should be able to suppress a well it is not using; it currently cannot. **Open.**
- The section has no guided notes or practice set. Out of scope for this test, and next in the
  documented build order.
