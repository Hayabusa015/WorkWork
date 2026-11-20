# SHULL-CHG-0075 — Print: mirror binding margin and three-hole guides, all courses

> **Implementation status: PARTIAL.** The documentation and token side is applied (uncommitted at
> the time of writing): `brand/tokens.json` (`print.binding`, `print.holeGuides`),
> `brand/SHULL_DESIGN_SYSTEM.md` §8, `standards/QA_GATE.md` §2, the `build-lab` and
> `build-document` skills, `templates/lab/README.md`, and the CHANGELOG row. The builders (section
> 3), the hole-zone audit, and the test punch (section 5) are still to do. **The section 7 questions
> are answered by the main-session defaults in `Decision:`.** Where those defaults differ from
> section 2, the Decision wins. The guide weight is hairline (`0.25pt`), not the 0.75 pt in
> section 2.1/2.2.
>
> **Path B (build and brand change), all three courses.** It touches `brand/`, `standards/`, two
> skills, and every print builder. No course `DECISIONS.md` is changed.
>
> **Conflict with a rule described as locked. Marked here, not resolved.** The lab skill says
> "**Margins are locked.**" (`.claude/skills/build-lab/SKILL.md` line 33). The lab template says the
> margins "are the confirmed SHULL print standard and are locked"
> (`templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 31 and 37). The token those files point to is
> labelled **PROVISIONAL** (`brand/tokens.json` line 482). Approving this record changes the lab
> margins. The lock and the PROVISIONAL label already contradict each other (section 4). This record
> does not decide which label was right.
>
> **Finding, not fixed here.** The print margins are already set in six places with three different
> values, and only one builder reads the token (section 4, table B). This record does **not** unify
> them, because that is a separate change. It only requires that the new inside margin and hole
> guides come from tokens.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0075 |
| **Date** | 2026-11-20 |
| **Source** | User. Matt's request in chat on 2026-11-20, his answers to two offered questions, and his amendment "well, just make it a slight push.", all quoted verbatim in section 1 as relayed to the Secretary by the main session. The dimensions in section 2 are the main session's translation of "a slight push" (0.60 in inside, +0.25 in on the token value). Matt has not seen the numbers. |
| **Current Rule** | (1) `brand/tokens.json` lines 477-483, `print.margins`: `"top": "0.30in", "left": "0.35in", "right": "0.35in", "bottom": "0.45in", "status": "PROVISIONAL"`. (2) `.claude/skills/build-lab/SKILL.md` line 33: "**Margins are locked.** Never adjust them to fix a page count; reduce body size or line-height." `templates/lab/README.md` lines 81-82: "**Margins.** Per `brand/tokens.json` → `print.margins`. **Don't touch them to fix a page-count problem**". (3) `standards/QA_GATE.md` lines 39-40: "If over, fix **in this order**: reduce `@page` margins → reduce base font size → tighten line-height → reduce block bottom margins." Restated in `.claude/skills/build-document/SKILL.md` line 150. (4) No rule for binding, duplex or punch holes anywhere in `brand/`, `standards/` or the skills. A grep for "binding", "hole" and "punch" finds none. (5) `brand/SHULL_DESIGN_SYSTEM.md` §8 "Print discipline — a hard rule" (lines 223-249) sets scope ("worksheets, practice sets, guided and Cornell notes, labs, study guides, reference sheets") but says nothing about margins. |
| **Proposed Rule** | Section 2 (the rule), section 3 (scope and builders), section 6 (exact text to add). |
| **Supersedes** | `brand/tokens.json` `print.margins` (lines 477-483) for the binding side only. `.claude/skills/build-lab/SKILL.md` line 33 and `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 31 and 37-40 ("locked" margins), for the binding side. `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` line 25. `standards/QA_GATE.md` §2 lines 39-40 and `.claude/skills/build-document/SKILL.md` line 150, to the extent that "reduce `@page` margins" would let the inside margin shrink. |
| **Reason** | Matt three-hole punches everything. A typical punch centres its holes about 0.38 in from the edge with a diameter of about 0.26 in, so a hole reaches about 0.51 in from the edge. Content at 0.35 in (labs, practice prototype) is punched through, and content at 0.50 in (worksheets, notes) is grazed. Most of his printing is double-sided, so a fixed wider left margin would put the holes in the content of every even page. He asked for "a slight push" rather than a wide gutter. He chose faint printed circles to show students where the holes go. |
| **Affected Agents** | Designer (builds every print document). Auditor (new hole-zone check, ink check on the guides). Secretary (implements). Librarian (any rebuilt file that is re-filed). |
| **Affected Skills** | `build-lab` (line 33, the lock). `build-document` (line 150, the page-budget order). `audit-deliverable` (gains the hole-zone check). The worksheet and practice-set skills that call `build_worksheet_docx.py` / `build_worksheet_key_docx.py`. No skill restates the new numbers; they point at tokens. |
| **Affected Courses** | Chemistry, Physics and Geology, all printed documents. Slides excluded. |
| **Risk** | **Medium.** Every rebuilt print document reflows and may change page count. The text block narrows by 0.10 in (worksheets, notes, currently 0.50 in) or 0.25 in (labs, currently 0.35 in). "Practice set is exactly 2 pages" (`standards/QA_GATE.md` line 37) may fail on rebuild. Word and LibreOffice must both render mirrored margins and even-page headers correctly, which has not been tested in this repository. **Clearance is thin:** about 0.09 in past a typical hole. A punch whose holes sit deeper or are larger than typical (the wider range quoted to the Secretary, centre up to 0.5 in and diameter up to 0.3125 in, reaches about 0.66 in) would cut into content at 0.60 in. Matt's actual punch has not been measured. |
| **Recommendation** | Approve sections 2-3 and 6 as written, with the dimensions marked PROVISIONAL until a test sheet punched on Matt's own punch confirms them (section 5, step 1). That check matters more at 0.60 in than it would with a wide gutter. Leave already-filed documents alone unless Matt asks for a rebuild. Answer the section 7 questions first; question 1 changes what is built. |
| **Decision** | Approved by the user in chat, 2026-11-20. Request: "I 3 hole punch everything, is there a way we could slide my docuemnts slightly right on the paper to leave a margin to 3 ring hole punch, or do anything to give some design to where the holes will be puinches around the circle?" Choices: Duplex "Mostly double-sided" (mirror margins); Hole design "Faint hole circles (Recommended)"; amendment "well, just make it a slight push." (inside margin 0.60 in). Main-session defaults on section 7 questions, open to his correction: mirror margins also used for single-sided prints; answer keys follow the same rule; guides at hairline weight; recommend one test punch before CONFIRMED. Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Matt's words (verbatim, chat, 2026-11-20)

Relayed to the Secretary by the main session. The Secretary did not see the chat.

> "so thought, I 3 hole punch everything, is there a way we could slide my docuemnts slightly right on
> the paper to leave a margin to 3 ring hole punch, or do anything to give some design to where the
> holes will be puinches around the circle?"

| # | Question | Matt's choice (verbatim) | As offered to him (verbatim) |
|---|---|---|---|
| 1 | Duplex | "Mostly double-sided" | "Mirror margins: wide on the left of odd pages, wide on the right of even pages." |
| 2 | Hole design | "Faint hole circles (Recommended)" | "Three light-grey circle outlines where the punch lands. They look designed and show students where the holes go." |

**Amendment, same day.** Matt's words were relayed by the main session after a first draft
proposed a 0.75 in inside margin:

> "well, just make it a slight push."

The main session translated this as a 0.60 in inside margin (+0.25 in on the 0.35 in token value),
with guides resized to match. The 0.75 in draft is withdrawn and appears nowhere below.

These answers are the source of this record. They are **not** its approval. Under CHANGE_CONTROL
§4.1, an approval is a `Decision:` line, written by the main session, quoting Matt's words about this
ID.

## 2. The proposed rule

### 2.1 Mirror (binding) margin

- Every printed document uses **mirror margins**. The **inside** (binding) margin is **0.60 in**,
  "a slight push": +0.25 in on the token's 0.35 in, and +0.10 in on the 0.50 in that worksheets and
  notes use now. It is on the **left of odd pages** and the **right of even pages**.
- The **outside**, top and bottom margins are unchanged (but see section 4, table B: "unchanged"
  currently means different values in different builders).
- **The inside margin never shrinks to meet a page budget.** It is not one of the "`@page` margins"
  in `standards/QA_GATE.md` §2. The outside, top and bottom margins keep whatever status they have
  now.
- New tokens, PROVISIONAL until the test sheet (section 5, step 1) passes:

```json
"print": {
  "margins": {
    "top": "0.30in", "left": "0.35in", "right": "0.35in", "bottom": "0.45in",
    "status": "PROVISIONAL"
  },
  "binding": {
    "$comment": "SHULL-CHG-0075. Three-hole punch, mostly duplex. Inside = left on odd pages, right on even pages.",
    "mirror": true,
    "inside": "0.60in",
    "status": "PROVISIONAL"
  },
  "holeGuides": {
    "$comment": "SHULL-CHG-0075. Three faint outlines where a standard US three-hole punch lands. Binding side of every page; flips on even pages.",
    "count": 3,
    "diameterIn": 0.26,
    "centreFromBindingEdgeIn": 0.38,
    "centresFromTopIn": [1.25, 5.5, 9.75],
    "stroke": "ruleHairline",
    "strokeWeight": "0.75pt",
    "fill": "none",
    "status": "PROVISIONAL"
  }
}
```

`print.margins.left` and `.right` are not deleted. Under mirroring, Word and CSS read them as the
inside and outside. In the implementation, the inside value comes from `print.binding.inside`, and
the outside keeps its current per-builder value.

### 2.2 Hole guides

- **Three circle outlines**, about 0.26 in across, centred 0.38 in from the binding edge, at 1.25 in,
  5.5 in and 9.75 in from the top (4.25 in apart, centred on 11 in).
- **On the binding side of every page.** They are on the left on odd pages and the right on even
  pages.
- **Light grey, outline only, no fill.** The colour is the existing `ground.ruleHairline` token
  (`#C8CDC2`, INHERITED, "Hairline table and box rules on print. Never text.",
  `brand/tokens.json` lines 77-80). The record points at the token rather than adding a new hex.
- **Weight:** 0.75 pt, which matches the `print.weights.writingLine` floor (`brand/tokens.json`
  lines 489-492). The main session's draft said "hairline". A thinner stroke in a colour this light
  may drop out on a copier. This is question 3 in section 7, and it does not block approval.
- **Clear of all content.** No text, rule, box, image or running header/footer may enter the
  **hole zone**. The hole zone is the full height of the inside margin, from the binding edge to
  `print.binding.inside`. The guides are the only marks allowed there.
- **Within print-ink limits.** This is measured by `scripts/audit_print_ink.py`. It is expected to
  pass easily: three 0.26 in outlines at about 20% darkness add almost no toner, and an outline has
  no solid band for the fill detector (`FILL_MIN_IN = 0.60`, line 57) to find.

### 2.3 Clearance check

| Measurement | Value |
|---|---|
| Typical hole (centre 0.38 in, diameter 0.26 in), and the guide circle: span from edge | 0.25 to 0.51 in |
| Inside margin | 0.60 in |
| Clearance, typical hole to content | **about 0.09 in** |
| Worst hole in the wider range first quoted (centre 0.5 in, diameter 0.3125 in), outer edge | about 0.66 in, which is **0.06 in into content** |

0.60 in clears a typical punch, with little room to spare. It does not clear every punch in the
wider range. **Recommend a check on Matt's own punch** (section 5, step 1) before the numbers become
CONFIRMED. If his holes reach past about 0.55 in, the inside margin needs to grow, and that is a
question for him, not a build-time adjustment.

## 3. Scope, and every place that sets page margins

**In scope:** every printed document type. That covers guided and Cornell notes (and keys),
worksheets and practice sets (and keys), labs (and teacher keys), assessments, study guides and
reference sheets. It follows `brand/SHULL_DESIGN_SYSTEM.md` §8, line 225. **Excluded:** slides
(`brand/tokens.json` `slideGeometry`, `templates/slide/`), and the digital-only deliverables §8
already exempts.

| # | File | What it sets now | Reads tokens? | Change needed |
|---|---|---|---|---|
| 1 | `templates/_shull_docx.py` lines 669-678, `page_setup()` | `margin_lr=0.5`, `margin_tb=0.44` defaults; left = right | **No** | Turn on mirror margins (`w:mirrorMargins` in settings). Inside from `print.binding.inside`, outside unchanged. Turn on even/odd headers (`w:evenAndOddHeaders`). Add one shared helper that draws the hole guides in the odd and even headers. Also the `width=7.5` defaults in `one_cell()` (line 349) and `equation_bar()` (line 455). |
| 2 | `templates/worksheet/build_worksheet_docx.py` line 1182 (`page_setup(doc)`), line 49 `TEXT_W_IN = 7.50` | Defaults from row 1 | No | Text width from tokens, not 7.50. Grid gutter check (README line 179) re-verified at the narrower line. |
| 3 | `templates/worksheet/build_worksheet_key_docx.py` line 357 (`page_setup(doc)`), line 50 `TEXT_W_IN = 7.50`, line 51 `HAND_W_IN = 7.20` | Defaults from row 1 | No | Same as row 2. **`HAND_W_IN = 7.20` is at risk.** The line becomes 7.40 in (8.5 - 0.60 - 0.50). Less the card's 130-twip cell margins each side (about 0.18 in), that leaves about 7.22 in, so check it and shrink it if needed. |
| 4 | `templates/notes/build_notes_docx.py` lines 71-84 (`TEXT_W_IN = 7.50`, `MARGIN_LR_IN = 0.50`, `MARGIN_TOP_IN = 0.42`, `MARGIN_BOTTOM_IN = 0.72`), applied at lines 1548-1555 | Own constants; does not call `page_setup()` | No | Mirror margins and even/odd headers. Text width, and the cue/notes column split (`CUE_W_IN 1.28`, `NOTES_W_IN 6.22`, lines 72-77), recomputed. The height predictor (`BODY_H_PT`, `SAFETY_PT`) is unaffected vertically but wraps more. |
| 5 | `templates/notes/SHULL_Notes_TEMPLATE.html` line 8, used by `templates/notes/build_notes.py` (WeasyPrint, Option B) | `@page` 0.5 / 0.5 / 0.55 / 0.5 | No (`shull-notes-tokens.css` has no margin) | `@page :left` / `:right`. Low priority: per `build-document` SKILL lines 16-18, it reads only the old flat spec. |
| 6 | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 31, 37-59 | `@page` 0.30 / 0.35 / 0.45 / 0.35, hard-coded; comment says "locked" | No (`shull-lab-tokens.css` has no margin) | `@page :right { margin-left: inside }`, `@page :left { margin-right: inside }`. Hole guides drawn in the page margin area (section 5). Lock comment rewritten to point at tokens and this record. |
| 7 | `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` line 25 | Same, hard-coded | No | Same as row 6. |
| 8 | `templates/lab/build_lab.py` line 53 | The page-budget message "`@page` margins → base font-size → ..." | n/a | Message says the inside margin is not on the list. |
| 9 | `templates/practice/build_practice.py` lines 41-43, 166-168 | Left, right and bottom **from tokens**; top hard-coded 0.50 | Partly | Inside from `print.binding.inside`, mirrored. It is a prototype (docstring line 6), so it is changed only if it is still in use. |

**Out of scope:**
- `templates/snow_day/build_snow_day_docx.py` line 105. Its docstring line 6 says snow-day work is
  posted to Google Classroom and done on a Chromebook, **not printed**.
- `scripts/build_handwriting_sheet.py` lines 98-99 (`margin: 0`). It is an internal scan-capture
  sheet with corner registration marks, not a classroom document.
- No assessment or study-guide builder exists in `templates/`. When one is built, it inherits the
  rule through tokens.

**Rule text that changes (section 6):** `brand/SHULL_DESIGN_SYSTEM.md` §8, `brand/tokens.json`
`print`, `standards/QA_GATE.md` §2 and a new check, `.claude/skills/build-lab/SKILL.md` line 33,
`.claude/skills/build-document/SKILL.md` line 150, `templates/lab/README.md` lines 81-82.

## 4. Status of every touched rule

### A. Labels

| Rule | Where | Label | Note |
|---|---|---|---|
| Print margins 0.30 / 0.35 / 0.35 / 0.45 | `brand/tokens.json` lines 477-483 | **PROVISIONAL** (explicit `status` field) | Changed on the binding side. |
| "Margins are locked" (labs) | `.claude/skills/build-lab/SKILL.md` line 33; `templates/lab/README.md` lines 79-82; `SHULL_Lab_TEMPLATE_MASTER.html` lines 31, 37 | **Described as locked in prose.** It has no LOCKED status label of its own. It came in with the lab template (SHULL-CHG-0010 line 73, SHULL-CHG-0031 lines 43 and 78). | **CONFLICT. Needs this record's approval.** The template comment calls the margins "the confirmed SHULL print standard", but the token it points to is PROVISIONAL. The Secretary does not resolve which label was right. Approving this record changes the binding side and keeps the "never adjust to fix a page count" part, extended to every document. |
| Page-budget order, "reduce `@page` margins" first | `standards/QA_GATE.md` lines 39-40; `.claude/skills/build-document/SKILL.md` line 150 | Standard. No status label. | Already contradicts the lab lock for labs. This record exempts the inside margin and the hole zone. |
| Print discipline (ink, outline-only) | `brand/SHULL_DESIGN_SYSTEM.md` §8 "a hard rule" | Hard rule. No LOCKED label. | Not changed. The guides must comply with it. |
| `ground.ruleHairline` `#C8CDC2` | `brand/tokens.json` lines 77-80 | **INHERITED** | Reused, not changed. |
| `print.weights.writingLine` 0.75 pt | `brand/tokens.json` lines 489-492 | No status label | Reused as the guide weight, not changed. |
| Practice set exactly 2 pages | `standards/QA_GATE.md` line 37 | Standard. No status label. | Not changed, but it may fail on rebuild (section 5). |

### B. Finding: margins already disagree (reported, not fixed here)

| Builder | Left / right | Top | Bottom | Source |
|---|---|---|---|---|
| Token | 0.35 / 0.35 | 0.30 | 0.45 | `brand/tokens.json` 477-483 |
| Labs (student and key) | 0.35 / 0.35 | 0.30 | 0.45 | Hard-coded copy, lab templates line 40 / line 25 |
| Worksheets and keys | 0.50 / 0.50 | 0.44 | 0.44 | `_shull_docx.py` `page_setup()` defaults |
| Guided notes (.docx) | 0.50 / 0.50 | 0.42 | 0.72 | `build_notes_docx.py` constants |
| Guided notes (HTML, Option B) | 0.50 / 0.50 | 0.50 | 0.55 | `SHULL_Notes_TEMPLATE.html` line 8 |
| Practice prototype | 0.35 / 0.35 (token) | 0.50 | 0.45 (token) | `build_practice.py` |

The one rule (CLAUDE.md §1) is broken here. Six copies exist, and only one builder reads the token.
Making the token authoritative for every builder would change worksheet and notes layouts beyond
what Matt asked for. Bundling that in would be an unapproved change inside an approved one, so it is
left out. **Suggested follow-up:** a separate record, possibly from the Janitor, to make
`print.margins` the single source and settle its PROVISIONAL status.

## 5. Implementation notes (for after approval, not done)

1. **Calibrate first.** Build one test page from tokens (guides only, with a faint line at the 0.60 in
   inside margin), print it duplex on Matt's printer, and punch it with his punch. Promote the
   `binding` and `holeGuides` tokens from PROVISIONAL to CONFIRMED only once he says the holes land
   in the circles. Until then, the numbers are the main session's estimate.
2. **Word (`.docx`)**:
   - `w:mirrorMargins` in `settings.xml`. With it on, `w:pgMar w:left` is the inside and
     `w:right` is the outside.
   - `w:evenAndOddHeaders` in `settings.xml`, plus a default (odd) header and an even header in
     every section.
   - Each header carries three anchored shapes (DrawingML `wps:wsp` ellipse, or VML `v:oval` for
     LibreOffice safety), positioned relative to the **page**, not the margin, with no fill and a
     `ruleHairline` stroke. Odd-header shapes are at x = 0.38 in - r, and even-header shapes at
     x = 8.5 - 0.38 in - r, where r = 0.13 in.
   - If a document sets "different first page" (`w:titlePg`), the first-page header must carry the
     guides too.
   - Render in LibreOffice (`soffice --headless --convert-to pdf`) and check that the guides and
     the mirror both survive conversion. The notes builder comments (lines 1552-1555) show that
     LibreOffice treats headers differently.
3. **HTML/PDF labs (WeasyPrint, `templates/lab/build_lab.py` line 16)**:
   - `@page :right { margin-left: <inside>; margin-right: <outside> }` and
     `@page :left { margin-left: <outside>; margin-right: <inside> }`. Page 1 is a right page.
   - Guides go in as a background SVG on `@page :right` / `:left`, or in margin boxes. The existing
     `@top-right`, `@bottom-left` and `@bottom-right` runheads (lines 42-57) must still clear the
     hole zone on even pages.
4. **Audits**:
   - Run `scripts/audit_print_ink.py` on a rebuilt page and record that the guides add negligible
     toner and trip no fill band.
   - **Add a hole-zone check.** It goes either in a new script or in `scripts/audit_worksheet.py`,
     with the same wiring for notes and labs. Rasterise each page, mask the three guide circles, and
     fail if any other dark pixel falls between the binding edge and `print.binding.inside`, on the
     correct side for the page's parity. Add the check to `standards/QA_GATE.md` and to the
     `audit-deliverable` skill.
5. **Page budget.** Rebuild each practice set and confirm it is still exactly 2 pages
   (`standards/QA_GATE.md` line 37). If one spills, the fix order applies with the inside margin
   exempt.

### Existing deliverables affected (Physics U3, `output/physics/u03/`)

| Deliverable | Files | Builder | Filed in Drive? | Proposal |
|---|---|---|---|---|
| Unit 3 Guided Notes | `Unit 3 Guided Notes.docx/.pdf`, `Unit 3 Guided Notes Key.docx/.pdf` | `build_notes_docx.py` | No ("Not filed (not approved)", `reports/drive-operations/2026-11-18_phys-u03-s03.2-fbd-practice-set-filing.md` line 51) | Rebuild after implementation |
| 3.2 Practice Set - Net Force | student and key, `.docx/.pdf` | `build_worksheet_*` via `build_phys_u03_s03.2_net_force.py` | Not verified by the Secretary | Rebuild. Its 2-page cut (SHULL-CHG-0074 item 1) is at risk. |
| 3.3 Practice Set - Frictionless Inclines | student and key, `.docx/.pdf` | `build_worksheet_*` | Not verified by the Secretary | Rebuild |
| Unit 3 Practice Set - Free-Body Diagrams | student and key, `.docx/.pdf` | `build_worksheet_*` (grid layout) | **Yes**, filed 2026-11-18 to the Section 03.2 folder (same drive-operations log) | **Rebuild only if Matt asks.** If rebuilt and re-filed, the Librarian logs the replacement before the Drive mutation (CHANGE_CONTROL §7). |
| 3.1 Lab - Newton's Laws | `3.1 Lab - Newton's Laws.html/.pdf`, `3.1 Lab Key - Newton's Laws.html/.pdf` | Lab template, `build_lab.py` | No (same log, line 51) | Rebuild after the lab template change. Re-check its page count (SHULL-CHG-0073). |

The main session's brief listed "both practice sets". Two section practice sets exist in the folder
(3.2 and 3.3), and both are listed above. Unit 3 Slides are excluded.

**Already-filed documents in any course** are rebuilt only on request. No sweep of Drive is
proposed.

## 6. Exact text to add on approval (not applied)

**`brand/SHULL_DESIGN_SYSTEM.md` §8, new bullet after "Minimum weights" (line 242):**

```markdown
- **Binding side.** Every printed page has a mirror margin for three-hole punching: the inside
  margin is `print.binding.inside`, on the left of odd pages and the right of even pages. Three
  hole guides (`print.holeGuides`) are drawn on the binding side. They are outline only, in
  `ground.ruleHairline`. Nothing else enters the inside margin, and it never shrinks to fit a page
  budget. SHULL-CHG-0075.
```

**`standards/QA_GATE.md` §2, after line 40:**

```markdown
The inside (binding) margin and the hole zone are not on this list. They never shrink
(SHULL-CHG-0075, `brand/SHULL_DESIGN_SYSTEM.md` §8).
```

Plus a new numbered check: "No content in the hole zone", with the audit command once it exists.

**`.claude/skills/build-lab/SKILL.md` line 33:**

```markdown
- **Margins come from `brand/tokens.json` (`print.margins`, `print.binding`).** Never adjust them
  to fix a page count; reduce body size or line-height. The binding side is in
  `brand/SHULL_DESIGN_SYSTEM.md` §8.
```

**`.claude/skills/build-document/SKILL.md` line 150:** append "The inside (binding) margin is
exempt; see `standards/QA_GATE.md` §2."

**`templates/lab/README.md` lines 81-82, and the lab template comments at lines 31 and 37:** point at
the tokens and at this record, and drop the word "locked" in favour of the rule above.

**`brand/tokens.json`:** add the `print.binding` and `print.holeGuides` objects from section 2.1.

## 7. Questions for the main session to put to Matt (one at a time, in this order)

1. **Single-sided printing.** "Mostly double-sided" means some documents print single-sided. In a
   single-sided multi-page document, every even page would have its wide margin on the right while
   the punch hits the left, and content at 0.35-0.50 in would be punched. Options: (a) mirror
   everything and accept that risk on single-sided prints; (b) mirror only multi-page documents
   and give one-page documents a plain wide left margin; (c) a per-document duplex flag in the
   spec, defaulting to duplex. **This changes what is built.**
2. **Answer keys.** Are teacher keys punched too? The scope above includes them. If they are kept
   loose, they can stay as they are.
3. **Guide weight.** 0.75 pt light grey (matches the writing-line floor) or a true hairline
   (thinner, may vanish on a copier)? This does not block approval.
4. **Test sheet.** Will Matt punch a test page on his own punch before the numbers become CONFIRMED
   (section 5, step 1)?

## 8. What this record does not do

- It does not edit `brand/`, `standards/`, any skill, any template, or any output. Nothing is
  implemented and nothing is committed.
- It does not unify the six existing margin copies (section 4, table B).
- It does not decide whether the lab "lock" or the token's PROVISIONAL label was right.
- It does not touch slides or `slideGeometry`.
- (Superseded at implementation: the `change-log/CHANGELOG.md` row was added as PARTIAL.)
