# SHULL-CHG-0110 — Chemistry U7 to five sections; U11 and U12 swap

> **No conflict with a LOCKED rule.** It replaces three lines of the CONFIRMED Chemistry curriculum
> map. Same shape as the U6 rework (SHULL-CHG-0099). **Codes change meaning.** 7.2–7.5 and every
> 11.x and 12.x code mean something new. `scripts/validate_codes.py` cannot catch that, because it
> only checks that a code exists. Only 7.6, 7.7 and 12.7 start failing.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0110 |
| **Date** | 2026-11-24 |
| **Source** | User. Matt, chat 2026-11-24, verbatim: "I want to combine 7.2 and 7.3 into one section and 7.5 and 7.6 into one section Also, id like to swap.unit 11 and 12. I want solution chemistru before gases. I thi k that makes more sense." Answers to the main session's questions: "Renumber 7.1–7.5 (Recommended)"; "Use these names (Recommended)" (The Mole & Molar Mass; Percent Composition & Empirical Formulas); "Keep ranges (Recommended)". |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, Curriculum map. Phase 2: "**U7 The Mole & Chemical Quantities** (7 sections) 7.1 Mathematical Tools · 7.2 The Mole & Avogadro's Number · 7.3 Molar Mass · 7.4 Mole Conversions · 7.5 Percent Composition · 7.6 Empirical Formulas · 7.7 Molecular Formulas". Phase 3: "**U11 Gases** (6 sections) 11.1 Kinetic Molecular Theory … 11.6 Ideal Gas Law". Phase 4: "**U12 Solution Chemistry** (7 sections) 12.1 Solutions & Dissolving … 12.7 Solution Stoichiometry". |
| **Proposed Rule** | U7 (7 section codes, 5 taught): 7.1 Mathematical Tools · 7.2 The Mole & Molar Mass · 7.3 Mole Conversions · 7.4 Percent Composition & Empirical Formulas · 7.5 Molecular Formulas · 7.6 — RETIRED, never reused · 7.7 — RETIRED, never reused. Phase 3 ends with U11 Solution Chemistry (11.1–11.7, same titles as old 12.1–12.7). Phase 4 opens with U12 Gases (12.1–12.6, same titles as old 11.1–11.6). Phase ranges are unchanged. Exact text below. |
| **Supersedes** | `courses/chemistry/DECISIONS.md`, Curriculum map: the U7, U11 and U12 lines. |
| **Reason** | Matt's call on the teaching order. Old 7.2 and 7.3 become 7.2; old 7.4 becomes 7.3; old 7.5 and 7.6 become 7.4; old 7.7 becomes 7.5. Solution Chemistry is taught before Gases. |
| **Affected Agents** | Overseer (code check), Designer, Librarian (Drive folders). |
| **Affected Skills** | None in this repository. |
| **Affected Courses** | Chemistry only. Taught sections go from 86 to 84. Codes the validator accepts go from 88 to 86. |
| **Risk** | Medium. The repository change is small, but existing U7, U11 and U12 materials keep passing the validator under numbers that now mean something else. |
| **Recommendation** | Approve. Apply the follow-ups below before anything new is built for U7, U11 or U12. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Exact edits to `courses/chemistry/DECISIONS.md`

Header: `**Last updated:** 2026-11-23` becomes `**Last updated:** 2026-11-24`.

U7 (replaces the current two-line entry):

```
**U7 The Mole & Chemical Quantities** (7 section codes, 5 taught) — *reworked 2026-11-24; see the log*
7.1 Mathematical Tools · 7.2 The Mole & Molar Mass · 7.3 Mole Conversions · 7.4 Percent
Composition & Empirical Formulas · 7.5 Molecular Formulas · 7.6 — RETIRED, never reused · 7.7 —
RETIRED, never reused
```

End of Phase 3 (replaces the U11 Gases entry):

```
**U11 Solution Chemistry** (7 sections) — *was U12 until 2026-11-24; codes changed meaning, see the log*
11.1 Solutions & Dissolving · 11.2 Solubility · 11.3 Factors Affecting Solubility & Dissolving
Rate · 11.4 Electrolytes · 11.5 Molarity · 11.6 Dilutions · 11.7 Solution Stoichiometry
```

Start of Phase 4 (replaces the U12 Solution Chemistry entry):

```
**U12 Gases** (6 sections) — *was U11 until 2026-11-24; codes changed meaning, see the log*
12.1 Kinetic Molecular Theory · 12.2 Gas Pressure & Variables · 12.3 Boyle's, Charles's &
Gay-Lussac's Laws · 12.4 Combined Gas Law · 12.5 Avogadro's Law & Molar Volume · 12.6 Ideal
Gas Law
```

Decision log (new entry at the top):

```
### 2026-11-24 — U7 to five sections; U11 and U12 swap
U7 The Mole & Chemical Quantities is taught as 7.1 Mathematical Tools, 7.2 The Mole & Molar Mass,
7.3 Mole Conversions, 7.4 Percent Composition & Empirical Formulas, 7.5 Molecular Formulas. Old 7.2
and 7.3 merge into 7.2, old 7.4 is now 7.3, old 7.5 and 7.6 merge into 7.4, and old 7.7 is now 7.5.
Codes 7.6 and 7.7 are retired and never reused. As with U6, 7.2–7.5 change meaning. Solution
Chemistry is now U11, the end of Phase 3, and Gases is now U12, the start of Phase 4. The phase
ranges and the section titles are unchanged. Every 11.x and 12.x code changes meaning, so never read
a document numbered under the old order as if it used the new one. Chemistry now has 84 taught
sections. Decided by Matt 2026-11-24 ("I want to combine 7.2 and 7.3 into one section and 7.5 and
7.6 into one section Also, id like to swap.unit 11 and 12. I want solution chemistru before gases.
I thi k that makes more sense."). He then chose to renumber 7.1–7.5, accepted the two merged names
and kept the phase ranges.
Supersedes: Curriculum map, U7, U11 and U12 lines.
Status: CONFIRMED · SHULL-CHG-0110
```

Nothing else in the file depends on these numbers. The pacing guide names phases by unit range,
and those ranges are unchanged. The U9 note, open question 4 (U9, U14), the real-world themes and
the short titles (which have no U7, U11 or U12 rows) are all unaffected. The file states no section
total. The "90 sections" in closed open question 1 is history and stays as written.

## Follow-ups (not part of this record)

1. `templates/unit-roadmap/specs/chem_u07.json`, `chem_u11.json` and `chem_u12.json` need
   rewriting, and the Course Outline needs rebuilding.
2. `templates/assessment/specs/chem_u07_unit_test.json` has 24 references to 7.x that need
   remapping.
3. `templates/worksheet/specs/chem_u07_s07.4.json` is "Mole Conversions", which is now **7.3**. It
   still passes the validator as 7.4. Its previews are
   `app/public/previews/worksheet-chem_u07_s07.4-*.png`, with an entry in `catalog.json`.
4. Two Drive folders need renaming: "Unit 11 - Gases" (`1Sc-90N1krbbMfXkG1KvitOEh75JHKaHO`) and
   "Unit 12 - Solution Chemistry" (`1qJ2vICzt5ivzEvkPjBM7YoV7UxEPCxbg`). Neither ID is in
   `config/drive.json` today. Log the renames in `reports/drive-operations/` first.
5. Any U7, U11 or U12 material already filed on Drive needs checking.
6. `scripts/validate_codes.py` counts sections from the map. Expected after the change: Chemistry
   88 → 86 valid codes (7.6, 7.7 and 12.7 out; 11.7 in).
