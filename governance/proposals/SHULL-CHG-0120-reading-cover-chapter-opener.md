# SHULL-CHG-0120 — Unit reading cover: chapter-opener layout (A), with wrapping Key Refreshers

> **Amends two IMPLEMENTED records in part. Neither record is edited.**
> - SHULL-CHG-0119 (`governance/proposals/SHULL-CHG-0119-unit-reading-stacked-cover.md`): its
>   "Cover layout" paragraph is replaced in full. The block order, the "about four lines" length,
>   the 1–4 How to Use steps and the scope-in-time sentence carry over unchanged.
> - SHULL-CHG-0117 (`governance/proposals/SHULL-CHG-0117-unit-reading-key-refreshers.md`): the
>   "one-line items" requirement in its Key Refreshers paragraph and audit bullet is replaced, and a
>   heading variant is allowed. Placement, the 2–5 count, the "Unit N (N.n):" opening, reminders
>   only, no bold, no tear-off questions, sourcing, and omission when there is no earlier unit all
>   stay.
>
> **This record changes nothing Matt asked for in his own words.** The "one-line" limit came from
> Matt ("Just make it a quick review", SHULL-CHG-0117 Source). Loosening it to "may wrap within its
> column" comes from mockup A as rendered, not from anything Matt said. He chose A ("I like A"),
> and A wraps its items. His approval of this record is what settles that point (see Source).
>
> **One layer: Path B, a build rule** (`governance/CHANGE_CONTROL.md` §1). The rule applies to unit
> readings in all three courses. No course fact changes, and no `DECISIONS.md` entry is needed.
>
> **ID allocation.** SHULL-CHG-0119 is the highest ID in the local checkout, and no file in the
> working tree mentions SHULL-CHG-0120 or a higher number. The main session has to confirm 0120 is
> free on a freshly fetched `origin/main` before committing (§2). Until that push, this ID is not
> allocated.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0120 |
| **Date** | 2026-11-26 |
| **Source** | User. Matt, main session. On 2026-11-25, of the stacked cover just implemented under SHULL-CHG-0119: "I still don't like this, could you give me 3 setups to choose from" (typed as "setupsnto"). Three mockups were rendered: A chapter opener, B two-panel, C clean minimal (`templates/reading/build_reading_docx.py`, `front.layout` `"mockA_opener"`, `"mockB_panel"`, `"mockC_minimal"`, marked temporary in the code). On 2026-11-26: "I like A". **Not in Matt's words:** every specific in the proposed text (the numeral, the vertical rule, the larger intro size, the In This Unit sidebar, the full-width refresher box with hairline columns, the "Before You Begin · Key Refreshers" heading, wrapping items, the single How to Use row, outlines and rules only) describes mockup A as built (`front_mock_a()`). Matt chose the rendering. He did not comment on any detail. |
| **Current Rule** | `workflows/unit-textbook.md`, "Prepare the unit reading and its detachable submission", item 1, as quoted in full under "Current and replacement text" below. That covers the Key Refreshers paragraph (SHULL-CHG-0117 text A) and the Cover layout paragraph (SHULL-CHG-0119), plus the "Independent accuracy and print review" bullet that begins "Check the Key Refreshers block" (SHULL-CHG-0117 text B). |
| **Proposed Rule** | Three replacements, quoted in full below: (a) the Cover layout paragraph, (b) the Key Refreshers paragraph, (c) the Key Refreshers audit bullet. Item 1's first paragraph ("**Cover.** Introduce the unit…") does not change, and items 1–5 keep their numbers. |
| **Supersedes** | In part: (1) SHULL-CHG-0119's Cover layout paragraph in `workflows/unit-textbook.md` item 1, replaced in full. (2) SHULL-CHG-0117 text A (Key Refreshers paragraph, item 1) and text B (audit bullet), only in "one-line items" / "two to five one-line items" and in the heading. The rest of their wording is kept. The 0117 and 0119 records and their changelog rows are not edited (append-only, `change-log/CHANGELOG.md`). This record's changelog row names them. |
| **Reason** | Matt rejected the stacked cover after seeing it built and chose mockup A from three alternatives. Layout A sets the refreshers as side-by-side columns, so a reminder that fits one full-width line has to wrap in a column about a third as wide. The 0117 "one-line" wording would make A non-compliant. The heading A prints ("Before You Begin · Key Refreshers") is also not allowed by the current text. |
| **Affected Agents** | Textbook Page Designer (builds the cover). Auditor (checks it against the revised bullet). Overseer (commissions readings and routes the U6 rebuild). Secretary (implementation only, after approval). `.claude/agents/textbook-page-designer.md` defers to the workflow and needs no change. |
| **Affected Skills** | None. `.claude/skills/verify-content/SKILL.md`, `.claude/skills/build-document/SKILL.md` and `standards/QA_GATE.md` do not describe the reading cover. |
| **Affected Courses** | Chemistry, Physics and Geology (all unit readings). No course fact changes. |
| **Risk** | Medium, because of the builder. Mockup A is temporary code with gaps the rule would expose. (1) **Item count.** The rule allows 2–5 refreshers, but `front_mock_a()` lays out exactly three columns. With one table item and two text items it renders them in the U6 order. With 2 items it fails (IndexError). With 4 or 5 items it **silently drops** items after the third. (2) **No refreshers.** It reads `fr["refreshers"]` without a default, so a course's first unit, which omits the block, crashes the build. (3) **How to Use.** The strip has three step cells. A fourth step is silently dropped, and one or two steps leave empty cells. (4) **No checks.** `check_front()` returns early for mock layouts, and `check_refreshers()` skips the width check, so neither the 1–4 step count nor any refresher length limit is enforced. (5) **"Short" is not measurable.** The revised wording gives the Auditor no line limit to check (see Open choices). (6) **Re-audit.** The Chemistry U6 reading's Round 4 audit PASS (`reports/chem_u06_reading_textbook_audit.md`) was for the stacked cover. A layout A rebuild needs a new audit round before filing. U6 is not yet filed (`reports/filing-queue.md`, row "Unit 6 Reading - Nomenclature", Ready), so no reading carries the stacked cover. |
| **Recommendation** | Approve, on condition that the builder work in "Implementation" step 2 is done under this ID before the next reading is built. Matt should answer the open choices below first. Each one changes the text he is approving. |
| **Decision** | 2026-11-26, user, in the main session. Asked "Approve SHULL-CHG-0120: cover layout A (chapter opener) for every new or revised reading in all three courses, plus the Key Refreshers update (items may wrap within their column; optional 'Before You Begin' heading), with the wording shown above?" (texts (a) and (b) were shown): "Approve". Asked "How long can one refresher be inside its column?" with options "At most 3 lines" and "Just 'short'": "Just 'short'" (no hard line limit; judged by eye). The count stays 2–5 and the heading stays optional, as drafted. |
| **Status** | **APPROVED** |
| **Implemented By** | pending commit; builder side by the U6 layout A rebuild |
| **Verified** | — |

---

## Current and replacement text in `workflows/unit-textbook.md`

### (a) Cover layout paragraph: item 1, third paragraph, replaced in full

**Current (SHULL-CHG-0119):**

> **Cover layout.** Set the cover in one column, in this order: the unit title; **Why It Matters**,
> a short paragraph of about four lines; **In This Unit**, the section list; **Key Refreshers**, when
> the block applies; **How to Use This Reading**, one to four short numbered steps that describe the
> reading and its tear-off leaf as they are printed; then the first section. Start each block with a
> caps label, put a rule between blocks, and use no fills. This applies to every new or revised unit
> reading in all three courses. A reading filed before SHULL-CHG-0119 keeps its cover unless the
> teacher asks for this layout at a revision.

**Replacement:**

> **Cover layout.** Open the cover like a chapter, in this order: a title block with a large "Unit"
> numeral and a thick vertical course rule beside the display title; **Why It Matters**, an unboxed
> intro paragraph of about four lines set slightly larger than the body text, with an outlined **In
> This Unit** box listing the sections beside it on the right; one full-width outlined **Key
> Refreshers** box, when the block applies, with each refresher in its own column and hairlines
> between the columns; **How to Use This Reading**, a single quiet row of one to four short numbered
> steps that describe the reading and its tear-off leaf as they are printed, just above the first
> section; then the first section. Use outlines and rules only, with no fills. This applies to every
> new or revised unit reading in all three courses. A reading filed before SHULL-CHG-0119 keeps its
> cover unless the teacher asks for this layout at a revision.

### (b) Key Refreshers paragraph: item 1, second paragraph

**Current (SHULL-CHG-0117 text A):**

> **Key Refreshers.** After the section list and Why It Matters, and before the first section, print
> a short **Key Refreshers** block. Give two to five one-line items, each in the form "Unit N (N.n):
> concept reminder". Each item names the earlier unit and section where the idea was covered, e.g.
> "Unit 3 (3.7): Metals lose electrons to become cations; nonmetals gain electrons to become anions."
> These are reminders only: no teaching, examples, bold terms or tear-off questions. Source the facts
> like the rest of the reading. Omit the block when there is no earlier unit. This applies to every
> new or revised unit reading in all three courses. A reading filed before SHULL-CHG-0117 gets the
> block only on a revision, and only if the teacher asks.

**Replacement** (only the first two sentences change):

> **Key Refreshers.** After the section list and Why It Matters, and before the first section, print
> a short **Key Refreshers** block; its heading may read "Before You Begin · Key Refreshers". Give two
> to five items. Each item is one short reminder that opens with "Unit N (N.n):" and may wrap within
> its column on the cover. Each item names the earlier unit and section where the idea was covered,
> e.g. "Unit 3 (3.7): Metals lose electrons to become cations; nonmetals gain electrons to become
> anions." These are reminders only: no teaching, examples, bold terms or tear-off questions. Source
> the facts like the rest of the reading. Omit the block when there is no earlier unit. This applies
> to every new or revised unit reading in all three courses. A reading filed before SHULL-CHG-0117
> gets the block only on a revision, and only if the teacher asks.

### (c) Audit bullet in "Independent accuracy and print review"

**Current (SHULL-CHG-0117 text B):**

> - Check the Key Refreshers block: it sits before the first section and has two to five one-line
>   items. Each item names an earlier unit and a section that exists in the course decisions. Trace
>   each reminder to that section. Confirm it has no bold term, teaching or example, and that no
>   tear-off question draws on it.

**Replacement:**

> - Check the Key Refreshers block: it sits before the first section and has two to five items. Each
>   item is one short reminder that opens with "Unit N (N.n):" and names an earlier unit and a
>   section that exists in the course decisions. Trace each reminder to that section. Confirm it has
>   no bold term, teaching or example, and that no tear-off question draws on it.

## Open choices for Matt (one at a time; each changes the text above)

| # | Question | Draft answer | Why it matters |
|---|---|---|---|
| 1 | Should a wrapped refresher have a length limit, e.g. "at most three lines in its column"? | None. The text says "short" | Without a limit, neither the builder nor the Auditor can fail a refresher that has grown into teaching. The old one-line rule could be checked. "Short" cannot. |
| 2 | Keep 2–5 refreshers, or match A's three columns? | Keep 2–5 (unchanged from 0117) | A as built handles exactly three. Keeping 2–5 means the builder has to lay out 2, 4 and 5 columns (or wrap to a second row). Limiting the count would change a rule Matt approved under 0117. |
| 3 | Is the heading "Before You Begin · Key Refreshers" required or optional? | Optional ("may read") | The coordinator's instruction was to allow it. A required heading would be one more thing the Auditor checks. |

## Affected files and implementation (after approval, in this order)

| File | Change |
|---|---|
| `workflows/unit-textbook.md` | Texts (a), (b), (c), verbatim |
| `templates/reading/build_reading_docx.py` | Promote mockup A to a real layout; remove mockups B and C |

1. **Secretary:** replace the three texts verbatim in one commit that carries SHULL-CHG-0120. Items
   1–5 keep their numbers.
2. **Builder** (build tooling, not a protected directory; do it under this ID): promote
   `front_mock_a()` to a named `front.layout` (e.g. `"opener"`) and make it the default. Keep
   `"columns"` (the U7 pin). Decide with the Overseer whether `"stacked"` is kept or removed. Delete
   mockups B and C and the three "MOCKUP" hook lines, as the code comment at the head of the mockup
   block instructs. Close the gaps in Risk 1–4: support 2–5 refreshers with no silent drop, build
   with no refreshers, support 1–4 How to Use steps with no silent drop, and restore
   `check_front()` / `check_refreshers()` for the new layout (a wrap limit if choice 1 sets one).
   Update the `0117` and `0119` comments on `REFRESH_MIN/MAX` and `FRONT_LAYOUTS`.
3. **Not part of this record:** rebuilding and re-auditing the Chemistry U6 reading in layout A.
   That is classroom work and goes through the Overseer (CLAUDE.md §6).

## Verification plan (for a checker other than the implementer)

1. The implementing diff to `workflows/unit-textbook.md` replaces exactly texts (a), (b), (c).
   Item 1's first paragraph and items 2–5 are byte-identical.
2. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass, and
   `hook-validate.sh` reports clean.
3. Builder: build test specs with 0, 2, 3, 4 and 5 refreshers and with 1–4 How to Use steps. Every
   case builds with every item present, and the no-refresher case prints no box. A 5-step spec and
   a 1- or 6-refresher spec fail. `chem_u07_reading.json` still builds as `"columns"`.
4. Fill in `Implemented By` with the commit SHA(s) and `Verified` with the results.
