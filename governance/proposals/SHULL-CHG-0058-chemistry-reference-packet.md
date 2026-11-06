# SHULL-CHG-0058 — Chemistry reference packet becomes a 12-sheet packet

**Path A — a course change.** Only `courses/chemistry/DECISIONS.md` is affected. No standard or skill
is edited by this record. (The filename this packet needs is a separate Path B question:
SHULL-CHG-0059.)

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0058 |
| **Date** | 2026-11-06 |
| **Source** | User. Contents and exclusions as specified by the user; the naming-procedure exclusion is the user's decision of 2026-11-05 (see Proposed Rule, sheet 7). |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, "## Reference packet contents", verbatim — see "Current Rule (verbatim)" below. |
| **Proposed Rule** | Replace that section with the text under "Proposed Rule (verbatim)" below. The given-Week-2 / usable-on-tests sentence and the "Do not test pure recall" line are kept unchanged. |
| **Supersedes** | `courses/chemistry/DECISIONS.md` § "Reference packet contents" (the four-item list). |
| **Reason** | The four-item list (periodic table, polyatomic ions, solubility rules, percent error) does not describe the packet the user wants to hand out. The user has specified a 12-sheet packet, including which polyatomic ions must be memorized and what is deliberately left out. |
| **Affected Agents** | None directly. Builders and checkers read the course file. |
| **Affected Skills** | `build-document` (builds the packet against this list), `verify-content` (checks a built packet against this list). Neither skill file is edited: neither currently states packet contents (a search of `.claude/skills/` for "reference packet", "polyatomic", "solubility" finds nothing), so there is no stale copy to report. |
| **Affected Courses** | Chemistry. |
| **Risk** | low |
| **Recommendation** | Approve. It replaces a short list with a complete one inside one course file; nothing else reads the old list. Two items under "Open points" should be answered first or alongside, because they decide how the packet is filed and named. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | — (not implemented) |
| **Verified** | no — not implemented |

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

Given to students around Week 2, usable throughout the year including on tests. A print PDF of
twelve sheets, in this order. Molecular shapes are drawn as SVG.

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
Status: CONFIRMED · SHULL-CHG-0058
```

## Open points (not resolved by this record)

1. **One file or twelve?** "Format: print PDF" reads as one packet PDF, but SHULL-CHG-0059's examples
   (`Chemistry Reference - Equations.pdf`, `Chemistry Reference - Polyatomic Ions.pdf`) read as one
   file per sheet. Which it is decides how many names SHULL-CHG-0059 has to produce. (0059's own
   example `Equations` is already a shortened form of sheet 1's title.)
2. **Short-title length.** If each sheet is its own file and its title becomes the filename topic,
   four sheet titles exceed the 20-character limit in `standards/NAMING.md` §2: Equations &
   Constants (21), Significant Figure Rules (24), Electronegativity Table (23), Metals with
   Multiple Charges (28). Strong Acids & Bases is exactly 20; the rest are under. Short forms are
   the user's call; this record does not invent them. See SHULL-CHG-0059.
3. **Filing and naming.** The packet spans the whole year, so it has no `S.S` or `Unit X` code. It
   cannot be named under the current grammar or filed under the current Drive architecture. That is
   SHULL-CHG-0059 (Path B). This record does not depend on 0059 being approved, but the packet
   cannot be filed until it is.
4. **Unit 6 organizer.** "Possibly a U6 organizer" is not a decision to build one. Nothing here
   commits to it.
