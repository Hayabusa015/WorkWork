# SHULL OS — Decision Record, 2026-09-07

**Authority:** These are Matthew Shull's explicit decisions, given in review of
`CONFLICT_REPORT.md`. Under Part 28 they are tier-1 sources and they win over every legacy file.
**Effect:** All seven CRITICAL conflicts are resolved except CONFLICT-09(a), which was not put to a
decision and remains open.
**Format:** Part 32 change records.

---

## SHULL-CHG-0001 — Repository identity

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-00 / Q-1 |
| **Current Rule** | SHULL OS and an unrelated Next.js/Neon/Electron ADHD capture app share the repository `Hayabusa015/ShullOS` and the same name |
| **Decision** | **A new repository named `workwork` has been created for SHULL OS.** The ADHD app keeps `ShullOS`. |
| **Affected** | Everything. `workwork` is the SHULL OS root. |
| **Risk** | Low |
| **Status** | **APPROVED — IMPLEMENTED 2026-09-07** |
| **Resolved** | Repository is `Hayabusa015/workwork`. Attached to this session, cloned to `/home/user/workwork`, empty at attach time, default branch `main`. This repository is now the SHULL OS root. |

---

## SHULL-CHG-0002 — Physics palette

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-01 / Q-2 |
| **Current Rule** | `SHULL_PHYS_Palette_QuietVoltage.md`, CONFIRMED 2026-09-06: Violet `#3A2168` / Violet Static `#A97BFF` on Porcelain `#E7DDD7`, one palette across both media |
| **Decision** | **Physics is Quantum Gold `#F5B82E` + Deep Purple `#8B5CF6`,** per specification Part 8. |
| **Supersedes** | `SHULL_PHYS_Palette_QuietVoltage.md` (all) · `SHULL_Slide_System_v2.md` §1 Physics exception · `shull-studio` §1a Kinetic row |
| **Reason** | Explicit current user decision |
| **Affected agents** | Designer, Auditor |
| **Affected skills** | `apply-shull-design`, `build-presentation`, `build-document` |
| **Affected courses** | Physics |
| **Risk** | **Medium — this decision has sunk cost behind it.** See consequences below. |
| **Status** | **APPROVED** |

### Consequences to record, not to fix silently

Quiet Voltage was CONFIRMED for one day and shipped. Retiring it strands:

| Artifact | Location | Disposition |
|---|---|---|
| `tokens.phys.js` | `_Brand/Templates/` | Retired. Do not delete — archive. |
| `build.js` `SHULL_TOKENS` env hook | `_Brand/Templates/` | **Keep.** The mechanism is good and `brand/tokens.json` should preserve it. |
| `regrade.py` | `_Brand/Templates/` | Retained; its violet ramp is now obsolete |
| 8 Physics Unit 1 lab photos | regraded to violet-black/chrome | **Now off-palette** |
| Physics Unit 1 practice set | rebuilt on Quiet Voltage | **Now off-palette** |
| Physics image-prompt style block | Quiet Voltage §7 | Superseded; a Quantum Gold block must replace it |

**Standing disposition:** under the no-retrofit policy (CONFLICT-15) these stay as-is and are
recorded in `brand/palette-archive/` so the Janitor does not flag them as defects. **User has not
elected to redo them.** Ask again before any rebuild.

---

## SHULL-CHG-0003 — Geology palette

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-02 / Q-3 |
| **Current Rule** | Three positions: identical-to-Chemistry (skill §7); the confirmed earth palette (governance §8, already used in the built U1 packet); Terra Teal slides-only (`shull-studio` §1a) |
| **Decision** | **Geology is Terra Teal `#16B8A6` + Rust Orange `#E85D24`, all media.** |
| **Supersedes** | Geology earth palette (Canyon Umber, Basalt Brown, Rust Red, Amber Ochre, Sage Moss, Sandstone) · `shull-geology-guidelines` §7 palette table |
| **Affected courses** | Geology |
| **Risk** | Medium — the built U1 packet uses the earth palette and is now off-palette (no-retrofit policy applies) |
| **Status** | **APPROVED** |
| **Note** | This also dissolves the governance §2 concept of a "declared course palette exception." All three courses now sit inside one shared system with per-course identity, per Part 30. |

---

## SHULL-CHG-0004 — Geology unit numbering

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-03 / Q-4 |
| **Current Rule** | `shull-geology-guidelines` §5 says Plate Tectonics U4; `SHULL_System_Governance.md` §8 working record says U5 — a one-unit offset from U4 onward |
| **Decision** | **Plate Tectonics is U4.** The `shull-geology-guidelines` §5 sequence is correct. |
| **Supersedes** | Governance §8 Geology row 1 (the U5/U9/U10 working record) |
| **Risk** | Low |
| **Status** | **APPROVED** |

**Confirmed Geology unit sequence (numbering now settled, content unchanged):**

| U# | Unit |
|---|---|
| U1 | The Universe & Solar System |
| U2 | Geologic Time |
| U3 | Rocks & Minerals |
| **U4** | **Plate Tectonics** |
| U5 | Volcanoes |
| U6 | Earthquakes |
| U7 | Caves |
| U8 | Glacial Geology |
| U9 | Oceans & Climate |
| U10 | Earth's Resources |

**Unblocks:** the ten Geology Drive unit folders may now be created (Phase 10), and
`courses/geology/DECISIONS.md` may carry the numbering as LOCKED.
**Still blocked:** Geology batch renaming, which additionally needs CONFLICT-09 and CONFLICT-25.

---

## SHULL-CHG-0005 — Drive architecture

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-06 / Q-6(b) |
| **Current Rule** | Specification Part 23 proposes root `Teaching/`, `_Brand/` siblings, en-dash separators, and Unit → seven numbered folders with no Section level |
| **Decision** | **The Drive stays exactly as built.** Root is `SHULL Science`. Part 23's `Teaching/` was not intended. |
| **Confirmed structure** | `SHULL Science/` → `_Brand/{Templates, Standards, Image Library}` and `[Course]/Unit ## - Name/Section ##.# - Name/{Homework, Presentations, Guided Notes, Tests-Quizizz, Labs-Case Studies-Projects}`. Hyphen separators. Section level preserved. |
| **Supersedes** | Specification Part 23 |
| **Affected** | `standards/DRIVE_ARCHITECTURE.md`, Librarian, `shelve-drive-file` |
| **Risk** | Low — this preserves the `U#/S#.#` chain linking document, filename, folder, and binder tab |
| **Status** | **APPROVED** |
| **Still open** | The `99 Archive/` folder proposal (P-3 / Q-13) was not put to a decision. Superseded material currently has nowhere to go and Part 47 forbids deleting it. |

---

## SHULL-CHG-0006 — Typography

| Field | Value |
|---|---|
| **Date** | 2026-09-07 |
| **Source** | User decision |
| **Resolves** | CONFLICT-04 / Q-5 |
| **Current Rule** | Ladder: Oswald/Inter → Poppins/Lato → Liberation Sans. **Verified false in this environment** — the build container has 59 fonts and none of Trade Gothic Next, Poppins, Lato, Oswald, Inter, or Source Sans 3 is among them. Only Liberation Sans, the last rung, exists. |
| **Decision** | **Archivo + Archivo Narrow.** |
| **Supersedes** | `shull-studio` §1 ladder · `shull-chemistry-guidelines` §12 · `shull-geology-guidelines` §7 — including the claim that "Poppins is present in the render container" |
| **Reason** | Both are OFL neo-grotesques with true condensed cuts, close in character to Trade Gothic Next — unlike Poppins, which is geometric and was selected for availability rather than resemblance |
| **Risk** | Low |
| **Status** | **APPROVED** |

**The two-rung ladder, both rungs real:**

```
Trade Gothic Next   — Matt's machine; the name written into .docx/.pptx
Archivo / Archivo Narrow — the build container; PDFs, and every QA render
```

**Implementation requirements (Phase 8–9):**

1. Archivo and Archivo Narrow (OFL) are committed to `brand/fonts/` in the repository.
2. A SessionStart hook installs them to `~/.fonts` and runs `fc-cache`. The hook mechanism is
   already proven working in this environment.
3. `.docx` and `.pptx` declare `Trade Gothic Next, Archivo, Liberation Sans` so the file resolves to
   the real brand font on Matt's machine and degrades predictably everywhere else.
4. **Trade Gothic Next is Monotype-licensed and must never be committed to the repository.**

**The defect this fixes.** QA gate step 1 renders through `soffice` and inspects pixels. Until the
fonts are installed, that render uses Liberation Sans — so the reserved-height rule, the 3- and
5-bullet line caps, and the clipped-text check have all been validated against metrics of a font
that never reaches a classroom. **The QA gate has been inspecting a different document than the one
students receive.** Installing Archivo makes the QA render and the shipped PDF the same artifact.

---

## SHULL-CHG-0007 — Naming grammar — **NOT DECIDED**

| Field | Value |
|---|---|
| **Resolves** | CONFLICT-09(a) / Q-6(a) — **still open** |
| **Status** | **PENDING** |

The Drive half of Q-6 was answered (CHG-0005). The naming half was not put to a decision.

The open question is section-code padding:

| Source | Form |
|---|---|
| `shull-studio` §2 | `U08_S8.4` — **unpadded** |
| `SHULL_Cowork_Folder_Organization_v2.md` | `SHULL_CHEM_Slides_U08_S08.2.pptx` — **padded** |
| Specification Part 25 | `CHEM_U03_Presentation_Periodic_Trends_v1` — no prefix, no section code |

**Recommendation, unchanged:** `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]` with
**zero-padded** sections, matching the Drive folder names now confirmed in CHG-0005.

**Blocks:** the `naming` skill, `validate_codes.py`, and all batch renaming.

---

# New issue raised by these decisions

## CONFLICT-28 — The locked course colours fail as text on the locked white background

**Severity: IMPORTANT.** Does not reverse any decision above; determines how the colours are *used*.
**Raised:** 2026-09-07, while recording CHG-0002 and CHG-0003.
**Method:** WCAG 2.x relative luminance, computed — not estimated.

### Measured

| Token | Hex | Grey | On White `#FFFFFF` | Verdict on white | On Asphalt `#14161B` |
|---|---|---:|---:|---|---:|
| CHEM Lab Lime | `#A3E635` | 190 | **1.51:1** | fails as text | 12.00:1 |
| CHEM Aqua | `#22D3EE` | 161 | **1.81:1** | fails as text | 10.01:1 |
| PHYS Quantum Gold | `#F5B82E` | 187 | **1.78:1** | fails as text | 10.15:1 |
| PHYS Deep Purple | `#8B5CF6` | 124 | 4.23:1 | large text only | 4.27:1 |
| GEO Terra Teal | `#16B8A6` | 134 | **2.49:1** | fails as text | 7.27:1 |
| GEO Rust Orange | `#E85D24` | 128 | 3.49:1 | large text only | 5.19:1 |

**Four of six fail outright as text on white; the other two reach large-text-only.** None passes
body text.

**Why.** These six hexes were selected in the 2026-09-06 memo for a **dark ground** (`#14161B`),
where all six pass comfortably. Part 6 then moved the default background to white. The colours were
never re-measured against the new ground.

### The second half: Geology fails the photocopier test

Grayscale separation within each course pair:

| Course | Primary grey | Secondary grey | Δ |
|---|---:|---:|---:|
| Chemistry | 190 | 161 | 29 |
| Physics | 187 | 124 | 63 |
| **Geology** | **134** | **128** | **6** |

Terra Teal and Rust Orange are **six grey levels apart**. Photocopied, they are the same colour.
This matters most in the course where it is least affordable: `shull-geology-guidelines` §7 states
that most Geology handouts print in grayscale, "so this matters even more here than in Chemistry."
It violates the grayscale rule that three separate legacy sources state independently.

### This is not a reason to reopen the decisions

The colours remain correct as an **identity system**. Ink-saving already restricts colour on print
to "a thin accent only — a chip outline, a rule line, a small tag, a border." Colours used as fills,
blocks, rules, chips, and dark-ground accents are unaffected by any of the above.

What is missing is a **text-safe variant per course** for the one place colour becomes type: the
single accent word per headline, and course-coloured labels on white.

### Two candidate resolutions — PROPOSED, not applied

**(a) One text-safe deep variant per course.** Preserve hue and saturation, reduce lightness until
the colour clears 4.5:1 on white. Computed candidates, **PROVISIONAL**:

| Course | Display (locked) | → Text-safe deep (proposed) | On white |
|---|---|---|---:|
| Chemistry | Lab Lime `#A3E635` | `#578310` | 4.51:1 |
| Physics | Quantum Gold `#F5B82E` | `#9C6E07` | 4.52:1 |
| Geology | Terra Teal `#16B8A6` | `#108578` | 4.52:1 |

This is precisely what the retired Quiet Voltage palette did — Violet `#3A2168` text-safe at 9.8:1,
Violet Static `#A97BFF` fill-only at 2.3:1, with an explicit rule that the fill colour is never body
text. **The palette is superseded; the method was right and should survive it.**

**(b) Colour is never load-bearing type.** Accent words on white use Asphalt Black `#14161B`
(18.10:1) or Graphite `#2E3338` (12.75:1); course colour appears only as fill, rule, chip, and
block. Simpler, and closer to the ink-saving rule — but it gives up the coloured headline word that
"one accent-colour word per headline" has specified since the beginning.

**Note on a wrong approach:** darkening *both* colours in a pair to 4.5:1 collapses their grayscale
separation to near zero, because equal contrast against the same background means equal luminance.
Only one text-safe variant per course is needed, and pair differentiation must come from **border
plus fill**, not luminance — which is the existing "never rely on colour alone" rule, and also what
Quiet Voltage did with its tag pills.

### Decision needed

1. Adopt (a) or (b)?
2. If (a), the three deep variants above are computed candidates and need your eye, not just a
   contrast ratio — a sign-off on the actual colours before they enter `tokens.json`.
3. Geology specifically: with Δ6 between Terra Teal and Rust Orange, confirm that every Geology
   categorical distinction carries a border or label difference as well as a fill difference.

**Until this closes, `brand/tokens.json` can record the six locked display colours but cannot
specify how colour is applied to type.** That is a Phase 8 blocker, not a Phase 7 one.

---

# Status after this record

| # | Conflict | Status |
|---|---|---|
| CONFLICT-00 | Repository identity | ✅ `Hayabusa015/workwork` — attached, cloned, in use |
| CONFLICT-01 | Physics palette | ✅ Quantum Gold + Deep Purple |
| CONFLICT-02 | Geology palette | ✅ Terra Teal + Rust Orange |
| CONFLICT-03 | Geology unit numbering | ✅ Plate Tectonics U4 |
| CONFLICT-04 | Typography | ✅ Archivo + Archivo Narrow |
| CONFLICT-06 | Drive architecture | ✅ As built, `SHULL Science` |
| CONFLICT-09(a) | Naming grammar | ⬜ **PENDING** |
| CONFLICT-28 | Colour-on-white contrast | ⬜ **NEW — blocks Phase 8** |

**Six of seven CRITICAL conflicts resolved.** Phase 7 (repository skeleton, legacy snapshots,
`CLAUDE.md`, governance) is **unblocked and ready to begin** — `workwork` is attached and this
analysis now lives in it. Phase 8 (design system and tokens) needs CONFLICT-28 and CONFLICT-09(a).

