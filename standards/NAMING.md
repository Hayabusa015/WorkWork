# Naming

**Authority:** SHULL-CHG-0007. Zero-padded section codes.
**Enforced by:** `scripts/validate_codes.py`
**Folder names** are in `standards/DRIVE_ARCHITECTURE.md`; this file covers documents and images.

---

## 1. The document code is one system, not four conventions

Every SHULL document carries `U#/S#.#`, and it must match **the binder tab, the slide footer, the
student organizer, and the folder path.** They are one system. A document whose code disagrees with
its folder is broken even if it is otherwise perfect.

**Before building anything, confirm the unit and section code exists in that course's
`DECISIONS.md`.** Never build against a code that appears only in a skill file. This is the check
that would have caught the Geology numbering offset before a packet printed with the wrong footer.

## 2. The grammar

```
SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]
```

| Part | Rule |
|---|---|
| Prefix | `SHULL_`, always |
| `COURSE` | `CHEM` · `PHYS` · `GEO` |
| `Type` | from the fixed list below |
| `U##` | unit, **zero-padded to two digits** |
| `S##.#` | section, **zero-padded to two digits** before the decimal |
| `_Descriptor` | optional, only when it disambiguates |
| `_Version` | parallel-form letter, appended last |
| `_Key` | answer keys are **always separate files**, ending `_Key` |

**Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` ·
`Reference` · `Key` · `Rubric` · `Activity` · `Organizer`

### Worked examples

```
SHULL_CHEM_Slides_U08_S08.2.pptx
SHULL_PHYS_Guided_Notes_U02_S02.3.docx
SHULL_GEO_Practice_Set_U04_S04.1.pdf
SHULL_CHEM_Test_U08_S08.4_A.docx
SHULL_CHEM_Test_U08_S08.4_A_Key.docx
```

### Why padded

The Drive folders are `Section 08.4 - Balancing Equations`. Padding the filename to match lets the
code validator compare a filename against a folder path without normalising either. Two legacy
sources disagreed on this — `shull-studio` §2 wrote `S8.4`, the folder standard wrote `S08.4` — and
that ambiguity is CONFLICT-09.

## 3. Images are not course documents

No `SHULL_` prefix. Lowercase. Named for the slot they were generated for.

```
[course]_u##_s##.#_[subject].png     →  chem_u01_s1.2_rutherford.png
```

Shared backgrounds drop the unit code: `bg_glassware.png`, `bg_notebook.png`.

Images live in `_Brand/Image Library/`, never in a course folder. An image used by two courses moves
to `Image Library/Shared/` rather than being duplicated.

## 4. The in-document chip

A rounded rectangle reading `U10 / S10.4`, letter-spaced, in the condensed face. Dark fill on light
pages, outlined on dark pages. **One chip family across print document types** — practice sets,
labs, quizzes, notes. The chip should not drift between them.

**Slides do not carry the chip.** Slide System v2 replaced it with plain footer text, and the user
confirmed that on 2026-09-08 (SHULL-CHG-0013 finding 3). A slide's code lives in its footer, in the
same grammar; it is simply not in a chip. `slideGeometry.footerChip` in `brand/tokens.json` records
the decision. Restoring the slide-to-print chip link would be a new proposal.

**Numbered lists carry no marker at all — just the number.** No square, no circle, no box, in any
format. SHULL-CHG-0015. This replaces the earlier number-square rule, which is withdrawn.

**Circles** remain the section marker on dark slide dividers. That is a section marker, not a list
number, and the two do not cross.

## 5. Renaming

**Never batch-rename without confirmation.** Renames break links that may exist elsewhere — in the
gradebook, in a Google Classroom post, in a student's bookmark.

The Librarian logs an object's ID, prior name, and prior parent to `reports/drive-operations/`
**before** renaming it. A rename that was not logged cannot be rolled back.

### Previously blocked, now clear

**Geology renaming was blocked** while CONFLICT-25 left it open whether Geology had section numbers
at all. **CLOSED by SHULL-CHG-0009** — Geology has section numbers, 10 units and 54 sections, and
the codes are in `courses/geology/DECISIONS.md`. All three courses are unblocked.

The logging rule above still binds: ID, prior name, and prior parent to `reports/drive-operations/`
**before** the rename.
