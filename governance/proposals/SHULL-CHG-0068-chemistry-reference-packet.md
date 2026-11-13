# SHULL-CHG-0068 — Chemistry reference packet becomes a 12-sheet packet

> **Renumbered 2026-11-10 from SHULL-CHG-0058.** This record was written on branch `ccr-eb4ada9c-82lvgm` as 0058, but another session pushed a different SHULL-CHG-0058 to `origin/main` first. Under `governance/CHANGE_CONTROL.md` §2 ("A record that cannot be pushed is not allocated") the main-line record keeps the number, and this one takes the next free ID on `origin/main`. Commit messages on this branch dated 2026-11-06 refer to it as SHULL-CHG-0058; they mean this record. Content, decision and approval are unchanged.

**Path A — a course change.** Only `courses/chemistry/DECISIONS.md` is affected. No standard or skill
is edited by this record. It edits two parts of that file: "Reference packet contents" and the
"Short titles" table. (The filename form and the `Chemistry/Reference/` folder are the separate Path B
change SHULL-CHG-0069.)

**Amended 2026-11-06** to state exactly the changes the main session offered to resolve this
record's open points. See "Resolved".

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0068 |
| **Date** | 2026-11-06 |
| **Source** | User. Contents and exclusions as specified by the user; the naming-procedure exclusion is the user's decision of 2026-11-05 (see Proposed Rule, sheet 7). |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, "## Reference packet contents", verbatim — see "Current Rule (verbatim)" below. |
| **Proposed Rule** | Replace that section with the text under "Proposed Rule (verbatim)" below: twelve sheets, delivered as 12 separate PDF files plus one combined `Reference - Full Packet.pdf` for printing, filed in `Chemistry/Reference/`. The given-Week-2 / usable-on-tests sentence and the "Do not test pure recall" line are kept unchanged. Also add thirteen `REF` rows to the "Short titles" table (text below). |
| **Supersedes** | `courses/chemistry/DECISIONS.md` § "Reference packet contents" (the four-item list). The "Short titles" table is extended, not superseded. |
| **Reason** | The four-item list (periodic table, polyatomic ions, solubility rules, percent error) does not describe the packet the user wants to hand out. The user has specified a 12-sheet packet, including which polyatomic ions must be memorized and what is deliberately left out. |
| **Affected Agents** | None directly. Builders and checkers read the course file. |
| **Affected Skills** | `build-document` (builds the packet against this list), `verify-content` (checks a built packet against this list). Neither skill file is edited: neither currently states packet contents (a search of `.claude/skills/` for "reference packet", "polyatomic", "solubility" finds nothing), so there is no stale copy to report. |
| **Affected Courses** | Chemistry. |
| **Risk** | low |
| **Recommendation** | Approve as amended. It replaces a short list with a complete one inside one course file; nothing else reads the old list. The packet can be named and filed only once SHULL-CHG-0069 is implemented. |
| **Decision** | User, 2026-11-06, in chat: "approve 0058 and 0059 with your changes" |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | 59858c0 |
| **Verified** | yes — `courses/chemistry/DECISIONS.md` diff checked against this record by the main session; `reference_titles('chemistry')` returns all 13 `REF` rows and each builds a valid `Reference - <topic>.pdf` name. |

---

## Current Rule (verbatim)

From `courses/chemistry/DECISIONS.md`:

```markdown
## Reference packet contents

Given to students around Week 2, usable throughout the year including on tests:

- Periodic table
- Polyatomic ions, with an indication of which ones must be memorized
- Solubility rules
- Percent-error formula/reference

Do not test pure recall of anything in the packet unless the learning target explicitly
requires memorization.
```

## Proposed Rule (verbatim)

```markdown
## Reference packet contents

Given to students around Week 2, usable throughout the year including on tests. Twelve sheets, in
this order. Each sheet is its own PDF, and all twelve are also combined into one
`Reference - Full Packet.pdf` for printing. Filed in `Chemistry/Reference/` and named at course
level (`standards/NAMING.md` §2); each file's topic is its `REF` row in "Short titles". The sheet
titles below are the on-page titles. Molecular shapes are drawn as SVG.

1. **Equations & Constants**
   - *Measurement:* density, percent error, percent composition, average atomic mass.
   - *Mole:* n = m/M; particles = n × N_A.
   - *Gases:* Boyle, Charles, Gay-Lussac, combined, Avogadro, ideal gas, Dalton partial pressures.
   - *Solutions:* molarity; dilution M1V1 = M2V2.
   - *Thermochemistry:* q = mcΔT.
   - *Acid/base:* pH, pOH, pH + pOH = 14, titration.
   - *Light:* c = λν, E = hν.
   - *Nuclear:* half-life.
   - *Constants:* N_A; R in L·atm, L·kPa and L·mmHg units; c; h; specific heat of water;
     pressure equivalents (atm, mmHg, kPa); K = °C + 273. STP = 0 °C and 1 atm; molar volume
     22.4 L.
   - Unit conversions, including metric prefixes; a dimensional-analysis setup template.
2. **Significant Figure Rules** — counting rules, plus the ×/÷ and +/− rounding rules.
3. **VSEPR Geometry** — up to 6 electron domains. Columns: domains, bonding vs lone pairs,
   electron geometry, molecular geometry, bond angle, drawn shape.
4. **Periodic Table** — atomic number, symbol, name, average atomic mass to 2 decimals.
5. **Electronegativity Table** — Pauling values to 2 decimals; noble gases blank.
6. **Polyatomic Ions** — 37 ions grouped by charge (1+, 2+, 1−, 2−, 3−). In each group the
   ions students must memorize come first, marked ★ and set in bold.
   - *Memorize (15):* ammonium NH4+, hydronium H3O+, acetate C2H3O2−, hydrogen carbonate HCO3−,
     chlorate ClO3−, cyanide CN−, hydroxide OH−, nitrate NO3−, nitrite NO2−, permanganate MnO4−,
     carbonate CO3 2−, chromate CrO4 2−, sulfate SO4 2−, sulfite SO3 2−, phosphate PO4 3−.
   - *Reference only, unstarred (22):* mercury(I) Hg2 2+; perchlorate ClO4−, chlorite ClO2−,
     hypochlorite ClO−, bromate BrO3−, iodate IO3−, periodate IO4−, hydrogen sulfate HSO4−,
     hydrogen sulfite HSO3−, hydrogen sulfide HS−, dihydrogen phosphate H2PO4−, thiocyanate SCN−,
     cyanate OCN−; dichromate Cr2O7 2−, hydrogen phosphate HPO4 2−, oxalate C2O4 2−, peroxide
     O2 2−, thiosulfate S2O3 2−, silicate SiO3 2−; phosphite PO3 3−, arsenate AsO4 3−,
     borate BO3 3−.
7. **Naming Toolkit** — Roman numerals I–VIII; covalent prefixes mono–deca; the seven diatomic
   elements (H, N, O, F, Cl, Br, I). **No naming procedure or rules** for ionic, covalent, or
   acid names: the procedure stays in the Unit 6 materials (possibly a U6 organizer), so the
   test-usable packet does not answer naming items.
8. **Metals with Multiple Charges** — Cu, Fe, Pb, Sn, Hg, Co, Ni, Cr, Mn, Au; plus Ag+, Zn2+ and
   Cd2+ shown as fixed-charge exceptions.
9. **Solubility Grid** — cations × anions (polyatomic anions included). Each cell is soluble,
   slightly soluble, or insoluble, marked by letter so it reads in greyscale. Plus a five-line
   rules summary.
10. **Activity Series** — metals and halogens.
11. **Strong Acids & Bases** — list.
12. **Specific Heats** — common substances.

**Deliberately excluded** (user decision): the electronegativity-difference bond-type scale,
nuclear particle symbols, acid naming rules.

Do not test pure recall of anything in the packet unless the learning target explicitly
requires memorization.
```

Note on ion-count arithmetic, checked while drafting: by group, 1+ = 2, 2+ = 1, 1− = 8 + 12 = 20,
2− = 4 + 6 = 10, 3− = 1 + 3 = 4; total 37 = 15 memorize + 22 reference-only. The brief's counts are
internally consistent.

### Short titles (verbatim rows to add)

In `courses/chemistry/DECISIONS.md` § "Short titles", append these rows to the table, after the
last existing row (`| 2.3 | Electron Configs |`). The code `REF` marks a course-level Reference
topic (SHULL-CHG-0069). Each is at most 20 characters; the sheet titles above stay as the on-page
titles.

```markdown
| REF | Equations |
| REF | Sig Figs |
| REF | VSEPR Shapes |
| REF | Periodic Table |
| REF | Electronegativity |
| REF | Polyatomic Ions |
| REF | Naming Toolkit |
| REF | Multi-Charge Metals |
| REF | Solubility |
| REF | Activity Series |
| REF | Strong Acids & Bases |
| REF | Specific Heats |
| REF | Full Packet |
```

Length check, and the sheet each row names:

| Sheet | On-page title | Short title | Characters |
|---|---|---|---|
| 1 | Equations & Constants | Equations | 9 |
| 2 | Significant Figure Rules | Sig Figs | 8 |
| 3 | VSEPR Geometry | VSEPR Shapes | 12 |
| 4 | Periodic Table | Periodic Table | 14 |
| 5 | Electronegativity Table | Electronegativity | 17 |
| 6 | Polyatomic Ions | Polyatomic Ions | 15 |
| 7 | Naming Toolkit | Naming Toolkit | 14 |
| 8 | Metals with Multiple Charges | Multi-Charge Metals | 19 |
| 9 | Solubility Grid | Solubility | 10 |
| 10 | Activity Series | Activity Series | 15 |
| 11 | Strong Acids & Bases | Strong Acids & Bases | 20 |
| 12 | Specific Heats | Specific Heats | 14 |
| all | (combined print file) | Full Packet | 11 |

All thirteen are at most 20. `&` is a legal filename character (it is not in NAMING.md §2's
dropped set), and `U1 | Matter & Atoms` already uses it.

## Decision-log entry (to append on approval)

To go at the **top** of `courses/chemistry/DECISIONS.md` § "Decision log"
(`governance/CHANGE_CONTROL.md` §5), dated the day the user approves:

```markdown
### YYYY-MM-DD — Reference packet: twelve sheets
The Week-2 reference packet is twelve sheets: Equations & Constants, Significant Figure Rules,
VSEPR Geometry, Periodic Table, Electronegativity Table, Polyatomic Ions (37, the 15 to memorize
starred and bold), Naming Toolkit, Metals with Multiple Charges, Solubility Grid, Activity Series,
Strong Acids & Bases, Specific Heats. The naming procedure is left out on purpose and stays in
Unit 6 materials (user, 2026-11-05), so the packet does not answer naming items on a test. Also
excluded: the electronegativity-difference bond-type scale, nuclear particle symbols, acid naming
rules. Full list in "Reference packet contents".
Supersedes: Reference packet contents (four-item list: periodic table, polyatomic ions, solubility
rules, percent error).
Status: CONFIRMED · SHULL-CHG-0068
```

## Resolved

The main session offered these changes on 2026-11-06, and this record now states them. The user's
reply referred to them as "with your changes". The user's decision itself is recorded in
`Decision:` and `Status:` by the main session, not here.

1. **One file or twelve?** Both: 12 separate PDF files, one per sheet, plus one combined
   `Reference - Full Packet.pdf` for printing. Filed in `Chemistry/Reference/`.
2. **Short titles over 20 characters.** Resolved by the thirteen `REF` short-title rows above, each
   at most 20 characters. The full sheet titles stay as the on-page titles.

## Still open

1. **Filing and naming depend on SHULL-CHG-0069.** The course-level name (`Reference - [Topic].pdf`)
   and the `Chemistry/Reference/` folder are defined there. This record does not depend on 0059
   to be applied, but the packet cannot be named or filed until 0059 is implemented, including its
   builder change, and until the Librarian has confirmed `Chemistry/Reference/` exists.
2. **Unit 6 organizer.** "Possibly a U6 organizer" is not a decision to build one. Nothing here
   commits to it.
