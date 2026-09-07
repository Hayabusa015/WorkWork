# SHULL OS — Conflict Report

**Prepared:** 2026-09-07
**Sources compared:** 10 installed skills · 6 Drive standards documents · `CHEM_DECISIONS.md` ·
`SHULL_Studio_System_Spec.md` · `SHULL_Course_Maps.md` · the 2026-09-07 task specification
**Total conflicts:** 28 — **7 CRITICAL · 9 IMPORTANT · 7 NON-BLOCKING · 5 DEPRECATED**

> **None of these has been resolved.** Part 26 forbids silently resolving substantive conflicts and
> Part 28 forbids inference becoming an authoritative rule. Where a proposed resolution appears
> below it is labeled **PROPOSED** and carries reasoning; it is not applied anywhere.

**Reading the priority column.** Part 28's order is: (1) explicit current user decisions,
(2) explicitly approved current design decisions, (3) current authoritative standards,
(4) consistent repeated decisions, (5) recent evidence, (6) older documents, (7) inference.
The 2026-09-07 specification is tier 1. But tier 1 only settles a conflict when the decision was
made *with sight of* the thing it contradicts — and in at least two cases below, it clearly was not.

---

> **⚠ SUPERSEDED IN PART — read `DECISIONS_2026-09-07.md` first.**
> Six of the seven CRITICAL conflicts below were resolved by user decision on 2026-09-07:
> CONFLICT-00 (repo → `workwork`) · CONFLICT-01 (Physics → Quantum Gold + Deep Purple) ·
> CONFLICT-02 (Geology → Terra Teal + Rust Orange) · CONFLICT-03 (Plate Tectonics → U4) ·
> CONFLICT-04 (typography → Archivo + Archivo Narrow) · CONFLICT-06 (Drive stays as built).
> **Still open:** CONFLICT-09(a) naming grammar, and the new **CONFLICT-28** (the locked course
> colours fail as text on the locked white background — measured, blocks Phase 8).
> The analysis below is preserved as the record of *why* each decision was put to you.

---

## Severity definitions

| Severity | Meaning | Effect |
|---|---|---|
| **CRITICAL** | Must resolve before production | **Blocks Phase 7.** Nothing is built until answered. |
| **IMPORTANT** | Should resolve before broad deployment | Build may proceed under a stated assumption; must close before Phase 12 |
| **NON-BLOCKING** | Can remain provisional | Recorded, revisited at the first weekly review |
| **DEPRECATED** | An old decision superseded by a current one | Needs **recording**, not deciding. Archive the old; do not resurrect it. |

---

# CRITICAL — must resolve before production

## CONFLICT-00 — Repository identity: two systems, one name

| | |
|---|---|
| **Sources** | `Hayabusa015/ShullOS` `README.md`, `package.json` vs. the SHULL OS specification |
| **Classification** | CONFLICT |
| **Blocks** | Phase 7 and everything after it |

**The conflict.** The repository named `ShullOS` contains a Next.js + Neon + Electron application
described as *"a zero-friction, dark-mode Personal Operating System for an ADHD brain"* with five
life domains (`teacher`, `dad_husband`, `coaching`, `home_car`, `hobbies_research`). The
specification describes SHULL OS as a **teaching** operating system: agents, skills, standards,
course decisions, Drive filing.

Both branches — `claude/adhd-os-phase-1-e4m32v` and `claude/shull-os-architecture-planning-jcyy5n` —
point at the same commit `99ccb8d`. The planning branch is currently just a second label on the
ADHD app.

**Why it is critical.** Part 37's tree would place `courses/`, `standards/`, `governance/`,
`brand/`, and `skills/` beside `app/`, `db/`, `electron/`, and `tailwind.config.ts` with no
relationship between them. A `CLAUDE.md` at the root would have to describe two unrelated systems.
`.claude/agents/` would load the SHULL agents into every session of the ADHD app's development.
And `tailwind.config.ts`'s zinc dark-mode palette sits one directory away from
`brand/tokens.json` — two colour systems in one repo is precisely the failure mode Part 39 forbids.

**Options.**

| | Option | Consequence |
|---|---|---|
| **A** *(recommended)* | New repository `shull-os`; ADHD app keeps `ShullOS` | Clean separation. Costs one repo creation and a GitHub scope addition. |
| B | SHULL OS takes this repo; ADHD app moves to `adhd-os` | Keeps the `ShullOS` name for the teaching system; requires migrating the app's history and its Vercel deployment. |
| C | Both under `shull-os/` and `adhd-os/` subdirectories in this repo | Avoids repo work; permanently couples two unrelated release cycles and complicates `.claude/` discovery. |

**Recommendation: A.** The two systems have different audiences, different lifecycles, and one is a
deployed web app with a Vercel config. They should not share a root. Note that GitHub access in this
session is scoped to `Hayabusa015/ShullOS`, so option A requires you to grant access to the new repo.

**Decision needed:** which option. **Nothing else can start until this is answered.**

---

## CONFLICT-01 — Physics palette: Quiet Voltage vs. Quantum Gold ⚠ HIGHEST VALUE

| | |
|---|---|
| **Sources** | `SHULL_PHYS_Palette_QuietVoltage.md` (2026-09-06) · `SHULL_Slide_System_v2.md` §1 · `shull-studio` §1a (2026-09-06) · `shull-studio` colour memo §3 · specification Parts 8 and 46 (2026-09-07) |
| **Classification** | CONFLICT |
| **Blocks** | `brand/tokens.json`, the design system, every Physics deliverable, the Physics slide template |

**Five positions exist for one course.**

| Position | Colours | Date | Status |
|---|---|---|---|
| 1. Base SHULL | Bio Lime `#A8C97F` on Parchment `#EDF0E5` | original | Superseded |
| 2. Slide System v2 medium split | Amber `#FFCB74` on Ink `#111111` projected | 2026-09-05 | Self-labeled WORKING, sign-off never recorded |
| 3. Kinetic (per-course memo) | Energy Orange `#FF6B1A` / Ice Blue `#3DD6F4` on `#14161B` | 2026-09-06 | Selected in the memo, then superseded the same day |
| 4. **Quiet Voltage** | **Violet `#3A2168` · Violet Static `#A97BFF` · Porcelain `#E7DDD7` · Chrome Light `#F7F3F0` · Chrome `#B9ADA6` · Ink Black `#0B0A0E` · Violet Mid `#6B4FA8`** | **2026-09-06** | **CONFIRMED. Shipped.** |
| 5. **This specification** | **Quantum Gold `#F5B82E` / Deep Purple `#8B5CF6`** | **2026-09-07** | **LOCKED per Part 46** |

**Why this is the hardest conflict in the migration.**

Quiet Voltage is not a proposal. It is CONFIRMED, cross-confirmed by `SHULL_Slide_System_v2.md`,
and **already in production**:

- `_Brand/Templates/tokens.phys.js` exists in Drive (created 2026-09-06)
- `build.js` was modified to read `process.env.SHULL_TOKENS` so a course can supply its own palette
  without forking the build
- `regrade.py` was written to bring eight existing Unit 1 lab photographs onto the palette, and was
  run at 78% strength
- A Unit 1 practice set was rebuilt on it and ink-measured at 5.2% pixel coverage, 2.9% heavy
- Contrast was measured for eight colour pairs, and one pair (Violet Static on Porcelain, 2.3:1)
  was explicitly failed and ruled out for body text
- A replacement image-prompt style block was written, because warm amber next to violet "reads as
  a mistake"
- `SHULL_PHYS_Palette_QuietVoltage_preview.png` was generated

**And the specification's replacement appears in the legacy record only as a rejected alternate.**
`shull-studio`'s colour memo §3, under "Back-burner reference — the other 6 options, filed not
lost," lists for Physics:

```
Physics (pick was #1):
  ✅ Kinetic Orange (selected above)
     Vector Red — Signal Red #F43F4F / Cool Gray #9CA3AF
     Quantum Gold — Solar Gold #F5B82E / Deep Purple #8B5CF6
```

Quantum Gold `#F5B82E` and Deep Purple `#8B5CF6` are exactly the hexes in Part 8. They were on the
not-selected list.

**The question that actually needs answering.** Part 28 puts your current explicit decision first,
so on a mechanical reading Quantum Gold wins. But Quiet Voltage is one day old, marked CONFIRMED,
and has a build system and regraded assets behind it — and Part 8's Physics pair is a revival of an
option that was explicitly passed over. That pattern reads less like "I changed my mind about Quiet
Voltage" and more like "I wrote Part 8 from the palette-library list without Quiet Voltage in
front of me."

There is also a partial reconciliation worth noticing: **both new options are a warm accent plus a
purple.** Deep Purple `#8B5CF6` and Violet Static `#A97BFF` are close relatives. It is possible
Part 8 was reaching for something Quiet Voltage already does better, with measured contrast.

**Decision needed — one of:**

- **(a)** Quantum Gold + Deep Purple stands; Quiet Voltage is DEPRECATED and archived; `tokens.phys.js`
  is retired; the regraded Unit 1 images are regraded again or regenerated.
- **(b)** Quiet Voltage stands as a declared course exception (as the governance model already
  permits); Part 8's Physics row is corrected.
- **(c)** A hybrid: Quiet Voltage's *method* — measured contrast, one palette across media, a
  text-safe accent distinct from a fill-only accent — applied to Quantum Gold + Deep Purple, with
  the contrast actually measured before it is locked.

**Recommendation:** answer (b) or (c) rather than (a) *unless* you did in fact decide against Quiet
Voltage on 2026-09-07. If (a), say so explicitly and the archive will record it as a same-week
reversal, which is the honest description.

---

## CONFLICT-02 — Geology palette: three positions, one course

| | |
|---|---|
| **Sources** | `shull-geology-guidelines` §7 · `SHULL_System_Governance.md` §8 · `shull-studio` §1a · specification Parts 8 and 46 |
| **Classification** | CONFLICT |
| **Blocks** | Design system, every Geology deliverable |

| Position | Detail | Evidence weight |
|---|---|---|
| 1. Identical to Chemistry | `shull-geology-guidelines` §7: "Teacher color palette (identical to Chemistry)" | Weakest — governance §8 already ordered this table cut |
| 2. **Earth palette** | Canyon Umber, Basalt Brown, Rust Red, Amber Ochre, Sage Moss, Sandstone. Governance §8 calls it **confirmed** and records it as **already used in the built U1 packet**. | Strong — CONFIRMED, and shipped |
| 3. **Terra Teal** | `#16B8A6` / `#E85D24` on `#14161B` — `shull-studio` §1a, **slides only** | Medium |
| 4. **This specification** | Terra Teal `#16B8A6` + Rust Orange `#E85D24`, **all media** | Tier 1 — but see below |

**The important detail.** The specification's Geology pair matches position 3's hexes exactly. So
Part 8 is consistent with the per-course slide memo — it simply *widens* Terra Teal from slides-only
to all media, which silently overrides the earth palette that governance §8 says is confirmed and
in a printed packet.

Note also that governance §8 treats Geology's palette as "the one declared course exception" to the
shared brand. Part 30's model — one shared design language with per-course identity for all three
courses — dissolves the concept of an exception entirely. That is a coherent change, but it means
the earth palette has nowhere to live except the archive.

**What the earth palette was for.** It is a print-first, earth-tone system for a visual, hands-on
course whose materials are heavily photocopied. Terra Teal + Rust Orange is a projection-first
accent pair. They solve different problems, which is why both exist.

**Decision needed:** does Terra Teal + Rust Orange replace the earth palette in **print** as well as
on slides? If yes, the built U1 packet is now off-brand and needs a decision about retrofitting
(see CONFLICT-15). If no, Geology keeps a documented print exception.

---

## CONFLICT-03 — Geology unit numbering: a one-unit offset

| | |
|---|---|
| **Sources** | `shull-geology-guidelines` §5 vs. `SHULL_System_Governance.md` §8 |
| **Classification** | CONFLICT |
| **Blocks** | Every Geology `U#` code · all batch renaming · **creating any Geology Drive folder** |

| Unit | Skill §5 | Governance §8 working record |
|---|---|---|
| Plate Tectonics | **U4** | **U5** |
| Glacial Geology | **U8** | **U9** |
| Oceans & Climate / Resources | Oceans **U9** | Resources **U10** |

A one-unit offset from U4 onward. The unit *content* is not in dispute; only the numbering.

**Why it is critical rather than important.** `Geology/` on Drive is an empty placeholder. The
course maps file states the reason plainly: *"Blocked on the numbering decision — creating them now
would bake in the wrong numbers."* Every Geology document that has ever been built carries a `U#`
in its filename, its footer, and its binder tab; getting this wrong means renaming all of them
twice. Governance §8 explicitly says: batch rename **after** unit numbering is settled, *"not
before, or it gets done twice."*

**Decision needed:** which numbering is real. Then, and only then, the ten Geology unit folders can
be created and `GEO_DECISIONS.md` written.

---

## CONFLICT-04 — Typography fallback stack is required but undefined

| | |
|---|---|
| **Sources** | Specification Part 11 · `shull-studio` §1 · `shull-chemistry-guidelines` §12 · `shull-geology-guidelines` §7 · `SHULL_Studio_System_Spec.md` §4.3 |
| **Classification** | LOCKED (the requirement) / UNKNOWN (the stack) |
| **Blocks** | Every rendered deliverable |

Trade Gothic Next is unanimously LOCKED as primary. Every source also agrees it is *almost never
available in a render environment*. Part 11 says: "use a documented fallback rather than silently
selecting a random font. **Determine an appropriate fallback stack during implementation.**"

The legacy ladder, stated identically in three skills:

```
Oswald (display) / Inter or Source Sans 3 (body)
  → Poppins (display) / Lato (body)
    → Liberation Sans (body) when Lato is missing
```

Two facts complicate simply adopting it:

1. `shull-studio` §1 records that **Poppins is present in the render container and Lato often is
   not** — so in practice the working pair is Poppins + Liberation Sans, and the first tier of the
   ladder may never fire.
2. The v2 slide template was rebuilt in Poppins, replacing Aptos. The template's twelve layouts are
   already committed to Poppins metrics; a different display font would change every line break.

**Decision needed:** confirm the ladder, and confirm that Poppins is the *practical* display font
even though Trade Gothic Next is the nominal primary. **Fonts should not be verified by assumption
— Phase 9 should actually check what is installed in the build container and record it.**

---

## CONFLICT-06 — Drive architecture: the specification vs. the built Drive

| | |
|---|---|
| **Sources** | Specification Part 23 vs. `SHULL_Cowork_Folder_Organization_v2.md` and the live Drive (verified read-only 2026-09-07) |
| **Classification** | CONFLICT |
| **Blocks** | `standards/DRIVE_ARCHITECTURE.md`, the Librarian, all filing |

Four incompatibilities:

| # | Part 23 | Live Drive | Impact of adopting Part 23 |
|---|---|---|---|
| 1 | Root `Teaching/` | Root **`SHULL Science`** | Renaming the root invalidates every recorded folder ID and every stored link |
| 2 | `Image Library/`, `Standards/`, `Templates/` as **siblings** of `_Brand/` | All three are **children of `_Brand/`** | Destroys the "one copy, not three drifting copies" purpose of `_Brand/` |
| 3 | `Unit XX – Unit Name/` with an **en dash** | `Unit 00 - Foundations of Chemistry` with a **hyphen** | Creates near-duplicate folders — the exact failure the routing rules forbid |
| 4 | Unit → **seven numbered folders** (`01 Presentations/` … `99 Archive/`), **no Section level** | Unit → **`Section ##.# - Name/`** → **five named folders** | **Breaks `U#/S#.#`** — the code that ties document, filename, folder, and binder tab into one system |

Item 4 is the serious one. Part 5.1 of the legacy record is explicit that the document code, the
binder tab, the slide footer, the organizer, and the folder name "are one system, not four
conventions." Removing the Section level from the folder tree severs it.

Part 23 itself says *"Do not arbitrarily redesign this structure"* and *"Inspect the actual Drive
structure available through the integration and document any differences."* This section is that
documentation.

**PROPOSED resolution:** keep the built structure in all four respects; record Part 23's tree in
`brand/palette-archive/`'s sibling — a `standards/superseded/` note — as a considered-and-declined
proposal. **Adopt one idea from Part 23:** a `99 Archive/` folder, as an *optional sixth* content
folder rather than a renumbering. Superseded material currently has nowhere to go and Part 47
forbids deleting it.

**Decision needed:** confirm the proposed resolution, and confirm the `99 Archive/` addition.

---

## CONFLICT-09 — Naming grammar: three incompatible forms, and one unfinished

| | |
|---|---|
| **Sources** | `shull-studio` §2 · `SHULL_Cowork_Folder_Organization_v2.md` · specification Part 25 · `CHEM_DECISIONS.md` Open Question 2 |
| **Classification** | CONFLICT + UNKNOWN |
| **Blocks** | The `naming` skill · `validate_codes.py` · **all batch renaming** |

| Source | Form | Section padding |
|---|---|---|
| `shull-studio` §2 | `SHULL_[COURSE]_[Type]_U##_S##.#` — example `U08_S8.4` | **Unpadded** |
| Folder Organization v2 | `SHULL_CHEM_Slides_U08_S08.2.pptx`; folders `Section 08.4 - …` | **Padded** |
| Specification Part 25 | `CHEM_U03_Presentation_Periodic_Trends_v1` | **No section code at all** |

Three problems, not one:

1. **Padding.** `S8.4` vs `S08.4`. Two installed/filed standards disagree in their own examples.
2. **Part 25's form drops the section code entirely** and the `SHULL_` prefix, and uses `_v1`
   versioning where the established convention uses parallel-form letters (`_A`, `_B`). Part 25
   labels itself "a PROPOSAL, not an automatically approved naming convention" and requires the
   final decision to be documented before enforcement — so this is a conflict the specification
   itself asked to have surfaced.
3. **The grammar was never finished.** `CHEM_DECISIONS.md` Open Question 2, `shull-studio` §7, and
   the librarian's standing open items all record the same thing: `U#/S#.#` is confirmed for notes
   and the roadmap, but the code grammar for **labs, slides, and keys** was never settled. This has
   been open since install and it is what blocks bulk renaming.

**PROPOSED resolution:**

```
SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]
```

with **zero-padded** section codes (`S08.2`), matching the Drive folder names, the v2 standard, and
`validate_codes.py`'s job of comparing a filename against a folder path. Images keep the lowercase,
prefix-less form. Keys always separate, ending `_Key`.

**Decision needed:** adopt the proposed form? And confirm the type vocabulary, including the two
additions the courses imply but no source lists: `Activity` (Geology) and `Organizer`.

**Until this closes, batch renaming stays blocked** — and it is also blocked on CONFLICT-03, so
Geology renaming needs both answers.

---

# IMPORTANT — resolve before broad deployment

## CONFLICT-05 — `shull-physics-guidelines` is stale in two ways

**Sources:** `shull-physics-guidelines` §§3, 4, 5 vs. `SHULL_Course_Maps.md` Part B.

1. **§3 declares the unit map NEEDED.** It exists: Units 0–10, 48 sections, verified
   (11+14+11+12 = 48). The skill must be cut to a pointer at `PHYS_DECISIONS.md`.
2. **§5 contradicts the map on significant figures.** The skill says *"Sig figs follow the
   measurement rules already taught in Chemistry — do not re-teach them from scratch."* The map
   teaches sig figs at `U0/S0.2`, week one, explicitly *because* Physics students have not
   necessarily taken Chemistry and because Chemistry deliberately delays them until after midyear.
   Building a Physics U0 document against the skill would produce a document that assumes knowledge
   the course is about to teach.
3. **§4 duplicates `shull-studio`.** Governance §8 already ruled: *"Delete. They belong to
   `shull-studio` and are duplicated here."* Not done.

**This is the conflict the system's own librarian caught and nobody acted on.** Its
known-absorptions table recorded the map as supplied while §3 still said NEEDED. Worth keeping as
the motivating example for why the Secretary exists.

**Decision needed:** none — this is a correction, not a choice. Recorded so the migration does not
carry §3 or §5's sig-fig line forward. **But see Q-14:** `SHULL_Physics_Unit_Map_1.pdf` is cited as
the map's source and is **not in Drive**. Where is it?

---

## CONFLICT-07 — Two slide type scales

**Sources:** `shull-slide-deck-builder/references/slide-standard.md` vs. `SHULL_Slide_System_v2.md` §3.

| Role | slide-standard.md | Slide System v2 |
|---|---|---|
| Unit title | 44–54 | 40 |
| Section number | — | 44 |
| Headline | 30–36 | **28** |
| Subhead | 20–22 | **17** |
| Body | 19–24 | **16** |
| Table cell | 16–18 | — |
| Card label | — | 12 |
| Eyebrow | — | 11 |
| Footer | 10–11 | 10 |

v2 is substantially tighter and introduces roles the older standard has no name for. Both are
installed and filed. Both claim authority over slide type.

**The one point of agreement, and it is the important one:** a **16pt floor for student-facing
content**. v2 permits 10–12pt only for eyebrows, card labels, and footers — "navigation, not
content" — and records that the prototype deck had 104 runs at 9pt, "unreadable past the second
row."

**PROPOSED resolution:** v2 wins. It is newer, it is tied to the twelve-layout template that
actually renders, and its role vocabulary is more complete. Record the older scale in the archive.

---

## CONFLICT-08 — The slide builder builds a system that was replaced

**Sources:** `shull-slide-deck-builder` + `slide-standard.md` vs. `SHULL_Slide_System_v2.md` §2 and
`SHULL_Studio_Architecture_v2.md` change 1.

The installed builder produces Parchment content slides with Deep Forest title/divider/summary and
a Bio Lime highlight block — **the print palette used on slides**, which v2 explicitly replaced. v2
says: *"Twelve layouts in the slide master. New slide → Layout → pick one. Never build a slide from
scratch."* Architecture v2 says the builder *"should be updated to build against this template
rather than generating decks from scratch."* It was not updated.

**Consequence:** any deck built today through the installed skill is off-brand against two newer
standards, and off-brand again against this specification's palette.

**PROPOSED resolution:** `build-presentation` builds from the template. The from-scratch generator
is archived. Note this compounds with CONFLICT-01 and -02 — the template's `tokens.js` still holds
the old palette, so the template itself needs regenerating once the palette conflicts close.

---

## CONFLICT-10 — The Anti-AI-Slop Standard is unreachable by the skill that mandates it

**Sources:** `shull-studio` Step 0.3 · `anti-ai` (20 lines) · `ANTI_AI_SLOP_EDUCATOR_STANDARD.md`
(21.3 KB, Drive) · specification Part 20.

`shull-studio` Step 0 says load the Anti-AI-Slop Standard and *"Do not skip 3."* It offers two
paths, and **both fail in Claude Code**:

- "If `ANTI_AI_SLOP_EDUCATOR_STANDARD.md` is in Project Knowledge, search it" — Claude Code cannot
  read Project Knowledge.
- "If not, `references/anti-slop-condensed.md` in this skill carries the operative rules" — that
  file **does not exist** (see CONFLICT-14).

The only *installed* skill named `anti-ai` is 20 lines about React, Tailwind, and Supabase null
handling. It is a UI system. It says nothing about documents, slides, voice, or padding.

Part 20 makes anti-slop a **core** standard, and Part 5 makes "generic with no soul" a central
quality-control principle. Right now the system's most important quality standard is a 21 KB file
sitting in Drive that no skill can reach.

**PROPOSED resolution:** the Drive standard's content becomes `standards/ANTI_AI_SLOP_STANDARD.md`
in the repository — reachable, version-controlled, diffable. The legacy `anti-ai` UI rules become a
clearly-scoped "interactive and digital output" section within it rather than a competing document.
A thin `anti-ai-slop` skill points at the standard and carries the runnable checklist.

**This is the highest-value, lowest-cost fix in the migration.**

---

## CONFLICT-14 — Ten referenced files do not exist

**Sources:** `shull-studio` §§2, 4, 5, Step 0 · `SHULL_Slide_System_v2.md` §5 ·
`SHULL_Cowork_Folder_Organization_v2.md` · `shull-course-librarian` §§3, 4 · the colour memo §3.

| File | Referenced by | Present |
|---|---|---|
| `references/connectors.md` | `shull-studio` §5 | ✗ |
| `references/file-routing.md` | `shull-studio` §2, librarian §3 | ✗ |
| `references/calendar-2026-2027.md` | `shull-studio`, librarian §4 | ✗ |
| `references/anti-slop-condensed.md` | `shull-studio` Step 0.3 | ✗ |
| `assets/shull_brand.css` | `shull-studio` §4 and routing table | ✗ |
| `assets/build_pdf.py` | `shull-studio` §4 | ✗ |
| `SHULL_Color_Palette_Library.md` | colour memo §3 and §1a — *"do not invent a fourth option without checking there first"* | ✗ **not in Drive** |
| `SHULL_Image_Prompt_Pack.md` | Slide System v2 §5, Architecture v2, Folder Org v2 | ✗ **not in Drive** |
| `SHULL_Physics_Unit_Map_1.pdf` | Course maps B.1, librarian absorptions | ✗ **not in Drive** |
| `SHULL_Physics_Pacing_Guide_20262027.pdf` | Librarian absorptions, course maps B.7 | ✗ **not in Drive** |

The specification counted five. There are ten.

Two are especially consequential. `SHULL_Color_Palette_Library.md` was supposed to be the single
place where the selected palette *and* the archived alternates live — the exact artifact that would
have prevented CONFLICT-01, since Quantum Gold's back-burner status would have been visible in one
file. It was specified and never created. And `SHULL_Physics_Unit_Map_1.pdf` is the cited source of
a curriculum map now treated as CONFIRMED — a map whose source document cannot be located.

**PROPOSED resolution:** in SHULL OS every one of these becomes either a real repository file or a
deleted reference. `brand/palette-archive/README.md` is the palette library, done properly. A
broken-reference check belongs in the Janitor's standing sweep so this class of defect surfaces
automatically.

---

## CONFLICT-23 — `shull-chemistry-guidelines` was ordered trimmed and was not trimmed

**Sources:** `SHULL_System_Governance.md` §8 (Chemistry table) vs. the installed 777-line skill.

Governance §8 lists seven specific cuts, dated 2026-09-05, and `CHEM_DECISIONS.md`'s decision log
records the content as already moved. **All seven sections are still in the installed file:**

| Governance says | Still present? |
|---|---|
| §4 curriculum map → move to `CHEM_DECISIONS.md` | ✗ still in the skill |
| §7 calendar and pacing → move | ✗ still there |
| §§I, J, G, H grading, late work, quiz/test structure → move | ✗ still there |
| §6 reference packet → move | ✗ still there |
| §12 brand section duplicating `shull-studio` §1 → **cut entirely** | ✗ still there |
| §§10, 11 lab template and graphing → **keep** | ✓ correctly kept |
| §16 Chemistry 9.6 → confirm or close | ✗ still open in the skill |

The 9.6 question is now **answered** — the course maps show the per-unit badges sum to 90 only when
U9 = 5, so there is no 9.6 — but it remains listed as open in `CHEM_DECISIONS.md`, `shull-studio`
§7, and `shull-course-librarian`'s standing items. **One resolved fact, three files still calling it
open.**

**What this proves.** A to-do list inside a document is not a mechanism. Governance §8 is a
well-written fix list that nobody worked through, and the drift it describes is still live two days
later.

**PROPOSED resolution:** in SHULL OS, `validate_layers.py` makes this a build failure rather than a
table row. That is the difference between a rule and an enforced rule.

---

## CONFLICT-24 — Chemistry grading: two framings that may or may not be the same thing

**Sources:** `CHEM_DECISIONS.md` vs. `SHULL_Course_Maps.md` A.6.

| Source | Statement |
|---|---|
| Confirmed gradebook weights | Tests 55% · Quizzes 20% · Labs & Projects 15% · Homework 7% · Binders 3% |
| `CHEM_DECISIONS.md` | "Daily practice … ~10% of the overall course grade" |

Homework 7 + Binders 3 = 10, so these *may* reconcile. But "daily practice" and "homework +
binders" are not obviously the same category — a binder check is not daily practice, and daily
practice done in class is not homework.

The course maps file flags this itself: *"Confirm which framing is the real gradebook before either
is written into the repo."*

**Decision needed:** which framing is the gradebook, and does the 5-point daily-practice rubric roll
up into Homework, Binders, or both?

---

## CONFLICT-25 — Geology has no section numbers, and the code check requires them

**Sources:** `shull-geology-guidelines` §10 item 4 · `SHULL_Course_Maps.md` C.3 · `shull-studio` §2.

`U#/S#.#` is described as universal. Geology has unit numbers but **no section numbers within
units**. The open question is whether section-level numbering is even useful given the course's
activity-driven, less lecture-sequenced structure.

**Why it matters mechanically:** `validate_codes.py` is designed to fail any document whose
`U#/S#.#` code is absent from the matching decisions file. **With no Geology section numbers, that
check fails every Geology document** — or has to be special-cased, which weakens it everywhere.

**Options:** (a) Geology gets section numbers, retrofitted; (b) Geology uses unit-level codes only
(`U5`) and the validator learns a per-course code shape; (c) Geology uses a different code entirely.

**Decision needed** before Phase 9 (the validator) and Phase 12 (`GEO_DECISIONS.md`).

---

## CONFLICT-26 — The Gizmos rule vs. the built Geology materials

**Sources:** `shull-geology-guidelines` §§3, 9 · `SHULL_System_Governance.md` §8 · course maps C.4.

The skill states it twice, once as an explicit Do-Not: *"Do not default to or recommend Gizmos"* —
students get little from it and tend to cheat through it.

**The built U1 S1.2 guided notes and a built worksheet both use the Red Shift Gizmo.** The rule and
the shipped material contradict each other, and the material is already in front of students.

**Decision needed:** keep the Red Shift Gizmo as a **named, documented exception** (the rule stands,
this one activity is carved out), or replace the activity. Governance §8 has carried this since
2026-09-05.

---

# NON-BLOCKING — may remain provisional

## CONFLICT-13 — Four near-identical dark neutrals

`#14161B` Asphalt Black · `#2A2F33` Charcoal · `#2E3338` Graphite · `#2C3338` Slate · plus
`#2C3B2D` Slate Stone (green-tinted, base palette) and `#0B0A0E` Ink Black (Quiet Voltage) and
`#111111` Ink (Slide System v2).

Charcoal, Graphite, and Slate differ by at most four points per channel — visually
indistinguishable, and each was assigned to a different course purely to give each palette its own
row in a table. Part 8 says *"Do not invent additional neutral colors unnecessarily"* and preserves
only Asphalt Black and Graphite.

**PROPOSED:** keep `#14161B` and `#2E3338`. Archive the rest. Recorded because Part 8 explicitly
asked for conflicting neutral values to be identified.

## CONFLICT-16 — Ink-saving vs. "white is the default background"

Not a contradiction — both point the same way — but a **strength mismatch**. Part 15 says student
materials should prioritize efficient ink usage and that white should normally be the background.
`shull-studio` §1 carries a much stronger, much more specific rule: no full-page banners, no shaded
section backgrounds, no solid-fill headers, colour as a thin accent only, hairline table borders,
outlined chips and number squares, full-colour variants never shipped as the default print file.

**Risk:** a migration that reads only Part 15 will produce a design system with a weaker ink rule
than the one currently in force, and printed materials will quietly get more expensive.

**PROPOSED:** the ink-saving block carries into `SHULL_DESIGN_SYSTEM.md` **verbatim and at full
strength**, with the measurement method from Quiet Voltage §5 (percent pixels marked) added to the
QA gate.

## CONFLICT-17 — The Atom Seal watermark across three courses

Three skills specify an **Atom Seal** watermark at 12–15% opacity. `shull-geology-guidelines` §7
also says *"Reserve the atom/beaker/molecule icon set for Chemistry"* and favour geology icons —
and then specifies the Atom Seal watermark for Geology anyway.

An atom watermark on a Geology handout is a small thing, but it is exactly the kind of detail Part
30 is about: Geology should look like SHULL Studio Geology.

**PROPOSED:** one seal *system*, three marks — atom (Chemistry), a Physics mark, a geology-hammer
or strata mark (Geology). Same size, same opacity, same placement. Non-blocking; revisit at the
first weekly review.

## CONFLICT-19 — Guided-notes footer at 6.4pt vs. the 8pt print floor

`shull-studio` §1: *"No text below 8pt on a student page except the running footer."*
`shull-guided-notes-builder`: running footer at **6.4pt**.

The exception clause covers it, so this is legal — but 6.4pt is small even for a footer, and the
rule's phrasing ("except the running footer") reads as an exemption without a floor of its own.

**PROPOSED:** set an explicit footer floor (7pt suggested) so the exception is bounded.

## CONFLICT-20 — Notes scaffolding is indexed to unit number, and the courses have different unit counts

The ladder is heavy at U0–3, medium U4–8, light U9+. Chemistry has 16 units; Physics has 11;
Geology has 10. **The same unit number lands at a different point in the school year in each
course.** Physics U9 arrives much later in the year, proportionally, than Chemistry U9 — so a
Physics U9 packet would be "light" at a point where Chemistry would still be "medium."

The course maps file flags this and says the ladder *"should probably be re-indexed to calendar
position rather than unit number for Physics, but that is Matt's call."*

**PROPOSED:** index the ladder to **fraction of the course elapsed** (first 20% heavy, 20–55%
medium, 55%+ light), which is course-count-independent and preserves the intent. Non-blocking
because Chemistry — the only course currently building notes at scale — is unaffected.

## CONFLICT-21 — Do labs have data tables or not?

`CHEM_DECISIONS.md` student lab template: *"Data/Observations (table, precise qualitative
description prompts, units in headers)."*
`SHULL_Studio_System_Spec.md` §6.5: *"**No write-lines, answer spaces, or data tables belong on lab
handouts.** The pre-lab must instruct students to draw their own data tables before class."*

Both describe the Chemistry lab template. One puts a table on the handout; the other forbids it.

The likely reconciliation is that the *handout* names what data to collect and the *notebook*
carries the table — but the decisions file says "table," not "table specification." Worth settling
before `build-lab` is written, since it changes the output.

## CONFLICT-27 — The QA toolchain is specified but unverified

`Python + WeasyPrint · Node + docx/pptxgenjs · pdf2image/pdftoppm · cairosvg · soffice --headless`.

None of this was verified present in the build container during this pass. The QA gate's step 1 —
"render and look at it" — is the load-bearing step of the entire quality system, and it depends
entirely on `soffice` and `pdf2image` existing.

**PROPOSED:** Phase 9 verifies each tool and records what is actually installed. If `soffice` is
absent, the QA gate needs a different rasterization path and that changes the plan.

---

# DEPRECATED — old decisions superseded by current ones

These need **recording**, not deciding. Each is archived, not deleted (Part 47).

## CONFLICT-11 — Dark ground as the projection default

**Superseded by:** specification Part 6.

| Superseded | Detail |
|---|---|
| Slide System v2 §1 | Projected slides on ink black `#111111` with amber |
| `shull-studio` §1a | All three per-course slide palettes sit on Asphalt Black `#14161B` |
| Quiet Voltage | Runs light Porcelain by default — already consistent with Part 6 |

Part 6: white/light is the presentation default; dark is an occasional tool for title slides,
dividers, major visual moments, and image-heavy slides.

**Note the near-agreement.** `slide-standard.md` and Slide System v2 §4 both already say *"Dark
grounds are structural only — unit title, section divider, unit summary, index. Content slides are
light."* That is Part 6's rule, arrived at independently. The genuine change is that the per-course
memo made the whole deck dark-ground; Part 6 pulls it back to light.

**Action:** archive the dark-default framing; keep "dark grounds are structural" as INHERITED.

## CONFLICT-12 — Parchment as the default background

**Superseded by:** specification Part 7.

Parchment `#EDF0E5` is the default light background in `shull-studio` §1, the default content-slide
ground in `slide-standard.md`, and the print ground in Slide System v2 §1. Part 7 keeps it as an
official colour but demotes it to a special-purpose branded surface, with White `#FFFFFF` as the
default.

**Action:** archive Parchment-as-default; keep Parchment as a token with its new, narrower scope
documented.

## CONFLICT-15 — The no-retrofit policy

`shull-studio` colour memo §2: the per-course palette *"applies to new slide decks only. Do not
retrofit existing decks (Chemistry U7, U10) to match."*

The specification does not address retrofitting. But the same question now applies far more widely:
the built Geology U1 packet uses the earth palette; eight Physics Unit 1 images were regraded to
Quiet Voltage; the Chemistry U7 and U10 decks use the original base palette.

**PROPOSED:** carry the no-retrofit principle forward explicitly — new work uses the new system,
existing work stays as-is unless you ask for a rebuild — and record which existing materials are
on which superseded palette, so a future audit does not flag them as defects. **Without that
record, the Janitor's first sweep will report every existing deliverable as off-brand.**

## CONFLICT-18 — Practice-set tag-pill colours

WARM-UP tinted green · PRACTICE white · CHALLENGE tinted earth · MULTI-TOPIC solid dark. These
colours belong to the base palette and do not survive the new course-colour system.

**Note what must survive:** the *structure* (four tiers, single thin rule, one solid-fill tier) and
the Quiet Voltage refinement that tag pills are separated by **border colour as well as fill**, so
categories never differ by fill alone in grayscale.

**Action:** re-derive the four tiers from each course's new palette; keep the structure and the
border-plus-fill rule.

## CONFLICT-22 — Hexes typed by hand in multiple files

**Superseded by:** specification Part 39 — "Do not create multiple competing palette files."

The base palette table is typed by hand in three skills. `tokens.js` and `tokens.phys.js` hold it
again in Drive. The system spec's own closing note diagnoses this correctly:

> *"Every palette conflict in Part 10 exists because the same hex was typed into two files by
> hand."*

**Action:** `brand/tokens.json` is the only place a hex is written. CSS, `tokens.js`, and the
documentation are generated from it. `scripts/validate_tokens.py` fails the build on a raw hex
found outside `tokens.json`, `brand/palette-archive/`, and `legacy/`.

**Keep the good pattern:** `build.js` reading `process.env.SHULL_TOKENS` is exactly the right
shape — one build, per-course token overlays, no forked template. `tokens.json` should preserve it.

---

# Summary: the decision list

## Blocking (answer these first — nothing starts without them)

| # | Conflict | Question |
|---|---|---|
| 1 | CONFLICT-00 | Which repository does SHULL OS live in? |
| 2 | CONFLICT-01 | Physics palette: Quiet Voltage, Quantum Gold, or a hybrid? |
| 3 | CONFLICT-02 | Geology palette: does Terra Teal replace the earth palette in print too? |
| 4 | CONFLICT-03 | Geology unit numbering: Plate Tectonics U4 or U5? |
| 5 | CONFLICT-04 | Confirm the typography fallback ladder |
| 6 | CONFLICT-06 | Confirm the Drive structure stays as built; add `99 Archive/`? |
| 7 | CONFLICT-09 | Adopt the padded `SHULL_..._U##_S##.#` naming grammar? |

## Important (answer before Phase 12)

CONFLICT-05 (Physics map source PDF) · CONFLICT-07 (slide type scale) · CONFLICT-08 (template-based
deck building) · CONFLICT-10 (anti-slop standard location) · CONFLICT-14 (broken references) ·
CONFLICT-23 (Chemistry skill trim) · CONFLICT-24 (grading framing) · CONFLICT-25 (Geology section
numbers) · CONFLICT-26 (Gizmos exception)

## Non-blocking (recorded; revisit at the first weekly review)

CONFLICT-13 · 16 · 17 · 19 · 20 · 21 · 27

## Deprecated (record and archive; no decision needed)

CONFLICT-11 · 12 · 15 · 18 · 22

---

## A closing note on colour

Part 29 asked for special attention to colour conflicts, and it named the ones it knew about: Lab
Lime, Kinetic, Terra, amber-on-near-black, the print palette, previous Geology earth-tone and Terra
systems, and white being under-represented. Every one of those is real and appears above.

The inspection found **one more that Part 29 could not have known about** — Quiet Voltage — and it
is the most consequential of them, because it is the only superseded palette that was CONFIRMED,
measured, tokenized, and shipped, all within twenty-four hours of the specification that replaces
it.

The underlying cause is not indecision. It is that six palette decisions were recorded in six
different files across three storage systems — installed skills, Drive standards, and an unlabeled
memo appended to the bottom of a skill — with no single place that lists what is current and what
was passed over. `SHULL_Color_Palette_Library.md` was specified to be that place. It was never
created.

`brand/tokens.json` plus `brand/palette-archive/README.md`, in Git, with a validator that rejects a
hex typed anywhere else, is the fix.

