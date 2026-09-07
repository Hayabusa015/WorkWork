# SHULL OS — Legacy Skill and Design Audit

**Prepared:** 2026-09-07
**Scope:** Every SHULL rule, decision, palette, and convention discoverable in the live environment.
**Method:** Read-only inspection of 10 installed skills, 6 Google Drive standards documents,
`CHEM_DECISIONS.md`, and the two specification files supplied with this task.
**Status:** ANALYSIS. Nothing was modified. No classification here is authoritative until you
confirm it — see the classification rule below.

Companions: `SHULLOS_IMPLEMENTATION_PLAN.md` · `CONFLICT_REPORT.md` · `SKILL_MIGRATION_MAP.md`

---

## How to read this document

Every rule carries five fields, per Part 42:

- **SOURCE** — the file and section it came from
- **RULE** — the rule, stated as the source states it
- **CLASSIFICATION** — Part 27 label
- **CONFLICT** — conflict ID, or `—`
- **DESTINATION** — where the rule belongs in SHULL OS

### Classification labels

| Label | Meaning |
|---|---|
| **LOCKED** | Explicitly approved by you and not contradicted by anything found |
| **INHERITED** | Consistently supported across the legacy system, no meaningful conflict |
| **PROVISIONAL** | Useful, not sufficiently established |
| **CONFLICT** | Two or more incompatible rules exist |
| **DEPRECATED** | Superseded by a newer decision |
| **ARCHIVE** | Historical, preserved for reference, not active |
| **UNKNOWN** | Insufficient evidence |

> **The rule that governs this whole document:** no item classified CONFLICT, PROVISIONAL, or
> UNKNOWN has been promoted to LOCKED. Where the 2026-09-07 specification asserts something the
> legacy record contradicts, the item is marked **CONFLICT**, not LOCKED — even though the spec is
> the newest source. Part 28 puts explicit current user decisions first, but Part 26 forbids
> silently resolving conflicts, and several of these contradictions look like they were written
> without sight of the legacy file that contradicts them.

---

## PART 1 — Source inventory

### 1.1 Installed skills (account-level, `~/.claude/skills/synced/<bucket>/`)

| # | Skill | Lines | Layer | State |
|---|---|---:|---|---|
| S-01 | `shull-studio` | 292 | Skill | Installed. 5 referenced files missing. Carries an appended, unlabeled color memo. |
| S-02 | `shull-chemistry-guidelines` | 777 | Skill | Installed. **Not trimmed** — still holds all Layer-2 content. |
| S-03 | `shull-physics-guidelines` | 167 | Skill | Installed. **Stale** — §3 declares the unit map NEEDED; it exists. |
| S-04 | `shull-geology-guidelines` | 305 | Skill | Installed. Holds curriculum, policy, and a palette table. Three live conflicts. |
| S-05 | `shull-slide-deck-builder` | 127 (+117 ref) | Skill | Installed. Builds the pre-v2 slide system. |
| S-06 | `shull-guided-notes-builder` | 138 | Skill | Installed. Clean. |
| S-07 | `test-quiz-generator` | 124 (+3 refs) | Skill | Installed. Clean. All refs present. |
| S-08 | `shull-course-librarian` | 185 | Skill | Installed. Strongest legacy artifact. |
| S-09 | `shull-student` | 186 (+1 ref) | Skill | Installed. Drafts-for-approval model already correct. |
| S-10 | `anti-ai` | **20** | Skill | Installed. UI/interactive only. Thinnest file in the system. |
| — | `shull-practice-set-generator` | — | Skill | **Referenced but NOT installed.** Rules survive in `shull-studio` §4. |
| — | Reference Sheet Generator | — | Skill | **Never built.** |
| — | Lab Document skill | — | Skill | **Never built.** Partial source exists in Drive. |

### 1.2 Google Drive standards (`_Brand/Standards/`)

| # | File | Size | Date | State |
|---|---|---:|---|---|
| D-01 | `SHULL_System_Governance.md` | 12.9 KB | 2026-09-05 | **CONFIRMED. Self-declared tiebreaker.** |
| D-02 | `SHULL_Slide_System_v2.md` | 7.3 KB | mod. 2026-09-06 | Self-labeled WORKING pending sign-off; Physics section CONFIRMED |
| D-03 | `SHULL_Studio_Architecture_v2.md` | 4.9 KB | 2026-09-05 | Status/routing document |
| D-04 | `SHULL_Cowork_Folder_Organization_v2.md` | 3.4 KB | 2026-09-05 | Folder + naming standard |
| D-05 | `ANTI_AI_SLOP_EDUCATOR_STANDARD.md` | 21.3 KB | 2026-09-05 | The full quality standard |
| D-06 | `SHULL_PHYS_Palette_QuietVoltage.md` | 5.8 KB | **2026-09-06** | **CONFIRMED. In production.** |
| D-07 | `SHULL_PHYS_Palette_QuietVoltage_preview.png` | 342 KB | 2026-09-06 | Visual reference |

### 1.3 Course decisions (Drive)

| # | File | Location | State |
|---|---|---|---|
| C-01 | `CHEM_DECISIONS.md` | `Chemistry/` | **CONFIRMED, complete, authoritative** |
| C-02 | `PHYS_DECISIONS.md` | — | **Does not exist** |
| C-03 | `GEO_DECISIONS.md` | — | **Does not exist** |

### 1.4 Referenced-but-absent files — seven broken references

| File | Referenced by | Present? |
|---|---|---|
| `references/connectors.md` | `shull-studio` §5 | ✗ |
| `references/file-routing.md` | `shull-studio` §2, librarian §3 | ✗ |
| `references/calendar-2026-2027.md` | `shull-studio`, librarian §4 | ✗ |
| `references/anti-slop-condensed.md` | `shull-studio` Step 0.3 | ✗ |
| `assets/shull_brand.css` | `shull-studio` §4, routing table | ✗ |
| `assets/build_pdf.py` | `shull-studio` §4 | ✗ |
| `SHULL_Color_Palette_Library.md` | `shull-studio` color memo §3, §1a | ✗ **not in Drive** |
| `SHULL_Image_Prompt_Pack.md` | D-02 §5, D-03, D-04 | ✗ **not in Drive** |
| `SHULL_Physics_Unit_Map_1.pdf` | course maps, librarian absorptions | ✗ **not in Drive** |
| `SHULL_Physics_Pacing_Guide_20262027.pdf` | librarian absorptions | ✗ **not in Drive** |

Ten broken references, not five. `shull-studio` Step 0 instructs every other skill to load
`references/anti-slop-condensed.md` "if the standard is not in Project Knowledge" — and Claude Code
cannot see Project Knowledge at all, so in this environment **the Anti-AI-Slop Standard is
unreachable by the skill that depends on it most.**

### 1.5 Supplied specification files (2026-09-07)

| # | File | Role |
|---|---|---|
| X-01 | `SHULL_Studio_System_Spec.md` | Legacy system description, self-labeled as preserving rather than resolving conflicts |
| X-02 | `SHULL_Course_Maps.md` | Layer-2 content for all three courses |
| X-03 | The task prompt itself | **The newest explicit user decisions.** Part 46 locked list. |

---

## PART 2 — Design decisions: colour and palette

This is the densest conflict area in the system. **Five distinct palette systems** are live
simultaneously; the specification introduces a sixth.

### 2.1 The five legacy palette systems

| ID | System | Where | Date | Scope |
|---|---|---|---|---|
| **P-A** | Base — Deep Forest / Moss / Bio Lime / Parchment | S-01 §1, S-02 §12, S-04 §7 | original | Everything |
| **P-B** | Slide System v2 medium split — Amber `#FFCB74` on Ink `#111111` projected, Bio Lime on Parchment print | D-02 §1 | 2026-09-05 | All courses, medium-split |
| **P-C** | Per-course dark-ground accents — Lab Lime / Kinetic / Terra Teal on `#14161B` | S-01 appended memo §2, §1a | 2026-09-06 | Slides only, new decks only |
| **P-D** | Geology earth palette — Canyon Umber, Basalt Brown, Rust Red, Amber Ochre, Sage Moss, Sandstone | D-01 §8 | pre-2026-09-05 | Geology, print, **already shipped in the built U1 packet** |
| **P-E** | Quiet Voltage — Violet `#3A2168` / Violet Static `#A97BFF` on Porcelain `#E7DDD7` | **D-06, D-02 §1** | **2026-09-06** | **Physics, both media. CONFIRMED. In production.** |
| **P-F** | *This specification* — Lab Lime+Aqua / Quantum Gold+Deep Purple / Terra Teal+Rust Orange, White default | X-03 Parts 8, 46 | 2026-09-07 | All courses, all media |

### 2.2 Colour tokens — full extraction

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-03 Part 6 | **White `#FFFFFF` is the default document background and an official design token** | **LOCKED** | — | `brand/tokens.json`, DESIGN_SYSTEM |
| X-03 Part 7 | **Parchment `#EDF0E5` remains official but is NOT the default background** — special-purpose surface only | **LOCKED** | CONFLICT-12 | `brand/tokens.json` |
| S-01 §1, S-02 §12, S-04 §7, `slide-standard.md` | Parchment `#EDF0E5` is the light background / content-slide ground | **DEPRECATED** | CONFLICT-12 | `brand/palette-archive/` |
| X-03 Part 8 | **Chemistry primary Lab Lime `#A3E635`** | **LOCKED** | — | `brand/tokens.json` |
| X-03 Part 8 | **Chemistry secondary Aqua `#22D3EE`** | **LOCKED** | — | `brand/tokens.json` |
| S-01 §1a | Chemistry — Lab Lime `#A3E635` / Aqua `#22D3EE` on `#14161B` | **INHERITED** *(hexes match the spec exactly)* | — | Confirms the Chemistry pair |
| X-03 Part 8 | Physics primary Quantum Gold `#F5B82E` | **CONFLICT** | **CONFLICT-01** | Blocked pending Q-2 |
| X-03 Part 8 | Physics secondary Deep Purple `#8B5CF6` | **CONFLICT** | **CONFLICT-01** | Blocked pending Q-2 |
| **D-06 §2** | **Physics: Violet `#3A2168`, Violet Static `#A97BFF`, Porcelain `#E7DDD7`, Chrome Light `#F7F3F0`, Chrome `#B9ADA6`, Ink Black `#0B0A0E`, Violet Mid `#6B4FA8`. CONFIRMED 2026-09-06. One palette across both media.** | **CONFLICT** | **CONFLICT-01** | Blocked pending Q-2 |
| S-01 §1a | Physics — Kinetic: Energy Orange `#FF6B1A` / Ice Blue `#3DD6F4` | **DEPRECATED** | CONFLICT-01 | `brand/palette-archive/` |
| S-01 memo §3 | Physics alternate "Quantum Gold — Solar Gold `#F5B82E` / Deep Purple `#8B5CF6`" filed as a **back-burner, not-selected** option | **ARCHIVE** → now cited as LOCKED by X-03 | **CONFLICT-01** | Evidence for Q-2 |
| X-03 Part 8 | Geology primary Terra Teal `#16B8A6` | **CONFLICT** | **CONFLICT-02** | Blocked pending Q-3 |
| X-03 Part 8 | Geology secondary Rust Orange `#E85D24` | **CONFLICT** | **CONFLICT-02** | Blocked pending Q-3 |
| S-01 §1a | Geology — Terra Teal `#16B8A6` / Rust Orange `#E85D24` on `#14161B` | **INHERITED** *(hexes match)* — but scope was **slides only** | CONFLICT-02 | Evidence for Q-3 |
| **D-01 §8** | **Geology has a CONFIRMED earth palette — Canyon Umber, Basalt Brown, Rust Red, Amber Ochre, Sage Moss, Sandstone — already used in the built U1 packet** | **CONFLICT** | **CONFLICT-02** | Blocked pending Q-3 |
| S-04 §7 | "Teacher color palette (identical to Chemistry)" | **DEPRECATED** | CONFLICT-02 | Cut; governance §8 already flags it |
| X-03 Part 8 | Asphalt Black `#14161B` preserved as a neutral | **INHERITED** | — | `brand/tokens.json` |
| X-03 Part 8 | Graphite `#2E3338` preserved as a neutral | **INHERITED** | — | `brand/tokens.json` |
| S-01 §1a | Charcoal `#2A2F33` (Chem neutral), Slate `#2C3338` (Geo neutral) | **PROVISIONAL** | **CONFLICT-13** | Three near-identical greys; see conflict report |
| S-01 §1 | Slate Stone `#2C3B2D` — secondary dark neutral | **DEPRECATED** *(green-tinted; belongs to P-A)* | CONFLICT-13 | `brand/palette-archive/` |
| S-01 §1 | Deep Forest `#1A2318` — dark backgrounds, banners, number squares | **DEPRECATED** | — | `brand/palette-archive/` |
| S-01 §1 | Moss Green `#4A7C59` — primary accent, rules, borders | **DEPRECATED** | — | `brand/palette-archive/` |
| S-01 §1 | Warm Earth `#8B6914`; `#6E5310` at small sizes for grayscale legibility | **DEPRECATED** | — | `brand/palette-archive/` |
| S-01 §1 | Bio Lime `#A8C97F` — highlight/must-write, **one per slide, no exceptions** | **DEPRECATED** as a *colour*; the **one-highlight-per-slide rule is INHERITED** | — | Colour → archive; rule → DESIGN_SYSTEM |
| D-02 §1 | Amber `#FFCB74` on Ink `#111111` for projection; Paper `#F6F6F6` | **DEPRECATED** | CONFLICT-11 | `brand/palette-archive/` |
| D-02 §1 | *"This split needs Matt's sign-off. Until then, treat it as WORKING."* | **UNKNOWN** — sign-off never recorded anywhere | CONFLICT-11 | Superseded by Part 6 |
| X-03 Part 9 | **Colour hierarchy: Primary → Secondary → Semantic → Neutral → White** | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 9 | **Semantic colours (red danger, amber caution, green correct) are permitted even outside the course palette; course identity does not override semantic meaning** | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 10 | **Course-first but functional. Colour must have a purpose. No rainbow documents.** | **LOCKED** | — | DESIGN_SYSTEM |
| S-01 memo §1 | *"Use white background on all student filled documents not the full color pallet to save on ink"* | **INHERITED** — the earliest statement of the White decision | — | Supporting evidence for Part 6 |
| S-01 memo §2 | Per-course palette applies to **new slide decks only**; U7 and U10 Chemistry decks are **not** retrofitted | **INHERITED** | CONFLICT-15 | Migration policy — must carry into SHULL OS |
| D-06 §3 | **Violet Static on Porcelain measures 2.3:1 — fails; never body text on a light ground** | **INHERITED** *(the method, regardless of which palette wins)* | — | DESIGN_SYSTEM: every palette needs measured contrast |
| D-06 §4 | Every categorical pair ≥20 grey levels apart | **INHERITED** | — | DESIGN_SYSTEM |

> **The single most important finding in this section.** `SHULL_PHYS_Palette_QuietVoltage.md` is
> dated 2026-09-06, is marked CONFIRMED, is cross-referenced as CONFIRMED by `SHULL_Slide_System_v2.md`,
> and has shipped: `tokens.phys.js` exists in `_Brand/Templates/`, `build.js` was modified to read
> `process.env.SHULL_TOKENS`, a `regrade.py` script was written to bring eight existing Unit 1 lab
> photos onto the palette, and a Unit 1 practice set was rebuilt and ink-measured at 5.2% pixel
> coverage. The specification's Physics assignment — Quantum Gold + Deep Purple — appears in the
> legacy record **only** as an explicitly *not-selected* back-burner alternate. Resolving this by
> date alone would discard a day-old confirmed decision with real implementation behind it.
> **It is Q-2 and it is not resolved here.**

---

## PART 3 — Typography

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-03 Part 11; S-01 §1; S-02 §12; S-04 §7; X-01 §4.3 | **Trade Gothic Next is the primary SHULL Studio typeface**, used throughout | **LOCKED** — unanimous across every source | — | DESIGN_SYSTEM, `tokens.json` |
| X-03 Part 11 | If unavailable, use a **documented** fallback rather than silently choosing a font. "Determine an appropriate fallback stack during implementation." | **LOCKED** *(the requirement)* / **UNKNOWN** *(the stack)* | CONFLICT-04 | Q-5 |
| S-01 §1; X-01 §4.3 | Ladder: Oswald (display) / Inter or Source Sans 3 (body) → **Poppins (display) / Lato (body)** → Liberation Sans when Lato is missing | **PROVISIONAL** | CONFLICT-04 | Candidate answer to Q-5 |
| S-02 §12 | Same ladder, phrased as "acceptable secondary fallbacks… preserve the same geometric/humanist character" | **INHERITED** *(duplicate of S-01)* | CONFLICT-04 | **Duplicate — cut from the course skill** |
| S-04 §7 | Same ladder restated a third time | **INHERITED** *(duplicate)* | CONFLICT-04 | **Duplicate — cut** |
| S-01 §1 | "Never substitute a font not on this ladder." | **LOCKED** | — | DESIGN_SYSTEM |
| D-02 §3 | Poppins replaced Aptos in the v2 template | **INHERITED** | — | Template history |
| S-01 §1 | Poppins is present in the render container; Lato often is not | **INHERITED** *(environment fact)* | — | DESIGN_SYSTEM note |
| `slide-standard.md` | Slide type scale: unit title 44–54 · headline 30–36 · subhead 20–22 · body 19–24 · highlight 20–24 · table 16–18 · footer chip 10–11 | **CONFLICT** | **CONFLICT-07** | Blocked |
| **D-02 §3** | Slide type scale: unit title 40 · section number 44 · headline 28 · subhead 17 · body 16 · work area 18–20 · card label 12 · eyebrow 11 · footer 10 | **CONFLICT** | **CONFLICT-07** | Blocked |
| `slide-standard.md`; D-02 §3; S-01 §1 | **16pt hard floor for student-facing slide content**; footer chip the only exception | **LOCKED** — all three sources agree | — | DESIGN_SYSTEM |
| S-01 §1 | No print text below 8pt except the running footer | **INHERITED** | — | DESIGN_SYSTEM |
| S-06 | Guided notes body 11pt; footer 6.4pt Poppins `#6B7265` | **INHERITED** | *(6.4pt < 8pt floor — see CONFLICT-19)* | `build-document` |
| S-01 §4 | Practice-set body 10.5pt; **no part of a multi-part item smaller than body** | **INHERITED** | — | `build-document` |
| S-04 §7 | Geology: "err toward slightly larger body text and shorter text blocks than Chemistry" | **INHERITED** *(course-specific)* | — | `courses/geology/DECISIONS.md` |
| S-01 §1 | **One accent-colour word per headline. No gradients on text, ever.** | **LOCKED** | — | DESIGN_SYSTEM |

---

## PART 4 — Document rules (print)

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-03 Part 15; S-01 §1 | **Student materials: readability, printer-friendliness, efficient ink, clear hierarchy, writing space, professional appearance. White background. Restrained colour.** | **LOCKED** | — | DESIGN_SYSTEM |
| **S-01 §1 (ink-saving block)** | **Ink-saving is a hard rule for anything printed.** Outlined/bordered treatments replace solid fills. No full-page banners, no shaded section backgrounds, no solid-fill headers. | **INHERITED — strongly** | CONFLICT-16 | DESIGN_SYSTEM. **Stronger than Part 15; must survive at full strength.** |
| S-01 §1 | Colour on print is a thin accent only — chip outline, rule line, small tag, border. Never a fill larger than a small label or icon. | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §1 | Table rows: hairline borders, never alternating solid shading. Light grey tint only if genuinely needed. | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §1 | Number squares, chips, border-tab labels stay outlined or light-fill on print; solid fill reserved for slides | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §1 | Full-colour variants preserved as `.bak` or on request — never shipped as the default print file | **INHERITED** | — | `build-document` |
| D-06 §5 | Ink measured on the rebuilt U1 practice set: 5.2% pixels marked, 2.9% heavy | **INHERITED** *(method)* | — | QA_GATE: ink check is measurable, not vibes |
| D-06 §5 | Chart areas **hatched**, not tinted, in print | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §1; S-02 §12; S-04 §7 | **Grayscale differentiation never relies on colour alone** — vary fill value, outline weight, and label together | **LOCKED** — three sources | — | DESIGN_SYSTEM |
| S-01 §1 | Box borders ≥1px at ~55% grey; writing lines ≥0.75pt at ~35% grey | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §1; S-02 §12; S-04 §7 | Atom Seal watermark 12–15% opacity; 8–10% on dense table pages; omit on heavily-inked pages | **INHERITED** *(stated 3×)* | CONFLICT-17 | DESIGN_SYSTEM **once**. Also: is an Atom Seal right for Geology and Physics? |
| S-01 §1; S-02 §12 | Dense tabular content uses real tables, never flexbox card grids | **INHERITED** | — | DESIGN_SYSTEM |
| X-01 §4.6; D-03 | Print margins: top `0.30in`, left/right `0.35in`, bottom `0.45in` — self-labeled **WORKING** | **PROVISIONAL** | — | DESIGN_SYSTEM, marked provisional |
| S-02 §12; S-04 §7 | Standard fields Name / Date / Period on every student document | **INHERITED** | — | `build-document` |
| S-06 | Name/Date/Period on page 1 only | **INHERITED** | — | `build-document` |
| S-01 §4 | Running footer with auto-generated `PAGE X OF Y` | **INHERITED** | — | `build-document` |
| X-03 Part 16 | Teacher materials use the same system; may carry more colour, metadata, answers, notes | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 12 | **Visual density: clean and moderately dense.** Avoid "beautiful but useless" and "textbook page on a slide". | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 13 | Decoration minimal and purposeful; every element serves hierarchy, navigation, explanation, emphasis, identity, or comprehension | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 14 | Prefer scientifically accurate images, authentic photographs, meaningful diagrams. No generic stock to fill space. | **LOCKED** | — | DESIGN_SYSTEM |

### 4.1 Practice sets — locked v2

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| S-01 §4; X-01 §6.1 | Exactly 8 questions: 2 warm-up / 3 practice / 2 challenge / 1 multi-topic | **INHERITED** | — | `build-document` |
| S-01 §4 | **Strict two pages**, enforced programmatically by a page-count check | **INHERITED** | — | `build-document`, QA_GATE |
| S-01 §4 | Tag pills, single thin rule: WARM-UP tinted green · PRACTICE white · CHALLENGE tinted earth · MULTI-TOPIC solid dark with light text | **DEPRECATED** *(colours belong to P-A)* | CONFLICT-18 | Structure survives; colours re-derive from the new palette |
| D-06 §4 | Tag pills separated by **border colour as well as fill** | **INHERITED** *(the principle)* | — | DESIGN_SYSTEM |
| S-01 §4 | Work boxes carry a border-tab label ("WORK — CARRY UNITS") **on** the border, not floating grey text inside | **INHERITED** | — | `build-document` |
| S-01 §4; X-01 §6.1 | `.write` ruled lines for prose; `.math` boxes for calculation, `s`/`m`/`l` = 0.72" / 0.92" / 1.18" | **INHERITED** | — | `build-document` |
| S-01 §4; D-03 | **Ruled lines = prose. Open boxes = math.** Holds in notes and practice sets alike. | **INHERITED** | — | DESIGN_SYSTEM |
| S-01 §4 | Bracketed self-check answers for **numeric results only** — never explanation, vocabulary, or graph-reading. Styled `#6E5310`. | **INHERITED** *(rule)* / **DEPRECATED** *(the hex)* | — | Rule → `build-document`; hex → archive |
| S-03 §8; X-02 B.4 | **Physics carries NO work areas on worksheets** — no ruled lines, no math boxes; a prior-knowledge and equations reminder block goes at the top instead | **INHERITED** — stated in three sources | — | `courses/physics/DECISIONS.md` |

### 4.2 Guided / Cornell notes

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| S-06 | **The notes and the deck are one object.** Locate the section deck first; if absent, build it first or state the notes are provisional. | **INHERITED** | — | `build-document` |
| S-06 | Scaffolding ladder: U0–3 heavy · U4–8 medium · U9+ light | **INHERITED** | CONFLICT-20 | `build-document`; **index is disputed for Physics** |
| X-02 B.5 | Physics has 11 units to Chemistry's 16, so the same unit numbers land at different points in the year — the ladder should probably be re-indexed to *calendar position* for Physics | **UNKNOWN** — explicitly "Matt's call" | **CONFLICT-20** | Q-open |
| S-06 | Geology runs one level heavier than Chemistry at the same point; Physics matches Chemistry unless told otherwise | **PROVISIONAL** | CONFLICT-20 | `courses/*/DECISIONS.md` |
| S-06 | Layout: letter portrait, 0.6" side margins, cue column 2.0", notes column 4.9", 1pt vertical rule | **INHERITED** *(rule colour Moss Green is DEPRECATED)* | — | `build-document` |
| D-03; X-01 §6.2 | Every section starts on a new page | **INHERITED** | — | `build-document` |
| D-03; X-01 §6.2 | Every section ends with a summary box plus self-check checkboxes | **INHERITED** | — | `build-document` |
| D-03; X-01 §6.2 | Worked problems use an open bordered box with a faint `SHOW WORK HERE` prompt — **never ruled lines** | **INHERITED** | — | `build-document` |
| X-01 §6.2 | Blanks are underscored runs **sized to the expected answer** — a one-word blank and a full-sentence blank must not look identical | **INHERITED** | — | `build-document` |
| X-01 §6.2 | Must-write cue: anything the deck marked with the highlight block gets a thin left-rule on that line in the notes | **INHERITED** *(colour re-derives)* | — | `build-document` |
| X-01 §6.2 | Leave a `NOTICE THIS` margin note where a common misconception lives, named plainly | **INHERITED** | — | `build-document` |
| S-06; X-01 §6.2 | **Always two files:** student copy with blanks empty, and `_Key` fully filled, generated from the same source so they cannot drift | **INHERITED** | — | `build-document` |

### 4.3 Assessments

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-01 §6.4 | Every item maps to a learning target and, when asked, an Ohio standard code | **INHERITED** | — | `build-assessment` |
| X-01 §6.4; S-03 §6 | **If the exact standard code is uncertain, say so — a wrong code is worse than none** | **INHERITED** | — | `build-assessment` |
| X-01 §6.4 | Every calculation solved during generation; ugly or unrealistic answers mean changing the numbers | **INHERITED** | — | `build-assessment` |
| X-01 §6.4 | Distractors represent real student misconceptions, never random wrong values | **INHERITED** | — | `build-assessment` |
| X-01 §6.4 | No "all of the above" / "none of the above". No trick questions on wording. | **INHERITED** | — | `build-assessment` |
| X-01 §6.4 | Parallel versions are not shuffles: reorder questions *and* answers, change values, swap scenarios; same blueprint, same standards coverage, same points. **Re-solve every version independently.** | **INHERITED** | — | `build-assessment`, QA_GATE |
| X-01 §6.4 | Answer keys always separate files: correct answer, point value, worked solution with units and sig figs, model responses with grading guidance, standard code per question | **INHERITED** | — | `build-assessment` |
| C-01 | Study guides align to concepts and skills but never duplicate test questions | **INHERITED** | — | `courses/chemistry/DECISIONS.md` |

### 4.4 Labs

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| C-01; X-01 §6.5 | Student template: Header → Topic/Goals → Purpose → Background → Safety → Pre-Lab → Materials → Procedure → Data/Observations → Disposal/Cleanup → Post-Lab Analysis | **INHERITED** | — | `build-lab` |
| C-01; X-01 §6.5 | Teacher section: materials per group and class · solution recipes · advance-prep timeline · room setup · duration by phase · safety/disposal · common failure points · expected data range · worked answers · cleanup checklist · Missed Lab guidance | **INHERITED** | — | `build-lab` |
| X-01 §6.5 | **Critical: student lab notebooks are the write-on surface. No write-lines, answer spaces, or data tables on lab handouts.** Pre-lab instructs students to draw their own data tables. | **INHERITED** | CONFLICT-21 | `build-lab`. **Contradicts C-01's "Data/Observations (table…)".** |
| X-01 §6.5; C-01 | Fit one 50-minute period with 5 minutes reserved for cleanup | **INHERITED** | — | `build-lab` |
| X-01 §6.5 | Every formula appears with its name | **INHERITED** | — | `build-lab` |
| X-01 §6.5; C-01; S-03 §5 | Percent error whenever an accepted value exists, and the accepted value is always supplied | **INHERITED** | — | `build-lab` |
| X-01 §6.5; C-01; S-02 §15; S-03 §5 | **"Human error" is never an acceptable error analysis** — stated in four sources | **LOCKED** | — | `build-lab`, VOICE |
| X-01 §6.5; S-02 §15 | Never invent a safety claim; flag uncertain handling or disposal for verification | **LOCKED** | — | `build-lab`, ANTI_AI_SLOP |
| X-01 §6.5 | All labs include the standardized Alconox cleanup block (blue spray bottle, test tube brush, distilled rinse, goggles off last) | **INHERITED** *(Chemistry-specific)* | — | `courses/chemistry/DECISIONS.md` |
| C-01; X-01 §6.5 | Missed lab → Missed Lab Analysis, not a re-run | **INHERITED** | — | `build-lab` |
| X-03 Part 17 | **Preserve the structural strengths of the existing lab template; apply the SHULL visual system; flag conflicts before changing major structure** | **LOCKED** | — | Migration policy |
| Drive `_Brand/Templates/Lab/` | `build_lab.py` + `README_Lab_Template.md` created 2026-09-07 — a lab template build was already in progress | **PROVISIONAL** — not yet read into the audit | — | Source material for `build-lab` |

---

## PART 5 — Presentation rules

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-03 Part 18 | **Teacher presentation first.** Slides support classroom instruction; they are not condensed textbooks. | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 18 | Strong hierarchy, meaningful visuals, restrained text, purposeful diagrams, clear sequencing, varied but coherent layouts | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 6 | **White/light backgrounds are the presentation default.** Dark is an occasional tool for title slides, dividers, major moments, image-heavy slides. | **LOCKED** | CONFLICT-11 | DESIGN_SYSTEM |
| `slide-standard.md`; D-02 §4 | **Dark grounds are structural only** — unit title, section divider, unit summary, index. Content slides light. | **INHERITED** — and consistent with Part 6 | CONFLICT-11 | DESIGN_SYSTEM |
| D-02 §1 | Projected slides run on **ink black `#111111`** with amber; print runs Bio Lime on Parchment | **DEPRECATED** | CONFLICT-11 | `brand/palette-archive/` |
| S-01 §1a | Per-course slide palettes all sit on **Asphalt Black `#14161B`** ground | **CONFLICT** | CONFLICT-11 | The per-course system was *dark-ground*; Part 6 makes light the default |
| X-01 §6.3 | One deck covers **one section**, not a whole unit. Default 12–20 content slides for a one-period section. | **INHERITED** | — | `build-presentation` |
| X-01 §6.3; S-02 §12 | Master sequence: Unit title → Agenda → Learning target → Vocabulary → Section divider → Content → Worked example → **Solution** → Lab/application → Formative check → Review → Unit summary | **INHERITED** | — | `build-presentation` |
| X-01 §6.3; D-02 §2 | **Every worked example is followed by a solution slide, every time. A worked example with no solution slide is a bug.** | **LOCKED** | — | `build-presentation`, QA_GATE |
| `slide-standard.md` | Geometry: 16:9, 13.333 × 7.5in. Headline band 0.5→1.5; rule at y=1.55; content column x 0.7→8.1 (or full 12.6); right rail x 8.5→12.6; footer chip y≈6.9 ~1.35×0.30in. Rail card content vertically centred. | **INHERITED** | — | `build-presentation` |
| `slide-standard.md`; D-02 §4; X-01 §6.3 | **The reserved-height rule.** The highlight block is placed *first*; content height = slide height − block − footer; text flows into what remains. Never place text first and overlay. | **LOCKED** — three sources, and named as the cause of a real shipped defect (U8 preview slides 8 and 17 clipped) | — | `build-presentation` |
| `slide-standard.md` | Hard line caps: with highlight block 3 bullets ≤2 lines · without 5 bullets ≤2 lines · vocabulary 4 terms · worked example 4 steps · table 6 data rows | **INHERITED** | — | `build-presentation` |
| `slide-standard.md` | **If content exceeds the cap, split the slide. Never shrink type to fit.** | **LOCKED** | — | `build-presentation`, QA_GATE |
| `slide-standard.md` | Spacing: ≥0.15" after a subhead · 0.18–0.22" between bullets · 0.35" min baseline to box edge · highlight block padding 0.14" v / 0.20" h | **INHERITED** | — | `build-presentation` |
| S-01 §1; `slide-standard.md`; D-02 §4 | **Exactly one highlight / must-write block per slide.** "Two cues means students copy neither." | **LOCKED** | — | DESIGN_SYSTEM |
| `slide-standard.md` | Card colour logic: either all cards white, or green = "write this definition" **with the Slide Key slide saying so in words**. Never mix with no stated rule. | **INHERITED** *(the principle)* | — | `build-presentation` |
| `slide-standard.md` | Section markers on dark dividers are **circles**; number **squares** are for print. Do not cross them. | **INHERITED** | — | DESIGN_SYSTEM |
| **D-02 §2** | **Twelve layouts in the slide master. New slide → Layout → pick one. Never build a slide from scratch.** | **INHERITED** | **CONFLICT-08** | `build-presentation`. **S-05 still builds from scratch.** |
| D-02 §2 | Layouts 09 (Example Problem) and 10 (Worked Solution) are a **pair** | **INHERITED** | — | `build-presentation` |
| D-02 §2 | Layout 12 (Deck Index) is reference — delete before class | **INHERITED** | — | `build-presentation` |
| D-02 §4 | Example problems ship with an **empty** work area, filled live on the board | **INHERITED** | — | `build-presentation` |
| D-02 §6; X-01 §6.3 | Template source in `_Brand/Templates/`; `tokens.js` holds every colour and size — change a token, run `node build.js`, all twelve layouts follow | **INHERITED** | CONFLICT-22 | **The single-source-of-truth principle for tokens. Adopt it.** Note: spec says `Templates/src/`; Drive has them flat. |
| D-02 §6; D-06 §6 | `build.js` reads `process.env.SHULL_TOKENS`, defaulting to `./tokens` — a course palette exception supplies its own token file rather than forking the build | **INHERITED** | — | Excellent pattern; carry into `brand/tokens.json` design |
| X-03 Part 19 | Animations and transitions subtle, purposeful, professional. Never animate because the software permits it. | **LOCKED** | — | DESIGN_SYSTEM |
| X-03 Part 18 | A long presentation needs enough variation that not every slide looks identical — but variation stays inside the system | **LOCKED** | — | DESIGN_SYSTEM |

---

## PART 6 — Voice and the Anti-AI-Slop Standard

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| X-03 Part 20; X-01 §7; D-05 | **Anti-AI-Slop is a binding production standard, not a style preference** | **LOCKED** | — | `standards/ANTI_AI_SLOP_STANDARD.md` |
| X-03 Part 5 | **"Generic with no soul"** is the definition of AI slop and becomes a central QC principle | **LOCKED** | — | ANTI_AI_SLOP |
| X-03 Part 20 | The test: *"Would this actually look like something the teacher would hand to students?"* If not, revise. | **LOCKED** | — | ANTI_AI_SLOP, QA_GATE |
| X-01 §7 | Prime directive: materials feel deliberately written by a real classroom teacher for a specific group. Authenticity comes from specificity, judgment, restraint, classroom awareness. | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7 | **Never imitate human writing by inserting mistakes, fake anecdotes, awkward grammar, or quirks. Never add intentional typos to evade AI detection.** | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7; S-01 §3 | Voice: knowledgeable teacher talking to his own 10th–12th graders. Direct, plain, specific. "You" and "your group." Reading level ~10th–11th. | **INHERITED** | — | `standards/VOICE.md` |
| X-01 §7; S-01 §3 | Banned openers: "Dive into…", "Embark on a journey…", "In today's fast-paced world…", "This engaging activity will…", "Let's explore the fascinating world of…", "It is important to note that…" | **INHERITED** | — | VOICE |
| X-01 §7 | Never "there are no wrong answers" when answers can be wrong; never "Great job!" as filler | **INHERITED** | — | VOICE |
| X-01 §7 | Never "critical thinking," "real-world application," "collaboration," "inquiry" unless the material demonstrates exactly what they mean | **INHERITED** | — | VOICE |
| X-01 §7 | Audit list: repeated "Students will…", repeated "Your task is to…", excessive colon headings, identical three-bullet lists, imperative-opening sentence runs, "Additionally/Furthermore/Moreover", "ensure/utilize/delve/foster/showcase/comprehensive/robust/seamless/dynamic/meaningful", "exciting/engaging/fun/powerful/unique", inflated claims, conclusions restating introductions, "What did you learn?", "Key Takeaways" on ordinary work, default reflection sections | **INHERITED** | — | VOICE |
| X-01 §7 | **"This is an audit list, not a word ban. Natural language beats mechanical compliance."** | **LOCKED** | — | VOICE. Critical nuance — a literal banned-word filter produces its own slop. |
| X-01 §7; X-03 Part 20 | Visual tells: emoji/icon before every heading · excessive rounded cards · a colour banner per subsection · generic clip art · fake sticky notes and lightbulb callouts · rainbow palettes · five font styles · unnecessary cover pages · repeated Objective/Materials/Instructions/Reflection templates · symmetrical grids the content doesn't call for · huge titles wasting half a page · decorative footer slogans · bold overuse · tables for prose · answer blanks too small | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7; S-02 §15 | **Never fabricate sources, quotations, data origins, standards, accepted values, chemical properties, safety guidance, or local policies** | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7 | **Never invent a statement, event, opinion, or classroom story and attribute it to Mr. Shull** | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7; S-01 §3 | **Never pad. Every question, box, heading, graphic, and instruction must earn its place.** | **LOCKED** | — | ANTI_AI_SLOP |
| X-01 §7; S-01 §3 | Do not label student copies "easy / medium / hard" — use content-based headings or none | **INHERITED** | — | `build-document` |
| X-01 §7; D-01 §3 | **Never present a PROVISIONAL or CARRIED OVER item as CONFIRMED** | **LOCKED** | — | GOVERNANCE |
| X-01 §7 | Delivery: usable student version first · teacher key and rationale separate · no long preface explaining what was created · no unrequested optional sections · briefly flag assumptions, scientific uncertainty, safety items needing verification | **INHERITED** | — | VOICE |
| X-01 §7 | **When revising an existing teacher-created file, preserve its useful personality and routines.** Improve weak areas without replacing everything with a generic template. | **LOCKED** | — | ANTI_AI_SLOP. Directly relevant to this migration. |
| S-04 §8 | Geology: same voice, simpler sentences, lower reading level, more plain-language explanation, lean on visuals | **INHERITED** *(course-specific)* | — | `courses/geology/DECISIONS.md` |
| **S-10 (`anti-ai`)** | **The entire installed anti-ai skill is 20 lines and covers only React/Tailwind UI.** Rules: reject purple/indigo gradients and floating pill cards; structure is information; density over padding; one styling approach; safe null handling; semantic markup over div stacks. | **INHERITED** *(the UI rules)* / **the scope is a defect** | **CONFLICT-10** | The UI rules become a scoped section of ANTI_AI_SLOP. |

> **CONFLICT-10 in plain terms:** `shull-studio` Step 0 says "Do not skip 3" — load the
> Anti-AI-Slop Standard — and then points at either Project Knowledge (invisible to Claude Code) or
> `references/anti-slop-condensed.md` (which does not exist). The only *installed* skill named
> `anti-ai` is about React components. **In this environment, the system's most important quality
> standard is not reachable by the skill that mandates it.** That is the highest-value fix in the
> entire migration and costs nothing to make — the 21 KB standard is sitting in Drive.

---

## PART 7 — Governance and architecture rules

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| **D-01 §1**; X-01 §2; X-03 Part 2 | **A fact lives in exactly one place.** Duplication is the defect. | **LOCKED** — the spec independently re-derives it | — | `governance/GOVERNANCE.md` |
| D-01 §2 | Layer 1 SKILLS own the build (course-independent). Layer 2 owns the course (course-specific). | **LOCKED** | — | GOVERNANCE |
| D-01 §2 | **The line as a test:** affects all three courses → skill. Affects one course → course decisions. | **LOCKED** | — | GOVERNANCE |
| D-01 §3 | Precedence: current instruction → course decisions (course facts) → skill (build mechanics) → CONFIRMED over CARRIED OVER/PROVISIONAL → newer over older | **LOCKED** | — | GOVERNANCE |
| D-01 §3 | **When a skill states a course fact the decisions file contradicts, the decisions file wins and the skill is reported stale** — not silently obeyed, not silently ignored | **LOCKED** | — | GOVERNANCE |
| D-01 §3 | When the layers genuinely overlap and it isn't clear which is which: **stop and ask. One question. Do not build on a guess.** | **LOCKED** | — | GOVERNANCE |
| D-01 §4 | **Course skills must point, never restate.** | **LOCKED** | — | GOVERNANCE |
| D-01 §5 | Decision-log entries carry a **`Supersedes:`** line — "what makes drift visible instead of silent" | **LOCKED** | — | CHANGE_CONTROL |
| D-01 §5 | Never edit history; append to the top of the log | **INHERITED** | — | CHANGE_CONTROL |
| D-01 §6 Check 2 | **Before any build, confirm the unit and section code exist in that course's decisions file. Never build against a code from a skill file alone.** | **LOCKED** | — | `validate_codes.py`, `build-*` skills |
| D-01 §6 Check 4 | Every audit output uses one fix-list format: `# / File / Problem / Your action / Time`, blocking first, then shortest fix first. Nothing over ten minutes stays one row. | **INHERITED** | — | Janitor, Auditor output format |
| D-01 §7 | Claude cannot write to Project Knowledge or installed skills; nothing propagates on its own; past-chat search cannot cross project boundaries | **LOCKED** *(environment fact)* | — | Plan §21 limitations |
| D-01 §10 | "Make drift **impossible to miss** rather than impossible to happen." | **LOCKED** *(design philosophy)* | — | GOVERNANCE preamble |
| X-01 §11 | `validate_layers.py` — fail CI if a course fact appears in a skill | **PROVISIONAL** *(proposed, never built)* | — | `scripts/` |
| X-01 §11 | `validate_codes.py` — fail CI if a `U#/S#.#` code isn't in a decisions file | **PROVISIONAL** *(proposed, never built)* | — | `scripts/` |
| X-01 §11 | **"`brand/tokens.json` should be the only place any hex value or measurement is written."** | **INHERITED** — and it is the correct diagnosis | CONFLICT-22 | `brand/tokens.json` + `validate_tokens.py` |
| S-08 | The librarian runs a Project Knowledge audit on **every** invocation, silently, and folds the result in | **INHERITED** | — | Janitor behaviour |
| S-08 | **Never delete, edit, or silently ignore a Project Knowledge file. Read and report only.** | **LOCKED** | — | Janitor authority |
| S-08 | "Flagged for removal" is not done until Matt confirms. If the same stale file appears again, flag it again — silence is not consent. | **LOCKED** | — | Janitor, Secretary |
| S-09 | The learning sweep **drafts changes for approval; it does not silently rewrite confirmed policy** | **LOCKED** | — | Researcher, `weekly-system-review` |
| D-03 | ⚠ **Skill files are not durable storage.** A reinstall overwrote user edits once. | **LOCKED** *(and it is the reason this repo exists)* | — | GOVERNANCE preamble |
| X-03 Part 47 | Not authorized: permanent deletion of legacy material · destructive Drive operations · autonomous modification of core standards · autonomous design-system rewriting · autonomous weekly changes | **LOCKED** | — | GOVERNANCE, agent authority |

---

## PART 8 — File naming, codes, and Drive routing

| SOURCE | RULE | CLASSIFICATION | CONFLICT | DESTINATION |
|---|---|---|---|---|
| S-01 §2; D-04; X-01 §5.1 | **Every SHULL document carries `U#/S#.#`, and it must match the binder tab, slide footer, student organizer, and folder name. One system, not four conventions.** | **LOCKED** | — | `standards/NAMING.md` |
| S-01 §2; D-04 | `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor].[ext]` | **INHERITED** | CONFLICT-09 | NAMING |
| S-01 §2 | Unit zero-padded to two digits; **section not padded** → `U08_S8.4` | **CONFLICT** | **CONFLICT-09** | Q-6 |
| **D-04** | Examples show **padded** sections → `SHULL_CHEM_Slides_U08_S08.2.pptx`; folders `Section 08.4 - …` | **CONFLICT** | **CONFLICT-09** | Q-6 |
| X-03 Part 25 | Proposal `COURSE_UNIT_RESOURCE_DESCRIPTOR_VERSION` → `CHEM_U03_Presentation_Periodic_Trends_v1` — **no `SHULL_` prefix, no section code, `_v1` versioning** | **CONFLICT** | **CONFLICT-09** | Explicitly a proposal, not approved. Q-6. |
| S-01 §2; D-04 | Types: `Slides` `Guided_Notes` `Practice_Set` `Quiz` `Test` `Lab` `Study_Guide` `Reference` `Key` `Rubric` | **INHERITED** | — | NAMING |
| S-01 §2 | Parallel-form version letters append last → `..._S8.4_A.docx` | **INHERITED** | — | NAMING |
| S-01 §2 | **Answer keys are always separate files ending `_Key`** | **LOCKED** | — | NAMING, QA_GATE |
| C-01; S-08; X-01 §5.1 | The universal doc-code grammar is **confirmed only for `U#/S#.#`** and was never finalized across labs, slides, and keys. **Batch renaming is blocked on this.** | **UNKNOWN** — open since install | CONFLICT-09 | Q-6 |
| D-04 | Images take **no** `SHULL_` prefix: `[course]_u##_s##.#_[subject].png` → `chem_u01_s1.2_rutherford.png`; shared backgrounds drop the unit code | **INHERITED** | — | NAMING |
| **D-04** | Drive tree: `_Brand/{Templates, Image Library/{Chemistry,Physics,Geology,Shared}, Standards}` and `[Course]/Unit ## - Name/Section ##.# - Name/{Homework, Presentations, Guided Notes, Tests-Quizizz, Labs-Case Studies-Projects}` | **INHERITED — and verified against the live Drive** | **CONFLICT-06** | `standards/DRIVE_ARCHITECTURE.md` |
| X-03 Part 23 | Proposed tree: root `Teaching/`; `Image Library/`, `Standards/`, `Templates/` as siblings of `_Brand/`; `Unit XX – Unit Name/` with **en dash**; **seven numbered content folders**, **no Section level** | **CONFLICT** | **CONFLICT-06** | Contradicts the built Drive on four counts |
| D-04 | The five content folders are **exactly** these five, same spelling, same order, every time | **INHERITED** | CONFLICT-06 | DRIVE_ARCHITECTURE |
| D-04 rule 2; S-08 | Reuse existing folders exactly, case-insensitively. **Never create `Tests` beside `Tests-Quizizz`.** | **LOCKED** | — | `shelve-drive-file` |
| D-04 rule 4 | If the unit or section is unclear, **ask**. Never default to a misc folder. | **LOCKED** | — | `shelve-drive-file` |
| D-04 rule 6 | **Never copy a template into a course folder.** Course decks reference `_Brand/Templates/`. One template, one place to fix it. | **LOCKED** | — | `shelve-drive-file` |
| D-04 rule 7 | An image used by two courses moves to `Image Library/Shared/` rather than being duplicated | **INHERITED** | — | `shelve-drive-file` |
| X-01 §5.5 | Drive ops: search by `parentId = '[ID]'` for reliable folder verification; create folders via `create_file` with the folder mimeType; **save markdown with `disableConversionToGoogleType: True` + `contentMimeType: text/plain`** | **INHERITED — verified working** (every `.md` in `_Brand/Standards/` is `text/plain`) | — | `shelve-drive-file` |
| X-03 Part 24 | Librarian defaults: READ allowed · CREATE allowed in authorized locations · RENAME allowed when deterministic · MOVE allowed when deterministic · OVERWRITE needs workflow authorization · **PERMANENT DELETE needs explicit user approval** | **LOCKED** | — | Librarian authority |
| X-03 Part 24; Part 3 | **The Librarian must verify every important file operation and must never claim a file is shelved until the destination is verified** | **LOCKED** | — | `shelve-drive-file` |
| S-08 | Don't batch-rename without confirmation — **renames break links Matt may have elsewhere** | **LOCKED** | — | Librarian authority |

---

## PART 9 — The QA gate

Nine steps, from `shull-studio` §6 and X-01 §9. All **INHERITED** unless noted.

| # | Step | Note |
|---|---|---|
| 1 | **Render and look at it.** PDF → rasterize with `pdf2image` and view. PPTX → `soffice --headless --convert-to pdf`, rasterize, view. **Never ship a document you have not seen rendered.** | **LOCKED** — stated in three sources |
| 2 | **Page budget.** Practice set = exactly 2. If over, fix in order: `@page` margins → base font size → line-height → block bottom margins. **Never shrink a single question to fit.** | INHERITED |
| 3 | **No clipped text.** Highest-priority visual defect. | **LOCKED** — tied to a real shipped failure |
| 4 | **Grayscale check.** If the only difference is hue, fix it. | INHERITED |
| 4b | **Ink check** (print only). Any solid fill larger than a small tag, chip, or icon fails. Full-page banners, shaded backgrounds, medium/full-saturation table shading fail. | INHERITED. D-06 shows this can be *measured*. |
| 5 | **Codes match** — document, filename, folder path all agree | INHERITED |
| 6 | **Voice pass.** Read the directions aloud in your head. Anything that sounds like a brochure gets rewritten. | INHERITED |
| 7 | **Answer key exists and is a separate file** | INHERITED |
| 8 | **Every number re-solved independently**, including each parallel version | INHERITED |
| — | Report the result as a short checklist, not prose | INHERITED |

**Toolchain:** Python + WeasyPrint · Node + `docx` / `pptxgenjs` · `pdf2image` / `pdftoppm` ·
`cairosvg` · `soffice --headless`. Classification **PROVISIONAL** — not verified present in this
container; verification is a Phase 9 task.

---

## PART 10 — Course-specific rules

### 10.1 Chemistry — the reference implementation

`CHEM_DECISIONS.md` (C-01) is complete, CONFIRMED, well-formed, and already follows the target
governance model. **Recommendation: adopt it wholesale into `courses/chemistry/DECISIONS.md`.**

| SOURCE | RULE | CLASSIFICATION | CONFLICT |
|---|---|---|---|
| C-01 | Curriculum map, Units 0–15, **90 sections**, four phases. The only authoritative copy. | **LOCKED** | — |
| X-02 A.1 | Section counts verified: 21 + 25 + 20 + 24 = **90**, matching the organizer header | **LOCKED** | — |
| X-02 A.1 | **U9 has 5 sections; there is no 9.6.** Per-unit badges sum to 90 only when U9 = 5. Resolved 2026-09-07. | **LOCKED** — resolves a long-standing open item | CONFLICT-23 *(C-01, S-01 §7, S-08 all still carry it as open)* |
| C-01; X-02 A.5 | Friday quizzes: 5–6 questions, 3–4 equivalent versions. Unit tests two days: ~25 MC A–D conceptual; ~5 free-response computational, current unit only. **No curve. No retakes.** | **LOCKED** | — |
| C-01 | Daily practice: 5-point rubric at the top of the page; **~10% of the course grade** | **CONFLICT** | **CONFLICT-24** |
| X-02 A.6 | Confirmed gradebook weights: Tests 55 / Quizzes 20 / Labs & Projects 15 / Homework 7 / Binders 3 | **CONFLICT** | **CONFLICT-24** |
| C-01 | Late work: −20% day 1 · −40% total day 2 · −50% max day 3+ · hard cutoff end of unit | **LOCKED** | — |
| C-01 | Reference packet ~Week 2: periodic table, polyatomic ions (marking which must be memorized), solubility rules, percent-error reference. **Do not test pure recall of packet contents.** | **LOCKED** | — |
| C-01 | **Delay the heavy math.** Sig figs enforced consistently **after midyear**. | **LOCKED** | CONFLICT-05 *(cross-course)* |
| C-01 | 176 student days, 4 quarters, full 2026–27 calendar and MP deadlines | **LOCKED** | — |
| C-01 | Pacing guide: phases map to quarters, ~1.5–2 days/section + 2-day unit test | **PROVISIONAL** — explicitly, until validated against real pace | — |
| C-01 | Population ~40–50; lab groups 3–4, ~six per class, rotate ~3 weeks; 50-minute period, last 5 for cleanup | **LOCKED** | — |
| C-01 | McNeal carbonless lab notebooks, individually graded from the carbonless copy | **LOCKED** | — |
| C-01 | One shared Google Sheet per lab across all periods; auto-calculates class statistics; can reveal prior-year data | **LOCKED** | — |
| X-02 A.8 | **Confirmed labs: only U0.3 Intro Skills and U0.4 11 Unknowns.** Everything else is PROVISIONAL. Building any lab past U0 as final is blocked. | **LOCKED** *(the constraint)* | — |
| X-02 A.8 | 11 Unknowns: every group identifies all eleven independently. No splitting, no pooling. −1 point per misidentification out of 11. | **LOCKED** | — |
| **C-01** | **"Course brand exceptions: None. Chemistry uses the base SHULL palette exactly as defined in `shull-studio`."** | **DEPRECATED** — the base palette is itself being replaced | CONFLICT-02 |
| X-02 A.13 | Build status: U0 full set · U1 notes S1.2–S1.5 · U7 and U10 built ahead · rest not started. Forward work on U7/U10 frozen until Q1 units are covered. | **INHERITED** | — |
| S-02 (whole file) | **The Chemistry skill still carries the full map, calendar, grading, reference packet, and a duplicate brand section** that C-01 now owns | **DEPRECATED** | CONFLICT-23 | Governance §8 already ordered the trim; it was never done |

### 10.2 Physics

| SOURCE | RULE | CLASSIFICATION | CONFLICT |
|---|---|---|---|
| X-02 B.1 | Curriculum map: **Units 0–10, 48 sections**, four phases. Verified: 11+14+11+12 = 48. | **LOCKED** | — |
| **S-03 §3** | **"There is no confirmed Physics unit list… ask, don't fill." Marked NEEDED.** | **DEPRECATED** — demonstrably false | **CONFLICT-05** |
| X-02 B.1 | **Sig figs are taught at `U0/S0.2`, week one** — the opposite of Chemistry's delay-the-math rule | **LOCKED** | — |
| **S-03 §5** | **"Sig figs follow the measurement rules already taught in Chemistry — do not re-teach them from scratch"** | **CONFLICT** | **CONFLICT-05** |
| X-02 B.4; S-03 §8 | **No work areas on Physics worksheets.** Prior-knowledge and equations reminder block at the top instead. | **LOCKED** — three sources | — |
| X-02 B.3; S-03 §5 | Vectors always carry direction. FBDs: object as dot or box, one labeled arrow per force, arrows scaled, **no arrow for "motion."** | **LOCKED** | — |
| X-02 B.3; S-03 §5 | **Graph interpretation is a first-class skill.** v-t slope = acceleration; v-t area = displacement; F-x area = work. At least one graph-reading item per relevant practice set. Taught explicitly at `1.3`. | **LOCKED** | — |
| X-02 B.3; S-03 §5 | Sign conventions stated explicitly in the directions, never implied by a diagram | **LOCKED** | — |
| X-02 B.3; S-03 §5 | Misconception distractors: heavier objects fall faster · a moving object must have net force · normal force always equals weight · centripetal force acts outward · energy is "used up" · mass/weight, speed/velocity, heat/temperature confusion | **LOCKED** | — |
| X-02 B.3 | Physics labs produce a measured value with uncertainty; percent error against an accepted value; a named specific error source | **LOCKED** | — |
| X-02 B.2 | Course identity — rigor placement relative to Chemistry and Geology — **not stated** | **UNKNOWN** | — |
| X-02 B.5; S-03 §4 | **Chemistry's gradebook weights are explicitly NOT carried over to Physics** | **LOCKED** *(the prohibition)* / **UNKNOWN** *(the real weights)* | — |
| X-02 B.5 | Chemistry's "delay the math" sequencing rule explicitly **not** carried over | **LOCKED** | — |
| X-02 B.5 | Notes-scaffolding index: unit number or calendar position — "Matt's call" | **UNKNOWN** | CONFLICT-20 |
| X-02 B.1 | `2.1` is labeled **(Review)** — vectors are expected knowledge entering U2 | **LOCKED** | — |
| X-02 B.1 | Physics U10 parallels Chemistry U15 closely — check for reusable assets | **INHERITED** | — |
| S-03 §4 | Practice progression, notes, slides, handouts, answer support, differentiation — all **CARRIED OVER from Chemistry** | **PROVISIONAL** | CONFLICT-05. Governance §8 says: **delete — these belong to `shull-studio` and are duplicated here** |
| X-02 B.8 | `Physics/` has 1 of 11 unit folders. The map supplies the other ten titles. | **INHERITED** | — |

### 10.3 Geology — the blocked course

| SOURCE | RULE | CLASSIFICATION | CONFLICT |
|---|---|---|---|
| S-04 §2; X-02 C.1 | **Geology is not "Chemistry with rocks."** Serves students needing a science credit. Intentionally lower rigor. Built *around* the students, not delivered at them. | **LOCKED** | — |
| S-04 §2 | Visuals over text; every concept gets a visual anchor | **LOCKED** | — |
| S-04 §2 | **Cut, colour, and glue projects are a first-class instructional tool here, not filler** | **LOCKED** | — |
| S-04 §2 | Graphic organizers are a **default** content-delivery and note-taking format | **LOCKED** | — |
| S-04 §2 | Lower reading level and vocabulary load, heavily scaffolded — but real vocabulary and real science, not watered down | **LOCKED** | — |
| **S-04 §5** | Unit map: Plate Tectonics **U4**, Glacial **U8**, Oceans **U9** | **CONFLICT** | **CONFLICT-03** |
| **D-01 §8** | Working record: Plate Tectonics **U5**, Glacial **U9**, Resources **U10** — a one-unit offset from U4 onward | **CONFLICT** | **CONFLICT-03** |
| X-02 C.3; S-04 §10 | **Geology has no section numbers within units.** Whether it should is an open question. | **UNKNOWN** | **CONFLICT-25** — blocks the code check |
| S-04 §3; X-02 C.4 | The only real hands-on labs are rocks and minerals. Everything else is an activity. No formal lab report cycle. | **LOCKED** | — |
| S-04 §3 | **Do not default to or recommend Gizmos** — students get little out of it and tend to cheat through it | **CONFLICT** | **CONFLICT-26** |
| D-01 §8; X-02 C.4 | The built U1 S1.2 notes and a built worksheet **both use the Red Shift Gizmo** | **CONFLICT** | **CONFLICT-26** |
| S-04 §4 | Single-day tests and quizzes. MC and matching heavy, plus labeled-diagram and fill-in-the-blank. **Avoid multi-step calculation-heavy free response.** | **LOCKED** | — |
| S-04 §4 | Completed graphic organizers, foldables, and cut/colour/glue projects are legitimate, valued demonstrations of understanding | **LOCKED** | — |
| S-04 §4, §6 | Grading weights, late-work scale, no-curve/no-retakes — **CARRIED OVER from Chemistry, unconfirmed for Geology** | **PROVISIONAL** | — |
| S-04 §7 | Favour Geology icons — hammer, magnifying glass, mountain/volcano, rock layers, wave, compass, timeline, map. **Reserve atom/beaker/molecule for Chemistry.** | **LOCKED** | — |
| S-04 §7 | Cut/colour/glue: clear fold lines, generous cut margins, print-safe non-bleeding colour regions — must survive scissors and glue in 50 minutes | **LOCKED** | — |
| S-04 §5 | U7 Caves, U8 Glacial, U9 Oceans & Climate, U10 Earth's Resources expansions | **PROVISIONAL** — explicitly, pending review | — |
| S-04 §5 | U2 Geologic Time: period-by-period deep dive, one period per day/section; **running personal timeline project** across the unit | **LOCKED** | — |
| X-02 C.10 | `Geology/` is an empty placeholder. **Blocked on the numbering decision — creating folders now would bake in the wrong numbers.** | **LOCKED** *(the constraint)* | CONFLICT-03 |

---

## PART 10.4 — Recurring user preferences

Patterns that appear across many sources and are worth encoding as standing behaviour.

| Preference | Evidence | Destination |
|---|---|---|
| **Ask one question, not six.** | S-01 Step 0 ("One question"), S-03 §7 ("Don't ask for all six at once"), D-01 §3 ("One question") | Every agent |
| **Never invent; label PROVISIONAL and flag it in the teacher notes — never on the student page.** | S-01 §7, S-02 §15, S-04 §1, S-03 §1, X-01 §7 | GOVERNANCE, VOICE |
| **Tables, not prose, for any audit or status output.** | S-08 ("a short table, not prose"), D-01 §6, S-01 §6 | Janitor, Auditor, Overseer |
| **Show the plan, get a yes, then build.** | S-08 ("A 'build me all of Unit 5' request is a plan first") | Overseer |
| **One unit at a time.** | S-02 §15, S-08, C-01 | Overseer |
| **Preserve useful existing personality when revising.** | X-01 §7, X-03 Part 17 | ANTI_AI_SLOP |
| **Verify, don't assert.** | X-03 Parts 3, 24, 34; S-01 §6 step 1 | Overseer, Librarian, Auditor |
| **Nothing gets deleted without confirmation; if it's still stale next time, flag it again.** | S-08, X-03 Part 47 | Janitor, Librarian |
| **Ink is a real cost.** | S-01 §1 (long block), memo §1, D-06 §5 | DESIGN_SYSTEM |
| **Grayscale survival is non-negotiable** — most handouts photocopy. | S-01, S-02, S-04, D-06 §4 | DESIGN_SYSTEM |

---

## PART 11 — Duplicated rules (the Part 2 violations)

Every row is the same fact written in two or more places. Each is a drift risk that has already
produced at least one real conflict.

| Rule | Written in | Should live in |
|---|---|---|
| The six-token base palette | S-01 §1, S-02 §12, S-04 §7 (3×) | `brand/tokens.json` |
| The typography fallback ladder | S-01 §1, S-02 §12, S-04 §7 (3×) | `brand/SHULL_DESIGN_SYSTEM.md` |
| Grayscale-safety rule | S-01 §1, S-02 §12, S-04 §7 (3×) | DESIGN_SYSTEM |
| One accent word per headline | S-01 §1, S-02 §12, S-04 §7 (3×) | DESIGN_SYSTEM |
| Atom Seal watermark opacity | S-01 §1, S-02 §12, S-04 §7 (3×) | DESIGN_SYSTEM |
| Chemistry curriculum map | S-02 §4, C-01, X-02 A.1 (3×) | `courses/chemistry/DECISIONS.md` |
| 2026–27 calendar and pacing | S-02 §7, C-01, X-02 A.10 (3×) | `courses/chemistry/DECISIONS.md` |
| Chemistry grading and late work | S-02 §§I,J, C-01, X-02 A.6 (3×) | `courses/chemistry/DECISIONS.md` |
| Reference packet contents | S-02 §6, C-01, X-02 A.7 (3×) | `courses/chemistry/DECISIONS.md` |
| Lab template (student + teacher) | S-02 §10, C-01, X-01 §6.5 (3×) | `.claude/skills/build-lab/` |
| Practice-set v2 rules | S-01 §4, X-01 §6.1 (2×), + a missing generator skill | `.claude/skills/build-document/` |
| Physics worksheet no-work-areas rule | S-03 §8, X-01 §6.1, X-02 B.4 (3×) | `courses/physics/DECISIONS.md` |
| Physics discipline rules (vectors, graphs, signs) | S-03 §5, X-02 B.3 (2×) | `courses/physics/DECISIONS.md` |
| The generated-vs-built image test | D-02 §5, X-01 §8.2 (2×) | DESIGN_SYSTEM |
| Doc-code grammar / filename pattern | S-01 §2, D-04, S-08, X-01 §5.1 (4×) | `standards/NAMING.md` |
| Drive folder structure | D-04, X-01 §5.2, X-03 Part 23 (3×, **and they disagree**) | `standards/DRIVE_ARCHITECTURE.md` |
| The QA gate | S-01 §6, X-01 §9 (2×) | `standards/QA_GATE.md` |
| Geology carried-over policies | S-04 §§4,6, X-02 C.5 (2×) | `courses/geology/DECISIONS.md` |
| The two-layer governance rule | D-01 §1–4, X-01 §2, X-03 Part 2 (3×) | `governance/GOVERNANCE.md` |
| "Human error is not an answer" | S-02 §15, S-03 §5, C-01, X-01 §6.5 (4×) | `.claude/skills/build-lab/` |

**Twenty duplicated rules.** Every one of them is an instance of the defect the governance file
names in its first sentence.

---

## PART 12 — Obsolete rules

| Rule | Source | Superseded by | Classification |
|---|---|---|---|
| `CHEM-EA-S 01–19` Electrons-in-Atoms deck codes | S-02 §14, C-01 note | `U#/S#.#` | **ARCHIVE** |
| Chemistry section 9.6 may exist | S-02 §16, C-01 Q1, S-01 §7, S-08 | X-02 A.1 — it does not | **DEPRECATED** |
| "Physics unit map is NEEDED" | S-03 §3, S-01 §7, S-08, D-03 | X-02 B.1 — supplied | **DEPRECATED** |
| "Rebuild the annual pacing guide" | S-02 §16 | Already marked done in the same file | **ARCHIVE** |
| Aptos as the slide font | D-03 change 1 | Poppins | **DEPRECATED** |
| Build decks from scratch | S-05 | D-02 §2 twelve-layout template | **DEPRECATED** |
| Build decks from `build_standard.js` | `README (2).md` (per D-01 §8) | D-02 — build from the template | **DEPRECATED** |
| Kinetic Orange as the Physics palette | S-01 §1a | Quiet Voltage, then this spec | **DEPRECATED** |
| Geology palette identical to Chemistry | S-04 §7 | D-01 §8 earth palette | **DEPRECATED** |
| Amber/Bio Lime medium split | D-02 §1 | Part 6 (light default) + Quiet Voltage (Physics opt-out) | **DEPRECATED** |
| Parchment as the default background | S-01 §1, `slide-standard.md` | X-03 Parts 6, 7 | **DEPRECATED** |
| `SHULL_Design_Refinements_v2.md` | S-08 absorptions | Absorbed verbatim into `shull-studio` §4 | **ARCHIVE** |
| `SHULL_Studio_Install_and_Architecture.md` | D-03 header | `SHULL_Studio_Architecture_v2.md` | **ARCHIVE** |
| `SHULL_Cowork_Folder_Organization.md` (v1) | D-04 header | v2 | **ARCHIVE** |
| `PHYSICS_Unit_Map_Request.md` | S-08 absorptions | The supplied map | **ARCHIVE** |

---

## PART 13 — What the audit found that nobody asked about

Five things worth your attention that fall outside the specification's questions.

1. **The librarian was right and two other files were wrong.** Its known-absorptions table recorded
   the Physics map as supplied while `shull-physics-guidelines` §3 still said NEEDED. The system's
   own audit mechanism worked; nobody acted on its output. **SHULL OS's problem is not detection —
   it is follow-through.** The Secretary exists to close that gap, and it should be built to be
   noisy rather than polite.

2. **`_Brand/Templates/` has become a scratch directory.** Fifteen PNGs, `make_art.py`,
   `regrade.py`, `demo_u1.js`, and a misfiled Geology guided-notes `.docx` are sitting in the
   folder whose stated contents are "the slide template, and future reference-sheet and lab-doc
   templates." The `.docx` is both in the wrong folder *and* under the wrong name — governance §8
   flagged that exact file for rename in a table nobody has worked through.

3. **The token-indirection pattern in `build.js` is the best engineering in the legacy system.**
   `SHULL_TOKENS=./tokens.phys.js node build.js` lets a course palette exception exist without
   forking the build, and it is the reason Quiet Voltage could ship in a day. `brand/tokens.json`
   should be designed to preserve that property: one schema, per-course overlays, one build.

4. **The Chemistry skill was ordered trimmed two days ago and was not trimmed.** Governance §8 lists
   seven specific cuts. All seven content sections are still in the installed 777-line file. This is
   the clearest evidence available that **a to-do list in a document is not a mechanism.** SHULL OS
   should make the trim a validator failure (`validate_layers.py`), not a table row.

5. **Nothing in the system records who decided what, when, in a form you can diff.** The decision
   log in `CHEM_DECISIONS.md` is the closest thing, and it has exactly one entry. Git history is the
   capability the legacy system was missing, and it is worth more than any single agent in Part 3.

---

## Appendix — Extraction coverage

| Domain | Rules extracted |
|---|---:|
| Colour and palette | 31 |
| Typography | 16 |
| Document rules (print) | 22 |
| Practice sets | 9 |
| Guided notes | 12 |
| Assessments | 8 |
| Labs | 12 |
| Presentations | 24 |
| Voice / anti-slop | 20 |
| Governance | 20 |
| Naming, codes, Drive | 21 |
| QA gate | 10 |
| Chemistry | 18 |
| Physics | 17 |
| Geology | 17 |
| Recurring preferences | 10 |
| **Total** | **267** |

| Classification | Count (approx.) |
|---|---:|
| LOCKED | 78 |
| INHERITED | 112 |
| PROVISIONAL | 19 |
| CONFLICT | 24 |
| DEPRECATED | 22 |
| ARCHIVE | 6 |
| UNKNOWN | 6 |

**No CONFLICT, PROVISIONAL, or UNKNOWN item was promoted to LOCKED in this pass.**

