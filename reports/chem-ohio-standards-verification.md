# Chemistry — Ohio Learning Standards code verification

Prepared by: researcher | Date: 2026-11-23 | Status: RECOMMENDATIONS ONLY. Nothing in `brand/`,
`standards/`, `governance/`, `courses/` or `templates/` was edited.

## 0. Bottom line

**No code below is confirmed from a primary source.** The official ODEW PDF could not be opened from
this session. Every code and title in this report is **UNVERIFIED**. Each one is tagged with how much
secondary support it has. Do not print standard codes on a student-facing Unit Roadmap until someone
checks them against the ODEW PDF.

## 1. Source access log

| Host / source | Tool | Result |
|---|---|---|
| `education.ohio.gov` (official PDF `SciFinalStandardsMC060719.pdf.aspx`) | WebFetch | **FAILED.** `getaddrinfo ENOTFOUND`: the host is outside this session's allowed network domains |
| `www.commonplanner.com` (third-party aggregator) | WebFetch | **FAILED.** `ENOTFOUND`, same cause. No more hosts were tried, per the session's network rule |
| WebSearch result snippets (search engine summaries of the ODEW PDF, us.alonot.com copy, lab-aids.com, chemquiz.net, commonplanner) | WebSearch | Worked. **Secondary only:** these are summarised snippets, not the document text |
| Google Drive (`SHULL Science`) | Drive search | No copy of the Ohio standards found |
| Repository | Grep | No OLS text in the repo. The only codes are in `chem_u06.json`, `output/chemistry/u06/Unit 6 Roadmap.html`, and report F3 in `reports/u2-content-briefs.md` (2026-10-04, also NOT VERIFIED) |

**Primary source to check against, once it is reachable:** Ohio's Learning Standards and Model
Curriculum for Science. Standards adopted February 2018; model curriculum adopted May 2019. The
Chemistry section reportedly starts at about p. 259.
https://education.ohio.gov/getattachment/Topics/Learning-in-Ohio/Science/Assessments-in-Science/SciFinalStandardsMC060719.pdf.aspx?lang=en-US
Landing page: https://education.ohio.gov/Topics/Learning-in-Ohio/Science/Ohios-Learning-Standards-and-MC

**Is a later revision in force?** Search found no evidence that Ohio adopted revised science
standards after 2018/2019. The 2025–2026 revisions found were in Technology, Physical Education and
ELA. One unofficial page claimed a 2023 science revision. It conflicts with ODEW's own dating and is
not relied on. **UNVERIFIED:** confirm on the ODEW science landing page.

## 2. Chemistry content statements: best available list (all UNVERIFIED)

Support key: **S2** = the code, title and sub-points appeared together in a snippet that quotes the
2018 text. **S1** = the code and title were seen, but the sub-points were not fully seen. **S0** = the
sub-points come only from my background knowledge of the 2011 or 2018 syllabus, with no snippet.

| Code | Strand | Title | Sub-points | Support | Notes |
|---|---|---|---|---|---|
| C.PM.1 | Structure and Properties of Matter | Atomic structure | Evolution of atomic models/theory; Electrons; Electron configurations | S2 | Snippet quoting the commonplanner copy: the elaboration covers "protons, neutrons and electrons, atomic number, mass number, cations and anions, isotopes and the strong nuclear force". Average atomic mass from isotope abundance appears in an aggregator's sub-objective (C.PM.1.RAS.c), not confirmed as ODEW wording |
| C.PM.2 | Structure and Properties of Matter | Periodic table | Properties; Trends | S1 (title) / S0 (sub-points) | |
| C.PM.3 | Structure and Properties of Matter | Chemical bonding | Ionic; Polar/covalent (snippet wording); Metallic and Polyatomic ions (S0) | S1 | Only "ionic and polar/covalent" was seen in a snippet. "Metallic" and "polyatomic ions" are not confirmed for 2018 |
| C.PM.4 | Structure and Properties of Matter | Representing compounds | Formula writing; Nomenclature; Models and shapes (Lewis structures, ball and stick, molecular geometries) | **S2** | Snippet quote: "C.PM.4: Representing compounds • Formula writing • Nomenclature • Models and shapes (Lewis structures, ball and stick, molecular geometries)" |
| C.PM.5 | Structure and Properties of Matter | Quantifying matter | Sub-points not retrieved. S0 recollection: significant figures, SI units, dimensional analysis, mole concept, molar mass, percent composition, empirical/molecular formulas | S1 (title) / S0 (sub-points) | Do not print the sub-points |
| C.PM.6 | Structure and Properties of Matter | Intermolecular forces of attraction | Types and strengths; Implications for properties of substances (melting and boiling point, solubility, vapor pressure) | S2 | The 2011 numbering used C.PM.7 "Intermolecular chemical bonding". Do not mix the two versions |
| C.IM.1 | Interactions of Matter | Chemical reactions | Types of reactions; Kinetics; Energy; Equilibrium; Acids/bases | S2 | |
| C.IM.2 | Interactions of Matter | Gas laws | Pressure, volume and temperature; Ideal gas law | S2 | |
| C.IM.3 | Interactions of Matter | Stoichiometry | "Molecular [sic? possibly 'Molar'] calculations"; Solutions; Limiting reagents | S2 (wording doubtful) | Check the first sub-point wording against the primary source |

**Is "C.PM.1 / C.PM.2 / C.IM.1" a real scheme?** Probably yes. Multiple independent secondary
sources use exactly this scheme for the 2018 syllabus: C.PM.1–C.PM.6 and C.IM.1–C.IM.3, nine
statements in all. **UNVERIFIED** against the primary source.

**Inquiry strand:** secondary sources say the 2018 high school syllabi carry a "Science Inquiry and
Application" expectation. The chemistry section reportedly also has a "Scientific Inquiry, Practice
and Applications" category adapted from the NGSS nature-of-science appendix. ODEW's FAQ reportedly
says HS science courses must be inquiry-based with lab experience. I did not see a code letter for
the inquiry strand. **UNVERIFIED. Do not invent a code** for it.

**Nuclear chemistry:** no snippet places radioactive decay, nuclear equations, half-life or
fission/fusion in any chemistry content statement. The C.PM.1 elaboration reportedly mentions only
isotopes and the strong nuclear force. Where nuclear decay lives in the 2018 HS standards (Physical
Science or Physics syllabus?) is **UNVERIFIED**.

## 3. Unit mapping to the DECISIONS.md curriculum map (PROPOSED, all codes UNVERIFIED)

This mapping is my inference from the titles and sub-points above. It is not an ODEW alignment.
Retired codes 1.4, 3.5, 6.5 and 6.6 are skipped.

| Unit | Section(s) | Main | Support | Confidence / note |
|---|---|---|---|---|
| U0 | 0.1 Equipment, 0.2 Safety | none | Inquiry/SIA (no code) | No chemistry content statement covers lab safety or equipment |
| U0 | 0.3 Lab & basic skills, 0.4 Observations | Inquiry/SIA (no code) | C.PM.5 (measurement, if sig figs/SI are taught) | Depends on C.PM.5 sub-points (S0) |
| U1 | 1.1 Matter & Changes | none found | C.PM.6 (properties) at a stretch | Classification of matter / physical vs chemical change was not seen in any chemistry statement. Possibly Physical Science (UNVERIFIED) |
| U1 | 1.2 History of Atomic Model | C.PM.1 | — | Sub-point "Evolution of atomic models/theory" (S2) |
| U1 | 1.3 Atomic Structure (incl. isotopes) | C.PM.1 | — | Elaboration reportedly names isotopes |
| U1 | 1.5 Average Atomic Mass | C.PM.1 | C.PM.5 | Aggregator sub-objective only |
| U2 | 2.1–2.4 | C.PM.1 | 2.4 → C.PM.3 (valence e⁻ → bonding) | "Electrons; Electron configurations" (S2) |
| U2 | 2.5 Atomic & Electron Spectra | C.PM.1 | — | Under "Electrons". Exact elaboration not seen |
| U3 | 3.1–3.6 | C.PM.2 | 3.6 → C.PM.1 | Title S1, sub-points S0 |
| U3 | 3.7 Ion Formation | C.PM.2 | C.PM.1, C.PM.3 | |
| U4 | 4.1–4.4 | C.PM.3 | C.PM.2 | "Metallic" sub-point is S0 |
| U4 | 4.5–4.6 Electronegativity, Bond Polarity | C.PM.3 | C.PM.2 | |
| U5 | 5.1–5.3 Lewis, VSEPR, Geometry | C.PM.4 | C.PM.3 | "Models and shapes (Lewis structures … molecular geometries)" (S2) |
| U5 | 5.4 Molecular Polarity | C.PM.4 | C.PM.3, C.PM.6 | |
| U5 | 5.5–5.6 IMFs, Structure & Properties | C.PM.6 | C.PM.4 | S2 |
| U6 | 6.1–6.4 | C.PM.4 | C.PM.3 (6.2–6.3); C.IM.1 (6.4) | "Formula writing; Nomenclature" (S2) |
| U7 | 7.1 Mathematical Tools | C.PM.5 | Inquiry/SIA | S0 sub-points |
| U7 | 7.2–7.7 | C.PM.5 | C.PM.4 (7.6–7.7 formulas) | S0 sub-points (mole, molar mass, % composition, empirical) |
| U8 | 8.1–8.4 | C.IM.1 | C.IM.3 (8.2 balancing, conservation) | "Types of reactions" (S2) |
| U9 | 9.1–9.4 | C.IM.1 | — | **Thermochemistry does have a home:** C.IM.1 "Energy" (S2) |
| U9 | 9.5 Spontaneity `EXT` | C.IM.1 (stretch) | — | Entropy/Gibbs is probably beyond the statement. Treat it as enrichment |
| U10 | 10.1–10.4 | C.IM.3 | C.PM.5 | "Limiting reagents" (S2) |
| U10 | 10.5 Theoretical & Percent Yield | C.IM.3 | — | Percent yield was not in the snippet's sub-point list |
| U11 | 11.2–11.6 | C.IM.2 | C.IM.3 (molar volume) | S2 |
| U11 | 11.1 Kinetic Molecular Theory | C.IM.2 | C.PM.6 | KMT not seen named. Inference |
| U12 | 12.1–12.3 | C.PM.6 | C.IM.3 | "Solubility" under C.PM.6 (S2) |
| U12 | 12.4 Electrolytes | C.PM.3 | C.IM.1 | Inference |
| U12 | 12.5–12.7 Molarity, Dilutions, Soln Stoich | C.IM.3 | C.PM.5 | "Solutions" under C.IM.3 (S2) |
| U13 | 13.1–13.2 | C.IM.1 | — | "Kinetics" (S2) |
| U13 | 13.3–13.5 | C.IM.1 | — | "Equilibrium" (S2) |
| U14 | 14.1–14.4 | C.IM.1 | — | "Acids/bases" (S2) |
| U14 | 14.5–14.6 Acid–base stoich, Titrations | C.IM.1 | C.IM.3 | |
| U15 | 15.1–15.6 Nuclear | **none found** | C.PM.1 (15.1 isotopes / nuclear force only) | No chemistry statement found for decay, half-life or fission/fusion. Label it "beyond the Ohio chemistry statements" or leave it blank until checked |

## 4. U6 spec check: `templates/unit-roadmap/specs/chem_u06.json`

| # | Item | Finding | Evidence | Verdict |
|---|---|---|---|---|
| 1 | C.PM.2 "Periodic table — properties and trends" | Code and title match secondary sources. "Properties; Trends" is S0 | Search snippets (§2) | **UNVERIFIABLE** (most likely correct) |
| 2 | C.PM.3 "Chemical bonding — ionic, polar/nonpolar covalent, metallic bonding; polyatomic ions" | Code and title match. **"nonpolar" was not seen.** The snippet reads "polar/covalent". "Metallic" and "polyatomic ions" were not seen in any 2018 snippet | Search snippets (§2) | **UNVERIFIABLE.** The key description may paraphrase beyond the official wording. Recommend using only the title until it is checked |
| 3 | C.PM.4 "Representing compounds — formula writing, nomenclature, models and shapes" | Matches the quoted snippet sub-points exactly | Snippet: "C.PM.4: Representing compounds • Formula writing • Nomenclature • Models and shapes (…)" | **UNVERIFIABLE** from the primary source. Strongest secondary support of the four |
| 4 | C.IM.1 "Chemical reactions — acids/bases" | Code, title and the "Acids/bases" sub-point match | Search snippets (§2) | **UNVERIFIABLE** (most likely correct). Mapping it as *support* for 6.4 acid naming is a judgment call. Acid naming itself is C.PM.4 nomenclature |
| 5 | `standards_source` "Ohio Learning Standards for Science (2018)" | The formal name appears to be "Ohio's Learning Standards for Science" (adopted Feb 2018; model curriculum May 2019) | Search snippets | Minor wording issue. UNVERIFIED |

## 5. Findings and recommendations

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| 1 | U6 Roadmap codes | Codes are printed on `output/chemistry/u06/Unit 6 Roadmap.html`, but none has been confirmed from a primary source | §1, §4 | **Blocking (for print)** | Hold the print, or remove the standards block, until the codes are checked against the ODEW PDF |
| 2 | Recurring pattern | This is the second time unverified Ohio codes have reached a build. The first was F3 in `reports/u2-content-briefs.md` (2026-10-04), which said "Do NOT print any standard code". There is no single authoritative home for OLS codes, so they end up written into individual specs | Grep of repo | High | Secretary to propose that one verified chemistry code list live in `courses/chemistry/DECISIONS.md`, with specs pointing at it. Builders would print no code that is absent from that list |
| 3 | Network access | `education.ohio.gov` is blocked in this session | §1 | High | Matt either allows `education.ohio.gov` in the session network settings, or drops the ODEW PDF into Drive. Then re-run this check (about 15 minutes) |
| 4 | C.PM.3 key wording | "nonpolar", "metallic" and "polyatomic ions" are unconfirmed | §4 #2 | Medium | Shorten the key to the title only until it is checked |
| 5 | U15 / U0 / U1.1 | No chemistry content statement was found for them | §3 | Low | Show "—" or "Course extension" on those Roadmaps rather than borrowing a code |
| 6 | Inquiry strand | Inquiry applies to all units, but no code letter was confirmed | §2 | Low | Do not print an inquiry code until it is verified |

## Sources (all secondary, reached through WebSearch snippets only)

- ODEW PDF (fetch blocked): https://education.ohio.gov/getattachment/Topics/Learning-in-Ohio/Science/Assessments-in-Science/SciFinalStandardsMC060719.pdf.aspx?lang=en-US
- ODEW landing page: https://education.ohio.gov/Topics/Learning-in-Ohio/Science/Ohios-Learning-Standards-and-MC
- ODEW Science FAQ: https://education.ohio.gov/Topics/Learning-in-Ohio/Science/Resources-for-Science/Frequently-Asked-Questions-for-Science
- Third-party copy of the 2018 Chemistry syllabus: https://us.alonot.com/wp-content/uploads/2025/02/Chemistry-Chemistry-Us-K12-Resources.pdf
- Commonplanner (aggregator, fetch blocked): https://www.commonplanner.com/standards/ohio-af084ca5/science/chemistry-content-statements-grades-9-12-94ab443e
- chemquiz.net alignment: https://chemquiz.net/docs/teachers/standards/ohio
- Lab-Aids Ohio Chemistry correlation: https://www.lab-aids.com/sites/default/files/2020-07/OH%20Chemistry%20Correlation%20v3.pdf
- Gizmos (2011 numbering, do not use): https://gizmos.explorelearning.com/find-gizmos/browse-by-standard-gizmos-listing?docId=2184
