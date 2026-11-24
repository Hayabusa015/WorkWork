# SHULL-CHG-0107 — Chemistry: one verified Ohio standards code list in `DECISIONS.md`

> **ID note.** The main session supplied 0107 and confirmed it is free on `origin/main` (highest
> record there: SHULL-CHG-0106). The Secretary that drafted this record has no shell and could not
> run `git fetch origin main` itself (`governance/CHANGE_CONTROL.md` §2, "Allocating a new Change
> ID"). Locally the highest record is also SHULL-CHG-0106, and nothing outside `legacy/` mentions
> 0107. Under that rule the ID is not allocated until this file is pushed to `origin/main`.

> **No conflict with a LOCKED rule.** This record adds one new section and one log entry. It
> changes no curriculum code, no section title, no assessment or grading rule. The Ohio scope limits
> it records are informational and do not override any course decision (§4).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0107 |
| **Date** | 2026-11-23 (drafted) |
| **Source** | User, from a Researcher finding. Finding F4 of `reports/chem-ohio-standards-verification.md` (researcher, 2026-11-23): "Codes still live only in per-unit specs. There is no single authoritative list". The main session offered to put the verified list in one place in the Chemistry decisions file. Matt's words in chat, 2026-11-23, as the main session relayed them: *"yes, have the secretary add the codes list"*. The Secretary did not hear him directly. **This record is not the approval.** The main session records his decision under `governance/CHANGE_CONTROL.md` §4. |
| **Current Rule** | **None.** `courses/chemistry/DECISIONS.md` has no Ohio standards section. Its only mention of Ohio is the hour requirement under "Pacing and calendar — 2026–2027". Ohio codes, titles and key wording live only in the 15 roadmap specs (`templates/unit-roadmap/specs/chem_u00.json`–`chem_u14.json`, fields `standards_source`, `standards_key`, and `standards` per section). Each spec restates them, and they already differ from one another (§3). The only standing instruction is in `.claude/skills/build-assessment/SKILL.md`: *"Maps to a learning target, and to an Ohio standard when alignment is requested."* |
| **Proposed Rule** | Add a new section, **"Ohio standards — verified code list"**, to `courses/chemistry/DECISIONS.md`, between "Pacing and calendar — 2026–2027" and "Course brand exceptions". That is the same position as "Ohio standards" in `courses/physics/DECISIONS.md`. It is the **one** authoritative home for: the source line; the 9 content statements with code, official title, official sub-points and the key wording roadmaps print; notes on inquiry, U15, the mole definition and Ohio scope limits; and the rule that specs cite this table and do not restate different wording. Plus a decision-log entry at the top of the log. Exact text in §2. |
| **Supersedes** | **No rule.** No decision is replaced. In practice, the per-unit `standards_source` and `standards_key` values in the roadmap specs stop being independent statements and become copies of the new table. If a copy differs, the table wins and the spec is reported stale (CLAUDE.md §2). |
| **Reason** | (1) CLAUDE.md §1: a fact lives in exactly one place. Ohio codes and key wording are written 15 times, once per spec. This is the third pass at them (F3 in `reports/u2-content-briefs.md` 2026-10-04; the secondary-source draft; the 2026-11-23 primary-source report). (2) The copies have already drifted (§3). (3) The list is now verified against the official PDF, so there is a settled text to hold. (4) The change-control test: it affects **one course**, so it belongs in `courses/chemistry/DECISIONS.md` (CLAUDE.md §2). It is filed as a record, as SHULL-CHG-0099 and SHULL-CHG-0106 were, because that file changes only against an approved record. |
| **Affected Agents** | Overseer (routes roadmap builds; checks codes against the table). Designer (builds roadmaps from the specs). Auditor (QA: printed codes and key wording must match the table). Researcher (future Ohio checks start from the table). Secretary (this record and the decisions-file edit). No responsibilities change. No agent file is edited. |
| **Affected Skills** | None edited. `.claude/skills/build-assessment/SKILL.md` ("an Ohio standard when alignment is requested") does not restate any code, so it does not conflict; for Chemistry it would now resolve to this table. `templates/unit-roadmap/build_unit_roadmap.py` is unchanged: it prints what the specs hold. |
| **Affected Courses** | **Chemistry only.** Physics ("Ohio standards" in `courses/physics/DECISIONS.md`) and Geology are untouched. The PS.M.5 and P.E.5 codes named in the notes belong to other courses. They are mentioned only to say where nuclear content lives, and they are not added to any table. |
| **Risk** | **Low** for the decisions-file edit (one new section, one log entry; outside the curriculum-map region that `scripts/validate_codes.py` parses). **Medium** for what it reveals: once the rule is in force, 5 specs do not match it (§3). Fixing them, and rebuilding any affected roadmap in `output/chemistry/`, is follow-up work. It is **not bundled** here. A rebuild is a classroom deliverable and routes through the Overseer. |
| **Recommendation** | Approve as written, after Matt answers the one open question in §5 (C.PM.4 key wording). The approval should cover the new section and the log entry only. Spec corrections and roadmap rebuilds are separate jobs. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Placement

The section goes immediately **before** "Course brand exceptions", after the pacing section. Physics
already puts its "Ohio standards" section there, so the two files line up. It stays outside the
"Curriculum map" region, which is the only part `scripts/_shullos.py` `section_codes()` parses. The
section codes mentioned in the new text (7.5–7.7, 14.2) are valid codes in any case.

## 2. Text to insert on implementation

**(i) New section in `courses/chemistry/DECISIONS.md`.** Insert after the "Pacing and calendar —
2026–2027" section, including its closing `---`, and before `## Course brand exceptions`:

```markdown
## Ohio standards — verified code list

**Source line:** `Ohio's Learning Standards for Science (adopted 2018) · Chemistry`.
Standards adopted February 2018; model curriculum adopted May 2019. **Verified 2026-11-23** against
the official PDF Matt uploaded (`SciFinalStandardsMC060719.pdf`). Whether a later revision has
replaced it is **UNVERIFIED**. Page-by-page evidence: `reports/chem-ohio-standards-verification.md`.

This is the only authoritative list of Ohio Chemistry codes, titles and key wording. Two strands:
C.PM Structure and Properties of Matter, and C.IM Interactions of Matter. Ohio sets no order: "The
following information may be taught in any order; there is no ODE-recommended sequence" (p. 259).

| Code | Official title | Official sub-points | Key wording (roadmap standards key) |
|---|---|---|---|
| C.PM.1 | Atomic structure | • Evolution of atomic models/theory • Electrons • Electron configurations | evolution of atomic models/theory; electrons; electron configurations |
| C.PM.2 | Periodic table | • Properties • Trends | properties and trends |
| C.PM.3 | Chemical bonding | • Ionic • Polar/covalent | ionic and polar/covalent bonds; metallic bonding also introduced |
| C.PM.4 | Representing compounds | • Formula writing • Nomenclature • Models and shapes (Lewis structures, ball and stick, molecular geometries) | formula writing; nomenclature; models and shapes (Lewis, ball-and-stick, geometries) |
| C.PM.5 | Quantifying matter | None. Ohio lists no sub-points for C.PM.5 (pp. 259, 272) | SI units, significant figures, dimensional analysis, the mole, molar mass |
| C.PM.6 | Intermolecular forces of attraction | • Types and strengths • Implications for properties of substances (sub-bullets: Melting and boiling point; Solubility; Vapor pressure) | types and strengths; effects on melting/boiling point, solubility, vapor pressure |
| C.IM.1 | Chemical reactions | • Types of reactions • Kinetics • Energy • Equilibrium • Acids/bases | types of reactions; kinetics; energy; equilibrium; acids/bases |
| C.IM.2 | Gas laws | • Pressure, volume and temperature • Ideal gas law | pressure, volume and temperature; ideal gas law |
| C.IM.3 | Stoichiometry | • Molar calculations • Solutions • Limiting reagents | molar calculations; solutions; limiting reagents |

Wording notes. C.PM.2 is written "Periodic Table" on p. 259 and "Periodic table" elsewhere.
C.IM.3: p. 259 says "Molecular calculations"; the content statement (p. 284) and its classroom
examples (p. 285) say "Molar", which is used here. C.PM.3's "metallic bonding" comes from the
elaboration (p. 266), not the sub-points. Polyatomic ions are C.PM.4 (p. 270), not C.PM.3. C.PM.5's
key wording comes from the elaboration (p. 272), because it has no sub-points.

### Notes

- **Inquiry has no code.** At high school, "Scientific Inquiry, Practice and Applications" is an
  uncoded Nature of Science category (pp. 11, 260). Never print an inquiry code. If inquiry must be
  cited, cite it in words: "Nature of Science: Scientific Inquiry, Practice and Applications".
- **U15 Nuclear Chemistry has no Chemistry content statement.** Ohio puts nuclear content in
  Physical Science PS.M.5 and Physics P.E.5. Those are other courses' codes and are not in this
  table. U15 sections show "—" or "Course extension (beyond the Ohio Chemistry statements)".
- **Mole definition.** Ohio's text defines the mole as "the number of atoms in exactly 12 grams of
  the isotope carbon-12" (C.PM.5, p. 272). That is the pre-2019 SI wording. Do not use it as the
  current definition. The mole has been defined by the fixed Avogadro constant since the SI
  redefinition of 20 May 2019.
- **Ohio scope limits (informational).** These describe Ohio's course. They do not override any
  decision in this file; where this file goes further (for example, the 15 memorized polyatomic
  ions), this file wins. Electron configurations for elements in the first three periods (p. 261).
  Lewis structures and VSEPR for H, C, N, O, P, S and the halogens (p. 270). Polyatomic ions "given
  the formula and charge" (p. 270). Limiting reagents "treated conceptually" (p. 284). No
  mathematical treatment of reaction rates or equilibrium (pp. 277–278). Entropy reserved for
  advanced study (p. 278). Brønsted-Lowry and Lewis acids "not the focus" (p. 278). Students are not
  asked to classify dissolving as a chemical or physical change (p. 274).

### Rule

- Roadmap specs (`templates/unit-roadmap/specs/chem_u*.json`) and all other Chemistry materials
  cite Ohio codes **only** from this table. No other code is printed on a Chemistry document.
- A spec's `standards_source` and each `standards_key` entry copy the source line, official title
  and key wording above **verbatim** (a closing full stop is allowed). They are copies, not sources.
  A unit-specific note may follow the key wording, kept visibly separate so it is not read as part
  of the standard. If a copy differs from this table, the table wins and the spec is reported stale.
- The section-to-code mapping (main and support codes per section) is per-page content. It lives in
  the roadmap specs, not here, and uses only codes in this table. The evidence for it is §5 of
  `reports/chem-ohio-standards-verification.md`, which also marks which mappings rest only on
  Ohio's non-mandatory classroom examples or on inference (for example 7.5–7.7 and 14.2).

---
```

**(ii) Decision log, at the top, above the 2026-11-23 "Course Outline filed as a Reference"
entry:**

```markdown
### 2026-11-23 — Ohio standards: one verified code list
The Ohio Chemistry code list (C.PM.1–C.PM.6, C.IM.1–C.IM.3), with official titles, sub-points and
the key wording roadmaps print, now lives once, in "Ohio standards — verified code list". It was
verified 2026-11-23 against the official PDF Matt uploaded; evidence is in
`reports/chem-ohio-standards-verification.md`. Specs and other materials cite codes from that table
and copy its wording rather than restating their own. The section-to-code mapping stays in the
roadmap specs and uses only those codes. Inquiry has no code, and U15 has no Chemistry content
statement. Decided by Matt 2026-11-23 ("yes, have the secretary add the codes list").
Supersedes: None (first record of Ohio codes in this file; the specs' standards keys become copies
of it).
Status: CONFIRMED · SHULL-CHG-0107
```

Nothing else in `courses/chemistry/DECISIONS.md` is edited. "Last updated" already reads
2026-11-23; if the implementation date differs, it is updated to match.

## 3. Drift the rule will expose (found while drafting; not fixed here)

Grep of `standards_key` in `templates/unit-roadmap/specs/chem_u*.json`, 2026-11-23. Every
`standards_source` already matches the source line. Key wording matches §2 (i) except:

| Spec | Code | Spec wording | Differs from the table by |
|---|---|---|---|
| `chem_u04.json`, `chem_u05.json`, `chem_u07.json`, `chem_u08.json` | C.PM.4 | "formula writing; nomenclature; models and shapes." | No parenthetical "(Lewis, ball-and-stick, geometries)". See §5 |
| `chem_u06.json` | C.PM.4 | "formula writing, nomenclature, models and shapes." | Commas for semicolons; no parenthetical |
| `chem_u06.json` | C.IM.1 | "acids/bases. 6.4 introduces acid names; acid–base chemistry is taught in Unit 14." | Official wording cut to one of five sub-points, then a unit note. Under the rule, the full key wording comes first and the note follows |

Section-to-code mappings were not re-audited for this record. All codes seen in the specs are in the
table. These are **follow-up jobs**, not part of this change. Spec edits can be made by the agent
that owns the roadmap specs. Any rebuild of `output/chemistry/u*/` roadmaps routes through the
Overseer.

## 4. Conflict check

| Existing text | Relation to this change | Result |
|---|---|---|
| Curriculum map, U15 Nuclear Chemistry (CONFIRMED) | The note says U15 has no Chemistry statement. It does not question the unit | No conflict |
| Reference packet, polyatomic ions (memorize 15, SHULL-CHG-0068) | Ohio's "given the formula and charge" is recorded as informational, and the note says this file wins | No conflict |
| U9 9.5 Spontaneity `EXT` | Ohio reserves entropy for advanced study, which fits `EXT` | No conflict |
| Reference packet, Equations & Constants (N_A) | Consistent with the fixed-N_A mole definition | No conflict |
| `courses/physics/DECISIONS.md` "Ohio standards" | Different course, separate file. Placement matches | No conflict |
| `.claude/skills/build-assessment/SKILL.md` | Names no code. It now has a table to resolve to for Chemistry | No conflict; no edit |
| Report §5 note: "Printing PS.M.5 or P.E.5 on a Chemistry roadmap is Matt's call" | The Rule ("no other code is printed") adopts the report's safe default and closes that option. Matt's approval of this record would settle it; printing those codes later would need a new record | **Flagged for Matt.** Not a LOCKED conflict, but approving this record decides it |
| CLAUDE.md §1, one fact in one place | Specs must still carry the key text, because the builder prints from the spec. That duplication cannot be avoided. The Rule makes the specs explicit copies with the table as the source. A validator comparing spec keys with the table would enforce it; that is a separate proposal if wanted | Allowed duplicate, pointed at the source |

## 5. Open question for Matt (one, before approval)

**C.PM.4 key wording.** The report's key wording (§4 of the report, used in §2 (i) above) is
*"formula writing; nomenclature; models and shapes (Lewis, ball-and-stick, geometries)"*. Four
specs already print the shorter *"formula writing; nomenclature; models and shapes"*. The report
calls the parenthetical optional (report §6, item 7). Both are faithful to Ohio's sub-points.

- **(a)** Keep the parenthetical, as drafted. Five specs (U4, U5, U6, U7, U8) are corrected in
  follow-up.
- **(b)** Drop the parenthetical. Only U6 needs correcting. On implementation the C.PM.4 key cell
  reads `formula writing; nomenclature; models and shapes`, and nothing else in §2 changes.

If Matt's approval does not name an option, the Secretary implements (a), which is the text as
drafted, and does not choose on his behalf.

## 6. Rollback

One commit carrying `SHULL-CHG-0107` that touches only `courses/chemistry/DECISIONS.md`.
`git revert <sha>` removes the section and the log entry. No Drive mutation is part of this change.

## 7. Verification plan (only after APPROVED and implemented)

1. `python3 scripts/validate_codes.py` passes with no new warnings. Chemistry's valid-section count
   is unchanged at 88, because the new section is outside the curriculum-map region.
2. The table in `courses/chemistry/DECISIONS.md` has exactly 9 rows (C.PM.1–6, C.IM.1–3). Titles,
   sub-points and key wording match §2 and §4 of `reports/chem-ohio-standards-verification.md`
   character for character, as amended by any §5 option Matt chose.
3. Grep: the section heading appears once. No standard or skill restates the table.
4. No other part of `courses/chemistry/DECISIONS.md` changed (diff limited to the new section and
   the log entry, plus "Last updated" if the date differs).
5. Fill in `Implemented By` (SHA) and `Verified` here. Update the CHANGELOG row's status.
