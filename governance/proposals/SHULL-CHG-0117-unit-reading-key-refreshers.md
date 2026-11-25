# SHULL-CHG-0117 — Unit readings open with a Key Refreshers block

> **No conflict with a LOCKED rule.** It adds one block to the reading cover and one audit check. The
> ten-term limit, the tear-off format and the cover breakdown in SHULL-CHG-0107 stay as they are.
> Nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.
>
> **One layer: Path B, a build rule** (`governance/CHANGE_CONTROL.md` §1). It applies to unit
> readings in all three courses, so it belongs in the workflow (CLAUDE.md §2 test). No course fact
> changes, and no `DECISIONS.md` entry is needed.
>
> **ID allocation.** The main session confirmed SHULL-CHG-0117 free on `origin/main` and committed
> the first PENDING draft. This revision shortens the rule at Matt's request (see Source).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0117 |
| **Date** | 2026-11-25 |
| **Source** | User. Matt, main session, 2026-11-25, while approving additions to the Chemistry U6 reading. His words: "Lets add something important to the beginning of all these reading that are key refreshers we need that we have done before. On this unit and for future units. I want to make this a rule". After reviewing the first draft of this record he asked for it shorter: "Just make it a quick review. Unit we covered it and a quick concept reminder." The rule text below is the shortened version. |
| **Current Rule** | `workflows/unit-textbook.md`, "Prepare the unit reading and its detachable submission", item 1: "**Cover.** Introduce the unit and give students its breakdown: list the confirmed numbered sections in order with their short topic titles. Use those same section numbers and sequence throughout the reading and response sheet." The "Independent accuracy and print review" section has no check for prior-unit content on the cover. The builder (`templates/reading/build_reading_docx.py`, `front()`) lays out the cover as the title, "In this unit" list and how-to line on the left, Why It Matters on the right, with the chapter starting below on the same page. |
| **Proposed Rule** | Two additions to `workflows/unit-textbook.md`, quoted in full under "Exact text" below: (A) a **Key Refreshers** paragraph appended to item 1 (Cover), and (B) a new bullet in "Independent accuracy and print review". |
| **Supersedes** | `workflows/unit-textbook.md` "Prepare the unit reading…" item 1 (Cover), which lists only the breakdown. This record adds to that item and does not replace it. SHULL-CHG-0107 (`governance/proposals/SHULL-CHG-0107-textbook-reading-and-tear-off.md`) is not changed. |
| **Reason** | Matt asked for it as a rule. A unit reading is handed out before the unit starts, so students meet the new material without a reminder of the earlier skills it uses. The U6 nomenclature reading depends on ion charges from 3.7 and on ionic and covalent bonding from U4. Opening with those prerequisites lets students check what they need before the first section. |
| **Affected Agents** | Textbook Page Designer (writes the block). Overseer (supplies the confirmed prerequisites at commissioning, step 1). Researcher (sources the block's facts like the rest of the reading). Auditor (new check). Secretary (implementation only, and only on approval). `.claude/agents/textbook-page-designer.md` needs no change: it defers to the workflow and does not list the format. |
| **Affected Skills** | None. `.claude/skills/verify-content/SKILL.md` and `standards/QA_GATE.md` do not list the reading format, so the workflow's audit section is the only place to add the check. `standards/NAMING.md` describes a Reading only to explain its filename and needs no change. |
| **Affected Courses** | Chemistry, Physics and Geology (all unit readings). No course fact changes. |
| **Risk** | Low. (1) **Page budget.** The block adds two to six lines to page 1 and pushes the first section down. A reading close to its page budget may gain a page, and the even-page and tear-off parity checks still apply. (2) **Builder support.** `build_reading_docx.py` has no field for the block. Until one is added (see "Implementation"), a reading cannot carry it. (3) **Gap in the source data.** No course `DECISIONS.md` lists prerequisites per unit. Unit roadmap specs with `builds_on` exist only for Chemistry (`templates/unit-roadmap/specs/chem_u*.json`), and their entries are not always section codes: `chem_u06.json` lists "U4 · Ionic vs. covalent bonding", and `chem_u07.json` lists "U6 · Writing chemical formulas" and a reference-packet line. So the rule requires each item to name a unit and section that exist in the course decisions file (CLAUDE.md §3). A unit-only `builds_on` entry has to be resolved to a section before it can be used, and reference-packet entries are left out. |
| **Recommendation** | Approve. Each open choice is answered below. If any answer is wrong, it can be changed before approval. |
| **Decision** | 2026-11-25, user, in the main session, answering "Approve the shortened Key Refreshers rule (SHULL-CHG-0117): 2–5 one-line items on the cover, each naming the unit (and section) where it was covered plus a quick concept reminder, reminders only, for every new or revised unit reading in all three courses?": "Approve". |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `01d0d05e4563e5c95d4ad6c5248861b45e090e1f` (Secretary, 2026-11-25). Step 1: text (A) appended to `workflows/unit-textbook.md` item 1 (Cover) as a second paragraph, and bullet (B) inserted after the "Audit the **exported student PDF**" bullet in "Independent accuracy and print review"; items 1–5 keep their numbering. Step 2: the optional builder field `front.refreshers` was already added to `templates/reading/build_reading_docx.py` during the Chemistry U6 build (commit 15968a1, "U6 reading: Key Refreshers box…"), not in this implementation. Its shape differs from step 2 as written: entries are `front.refreshers.items[]` of `{ "codes": ["4.2", "4.3"], "text": "…" }` (one or more codes from one earlier unit, label "Unit N (codes):"), with an optional `title`. It enforces the 2–5 count, no `**`, the one-line fit, codes present in the course decisions, and an earlier unit. |
| **Verified** | Yes, 2026-11-25. The main session ran `hook-validate.sh` on commit 01d0d05 and got "validators clean", and confirmed that the workflow contains the Key Refreshers rule text (A) and audit bullet (B). The Secretary confirmed that both texts are in `workflows/unit-textbook.md`, item 1 and the "Independent accuracy and print review" list, with items 1–5 unrenumbered. Builder: `front.refreshers` was exercised by the Chemistry U6 build. The export prints three one-line items, in the forms "Unit 3 (3.7): …" and "Unit 4 (4.2, 4.3): …", per the main session. The negative-case builds in verification-plan step 3 (1 or 6 items, a bold entry, an over-long entry, an unknown code, a same-unit code) were not run separately. The builder enforces each of these in `check_refreshers()` / `refresher_label()`. |

---

## Exact text to add to `workflows/unit-textbook.md`

**(A) Appended to item 1 (Cover)**, as a second paragraph of that item. It is not a new numbered
item: renumbering would make items 3–5 stale where `templates/reading/build_reading_docx.py` cites
them ("workflows/unit-textbook.md steps 3-5").

> **Key Refreshers.** After the section list and Why It Matters, and before the first section, print
> a short **Key Refreshers** block. Give two to five one-line items, each in the form "Unit N (N.n):
> concept reminder". Each item names the earlier unit and section where the idea was covered, e.g.
> "Unit 3 (3.7): Metals lose electrons to become cations; nonmetals gain electrons to become anions."
> These are reminders only: no teaching, examples, bold terms or tear-off questions. Source the facts
> like the rest of the reading. Omit the block when there is no earlier unit. This applies to every
> new or revised unit reading in all three courses. A reading filed before SHULL-CHG-0117 gets the
> block only on a revision, and only if the teacher asks.

**(B) New bullet in "Independent accuracy and print review"**, inserted directly after the bullet
that begins "Audit the **exported student PDF** for the detachable leaf":

> - Check the Key Refreshers block: it sits before the first section and has two to five one-line
>   items. Each item names an earlier unit and a section that exists in the course decisions. Trace
>   each reminder to that section. Confirm it has no bold term, teaching or example, and that no
>   tear-off question draws on it.

## The choices this record makes

| Question | Answer in the rule | Why |
|---|---|---|
| Placement | Full width on the cover, after "In this unit" and Why It Matters, before the first section heading | The cover is a two-column table: a narrow left column with the title, list and how-to line, and Why It Matters on the right. The chapter starts below it on page 1. A full-width block in that gap is read immediately before section 1 and needs no new page. Placing it above Why It Matters would push the hook down, and the narrow left column has no room for 2–5 items. |
| Source | Overseer-confirmed prerequisites (commissioning step 1), plus roadmap `builds_on` where it exists; every item names a unit and section that exist in DECISIONS | The decisions files list no prerequisites per unit, and only Chemistry has roadmap specs. Without this requirement, an item could cite a code that appears only in a skill file (CLAUDE.md §3). This guidance stays in the record; the workflow text was kept short at Matt's request. |
| Earlier units only | Yes | Matt's words were "we have done before" and "Unit we covered it". The reading is handed out at the start of the unit, so nothing from the same unit has been taught yet. |
| Count and form | 2–5 items, one line each, "Unit N (N.n): concept reminder" | Matt's refinement: "Just make it a quick review. Unit we covered it and a quick concept reminder." |
| Bold and tear-off | No bold; outside the ten; no tear-off question | The ten-term limit and the one-question-per-section tear-off from SHULL-CHG-0107 stay as written. The block is not a numbered section, so it gets no question. |
| Verification | Facts sourced like the rest of the reading; Auditor traces each item to the cited section | Same evidence standard as the rest of the student page. |
| First unit of a course | The block is omitted | There is no earlier unit to draw on. |
| Scope in time | All new readings and all revisions. Readings filed before this rule (Chemistry U7) add it only on request at a later revision. | "On this unit and for future units" means U6 onward in Chemistry and readings built from now on in Physics and Geology. U7 was filed before the rule, so it is optional and gets no forced reprint. The workflow text gives the general rule. The U7 case is recorded only here, so the course fact lives in one place. |

## Affected files and implementation (after approval, in this order)

| File | Change |
|---|---|
| `workflows/unit-textbook.md` | Text (A) and (B), verbatim |
| `templates/reading/build_reading_docx.py` | Optional `front.refreshers` list, with build checks (step 2) |

1. **Secretary:** add text (A) and (B) to `workflows/unit-textbook.md`, verbatim, in one commit that
   carries SHULL-CHG-0117.
2. **Builder support** (build tooling, not a protected rule directory; do it under this record's ID):
   add an optional `front.refreshers` list to `templates/reading/build_reading_docx.py`. Each entry
   should be `{ "code": "3.7", "text": "…" }`. Render it full width between the cover table and the
   first section, under the label "Key Refreshers", with each line printed as
   "Unit N (N.n): text" (unit taken from the code). The build should fail when the list has fewer
   than 2 or more than 5 entries, when an entry does not fit on one line at the cover's full width,
   when an entry contains `**`, when a code is not a section in the course decisions, or when a
   code's unit is not earlier than the spec's unit.
3. **Not part of this record:** adding the block to the Chemistry U6 reading
   (`templates/reading/specs/chem_u06_reading.json`). That is classroom work and routes through the
   Overseer (CLAUDE.md §6). A likely source for its items is `templates/unit-roadmap/specs/chem_u06.json`
   `builds_on` (3.7 Ion Formation; U4, which still has to be resolved to section codes such as 4.2 and
   4.3 against `courses/chemistry/DECISIONS.md`). The Overseer confirms the final items.

## Verification plan (for a checker other than the implementer)

1. The implementing commit's diff to `workflows/unit-textbook.md` adds exactly text (A) and (B), and
   the numbering of items 1–5 does not change.
2. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
3. If step 2 of Implementation is done: build a test spec with 1, 2, 5 and 6 refreshers, then with a
   bold entry, an over-long entry, an unknown code and a same-unit code. Only the 2- and 5-item cases build. The rendered
   page 1 shows the block after Why It Matters and before the first section.
4. Fill in `Implemented By` with the commit SHA(s) and `Verified` with the results.
