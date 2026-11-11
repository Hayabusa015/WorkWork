# SHULL-CHG-0071 — Every table cell is centred, horizontally and vertically, in every document

> **ID note.** IDs up to `SHULL-CHG-0070` are taken on other branches. The main session checked
> `origin` and supplied 0071. The Secretary that drafted this record had no shell and could not run
> `git fetch origin main` itself (`governance/CHANGE_CONTROL.md` §2, "Allocating a new Change ID").
> Under that rule the ID is not allocated until this file is pushed to `origin/main`. The main
> session must check the fetched `origin/main` again before it commits.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0071 |
| **Date** | 2026-11-11 (drafted) |
| **Source** | User, 2026-11-11, in the main session. The Secretary did not hear him directly; his words are as the main session relayed them. He edited the tables of the PhET activity (`templates/worksheet/specs/chem_u05_s05.3_phet_shapes.json`, Chemistry 5.3, *Molecular Geometry with PhET*) in Word himself and sent a screenshot. In his edit every table cell is centred horizontally and vertically: the header row and every body cell, the first column included. His words: *"note what i did with centering in the tables. i need this to be consistant in all documents from here on out, make it a rule and approve thew change in the repo"*. **This record is not the approval.** The main session records his decision under `governance/CHANGE_CONTROL.md` §4 once this record exists. |
| **Current Rule** | **No written rule on cell alignment exists.** `brand/SHULL_DESIGN_SYSTEM.md` §8: *"**Table rows use hairline borders**, never alternating solid shading. If shading is genuinely needed for scanability, use a very light grey tint — never a brand colour at medium or full saturation."* §11: *"Dense tabular content uses real tables, never card or flexbox grids."* Neither says how a cell's contents are aligned. Alignment today is whatever each builder does (§1). |
| **Proposed Rule** | See §2a. One new subsection, `### Tables`, in `brand/SHULL_DESIGN_SYSTEM.md` §11, stating that every cell of every table is centred horizontally and vertically, header and body, the label column included, student and key copies alike. No exceptions by default (§4). |
| **Supersedes** | **No written rule.** It supersedes the **unwritten built behaviour** listed in §1: `templates/_shull_docx.py` `fillin_table` (header cells left-aligned and top-aligned; body cells left-aligned, vertically centred), `templates/practice/build_practice.py` question tables (left, top), and the lab HTML templates' `text-align: left` on `th` and `vertical-align: top` on the key's `td`. **Also, pre-emptively:** the notes-table alignment "vertically centered, left-justified" on the unmerged branch `claude/bold-edison-rclt4e` (§3). That text is not in any committed record or standard the Secretary can see, so there is nothing committed to supersede; if that branch is ever merged, its left-justified rule conflicts with this one and this one governs. Not superseded: §8's hairline-border and light-tint rules, and SHULL-CHG-0033's tint on fill-in table header rows. |
| **Reason** | (1) Matt asked for it in plain terms: consistent "in all documents from here on out", and "make it a rule". (2) The builders disagree with one another today (§1): the practice builder already centres its equation tables, `fillin_table` left-aligns, the lab templates left-align and top-align. "One table style in the system rather than two" (`build_worksheet_docx.py` `table_block` docstring) is the intent, but alignment was never written down, so each builder chose. (3) A rule that lives only in a builder is a fact with no authoritative home (CLAUDE.md §1). The design system is the home for a design rule that affects all three courses. |
| **Affected Agents** | Designer (builds every document with a table; applies the rule). Auditor (checks it at QA). Secretary (this record and the design-system edit). No responsibility changes; no agent file is edited. |
| **Affected Skills** | `build-document` and `build-assessment` build tables through the shared templates; neither states an alignment, so neither is edited. They follow the design system. If a skill is found to state an alignment at implementation time, it is changed to point here, not to restate. |
| **Affected Courses** | **All three: Chemistry, Physics, Geology.** It changes all three courses, so it is a design rule (CLAUDE.md §2, Path B). No `courses/*/DECISIONS.md` edit. |
| **Risk** | **Low.** Visual only; no content, naming, filing or ink change. Two real risks, both caught by the verification plan (§7): a long-text cell that reads worse centred (§4 candidates), and a layout table (cards, Cornell columns) centred by mistake if the implementation reaches too far (§2a, definition; §4 Q1). One revertible commit per layer. |
| **Recommendation** | Approve §2a as written, with **no exceptions** (his "consistent in all documents"). Two points to put to him before or with approval, one at a time: **Q1** the definition of "table" that keeps layout grids out (§4); **Q2** whether any §4 candidate is an exception. If he says nothing on Q2, the default is no exceptions. Rule applies to documents built from approval forward; finished files on Drive are not rebuilt ("from here on out"). |
| **Decision** | Approved by the user, 2026-11-11: "note what i did with centering in the tables. i need this to be consistant in all documents from here on out, make it a rule and approve thew change in the repo" |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Current behaviour — what each table code path does today

None of this is a written rule. It is what the code does, read on 2026-11-11.

| # | Code path | Used by | Header cells | Body cells |
|---|---|---|---|---|
| 1 | `templates/_shull_docx.py` `fillin_table()`, lines 535–601 | Worksheets, activities and their keys (via `table_block`); guided notes and keys (via `build_notes_docx.py` line 665) | `para(...)` with no `align`, no `vertical_alignment` (lines 579–585): **left, top** | `c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER` (line 594); `para(...)` with no `align` (lines 595–600): **left, vertically centred** |
| 2 | `templates/worksheet/build_worksheet_docx.py` `table_block()`, lines 359–408 | Worksheet / activity `"kind": "table"` blocks (PhET 5.3, VSEPR 5.3, EN bond type 4.5) | Inherits #1 | Inherits #1; picture cells set `WD_ALIGN_PARAGRAPH.CENTER` (line 405), so the Sketch column is already centred horizontally |
| 3 | `templates/worksheet/build_worksheet_key_docx.py` line 175 | Worksheet keys | Calls `table_block(..., key=True)`: inherits #1 | Inherits #1 |
| 4 | `templates/notes/build_notes_docx.py` line 665 | Guided / Cornell notes `"table"` rows | Calls `fillin_table`: inherits #1 | Inherits #1 (`label_bold=False`) |
| 5 | `templates/practice/build_practice.py` question tables, lines 336–343 (`q["table"]`, built with `table()` at line 111) | Practice sets (`templates/practice/specs/chemistry.json`) | `para(cell, txt, 9.5, i==0, first=True, after=0)`, no `align`, no vertical alignment: **left, top** | Same: **left, top** |
| 6 | `templates/practice/build_practice.py` equation grid, lines 212–227 | Practice sets | n/a | Already `WD_ALIGN_VERTICAL.CENTER` and `WD_ALIGN_PARAGRAPH.CENTER` (lines 222, 227). **Already compliant** |
| 7 | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` `table.data`, lines 215–224 (reference data table, e.g. accepted densities, used at line 510) | Labs | `text-align: left` (line 218) | No alignment set: **left**, browser-default vertical middle |
| 8 | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` `.tbl td`, lines 204–212 (single-column data-table skeletons students copy into the notebook, used at lines 380–406) | Labs | n/a (caption is a `div`, not a cell) | No alignment: **left**. `.tbl td.note` is `text-align: right` (line 211) |
| 9 | `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` `table.grid`, lines 65–70 (prep, timing, expected-results tables, used at lines 101, 115, 136) | Lab teacher keys | `text-align: left` (line 67) | `vertical-align: top` (line 69), left |

**Not tables in the reader's sense** (layout grids: Word tables used to place things on the page,
mostly borderless). Listed so the implementation does not touch them by accident (§4 Q1):

- `_shull_docx.py`: `one_cell` (line 333), the given/need, work-box, cue-column and diagram scaffolds
  (lines 420, 447, 459, 496, 526, 617).
- `build_worksheet_docx.py`: the question cards and header bars (lines 173, 204, 222, 486, 493, 658,
  686, 770); the draw-it panels (line 241); the sort block (line 272); the match block (line 302);
  the reflection block (line 328).
- `build_notes_docx.py` `table()` (line 332) and its callers: the Cornell cue/notes grid (lines 820,
  953), title bars (843, 1096), cover boxes (1117, 1130, 1142), the cover's "Sections in this unit"
  checklist (1154), the equation toolbox (1182), the concept-review rows and compare columns (1230,
  1244); nested scaffolds at 392, 572, 614, 745, 988.
- `templates/notes/SHULL_Notes_TEMPLATE.html` / `build_notes.py` `table.cornell` (the Cornell layout).
- `build_practice.py` card and layout uses of `table()` (lines 202, 218, 224, 307, 324, 372, 388).
- Slides: `templates/slide/` builds no tables (`addTable` appears nowhere). Slides are not in his list.

---

## 2. Proposed Rule

### 2a. Text to add to `brand/SHULL_DESIGN_SYSTEM.md`

**Where.** A new subsection at the end of **§11 Documents**, after the bullet *"Dense tabular content
uses real tables, never card or flexbox grids."* §11 is where tables are already introduced; §8
keeps its print-ink rule (hairline borders, light tint) and is not edited. No new top-level section,
so no section is renumbered and no existing `§` reference breaks.

**Exact text:**

```markdown
### Tables

**Every cell is centred, horizontally and vertically.** The header row and every body cell, the
first (label) column included. Student copy and key alike. This holds in every SHULL document that
has a table: worksheets, practice sets, activities, guided and Cornell notes, keys, labs,
assessments, and reference sheets. There are no exceptions. SHULL-CHG-0071.

A *table* here is a grid the reader sees as rows and columns: a header row naming the columns, or
bordered cells holding values, blanks to fill in, or pictures. A grid used only to place things on
the page (a question card, the Cornell cue and notes columns, a title bar, a two-column layout) is
page layout, not a table, and this rule does not reach it.

Borders and header shading are §8's rule, not this one.
```

If Matt names exceptions under §4 Q2, the sentence "There are no exceptions." is replaced by one
line per exception, each naming the table and its alignment. Nothing else changes.

### 2b. What the rule covers, as a list

| Applies to | Yes |
|---|---|
| Header row | Yes, horizontal and vertical |
| Body cells | Yes, horizontal and vertical |
| First / label column ("Proton", "Cl-35", "Domains") | Yes |
| Key copies, including bold key answers | Yes; weight is unchanged, only alignment |
| Picture cells (e.g. the PhET Sketch column) | Yes; already centred horizontally, now vertically too |
| Blank cells | Yes (the cursor lands centred when typed into in Word) |
| Layout grids (§1, "Not tables") | **No**, by the definition in §2a (§4 Q1) |
| Finished files already on Drive | **No retrofit.** "From here on out." A file is brought into line when it is next rebuilt |

---

## 3. Conflicts

| Item | Status | Finding |
|---|---|---|
| Unmerged branch `claude/bold-edison-rclt4e`: notes tables "vertically centered, left-justified" | Not on main; not in any committed record or standard the Secretary can see | **Conflicts** with this record on horizontal alignment. Searched outside `legacy/` and `node_modules/` for "left-justif", "left-align", "centred", "centered", "vertically cent", and for "table" near "align/justif/cent/left": no standard, skill, agent or proposal states a left-justified table rule. The Secretary has no shell and **could not inspect the branch itself**; the main session should confirm the branch was never merged and has no open PR. If it is merged later, this record governs and the branch's rule must be dropped in the merge. |
| `fillin_table` header left/top, body left | Unwritten, built | Superseded by implementation (§5 item 2) |
| Lab templates `text-align: left` / `vertical-align: top` | Unwritten, built (templates from SHULL-CHG-0010 / 0031; neither record states an alignment) | Superseded by implementation (§5 items 4–5) |
| `brand/SHULL_DESIGN_SYSTEM.md` §8 hairline borders, light tint | LOCKED-equivalent design rule | **No conflict.** Kept; the new text points to it |
| SHULL-CHG-0033: `pal.surface` tint on fill-in table header rows | IMPLEMENTED | **No conflict.** Kept |
| `standards/ANTI_AI_SLOP_STANDARD.md` line 80: "tables used for paragraphs of prose" is a slop marker | Standard | **Supports** no exceptions: a table should not hold prose, so centred prose should not arise. Where it does (§4), the fix is usually the content, not the alignment |
| `fillin_table` docstring: key answers are bold "because a table cell has no left edge to draw one on" | Code comment | No conflict; the bold-for-answers convention is unchanged |

No LOCKED rule is contradicted. Nothing here is resolved by the Secretary; Matt's approval settles
the record.

---

## 4. Open questions for Matt — one at a time

**Q1 (asked first; it changes what the implementation touches).** *"When you say every table, do you
mean the grids that look like tables (a header row and boxed cells, like the PhET one), and not the
invisible grids the templates use to lay out a page, like the Cornell cue column or question cards?"*
Default and recommendation: **yes, visible tables only** (the definition paragraph in §2a). Without
it, a literal reading would centre the Cornell notes column and every question card, which is not
what his screenshot shows.

**Q2.** *"Any table where centring would get in the way?"* His words point to **no exceptions**, and
that is the default. Candidates the Secretary found, for him to keep centred or exempt:

| # | Table | Why it might be an exception | Secretary's proposal |
|---|---|---|---|
| a | Lab teacher key, prep table `DETAIL` column and timing table `WATCH FOR` column (`SHULL_Lab_TEMPLATE_TEACHER_KEY.html` lines 101–121) | Full sentences ("Exact recipe: g of solid, to what final volume, in what vessel."). Centred multi-line prose is ragged on both edges | Keep centred (no exception). Teacher-only, short. If it reads badly at the visual check, raise it then |
| b | Lab `.tbl` notebook skeletons (`SHULL_Lab_TEMPLATE_MASTER.html` lines 380–406) | Single column of row labels "with (units)" that students copy; and the `td.note` cell ("next class") is right-aligned on purpose as a margin note | Centre the row labels. Treat `td.note` as an annotation, not a table cell: leave it right-aligned **only if he agrees**; otherwise centre it |
| c | Worksheet match block (`build_worksheet_docx.py` line 302) and sort block (line 272) | Drawn with Word tables, but read as a question format, not a table; descriptions can be long | Classified as layout under Q1, so **not covered**. If he says they are tables, centre them |
| d | Notes cover "Sections in this unit" checklist with a `DIFFICULTY` column (`build_notes_docx.py` line 1154) | Has a header and rows, so it looks like a table; checkboxes sit at the left of each line | Classified as layout under Q1 (a checklist), **not covered**. If he says it is a table, centre it |

If he answers Q2 with nothing or "no exceptions", §2a stands as written and candidates a–b are
centred; c–d follow his Q1 answer.

---

## 5. What implementation touches

**Two layers, two commits, both citing SHULL-CHG-0071.** The Secretary edits the rule; the main
session edits the code. Neither is bundled with anything else.

| # | File | Who | Change |
|---|---|---|---|
| 1 | `brand/SHULL_DESIGN_SYSTEM.md` §11 | **Secretary** | Add the §2a `### Tables` subsection verbatim (amended only by his Q1/Q2 answers) |
| 2 | `templates/_shull_docx.py` `fillin_table()` lines 579–600 | Main session | Header cells: `c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER` and `align=WD_ALIGN_PARAGRAPH.CENTER` on the header `para`. Body cells: keep vertical centring (line 594); add `align=WD_ALIGN_PARAGRAPH.CENTER` to both `para` calls (label column and the rest). Update the docstring to cite SHULL-CHG-0071 by pointer, not restate the rule. This one change carries #3 and #4 |
| 3 | `templates/worksheet/build_worksheet_docx.py` `table_block()` | Main session | No code change expected; inherits #2. Confirm the picture-cell path (line 402–406) still centres; add nothing unless the visual check shows a picture cell sitting off-centre vertically |
| 4 | `templates/worksheet/build_worksheet_key_docx.py`, `templates/notes/build_notes_docx.py` line 665 | Main session | No code change expected; both call #2. Confirm by rebuild |
| 5 | `templates/practice/build_practice.py` lines 336–343 | Main session | For each cell in the question table: `cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER`; pass `align=WD_ALIGN_PARAGRAPH.CENTER` to `para`. The equation grid (lines 212–227) is already compliant; leave it |
| 6 | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 204–224 | Main session | `table.data th` and `table.data td`: `text-align: center; vertical-align: middle`. `.tbl td`: same. `.tbl td.note`: per Q2 (b) |
| 7 | `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` lines 65–70 | Main session | `table.grid th`: `text-align: center; vertical-align: middle`. `table.grid td`: `vertical-align: middle` (replacing `top`) and `text-align: center` |
| 8 | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.pdf`, `SHULL_Lab_TEMPLATE_TEACHER_KEY.pdf` | Main session | Regenerate from the edited HTML (`templates/lab/build_lab.py`) so the reference PDFs match |
| 9 | `change-log/CHANGELOG.md` | Main session | Row for 0071 |
| 10 | `courses/*/DECISIONS.md` | — | **None.** All three courses, so a design rule |
| 11 | `standards/QA_GATE.md` | — | **Not included by default.** An optional one-line check ("table cells centred, `SHULL_DESIGN_SYSTEM.md` §11 Tables") pointing to the rule would help the Auditor. It is a separate change; include it only if Matt's approval names it |

Layout grids (§1, "Not tables") are **not** edited. A grep for `add_table` and `<table` is not a
to-do list; most hits are layout.

Assessment builders: none exists under `templates/` as a separate builder. Assessments built through
the worksheet or practice paths inherit items 2 and 5. If an assessment builder is added later, it
follows §2a.

---

## 6. Rollback

- **Rule.** The Secretary's design-system edit is one commit carrying `SHULL-CHG-0071`. `git revert
  <sha>` removes the `### Tables` subsection; no other section moves, so no reference breaks.
- **Code.** The main session's code edit is one commit carrying `SHULL-CHG-0071`. `git revert <sha>`
  restores the §1 behaviour exactly (left-aligned headers and bodies, top-aligned lab key cells).
  Revert both commits together; reverting only one leaves the rule and the builders disagreeing,
  which is the drift this system exists to prevent.
- **Drive.** No Drive mutation is part of this change. Documents rebuilt and filed under the new rule
  are ordinary new versions; nothing is moved or trashed.

---

## 7. Verification plan — only after APPROVED and implemented

Run by the main session in its shell (the Secretary has none); results recorded in `Verified`.

1. **Rebuild the worksheet specs with tables**, student and key:
   `templates/worksheet/specs/chem_u05_s05.3_phet_shapes.json` (his source document),
   `chem_u05_s05.3_vsepr_structures.json`, `chem_u04_s04.5_en_bondtype.json`. All build without error.
2. **Rebuild the notes specs**, student and key: `templates/notes/specs/make_chem_u04-u05_notes.py`
   and `make_chem_u01_s01.1-s01.5_notes.py` (both use `"table"` rows). All build without error.
3. **Rebuild the Chemistry practice set** (`templates/practice/specs/chemistry.json`, the one spec
   with a question table) and run `templates/practice/test_practice.py`.
4. **Rebuild the lab template PDFs** (§5 item 8).
5. **Validators:** `python3 scripts/validate_profiles.py` passes (15 refusals fire, 2 allowances
   hold, 4 real specs build). Also run `validate_notes`, `validate_tokens`, `validate_layers`,
   `validate_references`, `validate_schemas`, `validate_codes`, `validate_agents`; report counts.
6. **Structural check, not just a look:** open the rebuilt PhET `.docx` with `python-docx` and assert,
   for every cell of every `table_block` table, `cell.vertical_alignment == CENTER` and every
   paragraph `alignment == CENTER`, header row included. Same for one notes table.
7. **Visual check:** render the PhET student copy and key to PDF and compare with Matt's screenshot:
   header row, the `Domains` label column, the filled key cells and the Sketch picture all centred
   both ways. Check one notes page with a fill-in table, the practice question table, and the lab
   reference table.
8. **Layout untouched:** on the same renders, the Cornell cue column, question cards, title bars,
   match and sort blocks are unchanged from before the commit (left-aligned as they were).
9. **Grep:** the alignment rule is stated only in `brand/SHULL_DESIGN_SYSTEM.md` §11; code comments
   point to it by Change ID and do not restate it.
10. Fill in `Implemented By` (both SHAs) and `Verified` here.
