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
