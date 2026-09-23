# SHULL-CHG-0029 — Naming: a range form for multi-section and unit-level files; three fixes to the image pattern

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0029 |
| **Date** | 2026-09-23 |
| **Source** | User, 2026-09-23, relayed by the main session. The Secretary did not hear it directly. Verbatim: *"difficulty ratings, keep and add, equation box, keep it, the filename came from codex so you can change it"*. The last clause **delegates the choice of form**. The first two clauses belong to SHULL-CHG-0025. **The range form in §2 is the main session's choice, made under that delegation. It is not the user's words, and it is not his approval of this record.** It answers the question already put to him, `_S01.1_S01.3_S01.5` or `_S01.1-S01.5`, in favour of the range. Findings: split out of SHULL-CHG-0027 §6. Librarian survey F9 (`reports/drive-operations/2026-09-23_chem-u01-folder-survey.md`). Auditor items 21 and 35 (`reports/2026-09-23_chem-u01-qa-audit.md`). The image item (§2c) was raised by the main session, from the Designer's notes cover asset. |
| **Current Rule** | See §1. `standards/NAMING.md` §2 and §3, verbatim |
| **Proposed Rule** | See §2 |
| **Supersedes** | `standards/NAMING.md` §2, in part: the grammar line and the `S##.#` row. It adds an optional range end and replaces nothing else. `NAMING.md` §3, in part: the example and the location sentence. **NAMING's authority is SHULL-CHG-0007 (CONFIRMED).** This record **amends** the grammar 0007 governs. It does not reverse 0007's own decision: zero padding is kept, and the image fix extends it. See §3. |
| **Reason** | Every filename must carry exactly one `S##.#`. A unit review, a unit test, or notes covering several sections have no single section, so **they have no legal name today.** Files already on Drive and in the build use four or more ad-hoc forms (survey F9). The notes builder already writes a range and cites NAMING for it (`templates/notes/build_notes_docx.py:1333–1337`), but NAMING has no such rule. Separately, the image pattern cannot name a unit-level image, its example contradicts its own padding, and it has no repo location for build assets. |
| **Affected Agents** | Designer and builders (they construct names). Librarian (renames, filing). Auditor (checks names) |
| **Affected Skills** | `naming` (`.claude/skills/naming/SKILL.md`, steps 4 and the check list). Notes, assessment and presentation builders that write a default filename |
| **Affected Courses** | All three |
| **Risk** | **Medium.** It is a grammar change in all three courses, to a standard that SHULL-CHG-0007 governs. It needs a validator change. Renames of existing files follow, each needing its own confirmation. |
| **Recommendation** | Approve §2a–§2b, the range form. Answer §5 item 1 (what the chip shows) first, because the builders and the Day 2 tests depend on it. Approve §2c, the image fix, if he agrees with it (§5 item 2). |
| **Decision** | *Pending.* |
| **Status** | **PENDING** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. Nothing has been implemented. The required checks are in §7. |

---

## 1. Current Rule — verbatim

### 1a. `standards/NAMING.md` §2, lines 19–47

> ## 2. The grammar
>
> ```
> SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]
> ```
>
> | Part | Rule |
> |---|---|
> | Prefix | `SHULL_`, always |
> | `COURSE` | `CHEM` · `PHYS` · `GEO` |
> | `Type` | from the fixed list below |
> | `U##` | unit, **zero-padded to two digits** |
> | `S##.#` | section, **zero-padded to two digits** before the decimal |
> | `_Descriptor` | optional, only when it disambiguates |
> | `_Version` | parallel-form letter, appended last |
> | `_Key` | answer keys are **always separate files**, ending `_Key` |
>
> **Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` ·
> `Reference` · `Key` · `Rubric` · `Activity` · `Organizer`
>
> ### Worked examples
>
> ```
> SHULL_CHEM_Slides_U08_S08.2.pptx
> SHULL_PHYS_Guided_Notes_U02_S02.3.docx
> SHULL_GEO_Practice_Set_U04_S04.1.pdf
> SHULL_CHEM_Test_U08_S08.4_A.docx
> SHULL_CHEM_Test_U08_S08.4_A_Key.docx
> ```
>
> ### Why padded
>
> The Drive folders are `Section 08.4 - Balancing Equations`. Padding the filename to match lets the
> code validator compare a filename against a folder path without normalising either. Two legacy
> sources disagreed on this — `shull-studio` §2 wrote `S8.4`, the folder standard wrote `S08.4` — and
> that ambiguity is CONFLICT-09.

### 1b. `standards/NAMING.md` §3, lines 56–67

> ## 3. Images are not course documents
>
> No `SHULL_` prefix. Lowercase. Named for the slot they were generated for.
>
> ```
> [course]_u##_s##.#_[subject].png     →  chem_u01_s1.2_rutherford.png
> ```
>
> Shared backgrounds drop the unit code: `bg_glassware.png`, `bg_notebook.png`.
>
> Images live in `_Brand/Image Library/`, never in a course folder. An image used by two courses moves
> to `Image Library/Shared/` rather than being duplicated.

### 1c. Names in use today that the grammar cannot express

| Name | Where | Problem |
|---|---|---|
| `SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5[_Key].docx` | Notes builder default, `build_notes_docx.py:1333–1337`. Its comment reads *"standards/NAMING.md range form (S01.1-S01.5)"* | **Cites a rule NAMING does not contain** |
| CHEM U01 unit review and Day 2 tests, `…S01.1-S01.5…` | Auditor items 21 and 35 | Range, not in the grammar |
| `…S01.1_S01.3_S01.5…` | Auditor item 35 | List, not in the grammar |
| `SHULL_PHYS_Quiz_U01_Fall2026_A` | Drive, PHYS U01 `Quiz` (survey F9) | No section code |
| `GEO_U1_S1.2-S1.4_Guided_Cornell_Notes.docx` | Drive, GEO U01 `Guided Notes` (survey F9) | Range, unpadded, no `SHULL_` |
| `Unit 1 - Matter and Atomic Theory Notes.pptx`, `Physics Unit 1 - Motion in 1D Pres.pptx` | Drive (survey F9) | Off-grammar entirely |

---

## 2. Proposed Rule

### 2a. The range form: the main session's choice, under the user's delegation

> **Chosen by the main session under the user's 2026-09-23 delegation** (*"the filename came from
> codex so you can change it"*). **Not his words.** His decision on this record confirms or changes it.

Grammar line (replaces `NAMING.md` §2 line 22):

```
SHULL_[COURSE]_[Type]_U##_S##.#[-S##.#][_Descriptor][_Version].[ext]
```

New row in the §2 table, after `S##.#`:

> | `-S##.#` | optional range end. A file that covers more than one section names the **first and last
> section it covers**, joined by a hyphen-minus: `S01.1-S01.5`. Both ends are zero-padded, both must
> exist in the course `DECISIONS.md`, both are in the same unit, and the first comes before the last.
> A whole-unit file (unit review, unit test, unit deck) uses the unit's first and last section. |

New worked examples (added to the list, none removed):

```
SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5.docx
SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5_Key.docx
SHULL_CHEM_Study_Guide_U01_S01.1-S01.5.docx
```

**Why this form, as the main session gave it:** the unit review, the Day 2 tests and the notes
builder's default already use it. So one grammar covers all of them and nothing already built has to
change form.

**No bare unit-only form** (`…_U01.docx`, no section). Every unit in all three `DECISIONS.md` files
has sections, so the range covers every unit-level case. The survey's `SHULL_[COURSE]_[Type]_U##…`
option is **not adopted**.

### 2b. `scripts/validate_codes.py`

**Behaviour today.** This comes from reading line 16. **It has not been run.**
Pattern: `SHULL_(CHEM|PHYS|GEO)_[A-Za-z_]+_U(\d{1,2})_S(\d{1,2}\.\d)`

- **Only the first code of a range is checked.** `…_U01_S01.1-S01.9` would pass, although 1.9 does
  not exist.
- **A `SHULL_` filename with no section code is skipped silently.** It does not match, so it is
  neither passed nor failed. `SHULL_PHYS_Quiz_U01_Fall2026_A` would be invisible to the validator.

**Proposed:**

- Capture the optional `-S(\d{1,2}\.\d)` end. Check that both ends exist, share the unit, and are in
  order.
- Report a `SHULL_(CHEM|PHYS|GEO)_` filename that has no `_U##_S##.#`. Run the check once and review
  the hits **before** making it an error, because existing repo text may hit it.

### 2c. The image pattern: the smallest fix

`NAMING.md` §3 has three problems:

| # | Problem | Evidence |
|---|---|---|
| 1 | The pattern requires a section code, but **a unit-level image has none** | The Designer named the notes cover image `templates/notes/assets/chem_u01_cover_atom.png`, which is outside the pattern |
| 2 | The pattern pads (`s##.#`), but **its own example is unpadded** (`s1.2`), and so is the only committed image | `templates/slide/assets/chem_u01_s1.4_nuclear_notation.png` |
| 3 | It places images only in Drive `_Brand/Image Library/`, but **a committed spec needs a repo path** | The repo already uses `templates/<type>/assets/` (`templates/slide/assets/`, `templates/notes/assets/`) |

**Proposed replacement for §3** (the unchanged sentences are kept word for word):

> ## 3. Images are not course documents
>
> No `SHULL_` prefix. Lowercase. Named for the slot they were generated for.
>
> ```
> [course]_u##_s##.#_[subject].png     →  chem_u01_s01.2_rutherford.png
> [course]_u##_[subject].png           →  chem_u01_cover_atom.png        (unit-level, no section)
> ```
>
> Section codes are zero-padded, as in §2. Shared backgrounds drop the unit code: `bg_glassware.png`,
> `bg_notebook.png`.
>
> An image a committed spec builds from lives in the repo, under `templates/<type>/assets/`. Images
> used outside the repo build live in `_Brand/Image Library/`, never in a course folder. An image used
> by two courses moves to `Image Library/Shared/` rather than being duplicated.

This rename falls out of it and is **not part of this record**: the committed
`chem_u01_s1.4_nuclear_notation.png` becomes `chem_u01_s01.4_…` under fix 2. The deck spec that
references it would change in the same commit. It also carries the folded code 1.4 (SHULL-CHG-0028).
So it is flagged for whoever rebuilds that deck, and not renamed here.

---

## 3. Supersedes

| Rule | Where | What happens to it |
|---|---|---|
| Grammar line `…_U##_S##.#[_Descriptor]…` | `NAMING.md` §2 line 22 | **Extended** with `[-S##.#]`. Every existing single-section name stays valid |
| Zero padding of unit and section | `NAMING.md` §2, SHULL-CHG-0007 | **Kept.** Applies to both range ends and to image section codes |
| Image example `chem_u01_s1.2_rutherford.png` | `NAMING.md` §3 line 61 | **Superseded** by the padded example. The pattern itself was already padded |
| "Images live in `_Brand/Image Library/`, never in a course folder." | `NAMING.md` §3 line 66 | **Narrowed.** Build assets live in `templates/<type>/assets/`. `templates/` is not a course folder, so the "never in a course folder" half stands |

**Conflict with a LOCKED record: none found.** SHULL-CHG-0007 decided padding, and padding is kept.
Because NAMING's authority line cites 0007, this record is marked as amending that standard, so the
change is visible and not silent.

---

## 4. Interactions

- **SHULL-CHG-0027** decides *where* these files go: loose in the unit folder, or in a unit-level
  folder if one exists. This record decides only *what they are called*. Neither waits on the other.
- **SHULL-CHG-0028** retires the code 1.4. A range may **span** a retired code (`S01.1-S01.5`), but
  may not **end** on one. The validator's both-ends check enforces that once 1.4 stops parsing as a
  live code (0028 option 1(b)).
- `NAMING.md` §2 "Why padded" argues from comparing a filename against its **section** folder path.
  A range file has no section folder. The naming skill's check *"the code matches the folder path it
  sits in"* needs a range reading: the unit matches the unit folder.

---

## 5. For the user

| # | Question | Why it matters |
|---|---|---|
| 1 | **The Auditor's point: a range can imply sections the file does not cover.** The CHEM U01 notes cover S01.1, S01.3 and S01.5, but `S01.1-S01.5` also implies 1.2 and 1.4. The Day 2 tests show the same problem the other way round (audit item 21). Their chip reads "U01 / S1.1, S1.3–S1.5" while the filename `S01.1-S01.5` includes 1.2. `NAMING.md` §1 requires the code on the document, in the filename and in the folder path to agree. **What should the chip and footer show on a range file?** (a) the same range as the filename, which agrees but is imprecise, or (b) the exact sections covered, with §1 amended to say the filename range must *contain* them. | Decides how the Designer fixes audit item 21, and what the builders print |
| 2 | **Image pattern (§2c): approve the three fixes?** A unit-level form `[course]_u##_[subject].png`, padded section codes, and build assets under `templates/<type>/assets/`. **Sub-point:** if the same image is also filed to `_Brand/Image Library/`, it exists in two places. Which copy is authoritative? The Secretary suggests the repo copy for build assets, because the repo is canonical for the system, but does not decide it. | Unblocks naming the notes cover image |

The earlier question, list form or range form, is **closed** by the delegation. The range form is
§2a.

---

## 6. Implementation plan — only after APPROVED

**Nothing is edited now.**

| # | File | Change |
|---|---|---|
| 1 | `standards/NAMING.md` | §2 grammar line, the new `-S##.#` row, worked examples (§2a). §3 per §2c. §1 per the answer to §5 item 1 |
| 2 | `.claude/skills/naming/SKILL.md` | Step 4: the range. Check list: a range's unit matches the unit folder. It **points to** NAMING and does not restate the grammar |
| 3 | `scripts/validate_codes.py` | Per §2b |
| 4 | `change-log/CHANGELOG.md` | Row for 0029 |

`templates/notes/build_notes_docx.py` already writes the range and needs no change. Its comment
becomes true once edit 1 lands. **Renames of existing Drive and repo files are not in this record.**
Each needs confirmation and a pre-rename log (`NAMING.md` §5). Edit 2 is under `.claude/`, with the
same caveat as SHULL-CHG-0026 §5 item 2.

---

## 7. Verification required before this is IMPLEMENTED

- [ ] `NAMING.md` §2 states the range form once. `naming/SKILL.md` points to it and does not restate
      it (grep `S##.#-S##.#` finds it in `standards/NAMING.md` only)
- [ ] `python3 scripts/validate_codes.py` is **run** against test names:
      `SHULL_CHEM_Guided_Notes_U01_S01.1-S01.5` passes. `…_U01_S01.1-S01.9` fails. `…_U01_S01.5-S01.1`
      fails. `…_U01_S01.1-S02.1` fails. `SHULL_PHYS_Quiz_U01_Fall2026_A` is reported
- [ ] The validator passes on the repo as it stands, or every new hit is listed and dealt with
- [ ] `NAMING.md` §3 example is padded. The unit-level image form is present
- [ ] `legacy/` untouched
- [ ] Commit carries `SHULL-CHG-0029`. `Implemented By` and `Verified` filled in here
