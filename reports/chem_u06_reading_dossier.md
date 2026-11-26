# Chemistry U6 Unit Reading: Source Dossier (four sections)

Prepared by: researcher | Date: 2026-11-25 | Workflow: `workflows/unit-textbook.md`, "Commission the chapter" step 2
Status: REPORT ONLY. Nothing outside `reports/` was edited.

**Scope.** U6 Chemical Nomenclature has four taught sections (`courses/chemistry/DECISIONS.md` l.50–52; decision log l.509–518, SHULL-CHG-0099): 6.1 Covalent Names & Formulas · 6.2 Polyatomic Ions · 6.3 Ionic Names & Formulas with Transition Metals · 6.4 Naming Acids & Formulas. Codes 6.5 and 6.6 are RETIRED. The unit title stays "Chemical Nomenclature" (l.447–455, SHULL-CHG-0116).

**Inputs.**
- The Overseer outline and Matt's decisions D3–D5 (2026-11-25), both as relayed in the commission.
- `reports/chem_u06_deck_extract.md`.
- DECISIONS l.50–52, 203–219, 498–507 and 509–518.
- `templates/reference/chem_data.py` l.74–108: the builder data for Reference sheets 6 and 8, which is what students actually hold.
- `templates/unit-roadmap/specs/chem_u06.json`.
- `templates/reading/specs/chem_u07_reading.json` l.188, the "formula unit" wording.
- `templates/slide/decks/chem_u14_s14.1_properties_definitions.json` l.65–84, for the acid-definition check.

I re-derived every formula and charge balance in this dossier. None was copied from the outline without checking.

**Network limitation (read this first).** Primary hosts were tried again this session. WebFetch failed with `ENOTFOUND` for `goldbook.iupac.org`, `iupac.org` (Red Book 2005 PDF), `iupac.qmul.ac.uk`, `www.ecfr.gov`, `www.law.cornell.edu` and `www.cdc.gov`. After that I stopped trying hosts, as the tool instructs. WebSearch worked. Every external locator below is backed by one of three things:
- **(S)**: a search-result excerpt from the named page;
- **(K)**: a value I know but could not retrieve this session;
- **(R)**: a repository file, with its line number.

Nothing marked (K) is verified until someone opens the locator. To open the primary pages directly, the session's network settings must allow `goldbook.iupac.org`, `iupac.org`, `iupac.qmul.ac.uk`, `www.ecfr.gov`, `www.law.cornell.edu`, `www.cdc.gov`, `www.fsis.usda.gov` and `pubchem.ncbi.nlm.nih.gov`. The Auditor should open each locator during QA. **Pattern:** primary hosts have now been blocked in two consecutive dossiers (U7 on 2026-11-24, and U6). See A-15.

**Status codes** (same as `reports/chem_u07_reading_dossier.md`):
- **SRC**: sourced, with a locator and an excerpt or data.
- **DER**: derived by arithmetic or charge balance from sourced inputs; the working is shown.
- **ILL**: illustrative.
- **SEC**: secondary sources only.
- **UNVERIFIED**: I could not find a source. Do not print it as fact.

---

## A. Findings (blocking first, then by fix time)

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| A-1 | D4 note wording: "they have both names and both are accepted" | **This overstates the position.** IUPAC no longer recommends the -ous/-ic metal names. The 2005 Red Book uses Stock (Roman-numeral) names. The classical names are still *used*: on labels, in older books, and in trade names. "Accepted" reads as though chemists' naming authority endorses them, and it does not. | encyclopedia.com, "Nomenclature of Inorganic Chemistry": the -ous/-ic method is "no longer recommended" (S, SEC). The Red Book text itself was not retrieved (K) | **Blocking (accuracy of a printed note)**. This is Matt's decision, so it is held for his review and not changed | Suggested wording: "Some iron and copper compounds have two names. Older names such as *ferrous* and *ferric* are still used on labels and in older books. The Roman-numeral name is the modern standard because it states the charge." Matt decides. |
| A-2 | Classical names to print (D4) | Verified pairs (§C 6.3-k): Fe ferrous/ferric; Cu cuprous/cupric; Sn stannous/stannic; Pb plumbous/plumbic; Co cobaltous/cobaltic; Hg mercurous/mercuric. The suffix rule is **-ous = lower charge, -ic = higher charge of that metal's two ions.** The suffix does **not** give the number: ferrous is +2 but cuprous is +1, and ferric is +3 but stannic is +4. Mercurous is Hg₂²⁺. Cobaltic chloride, CoCl₃, is a disputed compound | §C 6.3-k | **Major** | Print **Fe and Cu only** (ferrous/ferric, cuprous/cupric) in the student note. Put Sn/Pb/Co in the teacher key. **Leave mercury out entirely**: mercurous needs Hg₂²⁺, which D4 excludes, and printing only mercuric invites the wrong guess "mercurous = Hg⁺". State in the note that the ending tells *lower or higher*, not the charge. |
| A-3 | 6.2 On Your Own: PO₃³⁻ = phosphite, against D3 | **Phosphite is on the sheet but unstarred**: it is one of the 22 reference-only ions (DECISIONS l.212; chem_data.py l.91 `("phosphite","PO3^3-",False)`). D3 asks for the starred ions in On Your Own. Only two -ate/-ite pairs are starred at both ends: nitrate/nitrite and sulfate/sulfite. Sulfate/sulfite is the Example and nitrate/nitrite is the tear-off, so any third -ite item has to use an unstarred ion. Chemistry note: the free PO₃³⁻ ion is not a real species in water, and its acid H₃PO₃ is diprotic (§C 6.4-j). Neither matters for a naming-pattern item | DECISIONS l.205–213; chem_data.py l.79–92 | Major (D3 compliance) | Option A (keep): phosphite is a fair transfer item because its parent, phosphate, is starred. Label it a pattern item in the key. Option B (all-starred): "Carbonate is CO₃²⁻. Write the formula and charge of hydrogen carbonate." Answer: HCO₃⁻. This tests the hydrogen- rule instead. Option C: chlorate ClO₃⁻ (starred) → chlorite ClO₂⁻. **Do not** use phosphorous acid as a 6.4 item. |
| A-4 | 6.2 per-/-ate/-ite/hypo- generalization | **The rule has a trap: permanganate.** It is starred, but there is no "manganate" on the sheet, and real manganate (MnO₄²⁻) differs from permanganate in **charge**, not oxygen count. Dichromate, thiosulfate and thiocyanate are also not part of the oxygen ladder. "-ate" is a reference name, not a fixed oxygen count: nitrate has 3 O, sulfate has 4, carbonate has 3 | chem_data.py l.80–90; manganate (K) | Major | State the ladder for the **chlorine family** (the figure), and add "the same pattern holds for bromine and iodine (bromate, iodate, periodate)". Do **not** write "per- always means one more oxygen". Teacher note: permanganate is a name to memorize, not a ladder member. |
| A-5 | 6.4 binary-acid rule versus cyanide | **HCN (hydrocyanic acid) follows the hydro-…-ic pattern but is not binary** (it has three elements). Cyanide is starred, so students will meet it. The deck teaches "no oxygen → hydro-" (slide 33), which does cover HCN. A "binary acid" definition alone does not | deck extract §9; DECISIONS l.206 | Major | Teach the rule **by the anion's ending**: -ide → hydro-…-ic acid; -ate → -ic; -ite → -ous. Keep the bold "binary acid" definition as written. Either leave HCN out of student items, or add one sentence: "Cyanide, CN⁻, also ends in -ide, so HCN(aq) is hydrocyanic acid." |
| A-6 | 6.1 prefixes versus 6.4 "hydrogen chloride" | **An inconsistency students will notice.** After 6.1, a strict prefix rule would name HCl(g) "hydrogen monochloride" and H₂S "dihydrogen monosulfide". By convention, binary hydrogen compounds of nonmetals are named **without** prefixes (hydrogen chloride, hydrogen sulfide). Water and ammonia keep common names | Deck slide 32 uses "hydrogen chloride" (R); naming convention (K) | Major | Add one sentence in 6.1 or 6.4: "Compounds of hydrogen with one nonmetal are named without prefixes: HCl is hydrogen chloride. Water (H₂O) and ammonia (NH₃) keep their common names." Keep hydrogen-first compounds out of the 6.1 Example and On Your Own items. |
| A-7 | "Molecular" (deck) versus "covalent" (DECISIONS) | DECISIONS titles 6.1 "**Covalent** Names & Formulas". Sheet 7 says "covalent prefixes" (l.214). The roadmap's 6.1 focus says "Molecular compounds & prefixes", and its I-can statement says "binary **covalent** compounds". The U7 spec says "molecular substances" (l.188) | DECISIONS l.51, 214; roadmap l.16–21; deck extract §10 #4 | Minor | Print the section heading exactly as DECISIONS gives it. In the prose: "Covalent compounds are also called **molecular compounds** because they are made of molecules." Then use "covalent" in rule statements, matching the packet, and "molecule" for the particle. Both words then point at the same thing, and neither the deck nor U7 is contradicted. |
| A-8 | Oxide elision (D5) | Matt's choice: monoxide, tetroxide, pentoxide. This matches the deck (extract §6) and common US textbook usage. IUPAC 2005: numerical prefixes are **not** elided, and **monoxide** is the only allowed exception ("dinitrogen tetraoxide", "pentaoxide") | IUPAC provisional Red Book ch. 5 (2004): "The final vowels of numerical prefixes should not be elided (although monoxide, rather than monooxide, is an allowed exception through general use)", with the example N₂O₄ dinitrogen tetraoxide (S); Wikipedia cites Red Book 2005 p.69 (S, SEC); IUPAC Brief Guide: "no elision … e.g. tetraaqua, pentaoxide … except monoxide" (S) | Info (teacher key) | Key note: "This reading drops the vowel before 'oxide' (tetroxide, pentoxide), as most US textbooks do. IUPAC (2005) keeps it (tetraoxide, pentaoxide) and elides only 'monoxide'. Accept either spelling." Elide only before "oxide". Do not invent "tetriodide" and the like. |
| A-9 | Acid working definition versus U14.1 | **No clash.** DECISIONS gives no acid definition (14.1 is a title only, l.89). The U14.1 deck states the Arrhenius definition as "Acid: produces H+ in water" (deck l.81), the same wording the outline proposes. The Gold Book defines acid in Brønsted/Lewis terms, which U14.1 teaches next | U14.1 deck l.65–84 (R); Gold Book A00071: "a molecular entity or chemical species capable of donating a hydron (proton)…" (S) | Info | Definition: "a compound that produces hydrogen ions (H⁺) when it dissolves in water". Add "Unit 14 widens this definition." Do not name Arrhenius or Brønsted in U6. Key note: in water, H⁺ attaches to a water molecule as H₃O⁺, which is starred on sheet 6. |
| A-10 | Sheet 6 "hydrogen sulfide (bisulfide)" HS⁻ versus 6.4 H₂S | **A naming collision on the student's own sheet.** "Hydrogen sulfide" is the sheet's name for HS⁻ (chem_data.py l.85) and also the usual name for H₂S gas. The deck uses H₂S(aq) as hydrosulfuric acid (slide 34) | chem_data.py l.85 | Minor | If H₂S appears, say "hydrogen sulfide gas, H₂S", or avoid it. Report the sheet label to the Secretary as a possible clarity proposal. I have not changed it. |
| A-11 | Gold Book versus IUPAC spellings in the vocabulary | IUPAC uses **oxoacid / oxoanion** (Gold Book O04374; "oxyacid" was merged into it in 2011), **monoatomic** (K) and **hydrogencarbonate** as one word (S, SEC). US school usage is oxyacid / oxyanion / monatomic / hydrogen carbonate. The sheet says "hydrogen carbonate (bicarbonate)" (chem_data.py l.79) | §D | Info | Keep the school spellings so they match the sheet. Add one key line on the IUPAC variants. |
| A-12 | "Formula unit" wording reused from U7 | Verbatim U7 sentence (spec l.188): "A formula unit is the lowest whole-number ratio of ions in an ionic compound." No Gold Book entry was found for "formula unit" (search returned none) | §D | Info | Reuse it word for word, as commissioned. U7 dossier D8 ("not introduced before U7") becomes **outdated** once U6 ships. U7 can keep its definition at 7.2, since a repeated identical definition does no harm. The Secretary may want to note that U6 is now the first introduction. |
| A-13 | FeO / Fe₂O₃ colour connection | FeO is black and Fe₂O₃ is red-brown (§C 6.3-m). Supported by suppliers and secondary sources only; the CRC/PubChem rows were not opened. Caveats: FeO is nonstoichiometric and not thermodynamically stable at room temperature. Commercial "black iron oxide" pigment is usually Fe₃O₄, not FeO. Red ochre is clay **coloured by** hematite (Fe₂O₃), not pure Fe₂O₃ | §C 6.3-m, 6.3-n | Minor | Print: "Iron(II) oxide, FeO, is a black solid. Iron(III) oxide, Fe₂O₃, is red-brown; it is the mineral hematite, which gives red ochre its color." Do not call FeO a pigment. Do not say "rust" (same rule as the U7 spec l.503). |
| A-14 | Sodium nitrite: which regulation | 21 CFR 172.175 (FDA) covers sodium nitrite in smoked or cured **fish** and in **home-curing** preparations. **Commercial cured meat** is regulated by USDA FSIS under 9 CFR 424.21/424.22 (e.g. bacon: 120 ppm ingoing for pumped bacon, 200 ppm for dry-cured). FSIS states the purpose: nitrite is used "to inhibit the growth of the bacterial spores of C. botulinum" | §C 6.2-g | Minor | Cite **USDA FSIS** for the meat connection. Print no ppm figures and no health claims (the nitrosamine debate is outside scope). "Pink" is not in the FSIS excerpt: FSIS says "stable red color". Use "gives cured meat its color". |
| A-15 | Recurring blocked hosts (pattern) | This is the second dossier in a row whose primary IUPAC/NIST/CFR/CDC hosts did not resolve. Every IUPAC and CFR locator is therefore (S) or (K) | Network note above | Info (pattern) | The Secretary could propose a standing allow-list for research sessions: goldbook.iupac.org, iupac.org, iupac.qmul.ac.uk, ecfr.gov, law.cornell.edu, cdc.gov, fsis.usda.gov, pubchem.ncbi.nlm.nih.gov, physics.nist.gov, bipm.org, ciaaw.org. |
| A-16 | Deck errors (teacher information only) | Slide 21 shows strontium sulfide → SrS, but its speaker note reads "Calcium oxide is CaO." Slide 9 shows CO and PCl₃, but its note reads "CO2 is carbon dioxide. N2O4 is dinitrogen tetroxide." Both notes describe a different slide; the chemistry in each note is correct. I found no other science errors in the extract. NH₄⁺ on slide 14 checks: 7 + 4 = 11 protons, 11 − 1 = 10 electrons ✓ | deck extract §10 #11–12 | Info | Teacher-only. Do not carry either note into the reading key. Matt fixes the deck. |
| A-17 | Carbonic acid connection | CO₂ + H₂O ⇌ H₂CO₃ is correct. The hydration constant is about 1.7 × 10⁻³ at 25 °C, so well under 1% of dissolved CO₂ is present as H₂CO₃. Most stays as CO₂(aq) | §C 6.4-k | Info | The equation with ⇌ is fine to print. Key note: "Most dissolved CO₂ stays as CO₂; only a small fraction becomes H₂CO₃." Do not print a pH value (SEC only). |

---

## B. Names, formulas and charges checked by charge balance (DER)

| Item | Ions | Balance | Result | Status |
|---|---|---|---|---|
| N₂O | covalent, prefixes | di- (2 N), mono- (1 O) | **dinitrogen monoxide** ✓ | DER + SRC (6.1-c) |
| SF₆ | covalent | mono- omitted on S; hexa- = 6 F | **SF₆** ✓ | DER |
| CO / CO₂ | covalent | 1 O / 2 O | carbon monoxide / carbon dioxide ✓ | DER |
| SO₄²⁻ → SO₃²⁻ | -ate → -ite | one fewer O, same 2− charge | **sulfite** ✓ (both starred) | SRC (R) chem_data.py l.87–88 |
| PO₄³⁻ → PO₃³⁻ | -ate → -ite | one fewer O, same 3− | **phosphite** ✓ (unstarred; A-3) | SRC (R) l.91 |
| CO₃²⁻ + H⁺ → HCO₃⁻ | hydrogen- ion | −2 + 1 = −1 | **hydrogen carbonate** ✓ | DER; SRC (R) l.79 |
| ClO₄⁻ / ClO₃⁻ / ClO₂⁻ / ClO⁻ | chlorine ladder | 4, 3, 2, 1 O; all 1− | perchlorate / chlorate★ / chlorite / hypochlorite ✓ | SRC (R) l.80–82 |
| Al₂O₃ (charge tiles) | Al³⁺, O²⁻ | 2(+3) + 3(−2) = +6 − 6 = 0 | **Al₂O₃** ✓; LCM 6 | DER |
| Fe₂O₃ | O²⁻ | 3(−2) = −6; 2 Fe share +6 → +3 each | **iron(III) oxide** ✓; classical: ferric oxide | DER |
| FeO | O²⁻ | −2 → Fe +2 | iron(II) oxide; classical: ferrous oxide | DER |
| FeCl₃ (tear-off 6.3) | Cl⁻ | 3(−1) → Fe +3 | iron(III) chloride. Iron has two common ions (Fe²⁺, Fe³⁺; sheet 8), so the numeral is needed. Na has only Na⁺ (Group 1), so NaCl needs none ✓ | DER; SRC (R) l.98 |
| lead(II) nitrate | Pb²⁺, NO₃⁻ | +2 + 2(−1) = 0 | **Pb(NO₃)₂** ✓. Parentheses because there are two nitrate ions | DER; SRC (R) l.99, l.81 |
| NH₄Cl etc. | NH₄⁺ | ammonium compounds are ionic | ✓ (deck slide 3, 27) | SRC (R) |
| HNO₃ | NO₃⁻ (-ate) | 1 H⁺ per 1− | **nitric acid** ✓ | DER |
| H₂CO₃ | CO₃²⁻ (-ate) | 2 H⁺ per 2− | **carbonic acid** ✓ | DER |
| H₂SO₄ / H₂SO₃ | sulfate / sulfite | 2 H⁺ | sulfuric / sulfurous (stem "sulfur-") ✓ | DER |
| H₃PO₄ | phosphate | 3 H⁺ | phosphoric (stem "phosphor-") ✓ | DER |
| HCl(g) / HCl(aq) | — | — | hydrogen chloride / hydrochloric acid ✓ | SRC (R) deck slide 32 |
| NaHCO₃ | Na⁺, HCO₃⁻ | +1 − 1 = 0 | sodium hydrogen carbonate ✓ | DER + SRC (WIM) |

---

## C. Source dossier: every factual claim in the outline

### Why It Matters (front page)

| ID | Claim | Value / excerpt | Source (title, edition/date) | Locator | Status |
|---|---|---|---|---|---|
| WIM-a | NaHCO₃ = sodium hydrogen carbonate = sodium bicarbonate = baking soda | FDA lists the GRAS food substance as "Sodium bicarbonate", identified as NaHCO₃ (CAS 144-55-8) | 21 CFR 184.1736 "Sodium bicarbonate" (eCFR current through July 2026) | ecfr.gov/current/title-21/…/part-184/subpart-B (excerpts via codes.findlaw.com/cfr/title-21-food-and-drugs/cfr-sect-21-184-1736/) | SRC (S) for NaHCO₃ = sodium bicarbonate |
| WIM-b | "hydrogen carbonate" is the systematic name for HCO₃⁻ | Sheet 6 prints "hydrogen carbonate (bicarbonate)", starred. IUPAC 2005 writes "hydrogencarbonate" (one word) | chem_data.py l.79 (R); Wikipedia "Bicarbonate", citing Red Book 2005 p.137 (S, SEC) | en.wikipedia.com/wiki/HCO3 | SRC (classroom) / SEC (IUPAC spelling) |
| WIM-c | "baking soda" is the common name | PubChem synonym list for CID 516892 (K) | PubChem, Sodium bicarbonate | pubchem.ncbi.nlm.nih.gov/compound/516892 | (K). Low risk; host blocked |
| WIM-d | Do not claim "IUPAC rejects bicarbonate" | The search found no Red Book statement that "bicarbonate" is unacceptable | — | — | **UNVERIFIED**. Do not print |

### 6.1 Covalent Names & Formulas

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 6.1-a | Prefixes mono–deca (1–10) | mono di tri tetra penta hexa hepta octa nona deca | Sheet 7 Naming Toolkit, DECISIONS l.214; deck slide 7 | (R) | SRC (classroom) |
| 6.1-b | mono- omitted on the first element; the second element always takes a prefix and -ide | Deck slides 6, 8, 9. IUPAC compositional names follow the same pattern (K) | deck extract §2 | (R) | SRC (classroom) |
| 6.1-c | N₂O = dinitrogen monoxide | PubChem CID 948 synonyms include "dinitrogen monoxide", "dinitrogen oxide", "laughing gas" | PubChem, Nitrous oxide (CID 948), archived copy | webarchive.library.unt.edu/web/20130301075049/http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=948; Sigma-Aldrich 295590 lists "dinitrogen monoxide" | SRC (S). Key note: the common name is nitrous oxide. Keep "nitrous" off the student page, so it is not confused with 6.4's nitrous acid (an older -ous naming of N oxides) |
| 6.1-d | SF₆ = sulfur hexafluoride | Deck slide 11 | (R) | — | SRC (classroom) + DER |
| 6.1-e | Why prefixes are needed (tear-off) | The same two nonmetals can combine in more than one ratio (CO/CO₂; NO₂/N₂O₄, deck slide 12). Covalent compounds have no ion charges to fix the ratio | deck slide 12 | (R) | DER. **Answerable only if the prose states both reasons** |
| 6.1-f | CO is a toxic gas | CDC: carbon monoxide is "an odorless, colorless gas that can kill you"; "hundreds" die each year; sources include furnaces, generators, charcoal grills | CDC, "Carbon Monoxide Poisoning Basics" | cdc.gov/carbon-monoxide/about/index.html | SRC (S). Host blocked for fetch |
| 6.1-g | CO₂ is the gas we exhale | NHLBI: cells "create the waste product carbon dioxide", which breathing removes; NLM ToxTown (archived): "When people breathe, they exhale carbon dioxide." | NIH NHLBI, "How the Lungs Work / Breathing benefits"; NLM ToxTown (archived 2013) | nhlbi.nih.gov/health/lungs/breathing-benefits; webarchive.library.unt.edu/web/20130214011323/http://toxtown.nlm.nih.gov/text_version/chemicals.php?id=6 | SRC (S). No CDC/EPA page was found with this wording, so NIH is the best reachable source |
| 6.1-h | Figure: CO vs CO₂ | One C + one O versus one C + two O; different substances | DER from formulas | — | DER. A drawn molecule figure needs no external data. Use the repository molecular-structure builder (workflow table) |

### 6.2 Polyatomic Ions

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 6.2-a | Polyatomic ion = a group of covalently bonded atoms with an overall charge | Roadmap 6.2 I-can: "a group of covalently bonded atoms that carries an overall charge"; deck slide 14 | roadmap l.27 (R) | — | SRC (classroom). No Gold Book entry was searched successfully |
| 6.2-b | -ate / -ite: same charge, one fewer O | nitrate NO₃⁻/nitrite NO₂⁻; sulfate SO₄²⁻/sulfite SO₃²⁻; chlorate ClO₃⁻/chlorite ClO₂⁻; phosphate PO₄³⁻/phosphite PO₃³⁻ | chem_data.py l.80–91 (R) | — | SRC (classroom). See A-4 caveats |
| 6.2-c | per- (one more O than -ate), hypo- (one fewer O than -ite) | perchlorate ClO₄⁻, hypochlorite ClO⁻; also periodate IO₄⁻ vs iodate IO₃⁻ | chem_data.py l.82–83 | — | SRC (classroom) |
| 6.2-d | hydrogen- ions: adding H⁺ lowers the charge by 1 | HCO₃⁻★, HSO₄⁻, HSO₃⁻, H₂PO₄⁻, HPO₄²⁻ | chem_data.py l.79, 84–85, 88 | — | SRC (classroom) + DER |
| 6.2-e | Example: sulfate → sulfite | SO₄²⁻ → SO₃²⁻; both starred | l.87–88 | — | SRC + DER |
| 6.2-f | On Your Own: PO₃³⁻ = phosphite; it is on the 37-ion sheet | **Yes, on the sheet, unstarred** | DECISIONS l.212; chem_data.py l.91 | — | SRC. See A-3 |
| 6.2-g | Sodium nitrite in cured meat | FSIS: "Nitrites are used in certain cured meat and poultry products to inhibit the growth of the bacterial spores of C. botulinum"; nitrite first authorized in meat in 1925. FSIS training: "development and maintenance of a stable red color is very important in cured … meat". 9 CFR 424.22: bacon 120 ppm ingoing (pumped/massaged), ≤200 ppm (dry-cured). 21 CFR 172.175 (FDA): sodium nitrite in smoked cured fish (≤200 ppm) and home-curing preparations | USDA FSIS, *Clostridium botulinum* fact sheet (Jan 2010); FSIS FPLIC 5a "Cured Meat and Poultry Operations"; 9 CFR 424.22; 21 CFR 172.175 | fsis.usda.gov/sites/default/files/media_file/2021-02/Clostridium_botulinum.pdf; fsis.usda.gov/sites/default/files/media_file/2021-03/fplic-5a-cured-meat-and-poultry-operations.pdf; law.cornell.edu/cfr/text/9/424.22; law.cornell.edu/cfr/text/21/172.175 | SRC (S). Fact sheet dated 2010; check the current FSIS page. See A-14 |
| 6.2-h | Figure: chlorine oxyanion ladder | ClO₄⁻ / ClO₃⁻ / ClO₂⁻ / ClO⁻, all 1− | chem_data.py l.80–82 | — | SRC (classroom). Show O count and charge as labels, not colour |
| 6.2-i | Tear-off: nitrate vs nitrite endings | -ate has one more O than -ite at the same charge: NO₃⁻ vs NO₂⁻ | as 6.2-b | — | DER. **Answerable only if the prose names nitrate and nitrite with formulas**. Sulfate/sulfite alone is not enough for a direct question |

### 6.3 Ionic Names & Formulas with Transition Metals

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 6.3-a | Main-group charges: G1 +1, G2 +2, Al +3; G15 −3, G16 −2, G17 −1 | Deck slide 16 | (R) | — | SRC (classroom). Builds on U3 3.7 Ion Formation (roadmap l.8) |
| 6.3-b | Charges sum to zero; lowest ratio | Deck slides 17–20 | (R) | — | SRC (classroom) |
| 6.3-c | Formula unit | "A formula unit is the lowest whole-number ratio of ions in an ionic compound." | U7 reading spec l.188 | `templates/reading/specs/chem_u07_reading.json` | SRC (classroom), verbatim. See A-12 |
| 6.3-d | Parentheses when more than one polyatomic ion | Ca(NO₃)₂, (NH₄)₂SO₄ (deck slides 28–29) | (R) | — | SRC (classroom) |
| 6.3-e | Ammonium compounds are ionic | Deck slide 3 TF, slide 27 | (R) | — | SRC (classroom) |
| 6.3-f | Stock Roman numeral worked back from the anion | Gold Book: "oxidation number", synonym "Stock number" (obsolete term) | IUPAC Gold Book O04363 | goldbook.iupac.org/terms/view/O04363 | SRC (S). Key note: the numeral is the oxidation number, which equals the charge for a monatomic ion. Do not name Alfred Stock (K, not sourced) |
| 6.3-g | Ag⁺, Zn²⁺, Cd²⁺ fixed | Sheet 8 fixed-charge exceptions | DECISIONS l.218–219; chem_data.py l.108 | — | SRC (classroom) |
| 6.3-h | Multi-charge metals on sheet 8 | Cu⁺/Cu²⁺, Fe²⁺/Fe³⁺, Pb²⁺/Pb⁴⁺, Sn²⁺/Sn⁴⁺, Hg₂²⁺/Hg²⁺, Co²⁺/Co³⁺, Ni²⁺/Ni³⁺, Cr²⁺/Cr³⁺, Mn²⁺/Mn³⁺, Au⁺/Au³⁺ | chem_data.py l.96–107 | — | SRC (classroom) |
| 6.3-i | Example: Fe₂O₃ = iron(III) oxide | §B | — | — | DER. Also U7 On Your Own option B, a good cross-unit link |
| 6.3-j | On Your Own: lead(II) nitrate = Pb(NO₃)₂ | §B | — | — | DER |
| 6.3-k | Classical names (D4) | -ous = lower, -ic = higher. Sn²⁺ stannous / Sn⁴⁺ stannic; Pb²⁺ plumbous / Pb⁴⁺ plumbic; Cu⁺ cuprous / Cu²⁺ cupric; Hg₂²⁺ mercurous / Hg²⁺ mercuric; Co²⁺ cobaltous / Co³⁺ cobaltic (CoCl₃ disputed); Fe²⁺ ferrous / Fe³⁺ ferric. IUPAC: -ous/-ic "no longer recommended" | Pearson study guide "Naming monatomic cations: systematic and common naming"; Purdue ChemEd "names" review; Wikipedia "Cobalt(II) chloride", "Cobalt(III) chloride"; encyclopedia.com "Nomenclature of Inorganic Chemistry"; LibreTexts "Transition Metals" | pearson.com/channels/intro-to-chemistry/study-guides/naming-monatomic-cations-systematic-and-common-naming; chemed.chem.purdue.edu/genchem/topicreview/bp/ch2/names.php; en.wikipedia.com/wiki/Cobalt(II)_chloride; encyclopedia.com/science/news-wires-white-papers-and-books/nomenclature-inorganic-chemistry | **SEC** (S). Fe/Cu pairs are universal in textbooks. IUPAC status SEC. See A-1, A-2 |
| 6.3-l | Figure: charge tiles for Al₂O₃ | 2 × (+3) and 3 × (−2) tiles; totals +6 and −6 | DER | — | DER. Label totals in text, not by colour |
| 6.3-m | FeO black; Fe₂O₃ red-brown | Sigma-Aldrich 400866 FeO: "grey-black powder". American Elements SDS Fe₂O₃: colour "red-brown". CRC Handbook: FeO "black cubic cryst", Fe₂O₃ "red-brown hex cryst" (K) | Sigma-Aldrich product 400866; American Elements "Iron(III) Oxide"; CRC Handbook, Physical Constants of Inorganic Compounds (K) | sigmaaldrich.com/…/aldrich/400866; americanelements.com/iron-iii-oxide-1309-37-1 | **SEC** (S); CRC (K). See A-13 |
| 6.3-n | Red ochre = Fe₂O₃ | MFA CAMEO "Red ochre": composition Fe₂O₃. U. Minnesota: earthy hematite "red to reddish brown … often called red ochre". Mindat: "Red Oxide of Iron" is a synonym of hematite, Fe₂O₃ | MFA Boston CAMEO; University of Minnesota Common Minerals "Hematite"; Mindat min-29771 | cameo.mfa.org/wiki/Red_ochre; commonminerals.esci.umn.edu/minerals-g-m/hematite; mindat.org/min-29771.html | SRC (S). Museum, university and mineral-database sources; no USGS page was found. Print "colored by hematite" (A-13) |
| 6.3-o | Tear-off: why iron(III) chloride needs a numeral and NaCl does not | §B FeCl₃ row | — | — | DER. **Answerable only if the prose says iron forms Fe²⁺ and Fe³⁺ and sodium forms only Na⁺** |

### 6.4 Naming Acids & Formulas

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 6.4-a | Acid: produces H⁺ in water (working definition) | U14.1: "Acid: produces H+ in water." Gold Book: hydron donor (Brønsted) / electron-pair acceptor (Lewis) | U14.1 deck l.81 (R); Gold Book A00071 | goldbook.iupac.org/terms/view/A00071 | SRC (classroom + S). See A-9 |
| 6.4-b | HCl(g) hydrogen chloride vs HCl(aq) hydrochloric acid | Deck slide 32: "(aq) means dissolved in water" | (R) | — | SRC (classroom). See A-6 |
| 6.4-c | Binary: hydro- + root + -ic | HCl hydrochloric, HBr hydrobromic, H₂S hydrosulfuric (deck slides 33–34) | (R) | — | SRC (classroom). See A-5 on HCN |
| 6.4-d | Oxyacids: -ate → -ic, -ite → -ous; keep per-/hypo-; no hydro- | Deck slides 31, 33; Gold Book O04374: "a compound which contains oxygen, at least one other element, and at least one hydrogen bound to oxygen, and which produces a conjugate base by loss of positive hydrogen ion(s)" | Gold Book O04374 (source: PAC 1995, 67, 1307; "oxyacid" O04380 merged 2011) | old.goldbook.iupac.org/html/O/O04374.html | SRC (S) |
| 6.4-e | H count = anion charge | HNO₃, H₂SO₄, H₃PO₄, H₂CO₃ (§B); deck slide 35 | (R) | — | DER |
| 6.4-f | Stem changes: sulfuric, phosphoric | sulfate → sulfuric, sulfite → sulfurous (deck slide 33); phosphate → phosphoric | (R) | — | SRC (classroom) |
| 6.4-g | Example: HNO₃ = nitric acid | Deck slide 31 | (R) | — | SRC + DER |
| 6.4-h | On Your Own: carbonic acid = H₂CO₃ | §B. Carbonate is starred (D3 ✓). Not in the deck (extract §9), so it is new to students | — | — | DER |
| 6.4-i | Tear-off: how an acid's ending shows its ion | -ic ← -ate (or hydro-…-ic ← -ide); -ous ← -ite | — | — | DER. Answerable |
| 6.4-j | Do not use phosphorous acid as an H-count example | H₃PO₃ is HPO(OH)₂: one H on P, so it is diprotic (pKa₁ ≈ 1.3, pKa₂ ≈ 6.7) | Wikipedia "Phosphorous acid" (S, SEC) | en.wikipedia.org/wiki/Phosphorous_acid | SEC. Teacher info only |
| 6.4-k | Carbonated drinks: CO₂ + H₂O ⇌ H₂CO₃ | Hydration constant [H₂CO₃]/[CO₂] = 1.70 × 10⁻³ at 25 °C, so most dissolved CO₂ stays as CO₂. At about 2.5 atm (a soda bottle), pH ≈ 3.7 | Wikipedia "Carbonic acid" (archived 2012), citing standard data; Clark, U. Ottawa GEO4342 "DIC" notes | webarchive.library.unt.edu/web/20120621033729/http://en.wikipedia.org/wiki/Carbonic_acid; mysite.science.uottawa.ca/idclark/GEO4342/2009/DIC.pdf | Equation: standard chemistry, SRC (S). Numbers **SEC**: key note only, do not print. See A-17 |

---

## D. The ten proposed bold terms (checked against IUPAC where an entry exists)

| Term | Section | Suggested student definition | IUPAC check | Status / note |
|---|---|---|---|---|
| binary compound | 6.1 | a compound made of exactly two elements | Red Book 2005 IR-5.2 "binary compounds" (K) | (K). Covers both NaCl and CO₂. Fine |
| molecular compound | 6.1 | a compound made of molecules, in which atoms (usually nonmetals) share electrons in covalent bonds | No Gold Book entry found | UNVERIFIED as an IUPAC term; it is the standard school term. See A-7 |
| monatomic ion | 6.3 (or 6.2) | an ion made of a single atom, such as Na⁺ or Cl⁻ | IUPAC spelling "monoatomic" (K) | (K). Keep "monatomic" (A-11) |
| polyatomic ion | 6.2 | a group of covalently bonded atoms that carries an overall charge | — | SRC (roadmap l.27). Matches the deck |
| oxyanion | 6.2 | a negative polyatomic ion in which an element is bonded to oxygen atoms, such as sulfate, SO₄²⁻ | IUPAC "oxoanion" (K) | Key note: hydroxide is not usually counted as an oxyanion |
| formula unit | 6.3 | the lowest whole-number ratio of ions in an ionic compound | No Gold Book entry found | **Verbatim U7 wording** (spec l.188) |
| Stock system | 6.3 | the naming system that shows a metal ion's charge with a Roman numeral in parentheses, as in iron(III) | Gold Book O04363: "Stock number" is an obsolete synonym of oxidation number (S) | SRC (S). Acceptable school term |
| acid | 6.4 | a compound that produces hydrogen ions (H⁺) when it dissolves in water | Gold Book A00071 is Brønsted/Lewis (S) | Matches U14.1 l.81 (A-9) |
| binary acid | 6.4 | an acid made of hydrogen and one other element, such as HCl | No IUPAC term (Gold Book calls these "hydracids", per O04374) | See A-5 (HCN) |
| oxyacid | 6.4 | an acid that contains hydrogen, oxygen and at least one other element | Gold Book O04374 "oxoacid" (S) | SRC (S). Spelling per A-11 |

Count = 10, at the workflow limit (`workflows/unit-textbook.md` step 2). If the designer needs a slot, "monatomic ion" is the least essential.

---

## E. Tear-off questions: answerable from the reading?

| Section | Question | Answerable? | Condition |
|---|---|---|---|
| 6.1 | Why are prefixes needed in covalent names? | Yes | The prose must say that two nonmetals can form more than one compound (CO/CO₂) and that covalent compounds have no charges to set the ratio |
| 6.2 | What do the endings in nitrate and nitrite tell you? | Yes | Nitrate NO₃⁻ and nitrite NO₂⁻ must both be named with formulas. The sodium nitrite connection helps |
| 6.3 | Why does iron(III) chloride need a Roman numeral when NaCl does not? | Yes | The prose must state that iron forms Fe²⁺ and Fe³⁺ and sodium forms only Na⁺ |
| 6.4 | How does an acid's name show which ion it came from? | Yes | Stated directly by the -ate → -ic / -ite → -ous rule |

Single-part check: as phrased, each is a single question. The 6.2 wording "nitrate vs nitrite endings" must not turn into "name both and explain" (two parts).

---

## F. UNVERIFIED or not opened (do not print as fact without the locator)

- Red Book 2005 primary text: IR-1.4/IR-5 elision rule, -ous/-ic status, hydrogencarbonate spelling, "monoatomic". Every IUPAC nomenclature statement is (S) via provisional drafts, the Brief Guide or Wikipedia, or (K).
- That IUPAC "rejects" bicarbonate: not found. Do not print.
- CRC Handbook colour rows for FeO and Fe₂O₃: (K). PubChem colour fields: not opened.
- PubChem "baking soda" synonym: (K).
- Current eCFR text of 21 CFR 172.175 and 9 CFR 424.21/424.22: excerpts only. FSIS fact sheet dated 2010.
- "Pink" as the cured-meat colour: not in the FSIS excerpt.
- Who Alfred Stock was, and the date of the Stock system: not sourced. Do not print.
- Carbonic-acid pH and hydration constant: SEC. Key only.
- Hydroxide's status as an oxyanion; manganate MnO₄²⁻: (K).

## G. Observation versus inference

- **Observed:** DECISIONS lines; chem_data.py sheet data; the roadmap, U7 and U14.1 spec text; the deck extract; search-result excerpts for each (S) locator.
- **Inferred:**
  - The A-6 hydrogen-compound inconsistency: inferred from the naming convention (K), not from a sourced statement.
  - That students will be confused by "nitrous oxide" beside "nitrous acid": a teaching judgement.
  - That printing mercuric alone invites "mercurous = Hg⁺": a teaching judgement.
  - That D4's "accepted" will be read as an IUPAC endorsement: a judgement about wording.
- **Not observed:** any primary page on iupac.org, goldbook.iupac.org, ecfr.gov, law.cornell.edu, cdc.gov or pubchem. All were blocked this session.

## H. Search sources used (accessed 2026-11-25)

- [IUPAC Brief Guide, inorganic](https://iupac.qmul.ac.uk/BriefGuide/inorganic.html) · [IUPAC provisional Red Book ch. 5 (2004)](https://stats.iupac.org/reports/provisional/abstract04/RB-prs310804/Chap5-3.04.pdf) · [Wikipedia, IUPAC inorganic nomenclature](https://en.wikipedia.com/wiki/Inorganic_nomenclature)
- [Gold Book O04374 oxoacids](https://old.goldbook.iupac.org/html/O/O04374.html) · [Gold Book O04363 oxidation number](https://old.goldbook.iupac.org/html/O/O04363.html) · [Gold Book A00071 acid](https://old.goldbook.iupac.org/html/A/A00071.html)
- [encyclopedia.com, Nomenclature of Inorganic Chemistry](https://www.encyclopedia.com/science/news-wires-white-papers-and-books/nomenclature-inorganic-chemistry) · [Pearson, naming monatomic cations](https://www.pearson.com/channels/intro-to-chemistry/study-guides/naming-monatomic-cations-systematic-and-common-naming) · [Purdue ChemEd names](https://chemed.chem.purdue.edu/genchem/topicreview/bp/ch2/names.php) · [Cobalt(II) chloride](https://EN.wikipedia.com/wiki/Cobalt(II)_chloride) · [Cobalt(III) chloride](https://Www.wikipedia.org/wiki/Cobalt(III)_chloride)
- [Wikipedia, HCO3 / bicarbonate](https://en.wikipedia.com/wiki/HCO3) · [21 CFR 184.1736 (FindLaw)](https://codes.findlaw.com/cfr/title-21-food-and-drugs/cfr-sect-21-184-1736/)
- [CDC CO basics](https://www.cdc.gov/carbon-monoxide/about/index.html) · [NHLBI breathing](https://www.nhlbi.nih.gov/health/lungs/breathing-benefits) · [NLM ToxTown CO₂ (archived)](https://webarchive.library.unt.edu/web/20130214011323/http://toxtown.nlm.nih.gov/text_version/chemicals.php?id=6) · [PubChem CID 948 (archived)](https://webarchive.library.unt.edu/web/20130301075049/http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=948)
- [FSIS C. botulinum fact sheet](https://www.fsis.usda.gov/sites/default/files/media_file/2021-02/Clostridium_botulinum.pdf) · [FSIS FPLIC 5a cured meat](https://www.fsis.usda.gov/sites/default/files/media_file/2021-03/fplic-5a-cured-meat-and-poultry-operations.pdf) · [9 CFR 424.22](https://www.law.cornell.edu/cfr/text/9/424.22) · [21 CFR 172.175](https://www.law.cornell.edu/cfr/text/21/172.175)
- [Sigma-Aldrich FeO 400866](https://sigmaaldrich.com/IN/en/product/aldrich/400866) · [American Elements Fe₂O₃](https://americanelements.com/iron-iii-oxide-1309-37-1) · [MFA CAMEO red ochre](https://cameo.mfa.org/wiki/Red_ochre) · [U. Minnesota hematite](https://commonminerals.esci.umn.edu/minerals-g-m/hematite) · [Mindat red oxide of iron](https://www.mindat.org/min-29771.html)
- [Phosphorous acid](https://en.wikipedia.org/wiki/Phosphorous_acid) · [Carbonic acid (archived)](https://webarchive.library.unt.edu/web/20120621033729/http://en.wikipedia.org/wiki/Carbonic_acid) · [U. Ottawa DIC notes](https://mysite.science.uottawa.ca/idclark/GEO4342/2009/DIC.pdf)
