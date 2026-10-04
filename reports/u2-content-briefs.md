# Chemistry U2 "Electrons & Atomic Theory" — Accuracy-Verified Content Briefs

Prepared by: researcher | Date: 2026-10-04 | Status: RECOMMENDATIONS ONLY — nothing in `brand/`, `standards/`, `governance/`, `courses/` was edited.

Section codes confirmed in `courses/chemistry/DECISIONS.md` (lines 29-31): 2.1 The Bohr Model · 2.2 Energy Levels, Sublevels & Orbitals · 2.3 Electron Configurations · 2.4 Electron Stability & Valence Electrons · 2.5 Atomic & Electron Spectra. No U2 lab is confirmed in DECISIONS.md (only U0.3 and U0.4 are); no lab is invented below.

## 0. Cross-cutting flags (read first)

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| F1 | Scientific notation / math sequencing | E_n = -2.18e-18 J/n^2 needs scientific notation, but the course sequencing rule delays scientific notation and heavy math until later in the year (DECISIONS.md "Course sequencing rules"). | DECISIONS.md lines 106-108 | Medium | Keep S2.1 numeric work to a pre-built table plus ONE student calculation (n=1..4). Keep one wavelength calculation in S2.5, marked "calculator provided". Use 3 sig figs everywhere without teaching sig-fig rules (enforced from Q3). Matt to confirm. |
| F2 | Ion configurations in S2.4 vs U3.7 Ion Formation | Matt's instruction (precedence 1) puts ion CONFIGURATIONS in S2.4. DECISIONS.md titles do not say so. Risk of the same fact living twice. | Task instruction; DECISIONS.md line 36 | Medium | S2.4 owns "what the configuration of an ion is". U3.7 owns "why/which charge an element forms, energetics, ionic compounds". Suggest the Secretary record this boundary as a proposal. S2.4 slides must not predict charges beyond group-number pattern. |
| F3 | Ohio Learning Standards alignment | NOT VERIFIED. A web search snippet suggested the Ohio chemistry course uses codes such as "C.PM.1 / C.PM.2" for atomic structure and periodic table, but the primary source could not be opened (egress blocked) and no OLS text exists in the repo. | WebSearch result only; fetches blocked | Low | Do NOT print any standard code on a slide. Matt to supply codes, or approve a later verification pass. |
| F4 | Lab / demo content | Flame test, gas-discharge tubes, and spectroscope use are not confirmed U2 labs. | DECISIONS.md Open Question 4 | Low | Treat as PROVISIONAL teacher-notes suggestions only. Flame-test slides below cover the science, not a procedure. |
| F5 | Configuration writing order | Two conventions: filling order ([Ar]4s2 3d6) vs shell order ([Ar]3d6 4s2). Both are accepted in textbooks. | General chemistry convention | Low | Matt to pick one and use it on every slide. This brief uses FILLING ORDER for neutral atoms and states ions in the same order (Fe2+ = [Ar]3d6 is identical either way). |
| F6 | Scope boundaries | Mole/per-mole ionization energy, Lewis structures (S5.1), periodic trends (U3) and ionization energy (S3.4) are later. | DECISIONS.md lines 29-45 | Low | Do not use mol-based energy in U2. Lewis dot symbols are optional preview only in S2.4 (PROVISIONAL). |
| F7 | Pacing | 1.5-2 days per section (PROVISIONAL pacing). 14-18 content slides per section is at the high end of a 50-min period pair. | DECISIONS.md lines 298-306 | Low | Slides marked (opt) can be cut without breaking the section. |

### Verified constants used throughout (re-solved)

| Quantity | Value | Check |
|---|---|---|
| E_n (hydrogen) | -2.18e-18 J / n^2 (R_H = 2.178e-18 J) | n=1: -2.18e-18; n=2: -5.45e-19; n=3: -2.42e-19; n=4: -1.36e-19; n=5: -8.72e-20; n=6: -6.06e-20 |
| h | 6.626e-34 J s | |
| c | 3.00e8 m/s | hc = 1.99e-25 J m |
| ΔE, n=3 to 2 | 3.03e-19 J | 2.18e-18 x (1/4 - 1/9) = 2.18e-18 x 0.13889 |
| Wavelength, 3 to 2 | 656-657 nm (red); measured H-alpha 656.3 nm | 1.988e-25 / 3.028e-19 = 6.565e-7 m. Accept 656-657 depending on constants |
| Frequency, 3 to 2 | 4.57e14 Hz | 3.028e-19 / 6.626e-34 |
| ΔE, 4 to 2 | 4.09e-19 J, 486 nm (blue-green) | 2.18e-18 x 0.1875 |
| ΔE, 5 to 2 | 4.58e-19 J, 434 nm (blue-violet) | x 0.21 |
| ΔE, 6 to 2 | 4.84e-19 J, 410 nm (violet) | x 0.2222 |
| ΔE, 2 to 1 | 1.64e-18 J, 122 nm (ultraviolet) | x 0.75 |
| ΔE, 4 to 3 | 1.06e-19 J, about 1876 nm (infrared) | x 0.04861 |
| Ionization of H (n=1 to infinity) | 2.18e-18 J | E_infinity = 0 |
| Visible light | about 400-700 nm (rough HS convention; strict limits about 380-750 nm) | |

---

# S2.1 The Bohr Model

**1) Learning targets**
1. Describe Bohr's model of hydrogen: electrons in fixed circular orbits (stationary states) with fixed energies.
2. Use E_n = -2.18e-18 J / n^2 to find the energy of a hydrogen level and ΔE for a transition.
3. Explain emission (electron drops, photon leaves) and absorption (electron rises, photon absorbed) using quantized energy.
4. State the limits of the Bohr model (works quantitatively only for hydrogen-like one-electron species; replaced by the quantum-mechanical model).

**2) Vocabulary**: quantum / quantized, energy level, n (principal quantum number), ground state, excited state, photon, ΔE, emission, absorption, ionization (n to infinity), line spectrum (preview, owned by S2.5), electron cloud (preview of S2.2).

**3) Slide outline (16 content slides)**

| # | Slide | Content |
|---|---|---|
| 1 | Hook / question | Why does hydrogen give only a few colors of light, not a rainbow? (Sets up the problem without answering.) |
| 2 | Before Bohr | Thomson (electrons in positive material), Rutherford 1911 (dense nucleus, electrons outside). Problem: a classical orbiting charge should radiate energy and spiral into the nucleus. Bohr proposed his model in 1913. |
| 3 | Bohr's postulates | (a) Electrons move in fixed circular orbits with fixed energies; (b) an electron in an allowed orbit does not radiate; (c) it changes orbit only by absorbing or emitting a photon whose energy equals the difference between the two levels. |
| 4 | Quantized energy | Energy comes in specific values only. Staircase vs ramp analogy: you stand on stairs, never between. n = 1, 2, 3... |
| 5 | The equation | E_n = -2.18e-18 J / n^2. Hydrogen only (also one-electron ions such as He+ with an extra Z^2 factor; mention only as a limit). Why negative: electron bound to nucleus; E = 0 means free (n = infinity). More negative = lower energy = more stable. |
| 6 | Energy-level diagram | Table plus diagram of n = 1-6 with values from the constants table. Levels crowd together as n increases. |
| 7 | Worked example 1: energy of a level | Find E for n = 3. |
| 8 | Solution 1 | E_3 = -2.18e-18 / 3^2 = -2.18e-18 / 9 = -2.42e-19 J. Check: it is less negative than E_2 (-5.45e-19), so higher energy. |
| 9 | Ground vs excited state | n = 1 is hydrogen's ground state. Any higher n is an excited state, short-lived. |
| 10 | Absorption | Electron jumps up only if the photon energy equals exactly E_final - E_initial. Photons of the wrong energy pass through. |
| 11 | Emission | Electron drops from a higher to a lower level, emitting a photon with energy |ΔE|. Bigger drop = higher-energy photon. |
| 12 | Worked example 2: transition energy | Hydrogen electron drops from n = 3 to n = 2. Find ΔE and say whether energy is absorbed or released. |
| 13 | Solution 2 | ΔE = E_2 - E_3 = (-5.45e-19) - (-2.42e-19) = -3.03e-19 J. Negative sign = energy leaves the atom. Photon energy = 3.03e-19 J. (Wavelength/color of this photon is calculated in S2.5.) |
| 14 | Worked example 3: ionization | Energy to remove the electron from ground-state hydrogen. |
| 15 | Solution 3 | n = 1 to n = infinity: ΔE = 0 - (-2.18e-18) = +2.18e-18 J absorbed. |
| 16 | Limits of the model | Fails for any atom with 2+ electrons (the formula does not give correct energies for He, Li ...); treats electrons as particles on orbits, which is not how electrons behave. Replaced by the quantum-mechanical (electron-cloud) model, S2.2. Keep what survives: quantized levels, energy change = photon. |
| (opt) 17 | Bohr radius | r_n = n^2 x 5.29e-11 m. Optional; do not test. |

**4) Formative check (5 items)**

| # | Item | Answer |
|---|---|---|
| 1 | In the Bohr model, why does an atom emit light only at certain colors? | Electron energy is quantized; only specific level differences exist, so only specific photon energies are possible. |
| 2 | Calculate E for hydrogen at n = 2. | -2.18e-18 / 4 = -5.45e-19 J. |
| 3 | A hydrogen electron goes from n = 4 to n = 2. Absorbed or emitted? Find |ΔE|. | Emitted. E_4 = -1.36e-19; E_2 = -5.45e-19; ΔE = -4.09e-19 J, so 4.09e-19 J leaves. |
| 4 | Which transition releases more energy, n = 3 to 2 or n = 2 to 1? | n = 2 to 1: 1.64e-18 J vs 3.03e-19 J. |
| 5 | Give one reason the Bohr model is no longer the accepted atomic model. | Works only for hydrogen-like species / cannot predict multi-electron atoms / electrons are not particles in fixed circular orbits (any one). |

**5) Common misconceptions**
- "Bohr's model works for all atoms." It gives correct energies only for hydrogen and one-electron ions.
- "More negative means more energy." The more negative level is the LOWER energy.
- "An electron can be between orbits." Not allowed; no values between levels.
- "Electrons orbit like planets." That is the model's picture, not reality (S2.2).
- "Emission means the electron goes up." It drops.
- "n=1 to n=2 and n=2 to n=3 need equal energy." Spacing shrinks as n rises (1.64e-18 vs 3.03e-19 J).

**6) Facts to be exact about**
- E_n = -2.18e-18 J / n^2, n = 1, 2, 3 ...; valid for hydrogen only (one-electron systems with Z^2 added; not in scope).
- E at n = infinity is 0; every bound level is negative.
- ΔE = E_final - E_initial; photon energy is the magnitude.
- Bohr 1913. Ground state n = 1.
- Do not state that the Bohr model "explains" intensities, multi-electron spectra, or chemical bonding.

---

# S2.2 Energy Levels, Sublevels & Orbitals

**1) Learning targets**
1. Describe the quantum-mechanical model: an orbital is a region where an electron is probably found, not a path.
2. Name the sublevels (s, p, d, f) in each principal energy level and the number of orbitals in each (1, 3, 5, 7).
3. State capacities: orbital 2 e-; subshells s2, p6, d10, f14; shell n holds 2n^2 (2, 8, 18, 32).
4. Relate sublevels and orbitals to the shape and the block layout of the periodic table.

**2) Vocabulary**: energy level / shell (n), sublevel / subshell (s, p, d, f), orbital, probability, electron cloud, quantum number (n, l - introduced lightly), spin, degenerate (opt), principal quantum number, wave-particle duality (opt).

**3) Slide outline (16 content slides)**

| # | Slide | Content |
|---|---|---|
| 1 | Hook | Bohr failed for helium. What replaced it? |
| 2 | Quantum-mechanical model | Schrödinger (1926) treated electrons with wave equations. Electrons are described by probability, not paths. Heisenberg's uncertainty principle: cannot know position and momentum exactly (named only). |
| 3 | Orbital definition | A region of space with a high probability (commonly 90%) of finding an electron. Not a path, not a physical container. |
| 4 | Energy levels | Principal energy level n = 1, 2, 3, 4... Higher n = farther on average and higher energy. |
| 5 | Sublevels | Level n contains n sublevels. n=1: 1s. n=2: 2s, 2p. n=3: 3s, 3p, 3d. n=4: 4s, 4p, 4d, 4f. |
| 6 | Orbitals per sublevel | s = 1, p = 3, d = 5, f = 7. |
| 7 | Capacity | Each orbital holds a maximum of 2 electrons (opposite spins; Pauli is formalized in S2.3). s = 2, p = 6, d = 10, f = 14. |
| 8 | Shapes | s spherical; p dumbbell, three orientations (px, py, pz); d mostly four-lobed (one differs); f complex (names only). Shape drawings must be labeled "probability regions". |
| 9 | Worked example 1: sublevels and orbitals in n = 3 | List sublevels, orbitals, and maximum electrons. |
| 10 | Solution 1 | 3s, 3p, 3d: 1 + 3 + 5 = 9 orbitals = n^2. Electrons: 2 + 6 + 10 = 18 = 2n^2. |
| 11 | Shell capacity table | n=1: 1 orbital, 2 e-. n=2: 4, 8. n=3: 9, 18. n=4: 16, 32. Rules: orbitals n^2, electrons 2n^2. |
| 12 | Energy order within a shell | In atoms with more than one electron: s < p < d < f within the same n. (In hydrogen alone, all sublevels of the same n have the same energy; do not generalize that to other atoms.) |
| 13 | Overlap of levels | 4s is below 3d in a neutral atom's filling order. Previews S2.3. |
| 14 | Worked example 2: capacity | What is the maximum number of electrons in the 4f sublevel? In the n = 2 level? |
| 15 | Solution 2 | 4f: 7 orbitals x 2 = 14. n = 2: 2s (2) + 2p (6) = 8 = 2(2)^2. |
| 16 | Periodic table link | Block widths: s = 2 columns, p = 6, d = 10, f = 14, matching sublevel capacities. Period lengths 2, 8, 8, 18, 18, 32 (32 for period 6 and 7). Quick-read: group 1-2 = s block (He sits in group 18 yet is 1s2), 13-18 = p, 3-12 = d. |
| (opt) 17 | Quantum numbers preview | n = 1, 2, 3...; l = 0 to n-1 (s,p,d,f = 0,1,2,3); ml = -l to +l (gives 1, 3, 5, 7 orbitals); ms = +1/2 or -1/2. Needed for the Pauli statement in S2.3. |

**4) Formative check (5 items)**

| # | Item | Answer |
|---|---|---|
| 1 | How is an orbital different from a Bohr orbit? | An orbit is a fixed path; an orbital is a region of probability for finding the electron. |
| 2 | List all sublevels in n = 2. | 2s and 2p. |
| 3 | How many orbitals are in a d sublevel? How many electrons can it hold? | 5; 10. |
| 4 | What is the maximum number of electrons in the third energy level? | 18. |
| 5 | How many orbitals are in the n = 4 level? | 16 (1 + 3 + 5 + 7). |

**5) Common misconceptions**
- "The electron travels around the nucleus along the dumbbell shape." The shape is a probability region.
- "An orbital holds as many electrons as its sublevel." One orbital holds 2.
- "The p sublevel has one dumbbell." It has three orbitals (three orientations).
- "The third shell is full at 8 electrons." The shell can hold 18; 8 is the stable octet in the outer shell only when s and p are filled (S2.4).
- "Every shell has s, p, d, f." Shell n has n sublevels. n = 1 has only s; n = 2 has s and p only.
- "Sublevels of the same n always differ in energy." True for multi-electron atoms only; hydrogen is the exception.
- "d starts at n = 2." d begins at n = 3; f at n = 4.

**6) Facts to be exact about**
- Orbitals per sublevel: s 1, p 3, d 5, f 7. Capacities: s 2, p 6, d 10, f 14.
- Shell n: n sublevels, n^2 orbitals, 2n^2 electrons (2, 8, 18, 32).
- Ground-state atoms known use only s, p, d, f (g and beyond exist mathematically but are not occupied in the ground state of any known element). Say "s, p, d, f" and stop.
- Letters s, p, d, f originate from spectroscopic descriptions (sharp, principal, diffuse, fundamental). Optional; label as historical.
- Orbital probability convention is "about 90%". Say "high probability" unless Matt prefers a number.

---

# S2.3 Electron Configurations

(Covers Matt's required topics: Aufbau, Hund's, Pauli; orbital diagrams; longhand and shorthand (noble-gas) configurations; exceptions; error-spotting.)

**1) Learning targets**
1. State and apply the Aufbau principle, Pauli exclusion principle, and Hund's rule.
2. Write ground-state longhand and noble-gas shorthand configurations and orbital diagrams for elements through Z = 36 (extension: period 5).
3. Identify and explain the Cr and Cu exceptions.
4. Check a given configuration or orbital diagram against the three rules and correct it (error-spotting).

**2) Vocabulary**: electron configuration, ground state, Aufbau principle, Pauli exclusion principle, Hund's rule, orbital diagram, spin (up/down), unpaired electron, paired electron, degenerate orbitals, noble-gas (shorthand) notation, core electrons, valence electrons (preview), exception.

**3) Slide outline (19 content slides)**

| # | Slide | Content |
|---|---|---|
| 1 | Hook | Reading the table as an address book: where are the electrons of oxygen? |
| 2 | What a configuration is | Distribution of an atom's electrons among levels, sublevels, orbitals. Ground state = lowest energy arrangement (all configurations below are ground state). Notation: 1s2 = level 1, s sublevel, 2 electrons. |
| 3 | Aufbau principle | Electrons fill the lowest-energy available orbital first. |
| 4 | Order of filling | 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p. The diagonal arrow chart is a memory aid; the table layout also gives it. Note: 4s fills before 3d. |
| 5 | Why 4s before 3d | In K and Ca the 4s orbital is lower in energy than 3d. Once 3d electrons are present, 3d lies below 4s, which is why 4s electrons leave first in ions (S2.4). Keep this wording; avoid "4s is always lower than 3d". |
| 6 | Pauli exclusion principle | An orbital holds at most 2 electrons, and they must have opposite spins. (Full statement: no two electrons in an atom have the same set of four quantum numbers.) |
| 7 | Hund's rule | In a set of equal-energy (degenerate) orbitals (e.g., the three 2p), electrons occupy separate orbitals with parallel spins before any orbital gets a second electron. |
| 8 | Orbital diagrams | A box (or line) per orbital; an up arrow and down arrow for spin. Fill all boxes in a sublevel with up arrows first, then pair. Draw the up arrow first in each pair. |
| 9 | Worked example 1: oxygen | Write the longhand configuration and orbital diagram for O (Z = 8). |
| 10 | Solution 1 | 1s2 2s2 2p4. 2p diagram: boxes 1, 2 = up-down, up, up (one pair, two unpaired). Check: 2 + 2 + 4 = 8. Unpaired = 2. |
| 11 | Longhand examples | N: 1s2 2s2 2p3 (three unpaired). Cl: 1s2 2s2 2p6 3s2 3p5 (sum 17). Ca: 1s2 2s2 2p6 3s2 3p6 4s2. Always check the sum equals Z. |
| 12 | Noble-gas shorthand | Replace the inner core with the symbol of the PREVIOUS period's noble gas in brackets. Cl = [Ne] 3s2 3p5. Ca = [Ar] 4s2. Common error: using the noble gas of the same period or the element's own. |
| 13 | Worked example 2: iron | Write longhand and shorthand for Fe (Z = 26), and count unpaired electrons. |
| 14 | Solution 2 | Longhand: 1s2 2s2 2p6 3s2 3p6 4s2 3d6. Shorthand: [Ar] 4s2 3d6. 3d diagram: one pair, four unpaired. Sum: 18 + 2 + 6 = 26. |
| 15 | Exceptions: Cr and Cu | Cr (Z = 24): predicted [Ar] 4s2 3d4; actual [Ar] 4s1 3d5. Cu (Z = 29): predicted [Ar] 4s2 3d9; actual [Ar] 4s1 3d10. HS explanation: half-filled (d5) and completely filled (d10) d sublevels are especially stable, and 4s and 3d are very close in energy. Label this a simplification. |
| 16 | Worked example 3: error-spotting | Five "student" configurations; each ground-state. Decide which rule or fact is broken. (a) O: 1s2 2s2 2p6 (b) K: 1s2 2s2 2p6 3s2 3p6 3d1 (c) N 2p diagram: up-down, up, blank (d) Ne: 1s2 2s2 2p6 with a 2s box drawn up-up (e) Ca: [Ne] 4s2. Plus an extra on Cr 4s2 3d4. |
| 17 | Solution 3 | (a) 10 electrons, oxygen has 8: wrong count. (b) Should be 4s1: Aufbau violated (4s before 3d). (c) Hund's rule violated: electrons paired while a 2p orbital is empty; correct is up, up, up. (d) Pauli violated: two electrons in one orbital must have opposite spins. (e) Wrong shorthand core: [Ne] + 2 = 12 electrons; Ca needs [Ar] 4s2. Cr 4s2 3d4: follows the rules but is not the real ground state; real is 4s1 3d5. Teach: "rules-consistent" versus "observed". |
| 18 | Error-spotting checklist | (1) Add electrons: does the total equal Z (or Z minus charge)? (2) Does each sublevel hold no more than 2, 6, 10, 14? (3) Is the filling order followed? (4) Hund: singles before pairs. (5) Pauli: pairs have opposite spins. (6) Is the shorthand core the previous noble gas? (7) Is it Cr or Cu (or a known exception)? |
| 19 | Exception scope slide | Same pattern one row down: Mo [Kr] 5s1 4d5, Ag [Kr] 5s1 4d10, Au [Xe] 4f14 5d10 6s1 (extension; do not test). Other exceptions exist (e.g., Pd [Kr] 4d10); the half/full heuristic does not predict all of them. Students should use "look it up" outside Cr and Cu. |

**Exception scope recommendation (for Matt to decide)**: Require Cr and Cu only. Mention Mo and Ag (same groups, one period down) and Au (group 11) as "same pattern, extension, not tested". Do NOT teach Pd, Pt, Nb, Ru, Rh, La, Gd, or others as expectations; they do exist, and several do not follow the half/full-subshell heuristic (e.g., Nb [Kr] 5s1 4d4), so teaching the heuristic as a predictive rule would be inaccurate. Also note that W is the regular [Xe] 4f14 5d4 6s2 even though Mo is an exception, which shows the heuristic cannot predict.

**Scope recommendation**: Required through Kr (Z = 36). Period 5 and 6 shorthand as extension. f-block: awareness only (PROVISIONAL scope; Matt to confirm).

**4) Formative check (5 items)**

| # | Item | Answer |
|---|---|---|
| 1 | Write the longhand configuration for phosphorus (Z = 15). | 1s2 2s2 2p6 3s2 3p3 |
| 2 | Write the noble-gas shorthand and 3p orbital diagram for sulfur (Z = 16). | [Ne] 3s2 3p4; 3p: up-down, up, up. |
| 3 | Write the shorthand for Mn (Z = 25) and count the unpaired electrons. | [Ar] 4s2 3d5; 5 unpaired. |
| 4 | Which rule is broken by 2p: up-down, up-down, blank for carbon, and what is correct? | Hund's rule. Carbon (2p2) is up, up, blank. |
| 5 | Write the actual ground-state configuration of Cu in shorthand and explain why it is an exception. | [Ar] 4s1 3d10; one 4s electron moves to 3d, giving a filled d sublevel (extra-stable; 4s and 3d are close in energy). |

**5) Common misconceptions**
- "3d is filled before 4s." 4s fills first.
- "Hund's rule means pair first." Singles first, parallel spins.
- "Shorthand uses the noble gas in the element's own period." Previous period's gas.
- "Pauli means two electrons per sublevel." Two per orbital.
- "Cr and Cu are errors in the textbook." They are measured ground states.
- "Half-full or full is always more stable, so any element will move electrons." Only specific known cases; the heuristic is not a predictor.
- "Any configuration whose total equals Z is valid." Must also follow the rules (an excited-state arrangement such as 3s1 3p1 for Mg totals 12 but is not the ground state).
- "Up arrows and down arrows are electrons orbiting in opposite directions." They are spin labels.
- "Number after the letter means the orbital number." It is the electron count (superscript).

**6) Facts to be exact about**
- Filling order: 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p.
- Pauli: maximum 2 electrons per orbital, opposite spins. Hund: degenerate orbitals singly occupied with parallel spins first. Aufbau: lowest energy first.
- Cr [Ar] 4s1 3d5 (24 e-: 18 + 1 + 5). Cu [Ar] 4s1 3d10 (29 e-: 18 + 1 + 10). Mo [Kr] 5s1 4d5 (42 e-). Ag [Kr] 5s1 4d10 (47 e-). Au [Xe] 4f14 5d10 6s1 (79 e-).
- Verified counts: Fe [Ar] 4s2 3d6 (26); Br [Ar] 4s2 3d10 4p5 (35); Ni [Ar] 4s2 3d8 (28); Ge [Ar] 4s2 3d10 4p2 (32).
- Valid shorthand cores: He, Ne, Ar, Kr, Xe, Rn; the core is the noble gas of the previous period.
- Write notation convention once (F5).
- "Why" statements for the exceptions are simplified; do not present "half-filled is stable" as the full cause.

---

# S2.4 Electron Stability & Valence Electrons

Ion configurations are covered here at the configuration level only (F2). Charge prediction, ionization energy trends, and ionic compound formation belong to U3 (S3.4, S3.7) and U4.

**1) Learning targets**
1. Identify valence electrons from a configuration and from the periodic table group (main-group elements).
2. Explain why noble gases are stable: outer s and p sublevels filled (ns2 np6; duet for He).
3. Write configurations for cations and anions, including noble-gas-like (isoelectronic) results.
4. Write transition-metal ion configurations by removing the 4s (outermost s) electrons first (Fe2+, Fe3+, Zn2+, Cu+, Cu2+).

**2) Vocabulary**: valence electron, core electron, valence shell, octet, duet, noble gas configuration, cation, anion, ion, isoelectronic, transition metal, pseudo-noble-gas configuration (opt), paramagnetic/unpaired electrons (opt).

**3) Slide outline (18 content slides)**

| # | Slide | Content |
|---|---|---|
| 1 | Hook | Why do He, Ne, Ar hardly react while Na and Cl are very reactive? |
| 2 | Core vs valence | Valence electrons: electrons in the outermost energy level (the highest n). Core: the inner filled levels. Cl: 1s2 2s2 2p6 | 3s2 3p5 → 7 valence. |
| 3 | Valence from the table | Main-group valence electrons = group number units digit: group 1 = 1, group 2 = 2, 13 = 3 ... 17 = 7, 18 = 8 (He has 2). |
| 4 | Worked example 1: valence electrons | Find the valence electrons of P and Ca from configurations. |
| 5 | Solution 1 | P: [Ne] 3s2 3p3 → outer level n = 3: 2 + 3 = 5 (group 15). Ca: [Ar] 4s2 → 2 (group 2). |
| 6 | Transition metals (caution) | Valence counting is less clean (ns and (n-1)d); for this course, name the outer s electrons as the ones lost first. PROVISIONAL: Matt to decide whether to count d electrons as valence. |
| 7 | Noble-gas stability | Filled outer s and p sublevels: He 1s2; Ne [He] 2s2 2p6; Ar [Ne] 3s2 3p6; Kr [Ar] 4s2 3d10 4p6. "Octet" = 8 outer electrons, "duet" = 2 for He (and H, Li, Be, B variations are a later topic). Clarify that "full" means the outer s and p sublevels; the n = 3 shell can still hold d electrons. |
| 8 | Ions and electron count | Cation = loses electrons (positive). Anion = gains electrons (negative). Electrons = Z - charge. Protons never change. |
| 9 | Main-group cations | Na (1s2 2s2 2p6 3s1) → Na+ 1s2 2s2 2p6 = [Ne]. Mg2+ = [Ne]. Al3+ = [Ne]. Ca2+ = [Ar]. Electrons come off the outermost (highest n) level. |
| 10 | Main-group anions | Added electrons go into the next open spot. Cl- = [Ne] 3s2 3p6 = [Ar] configuration. O2- = 1s2 2s2 2p6 = [Ne]. N3- = [Ne]. S2- = [Ar]. Br- = [Ar] 4s2 3d10 4p6 = [Kr] configuration. |
| 11 | Isoelectronic | Same electron count / configuration: O2-, F-, Ne, Na+, Mg2+, Al3+ (10 electrons). Different nuclei, so different sizes (size explained in U3). |
| 12 | Worked example 2: main-group ions | Write the configuration of Mg2+ and S2-, name the noble gas each matches. |
| 13 | Solution 2 | Mg (12 e-): 1s2 2s2 2p6 3s2 → lose 2 → 1s2 2s2 2p6 = [Ne] (10 e-). S (16 e-): [Ne] 3s2 3p4 → gain 2 → [Ne] 3s2 3p6 = [Ar] (18 e-). |
| 14 | Transition metal cations: rule | Remove electrons from the outermost s first (4s), then from d. Reason in student language: once 3d is occupied it lies lower in energy than 4s, so 4s electrons leave first, even though 4s fills first. |
| 15 | Worked example 3: iron, zinc, copper ions | Write [Ar] shorthand for Fe2+, Fe3+, Zn2+, Cu+, Cu2+. |
| 16 | Solution 3 | Fe [Ar] 4s2 3d6 → Fe2+ [Ar] 3d6 (24 e-) → Fe3+ [Ar] 3d5 (23 e-, half-filled d). Zn [Ar] 4s2 3d10 → Zn2+ [Ar] 3d10 (28 e-). Cu [Ar] 4s1 3d10 → Cu+ [Ar] 3d10 (28 e-); Cu2+ [Ar] 3d9 (27 e-). |
| 17 | More transition ions (opt) | Cr3+ [Ar] 3d3; Mn2+ [Ar] 3d5; Co2+ [Ar] 3d7; Ni2+ [Ar] 3d8; Sc3+ [Ar]; Ti4+ [Ar]; Ag+ [Kr] 4d10. Transition metals do not always reach noble-gas configurations. |
| 18 | Scope boundary slide | "Why does Na become +1 and not +2, and how much energy it takes" is Unit 3 (S3.4, S3.7). Here: only what the electron arrangement of the ion is. |
| (opt) 19 | Lewis dot symbols | Dots = valence electrons. This duplicates S5.1; show only if Matt wants a preview (PROVISIONAL). |

**4) Formative check (5 items)**

| # | Item | Answer |
|---|---|---|
| 1 | How many valence electrons do Al, Se, and Xe have? | 3, 6, 8. |
| 2 | Write the configuration for Ca2+ and name the isoelectronic noble gas. | 1s2 2s2 2p6 3s2 3p6 = [Ar]. Argon. |
| 3 | Write the full configuration for O2-. | 1s2 2s2 2p6 (10 electrons). |
| 4 | Write the shorthand for Fe3+, and state which electrons are removed first from Fe. | [Ar] 3d5; two 4s electrons first, then one 3d. |
| 5 | Write the configuration for Cu2+ and Zn2+. | Cu2+ [Ar] 3d9; Zn2+ [Ar] 3d10. |

**5) Common misconceptions**
- "Atoms want to be stable, so they feel the need to complete the octet." Describes outcomes; avoid personifying (observation vs. explanation).
- "Transition metals lose 3d electrons first because 3d was filled last." Remove from 4s first.
- "An ion's nuclear charge changes." Only electron count changes.
- "Anions gain electrons from the outermost shell of the neighbor, into a new shell." They fill the open spot in the same outer s/p sublevels.
- "Noble gas configuration is the only stable one." Fe3+ (3d5), Zn2+ (3d10), Cu+ (3d10) are stable without being noble-gas.
- "The octet applies to every element." Exceptions come later (H, He, Li, Be, B; expanded octets in U5).
- "Valence electrons = all electrons in the outer d too." Not for main-group counting.
- "Argon has a full n = 3 shell." Its s and p are full; 3d is empty.

**6) Facts to be exact about**
- Fe2+ [Ar] 3d6 (24 e-). Fe3+ [Ar] 3d5 (23 e-). Zn2+ [Ar] 3d10 (28). Cu+ [Ar] 3d10 (28). Cu2+ [Ar] 3d9 (27).
- Na+ , Mg2+, Al3+, O2-, F-, N3- = [Ne] (10 e-). K+, Ca2+, Cl-, S2-, P3- = [Ar] (18 e-). Br-, Rb+, Sr2+ = [Kr] (36 e-).
- Valence electrons: group 1-2 and 13-18 → 1, 2, 3, 4, 5, 6, 7, 8 (He 2).
- Transition-metal ions lose ns electrons before (n-1)d electrons.
- Pseudo-noble-gas (d10) configurations: Zn2+, Ga3+, Ag+ (term optional).
- Fe3+ half-filled d: keep as an observation of an electron count, not as proof of a cause.

---

# S2.5 Atomic & Electron Spectra

**1) Learning targets**
1. Explain how an atom emits light: electron excited, then falls to a lower level, releasing a photon of energy ΔE.
2. Relate color, wavelength, frequency, and energy (red long wavelength/low energy, violet short wavelength/high energy) and use E = hc/λ in one calculation.
3. Distinguish continuous, line emission, and absorption spectra, and explain that each element has its own line spectrum.
4. Identify metal ions from flame test colors and explain them with the same electron-transition model.

**2) Vocabulary**: spectrum, continuous spectrum, line (emission) spectrum, absorption spectrum, photon, wavelength (λ), frequency (ν), electromagnetic spectrum, visible light, excited state, ground state, flame test, spectroscope (opt), nanometer (nm).

**3) Slide outline (18 content slides)**

| # | Slide | Content |
|---|---|---|
| 1 | Hook | Fireworks and neon signs: where do the colors come from? |
| 2 | Light and color | Visible light about 400-700 nm: violet, blue, green, yellow, orange, red (short to long). Colors by wavelength (approximate): violet 400-450, blue 450-495, green 495-570, yellow 570-590, orange 590-620, red 620-700. |
| 3 | Wavelength, frequency, energy | c = λν (c = 3.00e8 m/s). E = hν = hc/λ (h = 6.626e-34 J s). Short wavelength = high frequency = high energy. Violet photons have more energy than red. |
| 4 | Electromagnetic spectrum | Radio, microwave, infrared, visible, ultraviolet, X-ray, gamma (increasing energy). UV and IR are invisible; hydrogen has lines in both. |
| 5 | How atoms produce light | Heat or electricity excites electrons to higher levels. They fall back and emit a photon equal to the energy gap. Light production by gas discharge is this process. |
| 6 | Other ways to make light (brief) | A hot solid (incandescent filament) gives a continuous spectrum; a hot gas or excited atom gives line spectra. LED/fluorescence not required (opt, PROVISIONAL). |
| 7 | Spectrum types | Continuous (rainbow), emission (bright lines on dark), absorption (dark lines on a continuous background at the same wavelengths the element emits). |
| 8 | Hydrogen emission spectrum | Four visible lines: 656 nm (red), 486 nm (blue-green), 434 nm (blue-violet), 410 nm (violet). They arise from transitions that end at n = 2. |
| 9 | Worked example 1: color of the 3 → 2 photon | Hydrogen drops from n = 3 to n = 2 (ΔE from S2.1: 3.03e-19 J). Find λ and color. |
| 10 | Solution 1 | λ = hc/E = (6.626e-34 x 3.00e8) / 3.03e-19 = 6.56e-7 m = 656 nm → red. Accept 656-657. Frequency 4.57e14 Hz. |
| 11 | Worked example 2: which transition | The 486 nm line comes from n = 4 to 2. Show that ΔE is consistent. |
| 12 | Solution 2 | ΔE = 2.18e-18 x (1/4 - 1/16) = 4.09e-19 J; λ = 1.99e-25 / 4.09e-19 = 4.86e-7 m = 486 nm. |
| 13 | Line spectra as fingerprints | Each element has unique energy levels, therefore unique line positions. Used to identify elements; helium was first detected in the Sun's spectrum (1868). Absorption lines in starlight reveal composition. |
| 14 | Why not a rainbow | Only certain ΔE values exist (quantized levels). Evidence for the Bohr/quantum idea from S2.1. |
| 15 | Flame tests: the idea | Heat excites metal-ion electrons; return releases visible light; color identifies the metal. |
| 16 | Flame test table | Li crimson/red; Na yellow-orange (intense yellow); K lilac (pale violet); Ca orange-red; Sr red (crimson); Ba pale (yellow-)green; Cu blue-green. See cautions below. |
| 17 | Worked example 3: identify the unknown | Unknown salt burns lilac with a trace of yellow; a second burns brick/orange-red. Which metals? (Teaching point: Na contaminates everything.) |
| 18 | Solution 3 | K (lilac, yellow from sodium impurity) and Ca (orange-red). Li and Sr both look red; Ca and Sr can be confused; flame tests alone cannot separate them. |
| (opt) 19 | Real-world uses | Fireworks (metal salts), neon signs, streetlights, forensic and astronomy spectroscopy. |

**4) Formative check (5 items)**

| # | Item | Answer |
|---|---|---|
| 1 | Which has more energy, a red photon (700 nm) or a blue photon (450 nm)? Why? | Blue; shorter wavelength = higher frequency = higher energy (E = hc/λ). |
| 2 | Why does each element have a different line spectrum? | Each has unique energy levels, so unique ΔE and unique photon energies. |
| 3 | Calculate the wavelength for a photon of 4.58e-19 J (n = 5 to 2 in hydrogen) and state the color. | λ = 1.99e-25 / 4.58e-19 = 4.34e-7 m = 434 nm; blue-violet. |
| 4 | Explain in terms of electrons how a flame test produces color. | Heat excites electrons; they drop to lower levels and emit photons of specific energy/color. |
| 5 | A flame test gives a lilac flame. Which ion? | K+ (potassium). |

**5) Common misconceptions**
- "Atoms burn so the color is combustion." The color is electron transitions (excitation then emission).
- "Electrons fall into the nucleus." They drop to lower energy levels, not into the nucleus.
- "Longer wavelength = more energy." Opposite.
- "The flame color is the color of the metal or its salt." It comes from emission by the excited atoms/ions.
- "All elements give a visible flame color." Many produce none in a flame, or the lines are not in the visible range.
- "Absorption lines are at different wavelengths from emission lines for the same element." They match.
- "The flame test identifies a metal conclusively." Limited: similar reds, sodium contamination.
- "Each color is a single line." Colors may be mixtures of lines or molecular bands.
- "Hydrogen has only four lines." Only four are visible; many more are in UV and IR.

**6) Facts to be exact about**
- Photon energy E = hν = hc/λ; c = λν. h = 6.626e-34 J s; c = 3.00e8 m/s.
- Visible about 400-700 nm; red = longest, violet = shortest; shorter wavelength = higher energy.
- Hydrogen visible lines (all end at n = 2): 656, 486, 434, 410 nm. 2 → 1 is UV (122 nm); 4 → 3 is IR (about 1876 nm).
- Flame colors per Matt's list. Sources of confusion: Li and Sr both red; Ca orange-red; Na masks K (K is traditionally viewed through cobalt-blue glass; PROVISIONAL because that technique is lab procedure and not in scope).
- PROVISIONAL (stated from memory, not verified against a cited source in this session): characteristic wavelengths Na about 589 nm (doublet 589.0 / 589.6), Li about 671 nm, K strongest atomic lines about 766 and 770 nm (edge of visible) with weaker violet lines near 404 nm; Ca, Sr, Ba and Cu flame colors arise largely from molecular species (such as CaOH, SrOH, BaOH, CuCl) rather than single atomic lines. Do not put these numbers on student slides without a source check; the electron-transition explanation is a valid HS simplification either way.
- PROVISIONAL gas-discharge colors: neon red-orange and hydrogen pink/magenta are standard; He, Ar, Hg tube colors vary with tube pressure and phosphor, so do not assert them.
- Student-slide caution: do not state that colors in a flame test have exactly one wavelength.

---

## Source basis and verification status

| Item | Status |
|---|---|
| Bohr formula, constants, all numerical results | VERIFIED: re-solved independently in this session (see constants table). |
| Subshell/orbital counts, filling order, Pauli, Hund, Aufbau statements | VERIFIED (standard general-chemistry content; arithmetic re-checked). |
| Cr, Cu, Mo, Ag, Au, Pd, Nb, W configurations | VERIFIED from general knowledge; electron counts re-added. Not checked against a cited table in this session; recommend one NIST/textbook spot-check before printing Mo, Ag, Au. |
| Ion configurations (all listed) | VERIFIED by electron count. |
| Flame test colors (Matt's list) | Matt's list used as given; consistent with common references. Wavelength details marked PROVISIONAL. |
| Ohio Learning Standards alignment | NOT VERIFIED (F3). |
| Slide counts and pacing | PROVISIONAL (F7). |
