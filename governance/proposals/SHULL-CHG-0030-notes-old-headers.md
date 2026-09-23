# SHULL-CHG-0030 — Guided notes: the SHULL-CHG-0014 headers on the SHULL-CHG-0025 paged layout

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0030 |
| **Date** | 2026-09-23 |
| **Source** | User, 2026-09-23. The main session relayed his words, so the Secretary did not hear them directly. He asked, verbatim: *"so the tempalte, i hope we didnt change the headers from the old guided note tempalte."* The main session confirmed that the headers had changed, showed him an old/new side-by-side of the Geology notes, and offered three options. **Option 1**, verbatim: *"Old headers on the new layout. Keep the new page structure (a new page per section, RECALL blocks, work boxes, and the Concept Review page) but bring back your old headers: the colored school line and title block; the targets ∥ key terms box and the section checklist; the section title bar with "U1 / S1.2" and the course-color rule; the "LEARNING TARGET" line; the colored small-caps row labels."* He answered, verbatim: *"I want to keep the old header, new slide format"*. The main session reads this as choosing Option 1. **Neither statement approves this record.** They are the finding it is written from. |
| **Amends** | **SHULL-CHG-0025** (IMPLEMENTED, `71e5e05`). The change is limited to the headers. Everything else in 0025 stays (§3c). |
| **Current Rule** | See §1. It is quoted verbatim from SHULL-CHG-0025 §3 and §4. |
| **Proposed Rule** | See §3. Five header elements are restored from SHULL-CHG-0014 on top of 0025's paged layout. |
| **Supersedes** | See §4. In short, from **SHULL-CHG-0025**: part of **§3a**, the per-page head at a section's start. Part of **§3b**, the black block title on the cue side. Part of **§3f**, the cover's title block, kicker, school line, key terms by section and "How to use the notes". The first bullet of **§3h**, *"Greyscale throughout."* Three **§4** rows are also reversed in part. These are the ones that took the 0014 unit wrapper, the 0014 header bar and learning target, and the 0014 accent header rules and labels. |
| **Reason** | The user wants the header design from his own Geology packet back, and wants 0025's page structure kept. SHULL-CHG-0014 adopted that packet with the words *"the structure is the asset and none of it was redesigned"*. SHULL-CHG-0025 §6 item 6 flagged that 0025 reversed that premise. This record restores the part the user has now asked for. |
| **Affected Agents** | Designer (rebuilds the headers in the builder). Auditor (independent pass, §7). Secretary (records this, and implements it once approved). |
| **Affected Skills** | `build-document` (`.claude/skills/build-document/SKILL.md`, which describes the cover and page head). `templates/notes/README.md` (spec schema: `unitTargets`, `keyTerms`, `howItWorks`, `sectionList`, `learningTarget`, `cueLabel`, `notesLabel`). |
| **Affected Courses** | All three: Chemistry, Physics and Geology. The template is shared. |
| **Risk** | **Medium.** This is a shared template used by three courses. It reverses part of an IMPLEMENTED record (0025 §3h, greyscale) and brings course colour back to the printed notes. No LOCKED rule is changed, but two sit close by: `brand/SHULL_DESIGN_SYSTEM.md` §8 (colour is a thin accent only) and SHULL-CHG-0015 (bare list numbers). See §5, items a and d. |
| **Recommendation** | Approve the five restored elements in §3a, subject to the user's answers to §5 a–d. Ask **a** first, because it decides whether any colour lands at all. Then ask **b**, because it decides the shape of page 1. |
| **Decision** | **Approved by the user, 2026-09-23**, in the main session. Verbatim: *"I want to keep the old header, new slide format"*. Then, on whether the template changes and not the Unit 1 notes: *"yes, use your recommendations for the template"*. The main session's recommendations he accepted, as he was shown them: a. thin course-color accents only, no fills; b. keep the separate cover page (atom image, difficulty ratings, equation box) with the old header block on it; c. a header only at the start of each section; d. drop the "01" block numbers. Also verbatim: *"no dont rebuild"*. The Chemistry U1 notes already delivered are not rebuilt. Recorded under SHULL-CHG-0026. |
| **Status** | **APPROVED** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. Nothing has been implemented. The required checks are in §7. |

---

## 1. Current Rule, verbatim

### 1a. SHULL-CHG-0025 §3a: the per-page head

> - **Every content page has its own head.** It carries the running head (`SHULL SCIENCE / CHEMISTRY /
>   GUIDED NOTES`), the section title, the section code at the top right (`S01.1`), and a subtitle
>   written for that page. For example, p.2 reads *"Classify matter as an element, compound, or
>   mixture; then classify mixtures."* and p.3 reads *"Mixtures, classification practice, and a
>   check of your understanding."*

As built (`templates/notes/build_notes_docx.py` `page_head()`, lines 701–723): the eyebrow and code
sit on one row. The title is on the next row, with a hairline rule under it. The subtitle is on the
row after that, with a second hairline rule under it. All four are in `pal.ink` or `pal.label`, so
the head has no course colour. *The "two rules" detail comes from the builder, not the record text.*

### 1b. SHULL-CHG-0025 §3b: the cue side

> - **Cue side:** the block number (`01`, `02` …), the block title (*"Vocabulary"*, *"The matter
>   flowchart"*), then one or two cue questions. **The block number is bare**, with no tint, chip or border
>   (SHULL-CHG-0015; see the §2 note). The RECALL / RECAP / REVIEW tags carry the light tint.

As built (`render_cue()`, lines 467–476): the number and the title are bold, in the default ink.

### 1c. SHULL-CHG-0025 §3f: the cover

> - The atom image as the hero, at the top right. This replaces the per-page watermark.
> - Course/unit eyebrow, unit title, `GUIDED NOTES • S01.1 / S01.3 / S01.5`, school, and Name / Date /
>   Period.
> - **Section breakdown / concepts to master.** Each section has its code, title, a one-line
>   description, and a **difficulty rating out of 10**, with the note *"Estimated for advanced high
>   school students: 1 = introductory; 10 = highly challenging."* See §6 item 4.
> - **Equation toolbox.** Formulas in two columns.
> - **Key terms, grouped by section.**
> - **How to use the notes.**

### 1d. SHULL-CHG-0025 §3h: ink

> - **Greyscale throughout.** No course accent colour in the printed notes. See §6 item 5.

### 1e. SHULL-CHG-0025 §4: what it superseded in SHULL-CHG-0014

> | Must-write bar in the course accent (lime in Chemistry), drawn as a cell border | 0014 Finding 1; 0024 `f76fea6` | A grey rule |
> | Course-accent colour in print: the cue-column accent rail, accent header rules, accent labels | 0014 Finding 4; 0024 `4234b69` | Greyscale |
> | Section rhythm *"header bar → learning target → Cornell rows → summary box"*, flowing | 0014 "What is preserved" | Paged: page head → about three open blocks → RECALL / RECAP / REVIEW blocks |
> | Full-width summary box and closing ("pulling it together") box | 0014 "What is preserved" | RECALL and REVIEW blocks in the two-column rhythm. The content survives: "close your notes", the checklist, the big picture, "still fuzzy on". |
> | Unit wrapper: *"targets ∥ key terms, 'how these notes work', section checklist"* | 0014 "What is preserved" | The cover in §3f |

---

## 2. The source of the restored design

**The target is the template at commit `0f3b078`** (`git show 0f3b078:templates/notes/build_notes_docx.py`).

**The Secretary could not read it.** This agent has no shell. `0f3b078` does not appear in
`.git/logs/HEAD`, whose history starts at `31b4c37`, and it is not a loose object, so it cannot be
opened with a file read. **The SHA has not been verified to exist.** The implementer confirms it with
`git show` before building. If it does not resolve, they stop and report back rather than pick
another commit.

The element definitions in §3 therefore rest on two sources:

- **The SHULL-CHG-0014 record text** (`governance/proposals/SHULL-CHG-0014-guided-notes-template.md`).
  This is the authority.
- **The 0014 Option B renderer, which is still in the repository.** 0014 says both renderers build
  from *"the same spec file. Identical structure, identical content, identical tokens"*. The files are
  `templates/notes/SHULL_Notes_TEMPLATE.html` (lines 25–28, 37–38, 42–43, 52–60, 99–119) and
  `templates/notes/build_notes.py` (lines 71–72). **This is corroboration only.** It is the HTML
  renderer, not the `.docx`, and it has been edited since 0014 (for example, the cue width is now
  SHULL-CHG-0018's 1.28 in). Where it and `0f3b078` disagree, `0f3b078` wins.

---

## 3. Proposed Rule

### 3a. Restored from SHULL-CHG-0014

| # | Element | 0014 record text | As in the 0014 renderer (corroboration) |
|---|---|---|---|
| 1 | **Packet opening.** The course-coloured `SHULL SCIENCE · JAMES A. GARFIELD LOCAL SCHOOLS` line, the unit title, the `GUIDED NOTES · PHASE nn · N SECTIONS` line, and Name / Date / Period. | "What is preserved": *"The unit wrapper: brand bar, name/date/period, …"*. Finding 1: *"Eyebrow labels \| amber \| `primaryDeep`"*. Finding 4: the brand bar is *"a hairline above and a heavy accent rule below"*. | `.brandbar`: the school line is in `--accent` and the bar is closed by a heavy `--accent-display` rule. `.kick` holds the spec's `kicker`. The Geology spec has `"GUIDED NOTES  ·  PHASE 01  ·  3 SECTIONS"`. `.fields` holds Name / Date / Period. |
| 2 | **Unit Learning Targets ∥ Key Terms box**, **"How these notes work"**, and the **"Sections in this unit"** checklist. | *"… targets ∥ key terms, "how these notes work", section checklist."* | `.two` is a two-column hairline box headed `UNIT LEARNING TARGETS` and `KEY TERMS`. `.howbox` has a left `--accent-display` rule and the label `HOW THESE NOTES WORK`. `.checklist` has the label `SECTIONS IN THIS UNIT` and a checkbox row per section. |
| 3 | **Section title bar.** The section title, the `U1 / S1.2`-style code at the right, and a course-accent rule under it. | *"The section rhythm: header bar → learning target → …"*. Finding 4: section heads are *"a hairline above and a heavy accent rule below"*. | `.sechead` has an ink rule above and a heavy `--accent-display` rule below. The code is at the right in `--accent`. The Geology spec code is `"U1 / S1.2"`. |
| 4 | **The `LEARNING TARGET` line** under the section title. | *"header bar → learning target → …"* | `.target`: the label `LEARNING TARGET` in `--accent`, then the section's `learningTarget`, closed by a hairline. |
| 5 | **Row labels** in course colour: the cue label and the notes heading. | Finding 1: *"Section labels \| rust \| Geology `primaryDeep` (Terra Teal Deep) — text-safe on white"*. | `.lbl` in `--accent`: `cueLabel` in the cue column and `notesLabel` over the notes. |

**Tokens.** The colours are 0014's and are not restated here, so that each fact lives in one place:

- `--accent` is `courses.<course>.primaryDeep` in `brand/tokens.json`. It is text-safe and used for
  type.
- `--accent-display` is `courses.<course>.primary`. It is used for rules only, never for type.

Both are LOCKED tokens. **No token changes.**

### 3b. What sits where

- **The start of a section** (the first page of each section) carries elements 3 and 4, then its
  blocks.
- **The packet opening** carries elements 1 and 2. Whether it is a separate page is §5 b.
- **Every block** carries element 5. Whether the `01`, `02` number stays beside it is §5 d.
- **Continuation pages** of a section: whether any head appears is §5 c.

### 3c. Kept from SHULL-CHG-0025, unchanged

- A new page for each section.
- The RECALL, RECAP and REVIEW blocks, and their light tint on the tag only.
- The **work boxes**, at a minimum of **1.4 in** (SHULL-CHG-0016).
- The **Concept Review** page.
- **Bare block numbers** (SHULL-CHG-0015), if the numbers are kept at all (§5 d).
- The **1.28 in cue column** (SHULL-CHG-0018).
- **Stacked fractions** (SHULL-CHG-0017).
- **Editable `.docx`**.
- **Archivo**, open blocks with one rule between them, the "Extra notes:" line, the grey must-write
  rule, and the 0025 footer.

The must-write rule **stays grey**. This record restores header colour only. It does not restore
0014's accent must-write bar.

---

## 4. Supersedes

| Rule | From | Replaced by |
|---|---|---|
| The per-page head at a section's start: eyebrow, title, code `S01.1`, and subtitle between two hairlines | 0025 §3a (first bullet, in part) | Section title bar with code and accent rule (3a #3), then the `LEARNING TARGET` line (3a #4). **Continuation pages: open, §5 c.** |
| The block title in bold ink on the cue side | 0025 §3b (cue side, in part) | Course-colour labels: the cue label and the notes heading (3a #5). **The block number: open, §5 d.** |
| Cover eyebrow, unit title, `GUIDED NOTES • S01.1 / …` kicker, school line, and Name / Date / Period | 0025 §3f (second bullet) | The 0014 packet opening (3a #1) |
| "Key terms, grouped by section" and "How to use the notes" | 0025 §3f (fifth and sixth bullets) | The targets ∥ key terms box, "How these notes work", and the section checklist (3a #2) |
| *"Greyscale throughout. No course accent colour in the printed notes."* | 0025 §3h (first bullet) | Course accent in the header elements and row labels only, as a thin accent (§5 a). **Everything else stays greyscale.** |
| 0025 §4 row: *"Course-accent colour in print: … accent header rules, accent labels → Greyscale"* | 0025 §4, in part | Accent header rules and accent labels are restored. **The cue-column accent rail stays superseded.** |
| 0025 §4 row: *"Unit wrapper … → The cover in §3f"* | 0025 §4 | The 0014 unit wrapper is restored (3a #1, #2) |
| 0025 §4 row: *"Section rhythm 'header bar → learning target → Cornell rows → summary box', flowing"* | 0025 §4, in part | "header bar → learning target" is restored at each section's start. Paged blocks and RECALL / REVIEW stay. |

**Not superseded.** The cover image, the section breakdown with its difficulty ratings, and the
equation toolbox (0025 §3f, first, third and fourth bullets) are **open, §5 b**. Every item in §3c
also stays.

---

## 5. Open questions for the user

These are listed, not resolved. Ask **a** first, then **b**. The answer to each changes what the
builder does.

**a. Course colour.**

- SHULL-CHG-0025 made the printed notes greyscale (§3h). The user's 0025 request asked for
  something *"that would improve this on greyscale"*, and his shading answer was *"Table headers +
  chips (Recommended)"*. 0025 §6 item 5 flagged that greyscale removes each course's printed
  identity, and nothing in the 0025 record shows that point being answered separately.
- This record brings course colour back into the headers and row labels.
- **Confirm:** it may be a **thin accent only**, per `brand/SHULL_DESIGN_SYSTEM.md` §8: *"Colour is a
  thin accent only — a chip outline, a rule line, a small tag, a border."*
- **Say which tokens:** 0014's course accent (`primaryDeep`, for type) and course display colour
  (`primary`, for rules), as in §3a.
- Note: Chemistry's `primary` (Lab Lime) measures grey 190 in `brand/tokens.json`, so a lime rule
  prints pale on a mono copier.

**b. The opening page.**

- Does it stay a **separate cover**, or return to 0014's **single opening page that flows straight
  into section 1**? 0014's opening flowed into the first section. 0025 made it a separate page.
- Whichever it is: do the **cover image**, the **difficulty ratings** and the **equation toolbox**
  stay on it?
  - The ratings are now a CONFIRMED Chemistry course fact (`courses/chemistry/DECISIONS.md`, U1 line
    and the 2026-09-23 log entry).
  - The user said *"equation box, keep it"* on 2026-09-23, under 0025.

**c. Continuation pages.** Does the per-page head survive there? 0025 repeats a head on every page.
0014 had a head only at the start of a section.

**d. Block numbers `01`, `02`.** Keep them beside the colour labels, or drop them? If they are kept,
they stay bare under SHULL-CHG-0015 (LOCKED): *"No box, square, circle or marker around a list
number. Just the number."* Colouring the number is not a marker, but that point has not been put to
the user.

### Flagged, not blocking

1. **Section-code format on the title bar.**
   - 0014 and the Geology spec print `U1 / S1.2`. 0025 prints `S01.1`.
   - `standards/NAMING.md` §4 gives the in-document form as `U10 / S10.4`. That example does not show
     whether a single-digit unit is padded.
   - SHULL-CHG-0029 §5 item 1 already asks what the chip and footer show on a multi-section file.
   - The title bar should follow whichever answer 0029 gets, and should not decide it here.
2. **Chemistry has no content for element 2.**
   - The committed Chemistry spec has `learningTarget` per section (lines 100, 264, 412). It has no
     `unitTargets`, `howItWorks` or `sectionList`, and its `keyTerms` are grouped by section.
   - Unit learning targets are course content. **The Designer must not invent them.** Listing the
     three section targets is a content choice for the user.
3. **Chemistry blocks have no notes heading.**
   - Chemistry blocks carry a `title`, not a `cueLabel` and `notesLabel`.
   - Which text fills each label on a Chemistry block depends on §5 d. It is settled at
     implementation and shown to the user.
4. **"Small caps."**
   - The user's option said *"small-caps"*. The 0014 renderer prints these labels as tracked
     capitals, not true small caps.
   - The implementation matches `0f3b078`, whichever it uses.
5. **The student-page wording in "How these notes work" must match 0025.**
   - The Geology spec says *"A teal rule down the left of a line means must-write."* Must-write stays
     grey (§3c).
   - The restored text must say what the page actually does. `LEGACY_HOW_TO_USE` in the builder
     already rewrites this line.
6. **The typeface is not restored.**
   - 0014 lists Trade Gothic Next. 0025 §3h keeps Archivo (SHULL-CHG-0006), and so does this record.

---

## 6. What stays out of this record

- **`brand/`:** no token changes.
- **`courses/`:** no course fact is written. If the user supplies Chemistry unit targets (flag 2),
  they go through Path A as a separate, labelled edit.
- **`change-log/CHANGELOG.md`:** not touched while this record is PENDING.

---

## 7. Verification required before this is IMPLEMENTED

All of these must pass after approval and before Status moves past APPROVED.

- [ ] `git show 0f3b078:templates/notes/build_notes_docx.py` resolves, and the header code is read
      from it rather than rebuilt from memory.
- [ ] Rebuild the **Chemistry** U01 notes (student and key), and the **Geology** and **Physics**
      legacy specs, with `--verify`. None of the designed pages spills.
- [ ] **Archivo only** on every rebuilt packet (`pdffonts` / `scripts/audit_fonts.py`).
- [ ] **Ink audit** (`scripts/audit_print_ink.py`): toner is within budget, and there is **no solid
      band**. Colour appears only as rules and label type (`brand/SHULL_DESIGN_SYSTEM.md` §8).
- [ ] **SHULL-CHG-0015:** block numbers, if kept, are bare.
- [ ] **SHULL-CHG-0016:** the work-box minimum is 1.4 in, and the strip test still refuses a build
      with the work box stripped.
- [ ] **SHULL-CHG-0017:** fractions are stacked.
- [ ] **SHULL-CHG-0018:** the cue column is 1.28 in and the notes column 6.22 in.
- [ ] No type is set in `courses.<course>.primary`. It is used for rules only.
- [ ] **An independent Auditor pass**, with its table stored in `reports/`. 0025's was not stored.
- [ ] **A side-by-side of the headers against the `0f3b078` build**, covering each element in §3a
      for all three courses.
- [ ] `templates/notes/README.md` and `.claude/skills/build-document/SKILL.md` describe the restored
      headers.
- [ ] The commit message carries `SHULL-CHG-0030`, and `Implemented By` and `Verified` are filled in
      here.
