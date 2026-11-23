# SHULL-CHG-0109 — Chemistry roadmaps and outline: two colours and a big headline

> **ID note.** The main session supplied 0109 and confirmed it is free on `origin/main` (highest:
> SHULL-CHG-0108). The drafting Secretary has no shell and did not fetch. Not allocated until pushed
> (`governance/CHANGE_CONTROL.md` §2).

> **Two CONFLICTS, marked, not resolved.** (1) The SHULL-CHG-0108 sentence "A document uses one
> pairing throughout and never mixes the two" (`brand/SHULL_DESIGN_SYSTEM.md` §3). (2) The LOCKED
> shared header, `brand/tokens.json` `print.header` and §11 (SHULL-CHG-0101): "Page 1 of every print
> document opens with the same header". Approving this record approves both amendments (§2a, §2b).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0109 |
| **Date** | 2026-11-23 (drafted) |
| **Source** | User, main session chat, 2026-11-23, as relayed. After the all-blue roadmaps Matt asked *"what if bith colors were used?"*, saw a preview (orange-deep type, Ice Blue rules), was told it needs a change to the 0108 sentence and was offered the big headline from his favourite U6 page, which needs an exception to the LOCKED header. He replied: *"both colors, outline too, and the big headline"*. **This record is not the approval.** The main session records it (§4). |
| **Current Rule** | §1 |
| **Proposed Rule** | §2 (exact text) |
| **Supersedes** | `brand/SHULL_DESIGN_SYSTEM.md` §3, the 0108 paragraph (lines 116-119). §11 first sentence "Page 1 of every print document opens with the same header" (exception added; `print.header` values unchanged). `courses/chemistry/DECISIONS.md` "Course brand exceptions" live text (lines 365-381), including the row "Unit Roadmap (U0–U15) \| Blue". **Not superseded:** the §3 boxed coloured-type rule (type on light ground stays a text-safe deep token); every token hex and status; `print.header` titlePt/kickerPt/metaPt for all other documents; the docx header `print_header()`. |
| **Reason** | Matt chose orange type with Ice Blue rules, for the Course Outline too, plus the U6-style large headline (Source). Which documents use it is a Chemistry decision (DECISIONS.md); the mechanism and the header exception are brand (Path B). |
| **Affected Agents** | Designer, Auditor (restatements, §2e). Overseer routes the rebuild (§4). |
| **Affected Skills** | None restate the changed text. `apply-shull-design` quotes only the boxed rule, which is unchanged. |
| **Affected Courses** | Chemistry only in effect. Mechanism wording is general; Physics and Geology list nothing and are unchanged. |
| **Risk** | Low-medium. Grey: Energy Orange Deep 93 vs Ice Blue ≈172, but no distinction is carried by colour. Header height grows on two one-page documents only; both builders fail unless the page count is 1, so overflow is caught. Title size and rule weight are PROVISIONAL until built. |
| **Recommendation** | Approve. Builder switch and the rebuild of 16 roadmaps plus the outline are a separate Overseer job (§4), not bundled. |
| **Decision** | Approved by the user, 2026-11-23: "both colors, outline too, and the big headline" |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

## 1. Current rule (verbatim)

`brand/SHULL_DESIGN_SYSTEM.md` §3, lines 116-119:

> A course with a `secondaryDeep` has a second print pairing: `secondary` for rules, borders and
> outline boxes, and `secondaryDeep` for coloured type. A document uses one pairing throughout and
> never mixes the two. Which documents use the second pairing is a course decision, recorded under
> "Course brand exceptions" in that course's `DECISIONS.md`. SHULL-CHG-0108.

§11, lines 309-315: *"Page 1 of every print document opens with the same header. Left: an outlined
code chip ... and a `COURSE · DOCUMENT TYPE` kicker ... then the title in condensed capitals with one
accent word. ... a double rule in the course display colour. Ruled, never filled, and no taller than
the rail header it replaced. Sizes ... live in `brand/tokens.json` `print.header` ... A builder never
draws its own header."* `print.header`: titlePt 17, kickerPt 7.5, metaPt 7, LOCKED, SHULL-CHG-0101.

`courses/chemistry/DECISIONS.md` lines 365-381: two pairings (Orange default, Blue); table row
`Unit Roadmap (U0–U15) | Blue | SHULL-CHG-0108`.

## 2. Exact edits

### 2a. `brand/SHULL_DESIGN_SYSTEM.md` §3 — replace lines 116-119 with

> A course with a `secondaryDeep` has a second print pairing: `secondary` for rules, borders and
> outline boxes, and `secondaryDeep` for coloured type. Any course may also use a mixed pairing:
> `secondary` for rules, borders and outline boxes, and `primaryDeep` for coloured type. A document
> uses one pairing throughout and never mixes two deep tokens as type on one document. Which documents
> use a pairing other than the default is a course decision, recorded under "Course brand
> exceptions" in that course's `DECISIONS.md`. SHULL-CHG-0108, SHULL-CHG-0109.

### 2b. `brand/SHULL_DESIGN_SYSTEM.md` §11 — header exception

First sentence becomes: *"Page 1 of every print document opens with the same header, except the
display header below."* Then add after the paragraph:

> **Display header (SHULL-CHG-0109).** A Unit Roadmap or Course Outline may open with a display
> header instead, where its course's `DECISIONS.md` lists it under "Course brand exceptions". No
> other document type may. The outlined chip sits on its own line above the `COURSE · PHASE`
> kicker; the title is large condensed capitals (Archivo Narrow bold), in ink except one accent
> word; a single rule in the course display colour replaces the double rule. The right-hand meta is
> unchanged. It is exempt from the height limit above. Same drawing files; sizes in
> `brand/tokens.json` `print.header.display`.

`brand/tokens.json`, inside `print.header`, after `"source": "SHULL-CHG-0101"` (add a comma):

```json
      "display": {
        "$comment": "Display header, Unit Roadmap and Course Outline only, where the course DECISIONS.md lists it (brand/SHULL_DESIGN_SYSTEM.md section 11, SHULL-CHG-0109). Values set by the designer's build and reported in the record.",
        "titlePt": 32,
        "rulePt": 1.5,
        "status": "PROVISIONAL",
        "source": "SHULL-CHG-0109"
      }
```

`titlePt` 32 (Matt's range 30–34) and `rulePt` 1.5 are **PROVISIONAL starting values**. The
designer's build sets the final numbers and reports them in `Verified`. Bump `version` to 1.3.0 and
`updated` to the implementation date. The parent `print.header` keys keep LOCKED.

### 2c. `courses/chemistry/DECISIONS.md` — replace lines 365-381 with

```markdown
**Print pairings and header.** Chemistry's identity colours are `courses.chemistry` in
`brand/tokens.json`, inside the shared system (SHULL-CHG-0054). This file does not restate them.
Chemistry has three print pairings (`brand/SHULL_DESIGN_SYSTEM.md` §3):

- **Orange (default):** `primary` for rules, borders and outline boxes; `primaryDeep` for accent
  text.
- **Blue:** `secondary` (Ice Blue) for rules, borders and outline boxes; `secondaryDeep` (Ice Blue
  Deep) for accent text. Available; no document type uses it now.
- **Mixed:** `secondary` (Ice Blue) for rules, borders, number boxes, standard outlines, checkboxes
  and the measured box; `primaryDeep` (Energy Orange Deep) for accent text: the headline accent
  word, kicker, labels and chevrons.

A document uses one pairing throughout. Every document type not listed below uses orange and the
standard header.

| Document type | Pairing | Header | Since |
|---|---|---|---|
| Unit Roadmap (U0–U15) | Mixed | Display | SHULL-CHG-0109 (Blue under SHULL-CHG-0108) |
| Course Outline (Reference - Course Outline) | Mixed | Display | SHULL-CHG-0109 |

Adding a document type to this table is a course decision (a dated log entry) and needs no brand
change, except that the display header is limited to the types `brand/SHULL_DESIGN_SYSTEM.md` §11
names. Energy Orange is not retired.
```

The `*Superseded 2026-09-07...*` line stays. Log entry at the top of the decision log; "Last
updated" set to the implementation date:

```markdown
### YYYY-MM-DD — Roadmaps and Course Outline: mixed pairing, display header
Unit Roadmaps (U0–U15) and the Course Outline use the mixed pairing: Energy Orange Deep for accent
text, Ice Blue for rules, borders and outlines. Both open with the display header (large condensed
title, chip above the kicker, single rule). The blue pairing and Ice Blue Deep stay available,
unused. Decided by Matt 2026-11-23 ("both colors, outline too, and the big headline").
Supersedes: Course brand exceptions, Unit Roadmap → Blue (SHULL-CHG-0108).
Status: CONFIRMED · SHULL-CHG-0109
```

### 2d. `scripts/build_lab_css.py`

After line 66 (`body.chem.pair-blue ...`):

```python
body.chem.pair-mixed {{ --accent: {c['chemistry']['primaryDeep']['hex']}; --accent-display: {c['chemistry']['secondary']['hex']}; }}
```

In `:root`, after `--header-meta-size` (line 59):

```python
  --header-display-title-size: {hdr['display']['titlePt']}pt;
  --header-display-rule:       {hdr['display']['rulePt']}pt;
```

Closing comment, append: *"body.chem.pair-mixed: primaryDeep as type, secondary as rule
(SHULL-CHG-0109)."* Re-run the script; it rewrites `templates/lab/shull-lab-tokens.css` and
`templates/notes/shull-notes-tokens.css`.

### 2e. Restatements the main session updates (same commit, labelled; outside the Secretary's directories)

| File | Edit |
|---|---|
| `templates/_shull_header.css` | Add the one display variant (no sizes typed): `.sh-head.sh-display { border-bottom: var(--header-display-rule) solid var(--accent-display); }` `.sh-display .sh-chip { display: table; margin: 0 0 3pt; }` `.sh-display .sh-title { font-size: var(--header-display-title-size); line-height: 1; }`. Header comment: "`.sh-display` = display header, §11, SHULL-CHG-0109". Designer may tune spacing in the build. |
| `.claude/agents/auditor.md` line 34 | "...(`primaryDeep` or `secondaryDeep`), setting two deep tokens as type on one document, or using a non-default pairing or the display header on a document type its course's `DECISIONS.md` does not list." |
| `.claude/agents/designer.md` line 21 | Parenthetical becomes "(`primaryDeep`, or `secondaryDeep` where the course's `DECISIONS.md` lists the document type for its blue pairing; rules follow the listed pairing)". |
| `templates/lab/README.md` line 39 | Append: "`chem pair-mixed` switches to Chemistry's mixed pairing (SHULL-CHG-0109)." |
| `templates/unit-roadmap/README.md` lines 73-74, 83-87 | Header: "display header (`.sh-display`, SHULL-CHG-0109)". Colours: Chemistry roadmaps and the outline use `chem pair-mixed` per the DECISIONS table; delete "The Course Outline ... stays orange". |
| `templates/unit-roadmap/unit_roadmap.css` line 5 | "...SHULL-CHG-0101, LOCKED; display variant SHULL-CHG-0109); nothing here restyles it." |

Unchanged: `apply-shull-design/SKILL.md` (boxed rule unchanged), `templates/_shull_docx.py`
(both document types are HTML).

## 3. Verification (after APPROVED and implemented)

`build_lab_css.py` output contains `body.chem.pair-mixed` with `#B84100` / `#3DD6F4` and the two
display header variables; `validate_tokens.py`, `build_app_css.py --check`, all `validate_*.py`
pass; `#B84100` and `#3DD6F4` appear nowhere new outside `tokens.json` and generated CSS. Diff of
DECISIONS.md limited to the exception text, log entry and "Last updated". Final titlePt and rulePt
from the build recorded here.

## 4. Follow-up (not bundled; through the Overseer)

Builders: `build_unit_roadmap.py` line 28 and `build_course_outline.py` line 26 → `"chem pair-mixed"`
(comments point at the DECISIONS table); header markup gains `sh-display` with the chip on its own
line. Rebuild U0–U15 roadmaps and the Course Outline, usual print QA, printed proof.

## 5. Rollback

One commit with `SHULL-CHG-0109`; `git revert`, then re-run `build_lab_css.py`. No Drive mutation.
