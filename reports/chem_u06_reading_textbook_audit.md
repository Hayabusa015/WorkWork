# Chemistry U6 Unit Reading: Independent Accuracy and Print Review

Auditor | 2026-11-25 | Workflow: `workflows/unit-textbook.md`, "Independent accuracy and print review"; `.claude/skills/verify-content/SKILL.md`; `standards/QA_GATE.md`
Status: REPORT ONLY. No deliverable, spec, standard or other file was changed. The only file written is this report.

## Verdict: **FAIL (INCOMPLETE)**

I found no wrong science. Every printed compound, ion, Example, On Your Own item and key answer checks out when I work it myself. The tear-off leaf passes every parity and format check. The edition still cannot be released, for three reasons:

1. **Figure 6.1 vs SHULL-CHG-0042 (major, Matt's ruling needed).** The figure is a hand-drawn molecule picture. It shows overlapping atom circles, and CO₂ is drawn in O–C–O order. SHULL-CHG-0042 says that if RDKit cannot draw a structure well, the designer must "stop and ask Matt — do not improvise". The designer did not ask (A-1).
2. **Classical-names note (major).** The student note does not use Matt's approved "still used" wording. His approved text is not recorded anywhere in the repository (A-2).
3. **Primary sources (open).** Every primary source host was refused by the session proxy, so no locator could be opened. Under the workflow, a missing source stays open (§4).

## 1. Version and coverage

| Item | Value |
|---|---|
| Branch / commit | `claude/ecstatic-pascal-9cro1w` @ `6623322` (HEAD). The edition files were built at 19:47 UTC, before this commit. The commit's only change is one line in `templates/reading/build_reading_docx.py`: the fallback colour for the equilibrium arrow now comes from `T["ground"]["asphalt"]["hex"]` instead of `#000000` |
| Student PDF | `build/chem_u06_reading/Unit 6 Reading - Nomenclature.pdf`, 8 pp, Letter. sha256 `27bb35fb…5f78f` |
| Student DOCX | sha256 `dad075ce…725ed` |
| Key PDF | `build/chem_u06_reading/Unit 6 Reading Key - Nomenclature.pdf`, 2 pp. sha256 `884670c2…40ff2f` |
| Key DOCX | sha256 `a3e61381…f04196` |
| Identity after the builder change | I rebuilt U6 from the committed spec with the current builder, into the scratchpad. Both DOCX files match the shipped ones part for part. Both PDFs have identical text and **zero** differing pixels at 100 dpi. The arrow-colour change does not affect this edition |
| U7 regression | I also rebuilt U7 with the current builder and compared it with `build/chem_u07_reading/` (24 Nov). Both DOCX files match part for part, text is identical, and zero pixels differ on all 8 + 2 pages. **The claim that U7 is unchanged is confirmed** independently, at HEAD and not only at the designer's earlier build |
| Coverage | Student pp. 1–8 and key pp. 1–2: every page inspected, every figure, every compound and ion |
| Proof method | **Screen proof only.** Full pages were rendered with PyMuPDF at 110 dpi in grayscale and in colour, at print scale (Letter, 100%). Figure 6.3 and the header were checked in crops at 200–400 dpi. **No physical photocopy was made.** The grayscale verdicts are screen-proof verdicts |

## 2. QA gate checklist

| Check | Result |
|---|---|
| Deliverable exists, opened | PASS. Both PDFs and both DOCX files were opened and hashed |
| File type / naming | PASS. `Unit 6 Reading - Nomenclature` and `Unit 6 Reading Key - Nomenclature` (NAMING.md l.54–63; DECISIONS SHULL-CHG-0116). The key is a separate file |
| Codes / scope | PASS. Chip `U06 / S6.1–S6.4`. The cover list, headings, question labels and key all read 6.1 Covalent Names & Formulas · 6.2 Polyatomic Ions · 6.3 Ionic Names & Formulas with Transition Metals · 6.4 Naming Acids & Formulas, verbatim from DECISIONS l.50–52. 6.5 and 6.6 appear nowhere. `validate_codes.py` OK |
| Unit title | PASS. "Chemical Nomenclature" on the cover, the header and every running head |
| Fonts | PASS. `pdffonts` shows ArchivoRoman Regular and Bold, plus ArchivoNarrow (Type 3, as in U7). The key adds ShullHand, Patrick Hand and Archivo SemiBold Italic. `audit_fonts.py` and `--key` both report OK. No DejaVu or Liberation |
| Ink | PASS. Student pages: worst 8.04% toner (p3), average 4.29%. Key: worst 6.46%. Every page reports "no fill", and the widest solid band is 0.00 in |
| Binding / holes | PASS. `audit_binding.py`: the hole zone is clear, the guides sit on the binding side, outline only, and alternate sides p1–p8 |
| Thumb tab | PASS. Outline only and 0.20 in wide. Its outer stroke is **0.22 in** from the paper edge on all 8 pages (x0 = 15.9 pt / x1 = 596.2 pt). It sits right on odd pages and left on even pages, never on the binding side |
| Coloured type | PASS. Coloured text uses only `primaryDeep` #B84100. Display orange #FF6B1A appears only as rules and outlines. Label and footer greys are tokens. Only one deep token is used |
| Standing decisions | PASS: Option B two-column layout with a display-title opener · Archivo only · no fills · Why It Matters (p1) · exactly one Connection per section (6.1 One oxygen atom apart, 6.2 Nitrite in cured meat, 6.3 Two iron oxides, 6.4 Carbonated drinks) · "monoxide/tetroxide/pentoxide" (D5; grep finds no tetraoxide, pentaoxide or monooxide) · Fe and Cu only in the classical note (no Hg, Sn, Pb or Co on the student page) · starred-15 emphasis stated (p2) |
| Classical-names wording (D4) | **FAIL**. See A-2 |
| SHULL-CHG-0042 | **FAIL, held for Matt**. See A-1 |
| Clipped text | PASS. Nothing is clipped at any box, column or page edge. The only spans past the 0.50 in outside margin are 1–3 pt trailing glyph boxes (p1, p3; key p1 handwriting), and all are fully on the page |
| Grayscale | PASS on screen. C vs O (Fig 6.1) and cation vs anion tiles (Figs 6.4, 6.5) differ by solid vs dashed line. The chlorate box in Fig 6.3 renders mid-grey (luminance ≈ 142/255) at 1.6 pt and is backed by the bold "chlorate", so it is still distinct. See A-7 |
| Every number re-solved | PASS (§3) |
| Voice | PASS. Direct, second person, no brochure sentences |
| Answer key | PASS. Separate file, matches one-to-one (§5) |
| Banned-content grep (spec `banned` list) | PASS. No rust, pink, ppm, "reject", mercury/Hg, stann/plumb/cobalt, HCN, nitrous oxide, -aoxide, phosphorous acid, HS⁻, Arrhenius/Brønsted/Alfred, or pH on the student pages |
| Drive destination | N/A. This is a pre-audit edition and has not been filed. The filing gate follows QA |

## 3. Independent solutions (worked from the printed givens before reading the key)

| Item | My result | Printed / key | Match |
|---|---|---|---|
| Example 6.1: name N₂O | 2 N → di-; 1 O → mono- + oxide, elided → **dinitrogen monoxide** | same | ✓ |
| On Your Own 6.1: sulfur hexafluoride | no prefix → 1 S; hexa- → 6 F → **SF₆** | key SF₆ | ✓ |
| Example 6.2: sulfite from SO₄²⁻ | -ate → -ite, one fewer O, same charge → **SO₃²⁻** | same | ✓ |
| On Your Own 6.2: phosphite from PO₄³⁻ | **PO₃³⁻** (school convention; see A-6) | key PO₃³⁻ | ✓ |
| Example 6.3: name Fe₂O₃ | 3(−2) = −6 → 2 Fe = +6 → +3 each → **iron(III) oxide** | same | ✓ |
| On Your Own 6.3: lead(II) nitrate | Pb²⁺ + 2 NO₃⁻: +2 + 2(−1) = 0 → **Pb(NO₃)₂** | key Pb(NO₃)₂ | ✓ |
| Example 6.4: name HNO₃(aq) | NO₃⁻ nitrate, -ate → -ic, no hydro- → **nitric acid** | same | ✓ |
| On Your Own 6.4: carbonic acid | -ic ← -ate: carbonate CO₃²⁻; 2− → 2 H⁺ → **H₂CO₃** | key H₂CO₃ | ✓ |
| Al₂O₃ (prose + Fig 6.4) | 2(+3) + 3(−2) = 0, LCM 6 | Al₂O₃ | ✓ |
| CaO, not Ca₂O₂ | +2 −2; 2:2 reduces to 1:1 | CaO | ✓ |
| Ca(NO₃)₂ · CaCl₂ calcium chloride | +2 + 2(−1) = 0 | same | ✓ |
| FeCl₂ iron(II) chloride · FeCl₃ iron(III) chloride | Cl⁻ × 2 → Fe²⁺; × 3 → Fe³⁺ | same | ✓ |
| FeO iron(II) oxide · Fe₂O₃ iron(III) oxide (Connection) | O²⁻ → Fe²⁺; see above | same | ✓ |
| NH₄⁺: 11 p, 10 e⁻, 1+ | N 7 + 4 H = 11 p; 11 − 1 = 10 e⁻ | same | ✓ |
| NH₄Cl ammonium chloride, ionic | NH₄⁺ + Cl⁻ | same | ✓ |
| NaHCO₃ = Na⁺ + HCO₃⁻, sodium hydrogen carbonate | +1 − 1 = 0 | same | ✓ |
| HSO₄⁻ hydrogen sulfate | SO₄²⁻ + H⁺ → −1 | same | ✓ |
| Chlorine ladder ClO₄⁻ / ClO₃⁻ / ClO₂⁻ / ClO⁻ (per / -ate / -ite / hypo), all 1−, 4/3/2/1 O | as stated | same (prose + Fig 6.3) | ✓ |
| BrO₃⁻ bromate · IO₃⁻ iodate · IO₄⁻ periodate · MnO₄⁻ permanganate | correct formulas and charges | same | ✓ |
| NO₃⁻ / NO₂⁻ · SO₄²⁻ / SO₃²⁻ | correct | same | ✓ |
| NaNO₂ sodium nitrite · NaNO₃ sodium nitrate | correct | same | ✓ |
| N₂O₄ dinitrogen tetroxide · NO₂ nitrogen dioxide, both 1 : 2 | correct; not reduced | same | ✓ |
| HCl hydrogen chloride (g) / hydrochloric acid (aq) · HBr(aq) hydrobromic acid | correct | same | ✓ |
| HNO₂ nitrous · HClO₄ perchloric · HClO hypochlorous (names only printed) | correct | same | ✓ |
| H₂SO₄ sulfuric · H₂SO₃ sulfurous · H₃PO₄ phosphoric | 2, 2, 3 H⁺ per charge | same | ✓ |
| CO₂ + H₂O ⇌ H₂CO₃ | balanced: C 1, H 2, O 3 on each side; ⇌ glyph renders | same | ✓ |
| Classical names: ferrous Fe²⁺ / ferric Fe³⁺ / cuprous Cu⁺ / cupric Cu²⁺; -ous lower, -ic higher | correct | same | ✓ |
| Main-group charges G1 1+, G2 2+, Al³⁺, G17 1−, G16 2−, G15 3− | correct | same | ✓ |
| Ag⁺, Zn²⁺, Cd²⁺ fixed | matches sheet 8 (chem_data.py l.108) | same | ✓ (A-8 note) |
| Figs 6.2 (HCl(aq) acid, CaCl₂ ionic, CO₂ covalent), 6.5 (−6 / +6 / +3), 6.6 (-ide → hydro-…-ic; -ate → -ic; -ite → -ous) | correct | same | ✓ |
| Key-only species: Sn²⁺/Sn⁴⁺ stannous/stannic; Pb²⁺/Pb⁴⁺ plumbous/plumbic; Co²⁺/Co³⁺ cobaltous/cobaltic; Hg₂²⁺ mercurous; MnO₄²⁻ manganate; H₃O⁺; H₃PO₃ diprotic; HCN hydrocyanic (not binary); K_h ≈ 1.7 × 10⁻³ | all correct | — | ✓ |
| Prefix rules | mono- omitted on the first element ("A name never starts with mono-"); second element always prefixed; elision before "oxide" only (monoxide, tetroxide, pentoxide), per D5. The key notes IUPAC 2005 non-elision and accepts both spellings | — | ✓ |
| Sheet facts | 37 ions, 15 starred (chem_data.py: 2+1+20+10+4 = 37; stars 2+8+4+1 = 15); chlorate is the only starred halogen oxyanion; permanganate starred, no manganate on the sheet; phosphite unstarred | — | ✓ |

## 4. Source trace: claims, the four flagged sentences, primary-host attempts

**Primary hosts.** I tried each host by curl through the session proxy. Every one was refused with `CONNECT tunnel failed, response 403`: `www.cdc.gov` (CO basics), `www.ecfr.gov` (9 CFR 424.22; 21 CFR 184.1736), `www.law.cornell.edu` (9 CFR 424.22), `www.fsis.usda.gov` (C. botulinum fact sheet), `pubchem.ncbi.nlm.nih.gov` (CID 516892, 948), `goldbook.iupac.org`, `iupac.qmul.ac.uk`, and also `en.wikipedia.org`. No primary page was opened. This is the third session in a row with this pattern (dossier A-15).

| Claim (page) | Dossier locator | Assessment | Status |
|---|---|---|---|
| FDA lists baking soda as sodium bicarbonate, NaHCO₃ (p1) | WIM-a, 21 CFR 184.1736 (S, FindLaw) | Matches the excerpt | OPEN (primary refused). Low risk |
| CO: "odorless, colorless gas that can kill you"; furnaces, generators, charcoal grills (p2) | 6.1-f, CDC (S) | The printed wording follows the CDC excerpt | OPEN (cdc.gov refused). Low risk |
| CO₂ is the waste gas cells make and lungs breathe out (p1, p2) | 6.1-g, NHLBI / NLM (S) | Supported. See A-9 on the p1 phrasing | Supported (S) |
| **Flagged 1:** NaCl crystal is "a huge, repeating arrangement of Na⁺ and Cl⁻ ions" (p3) | Not in the dossier | Correct, standard chemistry. Classroom source: U4 deck `templates/slide/decks/chem_u04_u05/build.js` l.172, "Forms a crystal lattice" (R) | Supported (R). Low risk. Dossier gap, not an error |
| **Flagged 2:** perchlorate → perchloric acid; hypochlorite → hypochlorous acid (p4) | 6.4-d: "keep per-/hypo-"; deck slide 33 "Keep per- or hypo- when present" (R); deck extract l.229 | The names follow from the sourced rule (DER). HClO₄ perchloric and HClO hypochlorous are correct | Supported (R + DER) |
| **Flagged 3:** "Cured meats such as bacon can contain sodium nitrite" (p3) | 6.2-g: 9 CFR 424.22 bacon limits, 120 ppm pumped / ≤200 ppm dry-cured (S) | The dossier excerpt names bacon with sodium nitrite. No ppm figure is printed | Supported (S). OPEN for primary (eCFR/Cornell refused) |
| Nitrite "helps prevent botulism and keeps cured meat's red color" (p3) | 6.2-g FSIS: "inhibit the growth of the bacterial spores of C. botulinum"; "stable red color" (S) | A fair paraphrase. No "pink" | OPEN (fsis.usda.gov refused). Low risk |
| **Flagged 4:** "A soda is bottled with carbon dioxide dissolved in it" (p5) | 6.4-k: "at about 2.5 atm (a soda bottle)" (SEC) | Correct, general knowledge. "Some of that CO₂ reacts" is consistent with K_h ≈ 1.7 × 10⁻³ | Supported (SEC). Low risk |
| FeO black; Fe₂O₃ red-brown, hematite; red ochre "colored by it" (p4) | 6.3-m, 6.3-n (SEC/S) | Matches the dossier wording recommendation (A-13) | Supported (SEC). CRC/PubChem not opened |
| Ferrous/ferric/cuprous/cupric; -ous lower, -ic higher; Roman numeral is the modern standard (p4) | 6.3-k, A-1, A-2 (SEC) | Science correct. Wording: see A-2 | Science OK; wording FAIL |
| Acid definition, "Unit 14 widens this" (p4) | 6.4-a, A-9; DECISIONS l.88 (U14 Acids & Bases) | Correct | Supported (R) |
| "(Unit 4)" for covalent and ionic bonds (p1, p3) | DECISIONS l.42 (U4 Chemical Bonding) | Correct | Supported (R) |
| Formula-unit definition | 6.3-c; U7 spec l.191 | **Identical sentence** in U6 (p3, p8) and U7 | ✓ |

## 5. Tear-off leaf (exported student PDF)

| Check | Result |
|---|---|
| Final reading page / blank back / leaf | Reading ends on **p5** (odd). **p6** is the blank back: running head, outline thumb tab, hole guides and folio only, no content. The leaf is **p7 (front) / p8 (reverse)**, the last two physical pages |
| Cover list = headings = question labels = key | PASS, one-to-one: 6.1, 6.2, 6.3, 6.4 with DECISIONS titles on the cover and headings. Questions are labelled 6.1–6.4; key "Tear-off questions (page 7)" 6.1–6.4 |
| Name line | PASS. "NAME" with a rule at the top of p7 |
| Due line | PASS, verbatim: "Due ASAP. No late work will be accepted. We will start the unit with this." |
| Question count / single-part | PASS. Four questions, one per section, each a single direct question |
| Answerable from the reading | 6.1: both reasons on p1 (more than one compound, CO/CO₂; no ion charges to set the ratio) ✓ · 6.2: p2 "-ate has one more oxygen … Nitrate is NO₃⁻ and nitrite is NO₂⁻" ✓ · 6.3: p3 "Iron forms Fe²⁺ and Fe³⁺", "Sodium forms only one ion, Na⁺" ✓ · 6.4: p4 the -ate → -ic / -ite → -ous / -ide → hydro-…-ic rule plus Fig 6.6 ✓ |
| Writing space | PASS. Five ruled lines per question at print size |
| Vocabulary pairs | PASS. **10** pairs (≤10). Each matches its margin definition word for word and its bold first use (p1 binary compound, molecular compound; p2 monatomic ion, polyatomic ion, oxyanion; p3 formula unit, Stock system; p4 acid, binary acid, oxyacid). No other bold term in the body. The cover's "lists all ten" is accurate |
| Formula unit = U7 | PASS. "the lowest whole-number ratio of ions in an ionic compound", identical to U7 spec l.191 |
| Orientation | PASS. Both leaf sides are portrait and upright, with hole guides left on p7 and right on p8: correct for long-edge duplex |
| Simulated removal of the last leaf | PASS. Removing p7/p8 leaves p1–p6. All reading content (cover through the 6.4 Connection on p5) stays in the retained packet; p6 is blank. The cover's instruction "Tear off the last sheet" matches |
| Grayscale of the leaf | PASS. Text and rules only |

## 6. Findings

| # | Page / item | Claim or calculation | Independent evidence or result | Severity | Disposition |
|---|---|---|---|---|---|
| A-1 | p1 Figure 6.1 (CO / CO₂) | Caption: "The drawing shows atom counts only, not bonds or atom sizes." `make_chem_u06_figures.py` l.11–17 says the shared builder was tried and rejected for CO ("[C-]#[O+]" drops the C⁻ label; "[C]=O" draws a double bond), while O=C=O "drew correctly" | The figure draws touching, overlapping atom circles in a fixed spatial order. CO₂ is drawn O–C–O with carbon central, which is connectivity information, not a count. In my judgement that is a **molecular structure** under SHULL-CHG-0042 §2.1, whose stated purpose is to stop hand-drawn pictures that can disagree with their labels. `workflows/unit-textbook.md` also asks whether a diagram depicts a molecule. §2.1 says that if RDKit cannot draw it well, "stop and ask Matt — do not improvise". The designer improvised and disclosed it only in the key. The drawing is not wrong chemistry: C₁O₁ and C₁O₂, linear CO₂ order | **Major** (rule compliance on a student page) | **Matt decides**. Options: (a) approve the atom-count panel as an exception; (b) use builder CO₂ plus another agreed treatment for CO; (c) replace it with a non-spatial count panel (formula and atom tally, no arrangement). Hold release until he rules |
| A-2 | p4 "Older names" note (D4) | Expected: Matt's approved "still used" wording (dossier A-1 suggestion: "…Older names such as *ferrous* and *ferric* are still used on labels and in older books. The Roman-numeral name is the modern standard because it states the charge.") | The printed text reads "You may see older names like ferrous (Fe²⁺) and ferric (Fe³⁺), or cuprous (Cu⁺) and cupric (Cu²⁺), on labels and in older books. … The Roman-numeral name is the modern standard because it states the charge." **"Still used" does not appear on the student page.** It appears only in the key note (spec l.417). Matt's approved D4 text is not recorded anywhere in the repository, so verbatim compliance cannot be confirmed. The science of the printed version is correct and does not overstate IUPAC | **Major** (Matt-decision compliance) | Back to the designer through the Overseer: print the approved "still used" sentence, or obtain Matt's confirmation of the current wording. Record D4's text in the spec `$comment` so the next audit can check it |
| A-3 | All external locators | CDC, eCFR/Cornell (9 CFR 424.22; 21 CFR 184.1736), FSIS, PubChem, IUPAC Gold Book / Brief Guide | All refused: proxy `CONNECT tunnel failed, response 403` (§4). Every claim is consistent with its dossier excerpt and with standard chemistry. None is contradicted | Open (low risk per claim) | Open the locators when the network allows. The Secretary could act on dossier A-15 (allow-list) |
| A-4 | p3 "Ionic names never use prefixes" | Rule statement | The students' sheet 6 prints ionic names containing prefixes: dihydrogen phosphate, dichromate, hydrogen phosphate. The intended meaning (no counting prefixes for how many ions) is right, but the sentence as written is contradicted by the sheet beside them | Minor | Designer: e.g. "Ionic names never use prefixes to count ions." |
| A-5 | p4 Fig 6.6 caption; key p2 tear-off 6.4 handwriting | "Only an -ide anion takes hydro-"; "an -ate ion gives…" | Both break the suffix across lines: "Only an -" / "ide anion…" and "an -" / "ate ion". The suffix reads as a stray hyphen and the fragment "ide" | Minor | Designer: use non-breaking hyphens in suffix tokens (-ide, -ate, -ite, -ic, -ous) |
| A-6 | p3 On Your Own 6.2 / key | Phosphite = PO₃³⁻ | Matches sheet 6 (chem_data.py l.91) and the US school convention. Free PO₃³⁻ is not a real species in water (phosphite is in practice HPO₃²⁻), and the key itself says so. Dossier A-3 Option A was taken; phosphite is unstarred | Minor | Accept as a pattern item if Matt confirms Option A against D3 ("starred 15 with others for familiarity"). No change otherwise |
| A-7 | p2 Fig 6.3 chlorate box | "Heavy box: chlorate (starred)" | The box stroke is display orange #FF6B1A, which renders mid-grey (≈142/255) in grayscale. It is still distinct by 1.6 pt weight and bold "chlorate". "-ate" in the boxed row sits 1–2 pt from the box's left stroke, cramped but not clipped | Minor | Pass on screen. Optional: ink-coloured or heavier stroke and 2–3 pt inner padding. Confirm on a physical photocopy |
| A-8 | p3 "Silver (Ag⁺), zinc (Zn²⁺) and cadmium (Cd²⁺) are transition metals" | Classification | Ag is a transition metal. Under the strict IUPAC definition (incomplete d subshell), Zn and Cd are excluded, although they are commonly grouped with them. The sheet lists all three as fixed-charge exceptions | Minor | Optional: "are d-block metals with one common charge" or "are metals near the transition metals…". Teacher's choice |
| A-9 | p1 "Carbon dioxide is the gas you breathe out." | Simplification | Exhaled air is mostly N₂; CO₂ is the waste gas added (NHLBI excerpt). The p2 Connection states it precisely ("the waste gas your cells make and your lungs breathe out") | Minor | Optional: "Carbon dioxide is the waste gas you breathe out." |
| A-10 | p3 → p4 Figure 6.5 / Example 6.3 | Adjacency (QA §10) | First reference on p3 (right column). The figure and Example 6.3 sit on p4, one page turn later (p3/p4 are the two sides of one sheet) | Minor | Acceptable. Optional reflow |
| A-11 | Key p1 vs p2 | Labelling | The p1 kicker reads "ANSWER KEY" and the p2 running head reads "TEACHER KEY" | Minor | Optional consistency fix (builder-level) |
| A-12 | p6 | Blank back | Carries the running head, thumb tab, hole guides and folio "6". Consistent with the workflow; noted for the record | Info | None |
| A-13 | Builder change at `6623322` | Arrow colour fallback from tokens | Verified: U6 and U7 rebuilt at HEAD are byte-identical (DOCX) and pixel-identical (PDF) to the shipped editions | Info | None. Closed |

## 7. What returns to the designer through the Overseer

- **A-1:** Matt's ruling on Figure 6.1 under SHULL-CHG-0042.
- **A-2:** the classical-names wording.
- **Minor fixes:** A-4 and A-5. Optional polish: A-7 through A-11.

After the corrected export, I will recheck p1 (Fig 6.1), p3 and p4 (A-4, A-5, A-2 text and reflow), the key, pagination, and the leaf position. The verified content evidence for unaffected pages can be reused once their identity is confirmed.

---

# Round 2: recheck of the corrected export

Auditor | 2026-11-25 | Same workflow and gate as Round 1. Report only: no deliverable, spec or other file was changed.

## Verdict: **PASS**

- **A-1 and A-2 are fixed and verified** against the rulings as relayed by the coordinator.
- **The minor fixes (A-4, A-5, A-7, A-8, A-9, A-11) are applied correctly and add no errors.**
- **No regressions** in page breaks, leaf position, ink, fonts, binding, thumb tab, vocabulary or due line, and U7 is unchanged.
- **Two items stay open, neither blocking.** A-3 (primary locators unreachable) **stays open as a recorded limitation**, as in the U7 precedent (`reports/chem_u07_reading_textbook_audit.md`, Round 2). Every claim agrees with its dossier excerpt and none is contradicted. Matt either accepts this on the record or has the hosts allowed for a recheck. A-6 (Matt to confirm Option A for phosphite) also stays open as a minor item.

## R2-1. Version and evidence reuse

| Item | Value |
|---|---|
| Commit | `d7b001a` (HEAD), "U6 reading: apply audit fixes…". It changes `build_reading_docx.py` (a `keyLabel` option that defaults to the old labels), `make_chem_u06_figures.py` and `chem_u06_reading.json`. Round 1's report was committed separately at `919af39` |
| Student PDF | sha256 `74ddf5a4de99…6cd08fba`, 8 pp. DOCX `d4f031e7…44bc8` |
| Key PDF | sha256 `9ba316042ebc…cddebe76a1`, 2 pp. DOCX `4a2b93a0…e54927` |
| Round 1 baseline | `scratchpad/audited/` U6 copies hash `27bb35fb…` and `884670c2…`, identical to the edition audited in Round 1 |
| Rebuild at HEAD | U6 rebuilt from the committed spec into the scratchpad. Both DOCX files match the shipped ones part for part; PDFs have identical text and 0 differing pixels |
| My own diff, Round 1 → Round 2 (text, with U+2011 normalised to "-", plus a 100 dpi grayscale raster) | **p6, p8: identical (0 px).** p5 (164 px) and p7 (190 px): text identical, differences are hyphen glyphs only. p2: text identical; the differences are Fig 6.2 (caption line) and Fig 6.3 (box). p1, p3, p4: text changed exactly at A-9 + Fig 6.1 caption, A-4 + A-8, and A-2 + the Fig 6.6 caption respectively. Key p1: teacher-note reflow (Fig 6.1 note). Key p2: running head plus the 6.4 line break. **This matches the designer's description.** No page break moved: p1 ends "…keep their common names.", p3 ends "…the charge on each one.", p4 ends "…Hydrogen", and the reading ends on p5 |
| Reuse | Round 1 content evidence is reused for p5–p8. p1–p4 and both key pages were re-inspected in full |
| Proof method | Screen proof only (110 dpi full-page grayscale, 200–250 dpi crops). No physical photocopy |

## R2-2. Closure of Round 1 findings

| # | Page / item | Check | Result | Disposition |
|---|---|---|---|---|
| A-1 | p1 Fig 6.1 | Matt's "Counts-only panel" (relayed; recorded in the spec and key notes) | The figure has two ink-outline boxes (no fill). Each shows formula, name (primaryDeep), a hairline and a tally: "CO / carbon monoxide / 1 carbon atom / 1 oxygen atom" and "CO₂ / carbon dioxide / 1 carbon atom / 2 oxygen atoms". **No atoms are drawn, so there is no arrangement, no bonds, no charges and no sizes.** The tallies are correct. The caption ("The panel lists atom counts only; it is not a drawing of either molecule.") and the key note ("a counts-only panel with no structure: two labelled boxes giving each formula, name and atom tally (Matt's ruling, 2026-11-25…)") agree with the figure and with each other. SHULL-CHG-0042 no longer applies | CLOSED |
| A-2 | p4 Older names | Approved D4 text, verbatim | The PDF text contains the approved passage exactly, with superscripts flattened for the comparison: "You may see older names like ferrous (Fe²⁺) and ferric (Fe³⁺), or cuprous (Cu⁺) and cupric (Cu²⁺), on labels and in older books. -ous is the lower charge and -ic the higher. The Roman-numeral name is the modern standard because it states the charge." The designer's two following sentences ("The ending tells you lower or higher… ferrous is 2+ but cuprous is 1+." and "These metal endings have nothing to do with the acid endings…") are correct. The only difference from the approved string is the suffix hyphen: U+2011, which renders the same as "-". Matt's main-session message was not seen by me; the text was checked against the wording relayed by the coordinator, which is also recorded in the spec `$comment` | CLOSED |
| A-4 | p3 + Fig 6.2 | "prefixes" rule | The prose reads "Ionic names don't use prefixes to count ions." The Fig 6.2 footnote matches. The sheet's "dihydrogen phosphate" and "dichromate" no longer contradict it | CLOSED |
| A-5 | Suffix hyphens | U+2011 renders; no split | The DOCX files hold 27 (student) + 19 (key) U+2011. Every Archivo face in `brand/fonts` maps U+2011. The PDF hyphens render as normal hyphens, with no missing-glyph boxes. In the key's handwriting, ShullHand has no U+2011 glyph, so the hyphen comes from Patrick Hand, which is already an approved key face. It looks consistent at 250 dpi. A scan of every line on all 10 pages finds no line ending in a bare hyphen and none starting with an orphaned suffix. The Fig 6.6 caption now reads "Only an / -ide anion…", and key 6.4 reads "an / -ate ion…". `audit_fonts.py`: student "OK — Archivo only"; key `--key` "OK — Archivo and the key handwriting face only". `pdffonts` shows the same font set as Round 1 | CLOSED |
| A-7 | p2 Fig 6.3 | Chlorate box | The stroke is now ink (asphalt) at 1.6 pt, clearly heavier than the hairline row rules in grayscale. Columns are shifted right, giving about 3–4 pt inside the box ahead of "-ate". Not clipped | CLOSED |
| A-8 | p3 | Zn/Cd classification | Now reads "Metals such as silver (Ag⁺), zinc (Zn²⁺) and cadmium (Cd²⁺) have one common charge, so their names take no numeral." Accurate, and consistent with sheet 8 | CLOSED |
| A-9 | p1 | "Carbon dioxide is the waste gas you breathe out." | Judged accurate: CO₂ is the metabolic waste gas removed by breathing (NHLBI excerpt, dossier 6.1-g), and the sentence no longer implies exhaled air is CO₂. Consistent with the p2 Connection | CLOSED |
| A-11 | Key | Labels | The p1 kicker reads "CHEMISTRY · UNIT READING · ANSWER KEY" and the p2 running head reads "…READING · ANSWER KEY": consistent. The builder change is opt-in (`keyLabel`), and the U7 key is unchanged (R2-4) | CLOSED |
| A-3 | External locators | Retried this round | cdc.gov, ecfr.gov, fsis.usda.gov, pubchem.ncbi.nlm.nih.gov, goldbook.iupac.org: all `CONNECT tunnel failed, response 403` | OPEN, recorded limitation (not a content defect) |
| A-6 | p3 On Your Own 6.2, phosphite | Not part of this revision | Unchanged | OPEN, minor (Matt to confirm Option A) |
| A-10, A-12 | — | Not part of this revision | Unchanged; acceptable | No action |

## R2-3. Regression checks

| Check | Result |
|---|---|
| Science on the changed pages | Re-read p1–p4 and both key pages in full. No new claims beyond those listed in R2-2. Every compound, ion and answer is unchanged and still correct (Round 1 §3) |
| Ink | PASS. Student: worst 8.06% (p1), average 4.32%. Key: worst 6.63%. "No fill" on every page; widest solid band 0.00 in |
| Binding | PASS. `audit_binding.py` OK for 8 + 2 pages |
| Fonts | PASS (A-5). No DejaVu or Liberation |
| Clipped text | PASS. The only span past the outside margin is the same 3 pt handwriting glyph box on key p1 as in Round 1, fully on the page |
| Thumb tab, coloured type, codes, naming | Unchanged from Round 1 (pages identical apart from the listed edits). Fig 6.1 adds only ink outlines, a hairline and primaryDeep type |
| Tear-off leaf | PASS. Reading ends on p5; p6 is the blank back (0 px change); p7/p8 is the leaf (p7 hyphen glyphs only, p8 0 px). Cover list = headings = question labels = key (6.1–6.4). Name line and exact due line are present. Four single-part questions. 10 vocabulary pairs, identical to the unchanged bold and margin definitions. Long-edge orientation. Removing p7/p8 leaves all reading content in the packet |
| Key ↔ student | The key's tear-off answers, On Your Own solutions and vocabulary still match the student pages one-to-one. The Fig 6.1 key note matches the new figure |

## R2-4. U7 regression

I rebuilt U7 with the builder at `d7b001a` into the scratchpad and compared it with `build/chem_u07_reading/` (student sha256 `e52e57c9…`, key `e7d21724…`). The designer's `scratchpad/u7r2/` copy was compared with the same files. **Both match exactly:** DOCX files part for part, PDFs with identical text and 0 differing pixels on 8 + 2 pages. U7 is unchanged, including the key's "Answer Key" / "Teacher Key" labels. (The two U7 PDFs in `scratchpad/audited/` are an older U7 audit copy with different hashes, so they were not used as the baseline.)

## R2-5. Release note

QA passes. The edition can go to the ordinary approval-to-file gate. Carry A-3 (and A-6) forward on the record: they need Matt to accept them, or a recheck once the hosts are allowed. Drive destination is not yet checked, because the file has not been filed.

---

# Round 3: recheck after the Key Refreshers, monatomic-ion and write-in vocabulary changes

Auditor | 2026-11-25 | Same workflow, now including SHULL-CHG-0117 (Key Refreshers) and SHULL-CHG-0118 (write-in vocabulary): `workflows/unit-textbook.md` item 1, item 5 and the two audit bullets (l.17, l.21, l.55–56). Report only: no deliverable, spec or other file was changed.

## Verdict: **PASS**

- **The three approved additions are correct, sourced from classroom materials, and comply with both new rules.** The additions are the Key Refreshers box, "Naming monatomic ions" with the new Fig 6.4, and the element-vs-ion paragraph. Both rules are recorded as approved by the user in `governance/proposals/SHULL-CHG-0117…` and `…0118…`. The additions are recorded in the spec `$comment` (Matt, 2026-11-25, main session).
- **No science errors.** Figures are renumbered 6.1–6.7, and every cross-reference matches its figure.
- **The leaf, ink, fonts, binding, thumb tab and U7 regression all pass.**
- **Two new minor items (R3-1, R3-2), neither blocking.** A-3 (primary sources unreachable) stays open as a recorded limitation, and A-6 stays open as a minor item.

Note: the Round 2 PASS had led to a filing-queue row being marked Ready (`201e91d`). The edition then changed, so that PASS does not cover the current export. This Round 3 verdict is the one that applies to student `4f2814f5…` / key `c5002297…`.

## R3-1. Version and evidence reuse

| Item | Value |
|---|---|
| Commit | `041566b` (HEAD). Content commit `15968a1` (refreshers, 6.3 additions); builder write-in mode in `041566b` (U7 spec pins `vocabMode: print`) |
| Student PDF | sha256 `4f2814f5caca77b550261e1437fdaf2bf7f2357f5553cf8a40e5feaa11165bb2`, 8 pp. DOCX `7d7bb33f…e2396` |
| Key PDF | sha256 `c50022974d960c397f4195debb8347d4c2e4acec8c3e15e0fc91a07ed9749071`, 2 pp. DOCX `f7a702f3…c5386a` |
| Rebuild at HEAD | U6 rebuilt into the scratchpad. Both DOCX files match the shipped ones part for part; both PDFs have identical text and 0 differing pixels |
| Diff against Round 2 (my HEAD-of-R2 rebuild, identical to the R2 export) | **p6: identical (0 px).** **p7: text identical**; the 130 differing pixels are confined to the "UNIT 6" thumb-tab label (x 586–592 pt, y 186–210 pt, max grey delta 40), an anti-aliasing change with no content effect. p1–p5, p8 and both key pages changed. The text changes are exactly the three additions, the 6.3 charge sentence now pointing back to the refreshers, "each as above", the cover's sheet list, figure renumbering, and the write-in reverse |
| Reuse | Round 1/2 evidence is reused for p6 and p7 only. p1–p5, p8 and both key pages were re-inspected in full |
| Proof method | Screen proof only (110 dpi full-page grayscale). No physical photocopy |

## R3-2. Key Refreshers (SHULL-CHG-0117)

| Check | Result |
|---|---|
| Placement | PASS. Full-width outline box on p1, below the section list / Why It Matters band and above "6.1 Covalent Names & Formulas" |
| Count / form | PASS. Three items, each a single line at print size, each in the form "Unit N (N.n): reminder" |
| Sections exist | PASS. 3.7 Ion Formation (DECISIONS l.38); 4.2 Ionic Bonding and 4.3 Covalent Bonding (DECISIONS l.43). These are also the unit's builds-on in `templates/unit-roadmap/specs/chem_u06.json` l.7–9 |
| Item 1, "Unit 3 (3.7): Metals lose electrons to become cations; nonmetals gain electrons to become anions." | Correct. Traced to the U3 quiz, 3.7 items (`templates/activity/specs/chem_u03_quiz.json` l.58–72: Sr²⁺, Br⁻, Al³⁺; Ca loses two electrons to form Ca²⁺) and U6 deck slide 16 "Cations and anions" (deck extract l.60) (R) |
| Item 2, "Unit 3 (3.7): Main-group charges follow the group: Group 1 is 1+, Group 2 is 2+, Group 17 is 1−, Group 16 is 2−, Group 15 is 3−." | Correct. Traced to the U3 quiz 3.7 solutions (l.61, 113, 192: groups 1, 2, 13, 15, 16, 17) and deck slide 16 (R). See R3-1 (aluminum omitted) |
| Item 3, "Unit 4 (4.2, 4.3): Metals and nonmetals transfer electrons (ionic); nonmetals share electrons (covalent)." | Correct. Traced to the U4 deck `chem_u04_u05/build.js` l.170–186 ("Metal + nonmetal / Electrons transferred"; "Nonmetal + nonmetal / Electrons shared in pairs") (R) |
| Reminders only | PASS. No teaching, example or figure. The "Unit 3 (3.7):" lead-ins are grey label type, not bold terms. Bold body terms are still exactly the ten. "Cation" and "anion" appear unbolded |
| Tear-off independence | PASS. No question draws on a refresher: 6.1 prefixes, 6.2 -ate/-ite, 6.3 Roman numeral (key answer relies on "Sodium forms only one ion, Na⁺" in 6.3 body), 6.4 acid endings |
| One fact, one place | PASS. 6.3 now reads "Main-group ions have the charges listed in the Key Refreshers on page 1"; the group list is no longer restated in 6.3 |

## R3-3. New 6.3 content and figures

| Item | My independent result | Printed | Match |
|---|---|---|---|
| "A monatomic cation keeps the element's name: Na⁺ … sodium ion, Ca²⁺ … calcium ion. A monatomic anion takes the ending -ide, so chlorine becomes chloride and oxygen becomes oxide" | Correct. Deck slide 22 (R) | — | ✓ |
| Fig 6.4 ion table | fluorine → fluoride F⁻ · chlorine → chloride Cl⁻ · bromine → bromide Br⁻ · iodine → iodide I⁻ (Group 17, 1−) · oxygen → oxide O²⁻ · sulfur → sulfide S²⁻ (Group 16, 2−) · nitrogen → nitride N³⁻ · phosphorus → phosphide P³⁻ (Group 15, 3−) | all eight as printed. The charges agree with refresher item 2. Group bands are separated by rules, legible in grayscale. Outline only | ✓ |
| Fig 6.4 caption / footnote: "Keep the root of the element's name, add -ide, and read the charge from the group." | Correct | — | ✓ |
| "Chlorine is Cl₂, a gas made of molecules. Chloride is Cl⁻, an ion found in compounds such as NaCl." | Correct (K; low risk) | — | ✓ |
| "Sodium is a soft metal; the sodium ion is Na⁺." | Correct (K; PubChem refused, under A-3) | — | ✓ |
| Diatomic elements: H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂, "listed on your Naming Toolkit sheet" | Matches DECISIONS l.214–215: "the seven diatomic elements (H, N, O, F, Cl, Br, I)" | same seven | ✓ |
| "That subscript 2 belongs to the element… sodium chloride is NaCl, not NaCl₂." | Na⁺ + Cl⁻ → 1:1, NaCl | — | ✓ (wording note R3-2) |
| "To name an ionic compound, name the cation first and the anion second, each as above." | Points back to the new monatomic-ion paragraph, which comes before it in 6.3. Polyatomic and prefix sentences unchanged | — | ✓ |
| Figure numbering and cross-references | Fig 6.1 (p1), 6.2 (p2), 6.3 (p3), 6.4 (p3, new), 6.5 Al₂O₃ tiles (p4), 6.6 Fe₂O₃ working-back (p4), 6.7 acid endings (p5). Every "(Figure 6.n)" in the prose points at the correct figure, in order, on the same page as the figure | — | ✓ |
| All other compounds, Examples, On Your Own items, key answers | Unchanged text; re-read on the reflowed pages; still as in Round 1 §3 | — | ✓ |

Round 1's A-10 (Fig 6.5/6.6 one page turn after the reference) is resolved by the reflow: the Fe₂O₃ reference and Figure 6.6 now share p4.

## R3-4. Leaf and write-in vocabulary (SHULL-CHG-0118)

| Check | Result |
|---|---|
| Final reading page / blank back / leaf | Reading ends on **p5** (6.4 Connection). **p6** blank back (identical to R2). Leaf **p7 / p8**, the last two physical pages |
| Front (p7) | Unchanged text: NAME line; exact due line "Due ASAP. No late work will be accepted. We will start the unit with this."; four single-part questions 6.1–6.4, each answerable from its section; five ruled lines each |
| Cover = headings = labels = key | PASS: 6.1–6.4 throughout. The cover's "the last page lists all ten" is still accurate (the terms are listed) |
| Reverse (p8) | PASS. "Unit 6 vocabulary" with the instruction "Write each definition in your own words, using the reading. Each term is in bold where it is first defined." **10 terms, no definitions printed** (definitions-on-p8 check: 0 of 10). Two ruled lines per term, about 0.33 in apart and about 5.25 in long: adequate for a one- or two-sentence handwritten definition |
| Terms trace to bold definitions | PASS. Each p8 term is bolded where first defined (p1 binary compound, molecular compound; p2 monatomic ion, polyatomic ion, oxyanion; p3 formula unit; p4 Stock system, acid; p5 binary acid, oxyacid) with its margin definition |
| Key definitions = reading wording | PASS. Key p2 "Vocabulary (page 8) — expected definitions" gives all ten in the key hand; each matches the reading's margin definition word for word (programmatic comparison, 10/10). Accept-own-words note present |
| Formula unit = U7 | PASS, unchanged |
| Orientation / removal | PASS. Portrait, upright, hole guides left (p7) and right (p8), correct for long-edge duplex. Removing p7/p8 keeps p1–p6, which hold all reading content |

## R3-5. Gate re-run

| Check | Result |
|---|---|
| Fonts | PASS. `pdffonts`: student ArchivoRoman Regular and Bold, plus ArchivoNarrow; key adds ShullHand, Patrick Hand and Archivo SemiBold Italic. `audit_fonts.py` "OK — Archivo only"; `--key` "OK — Archivo and the key handwriting face only" |
| Ink | PASS. Student worst 7.72% (p1), average 4.42%; key worst 7.11%. "No fill" on every page; widest solid band 0.00 in. The refresher box and Fig 6.4 are outline only |
| Binding | PASS. `audit_binding.py` OK for 8 + 2 pages |
| Thumb tab | PASS. Outline only, 0.220 in from the outside edge on all 8 pages |
| Coloured type | PASS. Same palette as Round 1 (primaryDeep accent, label and footer greys; the key adds keyInk pen and pencil) |
| Clipped text / margins | PASS. No span crosses the outside margin on any page (the key-p1 handwriting overrun from Rounds 1–2 is gone after the reflow). No line ends in a bare suffix hyphen |
| Banned-content grep | PASS (no hits) |
| Codes | PASS. Chip `U06 / S6.1–S6.4`; `validate_codes.py` OK |
| Key notes | Accurate: refresher note (sections, builds-on, unbolded cation/anion), element-vs-ion note (NaCl₂ misconception; Naming Toolkit seven; Fig 6.4 eight anions). Earlier notes unchanged |

## R3-6. U7 regression

I rebuilt U7 at `041566b` into the scratchpad and compared it with `build/chem_u07_reading/` (student `e52e57c9…`, key `e7d21724…`, the same hashes as in Round 2). DOCX files match part for part; PDFs have identical text and 0 differing pixels on 8 + 2 pages. **U7 is unchanged**, including its printed-definition reverse (`vocabMode: print`).

## R3-7. Findings

| # | Page / item | Claim | Evidence / result | Severity | Disposition |
|---|---|---|---|---|---|
| R3-1 | p1 refresher item 2; p3 "Main-group ions have the charges listed in the Key Refreshers" | Main-group charge list | The list omits aluminum, Al³⁺ (Group 13), which 3.7 teaches (U3 quiz l.61) and deck slide 16 lists. Not wrong: Al³⁺ is stated where it is used ("In aluminum oxide, aluminum forms Al³⁺", p4). But 6.3 now sends students to a list that lacks it | Minor | Designer's choice: add "aluminum is 3+" to item 2 if it stays on one line, or leave as is |
| R3-2 | p3 element-vs-ion paragraph | "That subscript 2 … never carries over to the ion inside a compound" | True for the monatomic ions under discussion. The students' sheet 6 lists peroxide, O₂²⁻ (unstarred), which a literal reader could take as a counterexample | Minor | Optional: "…never carries over to a monatomic ion…" |
| A-3 | External locators (now also Cl₂ gas, soft Na) | — | Hosts still refused (proxy 403); the new facts are standard, low risk | OPEN, recorded limitation | Matt accepts on the record, or allow the hosts and recheck |
| A-6 | p3 On Your Own 6.2, phosphite | — | Unchanged | OPEN, minor | Matt to confirm Option A |
| A-10 | Fig 6.5/6.6 adjacency | — | Resolved by the reflow | CLOSED | — |

## R3-8. Release note

QA passes on student `4f2814f5…` / key `c5002297…`. The edition can go to the ordinary approval-to-file gate, with A-3 and A-6 carried on the record and R3-1/R3-2 at the designer's discretion. If the designer applies R3-1 or R3-2, the change is text-only on p1/p3. I would then recheck those pages, pagination, and the leaf position.

---

# Round 4: recheck after the stacked cover

Auditor | 2026-11-25 | Same workflow (including SHULL-CHG-0117 and SHULL-CHG-0118). Report only: no deliverable, spec or other file was changed.

## Verdict: **PASS**

- **The stacked cover is in the confirmed order** and every claim on it traces to a source.
- **The charge table matches 3.7**, and R3-1 (aluminum) and R3-2 ("a monatomic ion") are fixed.
- **The How to Use steps match the actual tear-off**, and both changed key notes are accurate.
- **The p2–p5 reflow changed no wording besides R3-2**, and no figure is separated from its reference.
- **p6–p8 are pixel-identical to Round 3.** The leaf, ink, fonts, binding, thumb tab and U7 regression all pass.
- **Four minor or info items (R4-1 to R4-4) are recorded below; none blocks release.** A-3 (sources unreachable) and A-6 (phosphite) stay open as before.

## R4-1. Version and evidence reuse

| Item | Value |
|---|---|
| Commit | `0947c27` (HEAD), "U6 reading: stacked cover…; R3-2 wording". It changes the builder (`front.layout`: `stacked` default, or `columns`), the U6 spec, and the U7 spec (pins `layout: columns`) |
| Student PDF | sha256 `0cdc631632ed9df76b04e7a47bb3e4bb1004ffca118128c5b3125b957ecdecdf`, 8 pp. DOCX `03c9add6…8b857` |
| Key PDF | sha256 `b384a4e7778bd4000af534dc39257498359f5759c7acee9975cbe62dd24c0798`, 2 pp. DOCX `56148586…f336fef` |
| Round 3 baseline | `scratchpad/old/` student `4f2814f5…` and key `c5002297…`, identical to the Round 3 export |
| Rebuild at HEAD | U6 rebuilt into the scratchpad. Both DOCX files match the shipped ones part for part; both PDFs have identical text and 0 differing pixels |
| My diff, Round 3 → Round 4 | **p6, p7, p8: text identical and 0 differing pixels.** Round 3 evidence is reused for them. p1–p5 and both key pages changed. A word-sequence diff over the whole student PDF shows the only text changes are: the new cover (shortened Why It Matters, How to Use, the charge table) and "the ion" → "a monatomic ion" (p3). Everything else in p2–p5 is the same words in the same order, only reflowed. Key: two notes changed (R4-3) |
| Proof method | Screen proof only (110 dpi full-page grayscale; a 220 dpi crop of the refresher table). No physical photocopy |

## R4-2. Cover

| Check | Result |
|---|---|
| Order (Matt, 2026-11-25, recorded in the spec `$comment`) | PASS: title → Why It Matters → In This Unit → Key Refreshers → How to Use This Reading → 6.1. Single column; blocks separated by rules |
| Why It Matters | "The box in your kitchen says baking soda. The FDA lists it as sodium bicarbonate, and a chemist may call it sodium hydrogen carbonate. All three names mean one compound, NaHCO₃. A systematic name tells you which ions it contains and in what ratio, so you can write its formula." Four lines. The FDA claim traces to dossier WIM-a (21 CFR 184.1736, S; primary still refused, A-3). Science correct. HCO₃⁻ is no longer printed (see the key note, R4-3) |
| In This Unit | PASS. 6.1–6.4 with titles verbatim from DECISIONS l.50–52 |
| How to Use, step 1: "Read one section at a time, with a pencil and your Polyatomic Ions, Naming Toolkit and Metals with Multiple Charges sheets." | PASS. These are sheets 6, 7 and 8 (DECISIONS l.205–217) |
| Step 2: "Each term in **bold** is defined where it first appears." | PASS. Ten bold body terms, each with its definition in the sentence |
| Step 3: "Tear off the last sheet. Answer its four questions, write the ten definitions, and turn it in." | PASS. p7 has four questions (6.1–6.4); p8 lists ten terms with write-in lines (SHULL-CHG-0118); the leaf is the last physical sheet |
| Line length | Why It Matters and How to Use wrap at about 70 characters. Refresher items are single lines at 9 pt (rule-mandated one-liners) |

## R4-3. Key Refreshers (SHULL-CHG-0117), the charge table and the box question

| Check | Result |
|---|---|
| Placement | PASS. After the section list and Why It Matters, before 6.1 |
| Count / form | PASS. Three items, each led by "Unit N (N.n):": "Unit 3 (3.7):", "Unit 3 (3.7):", "Unit 4 (4.2, 4.3):". Items 1 and 3 are single lines, unchanged from Round 3 and traced there (U3 quiz 3.7; deck slides 16, 22; U4 deck l.170–186) |
| Item 2 with inline table | Lead line "Main-group ion charges follow the group:" followed by a one-row table: GROUP 1 / 2 / 13 / 15 / 16 / 17 → CHARGE 1+ / 2+ / 3+ / 3− / 2− / 1−, with "aluminum (Al³⁺)" under 13. **Every value is correct** and matches 3.7: U3 quiz 3.7 solutions (`chem_u03_quiz.json` l.61, 113, 192: Sr²⁺ group 2, Br⁻ 17, Al³⁺ 13, K⁺ 1, S²⁻ 16, N³⁻ 15, Rb⁺, Se²⁻, P³⁻) and U6 deck slide 16 ("Group 1 +1, Group 2 +2, Aluminum +3 … Group 17 −1, Group 16 −2, Group 15 −3"). Tying 13 to aluminum specifically is right: it avoids implying that boron forms B³⁺. The table is live text (Archivo 9 pt; the note is 8 pt with a 4.6 pt superscript), outline only, and legible in grayscale. **R3-1 is closed.** See R4-1 on the "one-line" wording |
| Reminders only | PASS. No teaching sentence, example or bold term. The lead-ins are grey label type |
| Tear-off independence | PASS (p7 unchanged; no question draws on a refresher) |
| One fact, one place | PASS. 6.3 still points to the refreshers ("Main-group ions have the charges listed in the Key Refreshers on page 1"), and the list now includes aluminum |
| **Designer's question: rules, not an outlined box** | **Acceptable.** SHULL-CHG-0117 asks for a "short Key Refreshers block", not a box. On the stacked cover every block (Why It Matters, In This Unit, Key Refreshers, How to Use) uses the same treatment: a letterspaced label kicker and a rule above and below. The block is clearly separated in grayscale by its "KEY REFRESHERS" label and rules. Uniform treatment avoids giving one cover block more visual weight than the others. Ink and no-fill rules are unaffected either way |

## R4-4. Reflow (p2–p5) and R3-2

| Check | Result |
|---|---|
| R3-2 | p3 now reads "That subscript 2 belongs to the element. It never carries over to a monatomic ion inside a compound: sodium chloride is NaCl, not NaCl₂." Correct; the peroxide reading is excluded. **CLOSED** |
| Figure adjacency | PASS. Fig 6.1: p1, beside its reference in the same section. Fig 6.2: p2, directly under "Which naming system?" (reference). Figs 6.3 and 6.4: p3, each under its reference. Fig 6.5: p4, under "Writing the formula". Fig 6.6: p4, under its reference with Example 6.3 above. Fig 6.7: p5, under its reference. Numbering 6.1–6.7 is in order; all cross-references are correct |
| Splits | No Example, On Your Own or Connection box is split across a column or page. 6.4 now starts at the top of p5. Only prose sentences cross page boundaries. One margin note is separated; see R4-2 in the table below |
| Clipped text / margins | PASS. No span crosses the outside margin on any page of either PDF. No line ends in a bare suffix hyphen |
| Science | Unchanged wording, re-read on the reflowed pages; all as verified in Rounds 1–3 |

## R4-5. Key notes

| Note | Result |
|---|---|
| Key Refreshers note: "…three one-line reminders from 3.7 Ion Formation and 4.2/4.3 … The main-group charges are stated only in the refresher, as a small group/charge table that includes Group 13, aluminum (Al³⁺), and Section 6.3 points back to it." | Accurate as to content and sources. "One-line" sits slightly oddly beside "table" (see R4-1) |
| Phosphite note: "Carbonate → hydrogen carbonate was not used because sodium hydrogen carbonate, NaHCO₃, is named in Why It Matters." | Accurate for the shortened Why It Matters (it names sodium hydrogen carbonate and NaHCO₃; it no longer prints HCO₃⁻) |
| Everything else in the key | Unchanged text: tear-off answers, On Your Own solutions, and the ten expected definitions matching the reading word for word (Round 3). It reflowed: key p1 now ends after tear-off 6.1, and p2 carries 6.2–6.4, the solutions and the vocabulary. Nothing clipped |

## R4-6. Leaf and gate re-run

| Check | Result |
|---|---|
| Leaf | Reading ends on **p5**; **p6** blank back; leaf **p7/p8**. All three are pixel-identical to Round 3, so Round 3's leaf evidence holds: NAME line; exact due line; four single-part questions 6.1–6.4; ten write-in terms with no printed definitions; key definitions match the reading; long-edge orientation. Removing p7/p8 keeps all reading content |
| Fonts | PASS. Student: ArchivoRoman Regular and Bold, plus ArchivoNarrow; `audit_fonts.py` OK. Key: `--key` OK |
| Ink | PASS. Student worst 7.57% (p3), average 4.34%; key worst 6.74%. "No fill" on every page; widest solid band 0.00 in |
| Binding | PASS. `audit_binding.py` OK for 8 + 2 pages |
| Thumb tab | PASS. Outline only, 0.220 in from the outside edge on all 8 pages |
| Coloured type / codes / banned grep | PASS. Same token palette; chip `U06 / S6.1–S6.4`; `validate_codes.py` OK; banned list: no hits |

## R4-7. U7 regression

`build/chem_u07_reading/` (student `e52e57c9…`, key `e7d21724…`, unchanged since Round 2) was compared with `scratchpad/u7_before/`, `scratchpad/u7_after/` and my own HEAD rebuild. **All three match exactly** (DOCX part for part; PDF text identical and 0 differing pixels, 8 + 2 pages). The `layout: columns` pin keeps U7's two-column cover.

## R4-8. Findings

| # | Page / item | Claim | Evidence / result | Severity | Disposition |
|---|---|---|---|---|---|
| R4-1 | p1 refresher item 2 | SHULL-CHG-0117 "two to five one-line items" | Item 2 is a one-line lead plus an inline one-row data table and a note: about three printed lines. It is still a single reminder with no teaching, and the coordinator relayed the table as the answer to R3-1. I judge it within the rule's intent and pass it. It is the one place where the cover departs from the letter of "one-line" | Minor | Accept on the record. If Matt wants the letter of the rule, the fallback is Round 3's single text line with ", Group 13 (aluminum) is 3+" added |
| R4-2 | p1 → p2 | Margin note "Molecular compound — …" | The bold in-text definition is on p1 (last lines of the right column). Its optional margin note was pushed to the top of p2, the back of the same sheet. The definition itself is not separated, since the workflow keeps the definition in the prose | Minor | Optional: keep the margin note with its paragraph |
| R4-3 | p1, 6.1 left column | Column fill | The left column ends about 1.3 in early because Fig 6.1 did not fit under the first paragraph and moved to the top of the right column. Reading order is still correct, and the figure sits beside its reference | Nice-to-have | Optional |
| R4-4 | Builder, `front.layout` default | Cover layout for future readings | The builder now defaults every new reading spec (any course) to the stacked cover, attributed to Matt, 2026-11-25. The recorded decision is U6's cover. Whether it is the default for all Chemistry, Physics and Geology readings is a cross-course design choice (CLAUDE.md §2 test). U7 is pinned and unchanged | Info (process, not this deliverable) | Overseer: confirm with Matt that "stacked by default" is meant for all readings, or record it through change control |
| R3-1 | Refresher charges | Aluminum | Now in the table | CLOSED | — |
| R3-2 | p3 | "a monatomic ion" | Applied | CLOSED | — |
| A-3 | External locators | — | Unchanged; hosts refused (proxy 403) | OPEN, recorded limitation | As before |
| A-6 | p3 On Your Own 6.2, phosphite | — | Unchanged | OPEN, minor | Matt to confirm Option A |

## R4-9. Release note

QA passes on student `0cdc6316…` / key `b384a4e7…`. Any filing-queue status set after Round 3 should now point at these hashes. The edition can go to the ordinary approval-to-file gate, with A-3 and A-6 carried on the record. R4-1 to R4-3 are at the designer's or Matt's discretion; R4-4 goes to the Overseer.

---

# Round 5: full-document review after the chapter-opener cover (SHULL-CHG-0120)

Auditor | 2026-11-26 | Workflow as amended by SHULL-CHG-0120: item 1's Key Refreshers paragraph (b), Cover layout paragraph (a), and the Key Refreshers audit bullet (c), `workflows/unit-textbook.md` l.17, l.19, l.56. SHULL-CHG-0120 is APPROVED, with the user's decision recorded 2026-11-26, including "Just 'short'" for refresher length. Report only: no deliverable, spec or other file was changed.

## Verdict: **PASS**

- **The cover meets 0120 (a), (b) and (c)** clause by clause.
- **Reflow:** every page was re-inspected. No figure is separated from its reference, no box is split, all cross-references are correct, and the only white-space gaps are column-bottom gaps from keeping headings with their first paragraph.
- **Content:** no student-facing wording changed outside the cover's headings; the science is as verified in Rounds 1–4.
- **How to Use and the key:** the steps match the actual leaf, and the changed key note is accurate.
- **Gate:** the leaf, ink, fonts, binding and thumb tab pass. The filed U7 artifacts are untouched, and its PDF output is unchanged.
- **Two findings, neither blocking:** a nice-to-have (R5-1) and an info note on the U7 DOCX (R5-2). A-3 (sources unreachable) and A-6 (phosphite) stay open as before.

## R5-1. Version and evidence reuse

| Item | Value |
|---|---|
| Commit | `d11bf4f` (HEAD of `claude/ecstatic-pascal-9cro1w`), "SHULL-CHG-0120 (builder): chapter-opener cover as default…; U6 rebuilt". Preceded by `aa60728` (workflow text) and `23f4e74` (decision record) |
| Student PDF | sha256 `85b86d2bc5c1d39558b2379e142d175e256e9d2b0832e9c5c51f147ea481f95d`, 8 pp. DOCX `a55738e2…4ebc17` |
| Key PDF | sha256 `c7ce54557fe9a067ad55ece37ddec3934c726cbd4b70bdbea0aa537dbb6125d8`, 2 pp. DOCX `8454ab0d…ee122` |
| Rebuild at HEAD | U6 rebuilt into the scratchpad. Both DOCX files match the shipped ones part for part; both PDFs have identical text and 0 differing pixels |
| My diff against Round 4 (my R4 HEAD rebuild, identical to the R4 export) | **p5, p6, p7, p8 and key p2: text identical and 0 differing pixels.** p1–p4 changed. A whole-document word diff shows the only text changes are cover furniture: the "UNIT 6" numeral; the "BEFORE YOU BEGIN ·" prefix on the refresher heading; the How to Use label shortened from "HOW TO USE THIS READING"; and step numbers set as numerals. Key p1 has one changed note. **No body wording changed on p1–p4.** It only reflowed |
| Coverage | Full document: p1–p8 and key pp. 1–2 inspected rendered. p1–p4 and key p1 were read in full again. Rounds 1–4 content evidence (science, sources, leaf) is reused for text that is unchanged by word diff, and for pages that are pixel-identical |
| Proof method | Screen proof only (110 dpi full-page grayscale; vector geometry measured with PyMuPDF). No physical photocopy |

## R5-2. Cover against SHULL-CHG-0120

| 0120 clause | Edition | Result |
|---|---|---|
| (a) Title block: large "Unit" numeral and a thick vertical course rule beside the display title | "UNIT" letterspaced label over a large "6" (primaryDeep, about 41 pt tall). A **2.25 pt** vertical rule in course display orange (#FF6B1A; 1 pt elsewhere) at x 105 pt, 64 pt tall. Display title "Chemical Nomenclature" 34 pt, accent word in primaryDeep | PASS. The rule reads as mid-grey in grayscale and is clearly heavier than the 1 pt box rules |
| (a) Why It Matters: unboxed intro, about four lines, slightly larger than body | Unboxed; 11.5 pt (body 10.5 pt); five lines at this measure; same text as Round 4 (FDA claim → dossier WIM-a) | PASS ("about four"). See R5-1 |
| (a) Outlined In This Unit box beside it on the right | Outlined box at x 392–577 pt, 1 pt display-orange outline, no fill; 6.1–6.4 with titles verbatim from DECISIONS l.50–52 | PASS. It stays inside the 0.50 in outside margin (box right edge 576.6 pt; thumb tab starts at 581.8 pt) |
| (a) One full-width outlined Key Refreshers box; each refresher in its own column; hairlines between columns | Box x 43–577 pt (full text width), 1 pt orange outline, no fill. Three columns separated by 0.75 pt ruleHairline verticals; the charge table has its own (wide middle) column | PASS |
| (a) How to Use: a single quiet row of 1–4 short numbered steps describing the reading and tear-off as printed, just above the first section | One row: grey "HOW TO USE" label plus three numbered steps in small type, directly above "6.1 Covalent Names & Formulas". Step 1: read one section at a time with a pencil and sheets 6–8 (DECISIONS l.205–217). Step 2: bold terms are defined where they first appear (true: the ten bold terms, each defined in its sentence). Step 3: "Tear off the last sheet. Answer its four questions, write the ten definitions, and turn it in." True: the leaf is the last sheet (p7/p8), with four questions on p7 and ten write-in terms on p8 | PASS |
| (a) Then the first section; outlines and rules only, no fills | 6.1 follows; `audit_print_ink.py` "no fill" on p1 (the only filled shapes are type glyphs) | PASS |
| (b) Heading may read "Before You Begin · Key Refreshers" | "BEFORE YOU BEGIN · KEY REFRESHERS" | PASS |
| (b)/(c) Two to five items, each one short reminder opening "Unit N (N.n):", may wrap within its column | Three items: "Unit 3 (3.7):" cations/anions (three lines in its column); "Unit 3 (3.7):" main-group charges plus the group/charge table (1+, 2+, 3+ with "aluminum (Al³⁺)", 3−, 2−, 1−); "Unit 4 (4.2, 4.3):" transfer (ionic) vs share (covalent) (three lines). All are short. Sections exist (DECISIONS l.38, l.43). Sources as traced in Rounds 3–4: U3 quiz 3.7 l.58–72, 113, 192; U6 deck slides 16 and 22; U4 deck l.170–186 | PASS. Round 4's R4-1 ("one-line") is **closed**: 0120 removed the one-line limit, and the table item is within "short" |
| (c) No bold term, teaching or example; no tear-off question draws on it | Lead-ins are grey labels; no bold body terms; p7 unchanged (6.1 prefixes, 6.2 -ate/-ite, 6.3 Roman numeral, 6.4 acid endings) | PASS |

## R5-3. Reflow, page by page

| Page | Check | Result |
|---|---|---|
| p1 | Fig 6.1 | In the left column directly under its reference ("…CO₂ (Figure 6.1)"), caption intact. The right column continues 6.1: bold "binary compound" and "molecular compound" with both margin notes **beside their paragraph** (Round 4's R4-2 is closed). The left column is now full (R4-3 closed). The right column ends about 1.2 in early because "Naming with prefixes" was kept with its first paragraph and moved to p2 (R5-1) |
| p2 | Fig 6.2; Example 6.1; On Your Own 6.1 | Fig 6.2 is at the top of the right column, beside "Which naming system?… (Figure 6.2)" at the foot of the left column, on the same page. Example 6.1 and On Your Own 6.1 boxes are whole. Connection 6.1 is whole. The 6.2 heading is kept with its first paragraph |
| p3 | Figs 6.3, 6.4; Example 6.2; On Your Own 6.2; Connection 6.2 | Each figure sits under its reference. The boxes are whole (Example 6.2 left; On Your Own 6.2 and the Connection at the top of the right column). The 6.3 heading is kept with "Naming monatomic ions" |
| p4 | Figs 6.5, 6.6; Example 6.3; On Your Own 6.3; Older Names; Connection 6.3 | Fig 6.5 is under "Writing the formula… (Figure 6.5)". Fig 6.6 (right column) is beside its reference at the foot of the left column. All boxes are whole. The right column ends about 1.6 in early because 6.4's heading is kept with its first paragraph on p5 (R5-1) |
| p5 | 6.4 at top; Fig 6.7; Example 6.4; On Your Own 6.4; Connection 6.4 | Pixel-identical to Round 4; verified there |
| All | Figure numbering / cross-references | Fourteen "Figure 6.n" strings: each of 6.1–6.7 appears once in the prose and once as a caption, in order and on the same page |
| All | Clipping / margins / hyphen splits | No span crosses the outside margin in either PDF; no line ends in a bare suffix hyphen |

## R5-4. Key

| Item | Result |
|---|---|
| Changed note: "Key Refreshers (cover, SHULL-CHG-0117) are three short reminders, one per column of the Before You Begin box, from 3.7 Ion Formation and 4.2/4.3 … as a small group/charge table that includes Group 13, aluminum (Al³⁺), and Section 6.3 points back to it." | Accurate for the printed cover. The Round 4 "one-line beside table" oddity is gone |
| Everything else | Key p2 is pixel-identical to Round 4. Key p1's other notes and tear-off answer 6.1 are unchanged text, reflowed. Tear-off answers, On Your Own solutions and the ten expected definitions still match the student pages (verified in Round 3, unchanged since) |

## R5-5. Leaf and gate

| Check | Result |
|---|---|
| Leaf | Reading ends on **p5**; **p6** blank back; leaf **p7/p8** (pixel-identical to Rounds 3–4). NAME line; exact due line; four single-part questions 6.1–6.4; ten write-in terms, no definitions printed, each traced to its bold definition; key definitions match the reading; long-edge orientation. Removing p7/p8 keeps p1–p6, which hold all reading content |
| Fonts | PASS. `pdffonts`: ArchivoRoman Regular and Bold, plus ArchivoNarrow; `audit_fonts.py` OK; key `--key` OK |
| Ink | PASS. Student worst 7.36% (p3), average 4.36%; key worst 6.80%. "No fill" on every page; widest solid band 0.00 in |
| Binding | PASS. `audit_binding.py` OK for 8 + 2 pages |
| Thumb tab | PASS. Outline only, 0.220 in from the outside edge on all 8 pages; clear of the In This Unit box |
| Colour | PASS. Accent type primaryDeep #B84100 only; display orange #FF6B1A only on rules and outlines; greys are tokens |
| Codes / banned grep | PASS. `U06 / S6.1–S6.4`; `validate_codes.py` OK; banned list: no hits |

## R5-6. U7 regression

| Comparison | Result |
|---|---|
| Filed U7 artifacts (`build/chem_u07_reading/`, student `e52e57c9…`, key `e7d21724…`; filed 2026-11-25 per `reports/filing-queue.md`) | Unchanged on disk (timestamps 2026-11-24) |
| HEAD rebuild of U7 (spec pins `layout: columns`) vs the filed files | **PDF:** student and key text identical, 0 differing pixels (8 + 2 pages). **Key DOCX:** identical part for part. **Student DOCX:** `word/document.xml` differs. The rebuild adds `<w:keepLines/>` to five paragraphs (the new "section head keeps with its first paragraph" rule). LibreOffice renders it identically. See R5-2 |

## R5-7. Findings

| # | Page / item | Claim | Evidence / result | Severity | Disposition |
|---|---|---|---|---|---|
| R5-1 | p1 right column, p4 right column; Why It Matters length | White space and length | Keeping headings with their first paragraph leaves about 1.2 in (p1) and about 1.6 in (p4) empty at the foot of the right column. Nothing is separated and reading order is clear. Why It Matters is five lines against "about four" | Nice-to-have | Optional. Accept as is |
| R5-2 | U7 DOCX (process note) | Commit message: "U7 (columns) output unchanged" | True for the PDFs (0 px) and the key DOCX. A U7 student DOCX rebuilt today would differ from the filed one by five `keepLines` flags. Pagination is the same in LibreOffice; Word may paginate differently. The filed U7 files are not touched | Info | No action unless U7 is rebuilt; then re-check its pagination |
| R4-1 | Refresher "one-line" | — | The rule is now "short" (0120 (b)) | CLOSED | — |
| R4-2 / R4-3 | p1 margin note; p1 left column | — | Both resolved by the reflow | CLOSED | — |
| R4-4 | Builder default cover for all readings | — | Now governed by SHULL-CHG-0119/0120 (all three courses, approved) | CLOSED | — |
| A-3 | External locators | — | Unchanged; hosts refused (proxy 403) | OPEN, recorded limitation | As before |
| A-6 | p3 On Your Own 6.2, phosphite | — | Unchanged | OPEN, minor | Matt to confirm Option A |

## R5-8. Release note

QA passes on student `85b86d2b…` / key `c7ce5455…`. The filing-queue row should point at these hashes, not Round 4's. The edition can go to the ordinary approval-to-file gate, with A-3 and A-6 carried on the record.
