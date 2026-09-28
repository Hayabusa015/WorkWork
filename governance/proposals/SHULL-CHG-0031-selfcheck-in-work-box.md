# SHULL-CHG-0031 — Worksheets: the self-check bracket prints inside the work box

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0031 |
| **Date** | 2026-09-28 |
| **Source** | User, 2026-09-28. The main session relayed his words, so the Secretary did not hear them directly. He was looking at the optional Chemistry S1.5 practice set, where each self-check answer (for example *"[ 175.03 amu ]"*) sits on its own line below the work box. He said, verbatim: *"Theres so much wasted space with the answer. Remove the answer reallocate space. Condense add a 6th problem"*. Asked whether to drop the answers, he said, verbatim: *"Ok I lied dont remove the answer. Just put it in the work.box, I dont know why you are putting it outside the box and wasting so much space just to put a small answer in the corner"*. **Neither statement approves this record.** They are the finding it is written from. |
| **Current Rule** | See §1, quoted verbatim. |
| **Proposed Rule** | See §2. |
| **Supersedes** | `templates/worksheet/build_worksheet_docx.py` `question_card()`, the `selfCheck` block (lines 405–410 as first read, §1a): the bracket as a separate right-aligned 8 pt paragraph after the work box. **Applies only to questions that have a work box** (§2). SHULL-CHG-0021 is **not** superseded. |
| **Reason** | The bracket is one short line of 8 pt type. On its own line it adds height to every calculation card. The work box already has empty space in its bottom-right corner. |
| **Affected Agents** | Designer (builder change). Auditor (verification, §5). Secretary (records this, and implements it once approved). |
| **Affected Skills** | None directly. `templates/worksheet/README.md` "Self-check answers" says *which* questions carry a bracket, not where it prints. If placement is documented there on implementation, that is part of this change. |
| **Affected Courses** | All three, because the template is shared. **Chemistry:** the brackets move into the box. **Physics:** no change (§3). **Geology:** no change. Geology has no calculations, so it has no brackets. |
| **Risk** | **Low.** Placement only. No token, no LOCKED rule and no course fact changes. The one layout risk is a student writing over the bracket in the corner (§4, item 4). |
| **Recommendation** | Approve §2 as written. Answer §4 item 1 first, because it decides what happens to code that already cites this ID. |
| **Decision** | *(blank. Awaiting the user.)* |
| **Status** | **PENDING** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. The required checks are in §5. |

---

## 1. Current Rule, verbatim

### 1a. `templates/worksheet/build_worksheet_docx.py`, `question_card()`, lines 405–410 (as first read)

```python
    if q.get("selfCheck"):
        # Bracketed self-check answers for NUMERIC results only - never for an
        # explanation, a vocabulary term, or a graph reading, where the bracket hands
        # over the whole answer.
        pp = para(cell, q["selfCheck"], 8, color=pal.label)
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
```

This runs after the work box (lines 398–401 at that read), so the bracket is a separate paragraph
below the box. **This file changed while this record was being drafted. See §4, item 1.**

### 1b. SHULL-CHG-0021

`governance/proposals/SHULL-CHG-0021-self-check-answers.md` does **not** say where the bracket
prints. It says only which questions carry one:

> **Every calculation question carries its answer in brackets, except the last question in the
> section.**

and, under Verification:

> Answers render on questions 1–5 of each Physics section and on 1–7 of the Chemistry section;
> none on any last question.

The placement below the box was a builder choice, and no record ever decided it.

---

## 2. Proposed Rule

> **On a question with a work box, the self-check bracket prints inside the work box, in the
> bottom-right corner, in the same type as now (8 pt, `pal.label` grey). The separate line below
> the box is removed.**

- The work box keeps its minimum height and never splits across a page. **No height change.** The
  worksheet builder's floor is `WORK_MIN_IN = 1.6` (line 89). That is above SHULL-CHG-0016's 1.4 in,
  and it stays. The row stays `atLeast` and `cantSplit`.
- The **SHOW WORK HERE** watermark (SHULL-CHG-0019) stays where it is.
- **SHULL-CHG-0021 is unchanged.** Which questions carry a bracket stays the same: every
  `"calculation": true` question except the last. So do both refusals in `check_profile()`.
- **The answer key is unaffected.** `build_worksheet_key_docx.py` never prints `selfCheck`. It
  prints `solution` and `finalAnswer` (lines 77–82). No change there.

---

## 3. Physics

Physics prints self-check brackets. All three Physics worksheet specs carry `selfCheck` on their
calculations: `phys_u01_s01.1-s01.4.json`, `phys_u01_s01.2_10q.json` and
`phys_u01_s01.1_extended.json`. Physics has **no work boxes** (SHULL-CHG-0019), so there is no box to
put them in.

**Proposed: Physics is unchanged.** Its bracket stays a separate right-aligned 8 pt line at the
foot of the question card. Nothing moves and nothing is removed. The user's request was about the
Chemistry box. Whether the Physics line also wastes space is not decided here.

---

## 4. Flagged

1. **Code citing SHULL-CHG-0031 appeared before this record existed.** While this record was being
   drafted, the working tree changed in two files:
   - `templates/_shull_docx.py` `work_box()` gained a `corner=` parameter (lines 474–521). Its
     docstring cites *"SHULL-CHG-0031"*.
   - `templates/worksheet/build_worksheet_docx.py` lines 398–413 now pass `corner=q.get("selfCheck")`
     into `work_box()`. They keep the old below-card paragraph only for `selfCheck and not math`,
     which is the Physics case in §3.

   The Secretary did not write these edits and has not touched them. It could not check whether they
   are committed, because it has no shell. **This record is PENDING, so they are not authorized.**
   They must not be committed under this ID before approval. After approval, the implementer either
   adopts them as the implementation (and verifies them against §5) or rebuilds from the committed
   state. The user decides which.
2. **The Chemistry S1.5 spec is not in the repository.** `templates/worksheet/specs/` has no
   Chemistry U01 spec, and nothing in the repository contains *"175.03"*. The section itself is
   confirmed: `courses/chemistry/DECISIONS.md` line 27 has *"1.5 Average Atomic Mass"*, and the
   OPTIONAL-worksheet entry at lines 363–367 notes it is *"being built by a separate agent"*. The
   first check in §5 needs that spec located and committed.
3. **The "6th problem" is out of scope.** *"Condense add a 6th problem"* is a content change to one
   Chemistry deliverable. It is not a template rule, and this record does not decide it. The user's
   second message withdrew only the removal of the answer.
4. **Students may write over the corner.** The bracket now sits in the space students work in. At
   8 pt grey in the bottom-right corner the risk is small. It is named here rather than left out.
5. **A second builder is out of scope.** `templates/practice/build_practice.py` prints its `check`
   bracket **above** its work box (lines 342–343). No change record governs this builder, and this
   record does not change it.

---

## 5. Verification required before this is IMPLEMENTED

- [ ] Locate and commit the Chemistry S1.5 spec (§4, item 2). Then rebuild the optional S1.5 sheet.
      Each bracket is inside its work box in the bottom-right corner, and each calculation card is
      shorter than before.
- [ ] Run the worksheet regression. Every other spec builds: `chem_u07_s07.4`, `geo_u01_s01.4`,
      `geo_u04_s04.1` and the three Physics specs. The only difference is the self-check placement
      on Chemistry. Physics and Geology output is unchanged.
- [ ] Minimum box height is unchanged, the rows are still `atLeast` and `cantSplit`, and no box splits
      across a page.
- [ ] `scripts/audit_worksheet.py`: every section is within its declared `pagesPerSection`.
- [ ] `scripts/validate_profiles.py`: every refusal still fires, including both SHULL-CHG-0021
      refusals.
- [ ] `pdffonts` / `scripts/audit_fonts.py` shows Archivo only.
- [ ] `scripts/audit_print_ink.py` passes: toner is within budget and there is no solid band.
- [ ] The key builder builds the same specs unchanged.
- [ ] The commit message carries `SHULL-CHG-0031`, and `Implemented By` and `Verified` are filled in
      here.
