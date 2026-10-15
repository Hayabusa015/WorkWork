# Naming

**Authority:** SHULL-CHG-0024. Short, section-led names.
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

**Authority:** SHULL-CHG-0024 (supersedes SHULL-CHG-0007's padded `SHULL_` grammar).

Names are short so they stay readable in a narrow folder window. The **folder path carries the
course**; the name does not repeat it.

```
Section-level:  [S.S] [Type] [Version] [Key] - [Topic].[ext]
Unit-level:     Unit [X] [Type] [Version] [Key] - [Unit Title].[ext]
```

| Part | Rule |
|---|---|
| `S.S` | the section code exactly as the course `DECISIONS.md` writes it: `1.2`, `10.4`. Not padded. |
| `Unit X` | the unit number, not padded: `Unit 3` |
| `Type` | from the fixed list below, written with spaces |
| `Version` | parallel-form letter (`A`, `B`, `C`), only when there is one |
| `Key` | answer keys are **always separate files**; the word `Key` follows the type or version |
| `Topic` / `Unit Title` | read from the course `DECISIONS.md`, never typed from memory. If it is not there, **leave it off**; a name without a topic is correct, an invented topic is not. |
| separator | space, hyphen, space. A name never contains `: / \ * ? " < > |`. They are illegal on Windows and in synced folders, so they are dropped from a topic. |

A document that covers **more than one section** is unit-level. A document that covers one is
section-level.

**Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` ·
`Reference` · `Key` · `Rubric` · `Activity` · `Organizer`

### Worked examples

```
Unit 3 Guided Notes - Atomic Structure.docx
1.2 Practice Set - History of the Atomic Model.docx
4.1 Slides - Layers of the Earth.pptx
1.4 Quiz A - Reaction Time.docx
1.4 Quiz A Key - Reaction Time.docx
Unit 8 Test B - Unit Title.docx
```

Two courses can both have a `1.4 Slides`. They live in different course folders, so this is not a
collision. A file copied out of its folder loses its course. Put it back before filing.

The code is carried **inside** the document, in the chip (section 4) and the slide footer, which
is where it has to match the binder tab and the folder path.

Builders and the app take the name from `templates/_shull_name.py` and
`templates/shull_name.cjs`. They implement this grammar and are pinned to the examples above by
their tests.

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
