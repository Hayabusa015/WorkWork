# SHULL-CHG-0028 — Chemistry U1: 1.4 Isotopes is folded into 1.3 Atomic Structure

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0028 |
| **Date** | 2026-09-23 |
| **Source** | User. **Path A, a course fact.** It touches `courses/chemistry/DECISIONS.md` only. It is written as a record because only the Secretary may edit `courses/`, and only against an APPROVED record. Findings: Auditor items 31, 34 and 36 in `reports/2026-09-23_chem-u01-qa-audit.md`, and the Librarian survey `reports/drive-operations/2026-09-23_chem-u01-folder-survey.md`. The quotes below reached the Secretary through the main session. The Secretary did not hear them directly. |
| **Current Rule** | See §1 |
| **Proposed Rule** | See §2 |
| **Supersedes** | `courses/chemistry/DECISIONS.md`, Curriculum map, **U1 Matter & Atomic Structure**, lines 25–27, where "1.4 Isotopes" is listed as a taught section. **Not LOCKED-rule drift.** The curriculum map is CONFIRMED, and the user himself is changing it. No other record is superseded. |
| **Reason** | The fold is a course fact, but so far it is written only in a drive-operations log. `DECISIONS.md` is the only authoritative copy of the curriculum map, and it still lists 1.4 as a live section with no log entry. So a builder following `CLAUDE.md` §3 would still find S01.4 valid. |
| **Affected Agents** | Designer and builders (chip and section codes). Auditor (checks codes against the map). Librarian (the empty Drive `Section 01.4` folder) |
| **Affected Skills** | None edited. `build-lab` cites an S01.4 filename as an example (§5) |
| **Affected Courses** | Chemistry only |
| **Risk** | **Low.** One course, one unit, and no code is renumbered. The only thing to watch is the validator (§3). |
| **Recommendation** | **Option 1** in §3: keep 1.4 listed, mark it folded, and retire the code. 1.5 keeps its number. |
| **Decision** | *Pending.* |
| **Status** | **PENDING** |
| **Implemented By** | *(blank. Not implemented.)* |
| **Verified** | No. Nothing has been implemented. The required checks are in §6. |

---

## 1. Current Rule — verbatim

### 1a. `courses/chemistry/DECISIONS.md`, Curriculum map, lines 25–27

> **U1 Matter & Atomic Structure** (5 sections)
> 1.1 Matter & Changes · 1.2 History of the Atomic Model · 1.3 Atomic Structure · 1.4 Isotopes
> · 1.5 Average Atomic Mass

The decision log (from line 339) has **no entry** for the fold.

### 1b. Where the fold is recorded today: a drive-operations log only

`reports/drive-operations/2026-09-15_chem-u01-s01.2-s01.3-s01.5-folder-create.md`, lines 14–19:

> ## Scope note — Section 01.4
>
> Per Matt's instruction this session, Section 01.4's content is being folded into Section 01.3.
> No new Section 01.4 folder is created or requested. A `Section 01.4 - Isotopes` folder already
> exists from prior work (id `1WU_Mx3hYEDdNR8ADffg_bI16kPZ0GQDK`, created 2026-09-08) — left as-is,
> untouched, per instruction not to remove a pre-existing folder.

### 1c. The user, verbatim, 2026-09-23

His earlier instruction, as relayed (the brief does not give its date): *"Fold into U3"*

He was then asked: *"The earlier plan was to fold S1.4 Isotopes into S1.3 Atomic Structure ... Did you
mean S1.3?"*

He replied: *"retry, yes S1.3"*

**"U3" was a slip. His "yes S1.3" corrects it.** Chemistry U3 is The Periodic Table, and nothing here
moves isotopes out of Unit 1. His answer confirms the fold **target**. Whether it also approves the
`DECISIONS.md` edit below is his call. The Secretary does not read it as approval of text written
after he answered.

---

## 2. Proposed Rule

Isotope content is taught in 1.3 Atomic Structure and chipped `U01 / S01.3`. The code 1.4 is
**retired, not reused**. 1.5 Average Atomic Mass **keeps its code**.

### 2a. The U1 line (replaces lines 25–27), Option 1, recommended

```
**U1 Matter & Atomic Structure** (5 section codes, 4 taught) — *1.4 is folded into 1.3; see the log*
1.1 Matter & Changes · 1.2 History of the Atomic Model · 1.3 Atomic Structure (includes isotopes)
· 1.4 Isotopes — FOLDED into 1.3, code retired, never reused · 1.5 Average Atomic Mass
```

This follows the pattern already used on the U9 line (*"the 9.6 question is closed; see the log"*).
"5 section codes, 4 taught" is the Secretary's wording. The user may prefer other wording.

### 2b. Decision-log entry, for the top of the log (`CHANGE_CONTROL.md` §5)

```markdown
### 2026-09-23 — U1: 1.4 Isotopes folded into 1.3 Atomic Structure
Isotope content is taught in 1.3 Atomic Structure and chipped U01 / S01.3. The code 1.4 is
retired and never reused; 1.5 Average Atomic Mass keeps its code, so no file, folder or chip is
renumbered. First instructed 2026-09-15 and recorded then only in
reports/drive-operations/2026-09-15_chem-u01-s01.2-s01.3-s01.5-folder-create.md. Confirmed by Matt
2026-09-23 ("retry, yes S1.3"), correcting an earlier "Fold into U3", which was a slip.
Supersedes: Curriculum map, U1 line, "1.4 Isotopes" as a taught section.
Status: CONFIRMED · SHULL-CHG-0028
```

`Status: CONFIRMED` is written only on implementation, after approval. The header line
`**Last updated:** 2026-09-14` becomes the implementation date.

---

## 3. Which form keeps codes stable

| Option | What it does | Codes |
|---|---|---|
| **1. Keep 1.4 listed, mark it folded (recommended)** | §2a | **Stable.** 1.5 stays 1.5. `Section 01.5` on Drive, the S01.5 worksheet and key, and every "S1.5" citation stay correct |
| 2. Remove 1.4, leave a gap (1.1, 1.2, 1.3, 1.5) | Deletes the entry | Stable, but the gap has no explanation on the line, and the history is only in the log |
| 3. Remove 1.4 and renumber 1.5 → 1.4 | Closes the gap | **Unstable.** It breaks the Drive `Section 01.5` folder, the S01.5 files, and every S1.5 citation. **Not recommended** |

### The validator: a sub-choice inside Option 1

`scripts/validate_codes.py` gets its valid codes from the curriculum map through
`section_codes()` in `scripts/_shullos.py`, lines 42–59. Its plain-form pattern
`(?:^|[·|]\s*)(\d{1,2}\.\d)\s+(?=[A-Z(])` matches **"· 1.4 Isotopes"**. As a result:

- **1(a), as written in §2a.** 1.4 stays machine-valid. Nothing goes red, and nothing outside
  `courses/` has to change in the same commit. **But the validator will not catch a new S01.4
  build.** Only the human check in `CLAUDE.md` §3 would, by reading "FOLDED".
- **1(b).** Write the entry so the pattern cannot match it, e.g. `· ~~1.4 Isotopes~~ folded into 1.3`.
  Then the validator rejects S01.4 from then on. **But four live files fail at once** (§5, second
  table). Fixing them in this commit would bundle unapproved skill and template edits into this
  record, which is not allowed.

**Recommendation: 1(a) now.** Then 1(b) as a separate follow-up, once the four files are dealt with.
This is a reading of the regex. It has not been run.

---

## 4. For the user

| # | Question |
|---|---|
| 1 | Approve recording the fold as §2a and §2b (Option 1)? |
| 2 | Validator: 1(a) now with 1(b) later, or 1(b) straight away, accepting that four files fail until they are fixed? |

---

## 5. Downstream. Noted, not fixed

These all follow from the fold. **None is edited by this record.** Each belongs to its owner.

| Item | Where | Issue | Owner |
|---|---|---|---|
| Unit review: the whole S01.4 section | `…_Unit_Review` + `_Key` (audit item 31) | An "Isotopes & Notation" section is chipped **U01 / S01.4** | Designer: re-chip as S01.3, or merge it into S01.3 |
| Unit review: "Section 1.4" citations | same, S01.3 Q6 and S01.5 Q4b (audit item 31) | They cite "Section 1.4" | Designer |
| Slide 16 | `…_Slides_….pptx` (audit item 34) | Labelled **"SECTION 1.5 · BRIDGE FROM 1.4"** and chipped S1.5 | Designer, as part of the item 34 accept-or-rebuild decision |
| Empty Drive folder | `Section 01.4 - Isotopes`, `1WU_Mx3hYEDdNR8ADffg_bI16kPZ0GQDK`, under CHEM Unit 01 (survey §2) | Empty. Left in place 2026-09-15 on instruction | User. Trashing needs his approval and a pre-mutation log. It can also be left as a marker |

Also found by the Secretary. These are not in the brief, and not fixed:

| Item | Where | Issue |
|---|---|---|
| Filed deck | Drive `Unit 01/Presentations/SHULL_CHEM_Slides_U01_S01.4.pptx` (`1eSuicKHiQ7TzPj-7-Nwa64Vs8fIqj-AQ`) | Named and footered S01.4. A rename needs confirmation and a log (`NAMING.md` §5) |
| Deck spec | `templates/slide/decks/chem_u01_s01.4_isotopes.json` line 4, `"section": "1.4"` | Would fail the validator under 1(b) |
| Skill example | `.claude/skills/build-lab/SKILL.md:17`, `SHULL_CHEM_Lab_U01_S01.4_Isotope_Beans.html` | Would fail under 1(b). Stale as a worked example |
| Template README | `templates/lab/README.md:54, 55, 69`, the same Isotope_Beans filenames | Would fail under 1(b) |

---

## 6. Verification required before this is IMPLEMENTED

- [ ] `courses/chemistry/DECISIONS.md` U1 line matches the approved option exactly
- [ ] The decision-log entry is at the **top** of the log. No earlier entry is edited
- [ ] `Last updated` is set to the implementation date
- [ ] `python3 scripts/validate_codes.py` gives the result expected for the chosen sub-option. Under
      1(a): passes, and the Chemistry code count is unchanged. Under 1(b): the count drops by one,
      and failures are limited to the files in §5
- [ ] No other file changed in the commit. `legacy/` untouched
- [ ] The commit carries `SHULL-CHG-0028`. `Implemented By` and `Verified` filled in here
