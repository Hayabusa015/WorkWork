# SHULL-CHG-0025 — Guided notes: the paged redesign, from the Codex reference

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0025 |
| **Date** | 2026-09-23 |
| **Source** | User. Verbatim: *"i took this over to chat gpt codex and we worked on this to improve it to this, i like how we seperated and broke down the slides like this a bit more and improved it, can you take what we did here to improve this and add it to our repo to update our guided notes propfile."* and *"maybe any shading or somehting that would improve this on greyscale?"* Four follow-up answers from the same conversation are in §2. **Added 2026-09-23:** a later answer, relayed by the main session, verbatim: *"difficulty ratings, keep and add, equation box, keep it, the filename came from codex so you can change it"*. Its first two parts are recorded at §6 items 4 and 8. The third part belongs to SHULL-CHG-0029. **None of it approves this record.** |
| **Reference artifact** | `/root/.claude/uploads/26f8099c-89f2-51d6-8b84-531faeb169a3/3933feb4-SHULL_CHEM_U01_Guided_Notes_Cover_and_Review.pdf`. It has 8 pages and was made outside this repository with ChatGPT/Codex, using ReportLab and Helvetica/Arial. **It is not stored in the repo.** It lives under `/root/.claude/uploads/` and may not persist. §3 describes it from the page renders. |
| **Current Rule** | See §1 — verbatim, from SHULL-CHG-0014, SHULL-CHG-0016 and SHULL-CHG-0024 |
| **Proposed Rule** | See §3 |
| **Supersedes** | See §4. In short: from **SHULL-CHG-0024**, the per-page watermark, the per-cue recall lines, the EXTRA box, the 2×2 study recap, the lime/course-accent must-write bar and the course-accent rail. From **SHULL-CHG-0014**, the continuous section rhythm, the full-width summary and closing boxes, and course colour in the printed notes. From **SHULL-CHG-0016**, the GIVEN/NEED table only. The work box itself stays. |
| **Reason** | The user prefers how the Codex version splits a section into titled blocks and pages, and asked for it to become the template. It also answers his greyscale question without breaking `brand/SHULL_DESIGN_SYSTEM.md` §8. |
| **Affected Agents** | Designer (is rebuilding the template in the working tree now; builds from it afterwards). Auditor (the independent pass that SHULL-CHG-0024 never had — see §7). Secretary (records, and implements on approval). |
| **Affected Skills** | `build-document` — `.claude/skills/build-document/SKILL.md` is being updated by the designer to describe the new layout. `templates/notes/README.md` is being updated by the designer too. **Neither update is committed.** Both land with this change, and not before it. |
| **Affected Courses** | All three — Chemistry, Physics, Geology. The template is shared. |
| **Risk** | **Medium** — a shared template, three courses. See §6 for the items that need the user. **Two touched LOCKED rules** (§6, items 1 and 2). Item 1 has been resolved in favour of the LOCKED rule, pending the user's confirmation. Item 2 is open. |
| **Recommendation** | Approve the layout, subject to the user's answers in §6. The four decisions in §2 are already his. What is left is a set of places where the Codex reference and a standing rule disagree. §6 lists them. None is settled without the user. Items 1 and 3 have been brought back to the existing LOCKED rules (0015, 0016), pending his confirmation. Items 4 and 8 were answered on 2026-09-23. The recorded readings of those answers are the main session's, and his decision on this record confirms them. The others are open. |
| **Decision** | **Approved by the user, 2026-09-23**, in the main session. Verbatim: *"approved"*, then *"i like the newer style."* His answers to §6: *"difficulty ratings, keep and add, equation box, keep it, the filename came from codex so you can change it"*. Recorded under SHULL-CHG-0026. The approval covers the amended record, including bare block numbers (0015) and the 1.4 in work box (0016). |
| **Status** | **APPROVED** |
| **Implemented By** | *(blank — the rebuild is in progress in the working tree and will not be committed until the user approves this record)* |
| **Verified** | No — nothing has been implemented. The checks that will be required are in §7. |

**Depends on SHULL-CHG-0024.** This record's "Current Rule" is the template as the seven commits in
0024 left it. The user has not yet acknowledged 0024. This record makes sense whichever way 0024
goes, because it replaces most of what 0024 added. But 0024 should be answered first.

---

## 1. Current Rule — verbatim

### 1a. SHULL-CHG-0014, "What is preserved"

> - The section rhythm: header bar → learning target → Cornell rows → summary box.
> - **The closed-notes summary** — "close your notes before you write this" — and the self-check.
> - The unit wrapper: brand bar, name/date/period, targets ∥ key terms, "how these notes work",
>   section checklist.
> - The close: "pulling it together", checklist, big picture, **"still fuzzy on"**.

### 1b. SHULL-CHG-0014, Finding 1 — must-write

> | **Must-write rule** | **sage green** | Geology `primary` (Terra Teal) — a fill/rule, never type |

### 1c. SHULL-CHG-0016, "What his packet does" — the worked-example parts

> 3. **GIVEN / NEED table** — 2×2 nested, 0.72 in label column
> 4. **WORK box** — 1×1 nested table, `trHeight` 1411 dxa (**0.98 in**), `hRule="atLeast"`,
>    `cantSplit`, hairline border on all four sides, no fill

with the implemented minimum: *"Implemented at 1.4 in rather than his 0.98 in."*

### 1d. SHULL-CHG-0024, §3 — as committed at `4234b69`

> | 1 | `ed41fa0…` | Each section starts on a new page. The front matter becomes a standalone title page. New optional `titleImage` spec field (Bohr model). |
> | 4 | `fcdd544…` | `add_watermark()`: a floating behind-text header image on every page. … `study_recap_page()`: a standing last page, with a soft warning when absent. |
> | 5 | `f76fea6…` | … `matter_flowchart()`. The must-write accent bar moves … to a cell border. |
> | 6 | `9766298…` | A rule line under each cue question. A standing "EXTRA — anything else from the slide" box on every row. |
> | 7 | `4234b69…` | … The cue column gets an accent rail. … Rows get numerals. EXTRA is demoted to grey. The title image is framed. |

---

## 2. Decisions the user has already made — 2026-09-23, verbatim

The user answered four questions in the conversation. These are his choices. The record carries
them and does not reopen them.

| Question | Answer, verbatim | What it means |
|---|---|---|
| Format | **"Keep editable Word (Recommended)"** | The output stays `.docx`, for SHULL-CHG-0014's reason: guided notes are the document a teacher edits after the fact. It does not go HTML→PDF, the Codex route. |
| Watermark | **"Cover image only (Recommended)"** | The per-page watermark is removed. The atom image becomes the cover hero. |
| Recall | **"Codex way (Recommended)"** | The rule line under each cue is removed. Recall lives in a RECALL block in each section, plus a Quick Recall list on the review page. |
| Shading | **"Table headers + chips (Recommended)"** | *As offered:* a very light tint (`ground.parchment`, through `pal.surface`) goes on fill-in table header rows and on small chips only: block numbers and the RECALL / RECAP / REVIEW tags. No shaded cue column, no row backgrounds, no shaded page headers. This is the tint `brand/SHULL_DESIGN_SYSTEM.md` §8 allows: *"If shading is genuinely needed for scanability, use a very light grey tint."* **Narrowed. See the note below.** |

**Note, 2026-09-23 — the shading option conflicted with a LOCKED rule.** The answer above is the
user's and is recorded exactly as he gave it. **The option was offered by the orchestrating session
without checking SHULL-CHG-0015.** Its block-number part conflicts with that LOCKED rule: *"No box,
square, circle or marker around a list number. Just the number. Every format, no exceptions."*

**Resolution applied:** block numbers stay **bare**, with no tint, no chip and no border. The light
tint is kept only on:

- fill-in table header rows, and
- the RECALL / RECAP / REVIEW tags, which are labels, not list numbers.

This keeps the LOCKED rule as it stands and does not change it. **The user has not yet confirmed the
narrowing.** See §6 item 1.

---

## 3. Proposed Rule

**What the reference is.** An 8-page Chemistry U01 packet covering S01.1, S01.3 and S01.5. Page 1
is the cover. Pages 2–7 are the three sections, two pages each. Page 8 is the Concept Review. The
section codes and titles match `courses/chemistry/DECISIONS.md` U1.

### 3a. Page structure — paged, not flowing

- **Every content page has its own head.** It carries the running head (`SHULL SCIENCE / CHEMISTRY /
  GUIDED NOTES`), the section title, the section code at the top right (`S01.1`), and a subtitle
  written for that page. For example, p.2 reads *"Classify matter as an element, compound, or
  mixture; then classify mixtures."* and p.3 reads *"Mixtures, classification practice, and a
  check of your understanding."*
- **About three blocks per page. A section spans two pages.**
- **Footer:** `SHULL SCIENCE / CHEMISTRY / UNIT 01` at the left, and a **two-digit page number**
  (`01`, `02` …) at the right.

### 3b. The block — open layout

- **No boxed cells.** One horizontal rule between blocks and one thin vertical divider between the
  cue and notes sides.
- **Cue side:** the block number (`01`, `02` …), the block title (*"Vocabulary"*, *"The matter
  flowchart"*), then one or two cue questions. **The block number is bare**, with no tint, chip or border
  (SHULL-CHG-0015; see the §2 note). The RECALL / RECAP / REVIEW tags carry the light tint.
- **Notes side:** capture prompts carried over from SHULL-CHG-0024 `f76fea6` (`DEFINE: matter`,
  `Copy: the quick test for telling them apart`), each over a write line. Blocks can also hold a
  fill-in table, the flowchart, or a worked problem.
- **"Extra notes:"** is a single labelled line at the foot of every block. It replaces the EXTRA box.
- **Must-write** is a grey rule down the left of the line. It is no longer lime or the course
  accent.

### 3c. Worked problems

- **`Given:` and `Find:` sit inline** in bold-label text, with a labelled **WORK** box (*"WORK /
  show your reasoning and units"*) below them and an answer line under that. This replaces the
  GIVEN/NEED table.
- **SHULL-CHG-0016 stands.** A problem to solve still gets a bordered work box that grows but does
  not shrink below its minimum, does not split across a page, and is enforced at build time.
- **The work-box minimum stays 1.4 in, per SHULL-CHG-0016.** The Codex reference's box is about
  1.1 in and is not adopted. *Note, 2026-09-23:* the designer's working-tree rebuild had set the
  minimum to 1.1 in to match Codex. It has been told to restore 1.4 in. See §6 item 3.

### 3d. Section ends — two-column rhythm, not full-width boxes

- **RECALL — Section summary.** The cue side reads *"Close your notes before you write."* and *"Use
  the checklist to find what still needs practice."* The notes side holds a prompt, write lines, and
  an "I can…" checklist. This replaces the full-width summary box. The instruction 0014 called *"the
  point of the box"* survives.
- **RECAP** — an optional reference block, for example *"Particle-count reminders"* (p.5).
- **REVIEW — Pulling it together** — the big picture, a completion checklist, and *"Still fuzzy on /
  bring to review day:"*. This replaces the full-width closing box. "Still fuzzy on" survives.

### 3e. The flowchart

Drawn as an **image** with diagonal connectors: MATTER at the top, two boxes below it, and four
below those, all empty for students to fill in. It replaces the table-built `matter_flowchart()`.

### 3f. The cover — page 1

- The atom image as the hero, at the top right. This replaces the per-page watermark.
- Course/unit eyebrow, unit title, `GUIDED NOTES • S01.1 / S01.3 / S01.5`, school, and Name / Date /
  Period.
- **Section breakdown / concepts to master.** Each section has its code, title, a one-line
  description, and a **difficulty rating out of 10**, with the note *"Estimated for advanced high
  school students: 1 = introductory; 10 = highly challenging."* See §6 item 4.
- **Equation toolbox.** Formulas in two columns.
- **Key terms, grouped by section.**
- **How to use the notes.**

### 3g. The last page — Concept Review

A standing **Concept Review** page replaces the 2×2 Study Recap. It has one block per section, each
with the explanation, a two-column contrast where one helps, and a **"Watch out:"** line. It closes
with **"QUICK RECALL / COVER THE EXPLANATIONS ABOVE"**, a numbered list of questions.

### 3h. Ink and type

- **Greyscale throughout.** No course accent colour in the printed notes. See §6 item 5.
- **The font stays Archivo.** The reference's Helvetica/Arial is **not** adopted. Typography is
  brand-locked (SHULL-CHG-0006).
- **The only tint** is a very light tint (`ground.parchment`, through `pal.surface`) on:
  - fill-in table header rows, and
  - the RECALL / RECAP / REVIEW tags.

  Nothing else is tinted: not block numbers (bare, per SHULL-CHG-0015), not the cue column, not
  row backgrounds, not page headers.

### 3i. Older specs

The Geology and Physics specs (`templates/notes/specs/geo_u01_s01.2-s01.4.json`,
`phys_u01_s01.1-s01.4.json`) are **converted to the paged layout automatically at build time**. They
are not rewritten. See §6 item 6.

---

## 4. Supersedes

| Rule | From | Replaced by |
|---|---|---|
| Per-page header-image watermark (`add_watermark()`, and its 3 in / 80%-down placement) | 0024 `fcdd544`, `4234b69` | Cover hero image only |
| A rule line under each cue question | 0024 `9766298` | A RECALL block per section, plus Quick Recall on the review page |
| The standing "EXTRA — anything else from the slide" box on each row, and its grey demotion | 0024 `9766298`, `4234b69` | One "Extra notes:" line per block |
| 2×2 Study Recap as the standing last page (`study_recap_page()`) | 0024 `fcdd544` | Concept Review page |
| Must-write bar in the course accent (lime in Chemistry), drawn as a cell border | 0014 Finding 1; 0024 `f76fea6` | A grey rule |
| Course-accent colour in print: the cue-column accent rail, accent header rules, accent labels | 0014 Finding 4; 0024 `4234b69` | Greyscale |
| The framed standalone title page | 0024 `ed41fa0`, `4234b69` | The new cover (§3f) |
| Table-built `matter_flowchart()` | 0024 `f76fea6` | A flowchart image with diagonal connectors |
| Section rhythm *"header bar → learning target → Cornell rows → summary box"*, flowing | 0014 "What is preserved" | Paged: page head → about three open blocks → RECALL / RECAP / REVIEW blocks |
| Full-width summary box and closing ("pulling it together") box | 0014 "What is preserved" | RECALL and REVIEW blocks in the two-column rhythm. The content survives: "close your notes", the checklist, the big picture, "still fuzzy on". |
| Unit wrapper: *"targets ∥ key terms, 'how these notes work', section checklist"* | 0014 "What is preserved" | The cover in §3f |
| GIVEN / NEED 2×2 nested table | 0016, part 3 | `Given:` / `Find:` inline. **The work box rule is not superseded.** |

**Not superseded:** every section starts on a new page (0024 `ed41fa0`). `fillin_table()` and the
`"table"` key (0024 `e59ba21`). Capture-not-synthesis prompts (0024 `f76fea6`). The
split-protection fixes (0024 `e59ba21`, `2a02a58`). The `.docx` format (0014). Archivo (0006). The
work box and its 1.4 in minimum (0016). Bare block numbers (0024 `4234b69`, and SHULL-CHG-0015).

---

## 5. What stays out of this record

- **`courses/`, except one split-out edit.** The template writes no course fact. The per-section
  difficulty values **are** course facts (§6 item 4, answered 2026-09-23). Under `CHANGE_CONTROL.md`
  §1 they are split out as a separate, labelled Path A edit to `courses/chemistry/DECISIONS.md`. See
  §8.
- **`brand/`.** No token changes. `ground.parchment` is used as it already exists.

---

## 6. For the user — conflicts and risks

In the order they block. One question at a time. Nothing here is settled without the user.

1. **Block-number chips vs SHULL-CHG-0015 (LOCKED) — resolved in favour of 0015, pending the user's
   confirmation.** SHULL-CHG-0015 reads: *"No box, square, circle or marker around a list number.
   Just the number. Every format, no exceptions."* The §2 shading option, as offered, put a
   light-tint chip behind the block numbers (`01`, `02` …). The orchestrating session offered it
   without checking 0015.

   **Resolution applied (2026-09-23):** block numbers stay bare, with no tint, chip or border. The
   tint stays on fill-in table header rows and on the RECALL / RECAP / REVIEW tags. Those are labels,
   not list numbers. The reference PDF also prints bare numbers.

   The LOCKED rule is kept and not changed. **To confirm with the user:** does he accept the
   narrowing of his "Table headers + chips" answer? If he wants tinted block numbers, that is a
   change to SHULL-CHG-0015 and needs its own record.

2. **CONFLICT with a LOCKED rule — cue-column width vs SHULL-CHG-0018.** 0018 fixed the split at
   **1.28 in / 6.22 in**. The reference's cue column measures **about 1.8 in** on the render. That
   is approximate, read from pixels at about 90 px/in. The Proposed Rule does not say which width
   applies. **This record does not change 0018.** If the user wants the Codex width, that changes
   0018 and needs his say.

3. **Work-box height vs SHULL-CHG-0016.** 0016 implemented a **1.4 in** minimum. The reference's
   WORK boxes measure **about 1.1 in**. **The minimum stays 1.4 in, per 0016.** *Note, 2026-09-23:*
   the designer's working-tree rebuild had set 1.1 in to match Codex. It has been told to restore
   1.4 in, and §7 checks for it. This record also keeps the
   build-time refusal for rows titled EXAMPLE / PRACTICE / YOUR TURN and the like, which the new
   block titles (*"Chlorine example"*, *"Your turn: copper"*) must still trigger. Separately, 0016
   made the work-box label the course accent because a hairline-coloured label measured 1.62:1. In
   greyscale the label must use a grey that still clears contrast on white.

4. **Difficulty ratings are new course content. ANSWERED 2026-09-23.** The Codex cover rates S01.1
   at 1/10, S01.3 at 2/10 and S01.5 at 3/10. These did not come from this repository.
   `courses/chemistry/DECISIONS.md` has no difficulty rating.

   **The user, verbatim:** *"difficulty ratings, keep and add"*

   **The main session's reading. Not his words.** Keep the ratings on the notes cover, and add them
   as a standing feature of the notes template. The per-section values are course facts. So they live
   in `courses/chemistry/DECISIONS.md`, and not in a skill or template. The template carries the
   **field**. It carries no numbers. See §8, edit 2.

   Still to watch (flagged, not blocking):
   - The Codex cover rated only S01.1, S01.3 and S01.5. **S01.2 has no rating**, and none is invented
     here. S01.4 has none because it is folded into S01.3 (SHULL-CHG-0028).
   - Physics and Geology have **no values**. Their covers leave the field empty until he gives them.
   - A notes spec that states a rating restates a fact that lives in `DECISIONS.md`. The spec must
     match it, and §7 checks that. A builder that reads the value from `DECISIONS.md` would remove the
     duplicate. That is a possible later improvement, not part of this record.

5. **Greyscale removes course colour from printed notes in all three courses.** §8 already limits
   print colour to *"a thin accent only"*, so this is compatible. But it changes each course's
   printed identity. `templates/lab/README.md`, as corrected under SHULL-CHG-0010, says *"Course
   identity colours apply across all media, not projection only."* Worth confirming he means this for Physics and Geology too, not only for this Chemistry
   packet.

6. **The Geology structure 0014 preserved is being redesigned.** 0014 adopted his Geology packet
   (*"here is the guided notes for geology I loved"*) on the basis that *"the structure is the asset
   and none of it was redesigned."* This record converts that packet, and the Physics one, to a
   layout that came from a Chemistry packet. His instruction was to update the guided notes profile,
   which reads as all courses. But it reverses 0014's premise, so it is named here.

7. **Smaller points — flagged, not blocking.**
   - `ground.parchment` is `#EDF0E5`, which has a faint green cast. §8 says *"very light grey
     tint"*. It measures grey 238, so it prints as a pale grey on a mono copier, but it is not
     literally grey on a colour printer.
   - The reference's cover says *"Gray side rules mark must-write notes (lime blocks in the
     slides)."* Lime is Chemistry's colour. That sentence is on a student page and cannot go to
     Physics or Geology as written.
   - A flowchart drawn as an image cannot be edited in Word the way the rest of the document can.
     That sits slightly against 0014's reason for choosing `.docx`.

8. **The equation toolbox and RECAP give the answers to the S01.3 fill-in prompts. ANSWERED
   2026-09-23.** The Auditor asked whether the cover's equation toolbox (§3f) and the RECAP block
   (§3d) should stay, since together they hand students the answers to the S01.3 fill-in prompts.
   The question reached the Secretary through the main session. It is not in a report in this
   repository, because the Auditor's 2026-09-23 audit left guided notes out of scope.

   **The user, verbatim:** *"equation box, keep it"*

   **The main session's reading. Not his words.** The cover toolbox and the RECAP stay where they
   are, even though they give the S01.3 answers, because that matches the Codex reference.

   **Flagged, not resolved:**
   - The main session gave its reason as "the approved reference". **The reference is not approved.**
     This record, which would adopt it, is still PENDING. The accurate reason is that it matches the
     reference the user chose to work from.
   - His words name the "equation box" only. Reading them as covering the RECAP too is the main
     session's reading. He confirms or corrects it when he decides this record.

---

## 7. Verification required before this is IMPLEMENTED

These must pass after the user approves and before Status moves past APPROVED:

- [ ] `pdffonts` / `scripts/audit_fonts.py`: Archivo only, on every rebuilt packet
- [ ] `scripts/audit_print_ink.py`: toner within budget, **widest solid band stays under the fill
      limit** with the new tints
- [ ] The Chemistry U01 packet builds from a spec that **is committed** to `templates/notes/specs/`.
      0024 §5 found that the features it added were never exercised by a spec in the repository.
- [ ] The Geology and Physics specs build through the automatic conversion, and every page is
      inspected
- [ ] 0016's enforcement still fires: strip a `problem` block and the build refuses
- [ ] Work-box minimum is 1.4 in in the builder (not 1.1 in), and holds on the rendered page
- [ ] Block numbers render bare, with no tint, chip or border (SHULL-CHG-0015). The tint appears
      only on fill-in table header rows and on the RECALL / RECAP / REVIEW tags.
- [ ] The mis-cited Change IDs from SHULL-CHG-0024 finding 1 are gone:
      `grep -n "SHULL-CHG-001[89]\|SHULL-CHG-0020" templates/notes/build_notes_docx.py` returns only
      correct citations
- [ ] If `templates/_shull_docx.py` changes, both worksheet builders are rebuilt and checked
      (0024 finding 2)
- [ ] `templates/notes/README.md` and `.claude/skills/build-document/SKILL.md` describe what the
      builder actually does
- [ ] **An independent Auditor pass**, which 0024 never had
- [ ] The difficulty rating is a template **field** with no default value.
      `grep -rn "/10" templates/notes/build_notes_docx.py .claude/skills/build-document/SKILL.md templates/notes/README.md`
      finds no per-section rating
- [ ] Every rating in a committed notes spec matches `courses/chemistry/DECISIONS.md` exactly
- [ ] The cover equation toolbox and the RECAP block are present, as the §6 item 8 answer requires
- [ ] Commit message carries `SHULL-CHG-0025`, and `Implemented By` / `Verified` are filled in here

---

## 8. Implementation plan — the edits, split by layer

Under `CHANGE_CONTROL.md` §1, a change that touches both layers is split into two labelled edits.

| Edit | Path | File(s) | Change |
|---|---|---|---|
| 1 | **B** (build) | `templates/notes/build_notes_docx.py`, `templates/_shull_docx.py` if touched, `templates/notes/README.md`, `.claude/skills/build-document/SKILL.md`, and the committed Chemistry U01 spec | The layout in §3. It includes the cover's **difficulty-rating field**, a standing feature with no values in the template, and the equation toolbox and RECAP kept as they are (§6 item 8) |
| 2 | **A** (course) | `courses/chemistry/DECISIONS.md` | A dated entry at the **top** of the decision log recording the U1 difficulty ratings, and the values placed next to the U1 curriculum map. Text below |

Edit 2 draft, for the top of the decision log (`CHANGE_CONTROL.md` §5):

```markdown
### 2026-09-23 — U1 section difficulty ratings
Guided-notes covers carry a difficulty rating out of 10 per section ("Estimated for advanced high
school students: 1 = introductory; 10 = highly challenging"). Unit 1: S1.1 Matter & Changes 1/10 ·
S1.3 Atomic Structure 2/10 · S1.5 Average Atomic Mass 3/10. S1.2 is not yet rated. S1.4 has no
rating because it is folded into S1.3 (SHULL-CHG-0028). The values came from the Codex notes cover;
Matt kept them 2026-09-23 ("difficulty ratings, keep and add").
Supersedes: None (first record of difficulty ratings).
Status: CONFIRMED · SHULL-CHG-0025 (Path A edit split from a Path B record)
```

The exact wording and position of the values next to the U1 curriculum map are settled at
implementation. **They must not break the section-code parse** in `scripts/_shullos.py`
`section_codes()`. For example, "1/10" must not be written straight after a code in a way that adds
or drops a code. Run `scripts/validate_codes.py` afterwards. The Chemistry code count must not
change.

Edits 1 and 2 are separate commits, each carrying `SHULL-CHG-0025`. Edit 2 depends on nothing in
edit 1 and may land first. If SHULL-CHG-0028 lands first, the S1.4 wording above stands. If it does
not, the S1.4 clause is dropped rather than asserting a fold that is not yet recorded.
