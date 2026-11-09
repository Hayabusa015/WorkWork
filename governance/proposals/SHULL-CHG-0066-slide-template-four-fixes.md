# SHULL-CHG-0066 — Slide template: four fixes found by building the sample deck

> **Change ID is provisional.** Allocated as the next integer after `SHULL-CHG-0065` on a freshly
> fetched `origin/main` (2026-11-09). The session that wrote it can push only to its own branch,
> `claude/blissful-dijkstra-xkbx5q`, not to `main`. Under `governance/CHANGE_CONTROL.md` §2 the ID
> is not real until this record reaches `origin/main`. Do not cite it elsewhere before then.
>
> No conflict with a LOCKED rule is known. Item 3 touches the "empty image regions" design recorded
> in SHULL-CHG-0013; the writer has not re-read that record in full, so check it before approving
> item 3.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0066 |
| **Date** | 2026-11-09 |
| **Source** | User. Matt asked the main session on 2026-11-09 to analyse the repository and improve the slides, then said: "yes to A, B, C and draft D and E". This is D. Findings come from building `templates/slide/decks/chem_u01_s01.4_isotopes.json` with `build_deck.js`, running `scripts/audit_slide_geometry.py` on it, and looking at the rasterised slides. The Secretary did not write this record; the main session drafted it at the user's request. |
| **Current Rule** | See §1. |
| **Proposed Rule** | See §2. Four items, each separately approvable. |
| **Supersedes** | Item 1: the `color: C.accent` on the two "PROBLEM" labels in `templates/slide/build.js` (lines 387-389 and 438-440). Item 2: the card `x` and `w` values on the `03_GROUPED_CONCEPT` master (`build.js` lines 241-242). Item 3: nothing; it adds an option. Item 4: `templates/slide/assets/chem_u01_s1.4_nuclear_notation.png` as committed 2026-09-08. |
| **Reason** | Items 1 and 4 are leftovers of SHULL-CHG-0054 (the Chemistry palette change). Item 2 is a geometry error visible in the blank template. Item 3 is the open question logged in `change-log/CHANGELOG.md` on 2026-09-08 ("a deck cannot suppress a well it is not using"). |
| **Affected Agents** | Designer (builds decks), Auditor (item 1 is an audit failure today). |
| **Affected Skills** | `build-presentation` only if item 3 is approved: it would gain one line saying how to leave a well out. |
| **Affected Courses** | Item 1: Chemistry today; the fix is course-independent. Items 2 and 3: all three. Item 4: Chemistry U01 S1.4 only. |
| **Risk** | Low for items 1, 2 and 4. Medium for item 3, because it changes what a master draws. |
| **Recommendation** | Approve items 1, 2 and 4. Decide item 3 after answering the question in §4. |
| **Decision** | Approved by Matthew Shull in chat, 2026-11-09, verbatim: "approve all of 0066 and 0067 option B, leave wells empty". All four items approved. On §4 question 1: unused wells stay empty. §4 question 2 was not answered separately; the approval covers item 1 as proposed (neutral label). |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is not needed; this is a repository-only change. No deck on Drive is rebuilt by
this record.

---

## 1. Current state, with evidence

| # | Layout | What happens now | Evidence |
|---|---|---|---|
| 1 | `09_EXAMPLE_PROBLEM`, and the second problem layout at `build.js:438` | The "PROBLEM" label is the course accent on the dark card. For Chemistry that pair measures 4.48:1. The target in the audit is 5.5:1. | `audit_slide_geometry.py` on the built isotopes deck: 2 problems, slides 8 and 11. The other two courses were not measured this run. |
| 2 | `03_GROUPED_CONCEPT` | Card `c2` is placed at x 9.75 in, width 3.45 in, so it ends at 13.20 in. The slide is 13.333 in wide with a 0.75 in right margin (`slideGeometry` in `brand/tokens.json`), so the content edge is 12.583 in. The card runs 0.62 in into the margin. The must-write bar and footer code stop at the content edge, so the card overhangs both. | `build.js:241-242`; visible on slides 4 and 10 of the built deck and on the blank template. |
| 3 | Every layout with an image slot | A slot with no image renders as a dashed box, some inside a full accent frame. In the built isotopes deck 11 of 13 slides carry an empty well. A deck spec has no way to say "no image here". | `build.js:97` draws the dashed outline in the master. Open since 2026-09-08. |
| 4 | Slide 6 of the isotopes deck | The nuclear-notation figure has green labels. It was built from the Chemistry palette that SHULL-CHG-0054 replaced. | The asset's last commit is 2026-09-08. `scripts/build_diagram_nuclear_notation.py` reads `brand/tokens.json`, so a re-run should pick up the current palette. Not re-run this session. |

## 2. Proposed

**Item 1.** The "PROBLEM" label uses a colour that clears the audit target on the dark card for all
three courses. The simplest choice is the neutral light text the other card labels already use on
dark, which matches the existing rule "course colour is never a small label on a card"
(`templates/slide/README.md`). Verify by re-running the audit on a deck per course: zero problems.

**Item 2.** On `03_GROUPED_CONCEPT` the image slot and the two cards are re-spaced so the right
card ends at the content edge, the same edge as the must-write bar. Widths are taken from
`slideGeometry`, not typed. The audit gains a check that no card or block crosses a side margin,
so this cannot come back unseen.

**Item 3.** A deck spec may mark an image slot as unused. An unused slot draws nothing: no dashed
outline and no accent frame. The layout does not re-flow; the space stays empty. `image_prompts.py`
stops listing a slot marked unused. See the question in §4 first.

**Item 4.** Re-run `scripts/build_diagram_nuclear_notation.py` and commit the new figure. Look at
it before committing.

## 3. What this does not do

- It does not change any token in `brand/tokens.json`.
- It does not rebuild or re-file any deck already on Drive.
- It does not change the literal "SECTION TITLE" label on `02_SECTION_TITLE`. That is a separate
  question for Matt: is the label intended?

## 4. Questions for Matt

1. **Item 3.** When a slot is unused, should the space simply stay empty (proposed, smallest
   change), or should the text beside it widen to use the space? Widening is a larger change to
   the masters and would need its own record.
2. **Item 1.** Neutral label (proposed), or keep it in a course colour and pick a lighter one that
   passes? A new colour would be a token change.

## 5. Verification, once implemented

- `audit_slide_geometry.py` on a built deck for each course: zero problems.
- `pdffonts` on each: Archivo, embedded.
- Every slide of the rebuilt isotopes deck rasterised and looked at.
- `scripts/build_template_previews.py slide` re-run so the gallery shows the fixed layouts.
