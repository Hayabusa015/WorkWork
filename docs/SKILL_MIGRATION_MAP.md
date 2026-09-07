# SHULL OS — Skill Migration Map

**Prepared:** 2026-09-07
**Purpose:** Map every legacy skill and standards document to its SHULL OS destination.
**Governing rule (Part 26):** *Do not copy legacy skills blindly.* Every legacy artifact is
**decomposed**, not moved — rules go to standards, course facts go to course decisions, procedure
goes to a new focused skill, and anything superseded goes to an archive that is never deleted.

Companions: `SHULLOS_IMPLEMENTATION_PLAN.md` · `LEGACY_SKILL_AND_DESIGN_AUDIT.md` ·
`CONFLICT_REPORT.md`

---

## The decomposition rule

Every legacy skill is a mixture of four things that the two-layer model says must live apart:

```
            ┌─────────────── a RULE          → standards/ or brand/
LEGACY      ├─────────────── a COURSE FACT   → courses/<course>/DECISIONS.md
SKILL   ────┤
            ├─────────────── a PROCEDURE     → .claude/skills/<skill>/SKILL.md
            └─────────────── a DECISION      → governance/ + change-log/
                                                (or brand/palette-archive/ if superseded)
```

Nothing is carried across as-is. A skill that "just needs a light edit" is a skill that was already
obeying the rule — and inspection found none that were.

**Two hard constraints on this map:**

1. **Nothing is deleted.** Every legacy skill is snapshotted verbatim into `legacy/skills/` and
   every Drive standard into `legacy/drive-standards/` before any decomposition begins (Phase 7,
   step 3–4). The installed skills stay installed and untouched until Phase 14 passes.
2. **A conflicted rule does not migrate.** Where a rule is marked CONFLICT in the audit, the
   destination cell says **BLOCKED** and names the question. It does not get a best guess.

---

## PART 1 — Master map at a glance

| Legacy artifact | → Standards / brand | → Course decisions | → New skill | → Archive |
|---|---|---|---|---|
| `shull-studio` | DESIGN_SYSTEM, tokens, NAMING, QA_GATE, VOICE, DRIVE_ARCHITECTURE | — | `apply-shull-design`, `naming`, `build-document` | base palette, colour memo |
| `shull-chemistry-guidelines` | — *(brand section cut)* | **chemistry/DECISIONS.md** | `build-lab` (§10), `verify-content` (§11) | duplicate brand + typography |
| `shull-physics-guidelines` | — | **physics/DECISIONS.md** | `build-document` (worksheet rule) | §3 NEEDED, §4 carried-over, §5 sig-fig line |
| `shull-geology-guidelines` | — | **geology/DECISIONS.md** *(numbering BLOCKED)* | `build-document` (activity formats) | palette table |
| `shull-slide-deck-builder` + `slide-standard.md` | DESIGN_SYSTEM (slide geometry) | — | **`build-presentation`** | from-scratch generator, old type scale |
| `shull-guided-notes-builder` | DESIGN_SYSTEM (notes layout) | scaffolding index per course | `build-document` | — |
| `test-quiz-generator` + 3 refs | — | assessment shape per course | **`build-assessment`** | — |
| `shull-course-librarian` | — | — | **Librarian + Janitor agents**, `retrieve-`/`shelve-drive-file` | — |
| `shull-student` | — | — | **Researcher + Secretary agents**, `weekly-system-review` | — |
| `anti-ai` (20 lines) | **ANTI_AI_SLOP_STANDARD** §UI | — | `anti-ai-slop` | — |
| `shull-practice-set-generator` *(missing)* | — | — | `build-document` §practice-set | — |
| `SHULL_System_Governance.md` | **GOVERNANCE, CHANGE_CONTROL** | — | — | §8 fix list → change-log |
| `SHULL_Slide_System_v2.md` | DESIGN_SYSTEM (slides), tokens | — | `build-presentation` | amber medium split |
| `SHULL_Studio_Architecture_v2.md` | — | — | — | **whole file → archive** (status doc) |
| `SHULL_Cowork_Folder_Organization_v2.md` | **DRIVE_ARCHITECTURE, NAMING** | — | `shelve-drive-file` | — |
| `ANTI_AI_SLOP_EDUCATOR_STANDARD.md` | **ANTI_AI_SLOP_STANDARD, VOICE** | — | `anti-ai-slop` | — |
| `SHULL_PHYS_Palette_QuietVoltage.md` | **BLOCKED — CONFLICT-01** | physics brand exception | — | palette-archive if superseded |
| `CHEM_DECISIONS.md` | — | **chemistry/DECISIONS.md — adopt wholesale** | — | — |
| `_Brand/Templates/tokens.js`, `tokens.phys.js`, `build.js` | **tokens.json** (generated from) | — | `build-presentation` | — |

---

## PART 2 — Skill-by-skill decomposition

### 2.1 `shull-studio` (292 lines) — the biggest decomposition

The router-and-everything-else skill. It holds brand, codes, routing, connectors, voice, the
practice-set spec, and the QA gate. Under the one-fact-one-home rule it must become **six
standards, three skills, and one archive entry**.

| Legacy section | Content | → Destination | Class |
|---|---|---|---|
| Step 0 (load order) | Context-loading sequence | `CLAUDE.md` + Overseer agent | INHERITED |
| Step 0.3 | "Load the Anti-AI-Slop Standard. Do not skip 3." | Overseer; **the pointer is fixed** — CONFLICT-10 | INHERITED |
| Routing table | Request → specialist skill | **Overseer agent** | INHERITED |
| §1 six-token palette | Deep Forest, Slate Stone, Moss, Warm Earth, Bio Lime, Parchment | `brand/palette-archive/base-parchment-bio-lime.md` | DEPRECATED |
| §1 typography ladder | Trade Gothic Next → Oswald/Inter → Poppins/Lato → Liberation | `brand/SHULL_DESIGN_SYSTEM.md` — **BLOCKED, CONFLICT-04** | CONFLICT |
| §1 visual rules | Grayscale, one accent word, watermark, print weights, size floors, real tables | `brand/SHULL_DESIGN_SYSTEM.md` | INHERITED |
| §1 ink-saving block | The full hard rule for printed material | `brand/SHULL_DESIGN_SYSTEM.md` — **verbatim, full strength** (CONFLICT-16) | INHERITED |
| §2 doc-code grammar | `U#/S#.#`, filename pattern, chip, number squares | `standards/NAMING.md` — **BLOCKED on padding, CONFLICT-09** | CONFLICT |
| §3 voice | The short version | `standards/VOICE.md` | INHERITED |
| §4 practice-set v2 | 8 questions, 2 pages, tag pills, work boxes, `.write`/`.math` | `.claude/skills/build-document/` §practice-set | INHERITED |
| §5 connectors | Hand-built default, Higgsfield policy, Mobbin policy | `standards/` + Designer agent | INHERITED |
| §6 QA gate | Nine steps | **`standards/QA_GATE.md`** + `audit-deliverable` | INHERITED |
| §7 open items | 9.6, code grammar, lab placements | `courses/*/DECISIONS.md` open questions; **9.6 is resolved** (CONFLICT-23) | DEPRECATED |
| **Appended colour memo** | The unlabeled 2026-09-06 block after §7: per-course palettes + 6 back-burner alternates | `brand/palette-archive/per-course-2026-09-06.md` — **this is the file that proves Quantum Gold was a rejected alternate** | DEPRECATED / evidence |

**Note on the appended memo.** It sits below `## 7` with no heading level of its own, no frontmatter
reference, and no date in the skill's own structure — it reads as a paste, not an edit. Anything
that arrived that way is a candidate for having been lost on the next reinstall. Preserving it in
Git is itself part of the value of this migration.

**Not migrating:** `references/connectors.md`, `references/file-routing.md`,
`references/calendar-2026-2027.md`, `references/anti-slop-condensed.md`, `assets/shull_brand.css`,
`assets/build_pdf.py` — **none exists** (CONFLICT-14). Their *intended* content is reconstructed
from the sources that survived, and the dangling references are deleted rather than carried.

---

### 2.2 `shull-chemistry-guidelines` (777 lines) — mostly already relocated

Governance §8 ordered seven cuts on 2026-09-05 and `CHEM_DECISIONS.md` records them as done. **The
installed skill was never trimmed** (CONFLICT-23). This migration finishes the job.

| Legacy section | Content | → Destination | Class |
|---|---|---|---|
| §1 how to use / decision priority | Priority order and confidence labels | `governance/GOVERNANCE.md` | INHERITED (duplicate) |
| §2 course identity | Population, philosophy, time structure | `courses/chemistry/DECISIONS.md` | LOCKED |
| §3 A–R interview | Section shape, practice progression, notes, PPT, handouts, answers, quizzes, tests, grading, late work, labs, differentiation, demos, connections, organization | `courses/chemistry/DECISIONS.md` — **already there** | LOCKED |
| §3 I + J | Daily-practice ~10%; late-work scale | `courses/chemistry/DECISIONS.md` — **BLOCKED on framing, CONFLICT-24** | CONFLICT |
| §4 curriculum map | Units 0–15, 90 sections | `courses/chemistry/DECISIONS.md` — **already there** | LOCKED |
| §5 sequencing rules | Delay heavy math; sig figs after midyear | `courses/chemistry/DECISIONS.md` | LOCKED |
| §6 reference packet | Periodic table, polyatomics, solubility, percent error | `courses/chemistry/DECISIONS.md` | LOCKED |
| §7 pacing and calendar | Full 2026–27 calendar, MP deadlines, pacing guide | `courses/chemistry/DECISIONS.md` | LOCKED / pacing PROVISIONAL |
| §8 section production system | The section bundle, teacher-page standard | `workflows/build-deliverable.md` | INHERITED |
| §9 assessment construction | Quality rules, study guides, cumulative recall | `.claude/skills/build-assessment/` | INHERITED |
| **§10 lab design system** | Student + teacher lab templates | **`.claude/skills/build-lab/`** — governance §8 says *keep in the skill; build structure, not course content* | INHERITED |
| **§11 data and graphing** | Graph requirements, reasoning, error analysis | **`.claude/skills/verify-content/`** — same reasoning | INHERITED |
| **§12 SHULL Teacher Brand** | Palette table + typography + visual rules | **CUT ENTIRELY.** Governance §8: *"the studio owns brand."* | DEPRECATED (duplicate) |
| §13 tone and writing | Voice rules | `standards/VOICE.md` (duplicate) | INHERITED |
| §14 file consistency | `CHEM-EA-S 01–19` legacy codes | `brand/palette-archive/`'s sibling: `standards/superseded/` | ARCHIVE |
| §15 do-not rules | Sixteen prohibitions | Split: course-specific → DECISIONS; universal → ANTI_AI_SLOP | INHERITED |
| §16 future work | 9.6, code grammar, lab placements | Open questions; **9.6 resolved** | DEPRECATED |

**Result:** the 777-line skill becomes a course decisions file that already exists, two focused
skills, and roughly 40 lines of pointer.

---

### 2.3 `shull-physics-guidelines` (167 lines)

| Legacy section | Content | → Destination | Class |
|---|---|---|---|
| §1 confidence labels | CONFIRMED / CARRIED OVER / PROVISIONAL / NEEDED | `governance/GOVERNANCE.md` (mapped to Part 27 labels) | INHERITED |
| §2 course identity | Four unanswered questions about rigor and population | `courses/physics/DECISIONS.md` **open questions** | UNKNOWN |
| **§3 unit map "NEEDED"** | *"There is no confirmed Physics unit list"* | **DO NOT MIGRATE.** Replaced by the confirmed 11-unit / 48-section map | **DEPRECATED** |
| §4 shared standards | Practice progression, notes, slides, handouts, answers, differentiation, gradebook | **DELETE.** Governance §8: *"They belong to `shull-studio` and are duplicated here."* Gradebook weights → open question | DEPRECATED |
| **§5 physics rules** | Units, vectors, FBDs, graph interpretation, sign conventions, misconception distractors, labs | `courses/physics/DECISIONS.md` — governance §8 says keep as discipline build rules | **LOCKED** |
| §5 sig-fig sentence | *"follow the rules already taught in Chemistry — do not re-teach"* | **DO NOT MIGRATE.** Contradicts `U0/S0.2` (CONFLICT-05) | **DEPRECATED** |
| §6 Ohio standards | Tag when asked; say so if a code is uncertain | `.claude/skills/build-assessment/` | LOCKED |
| §7 open items | Six items, first now resolved | `courses/physics/DECISIONS.md` open questions | INHERITED |
| §8 worksheets | **No work areas; prior-knowledge and equations block at top** | `courses/physics/DECISIONS.md` | **LOCKED** |
| *(new)* | 11 units / 48 sections, four phases, from the course maps | `courses/physics/DECISIONS.md` curriculum map | LOCKED — **but source PDF is missing, Q-14** |

---

### 2.4 `shull-geology-guidelines` (305 lines) — the blocked course

| Legacy section | Content | → Destination | Class |
|---|---|---|---|
| §1 how to use | Decision priority and labels | `governance/GOVERNANCE.md` | INHERITED (duplicate) |
| §2 course identity | Not "Chemistry with rocks"; visuals over text; cut/colour/glue first-class; graphic organizers default; lower reading level | `courses/geology/DECISIONS.md` | **LOCKED** |
| §3 activities not labs | Rocks and minerals only; simulations; **no Gizmos** | `courses/geology/DECISIONS.md` — **Gizmos rule BLOCKED, CONFLICT-26** | LOCKED / CONFLICT |
| §4 assessment | Single-day, MC and matching, no calculation-heavy FR, organizers count | `courses/geology/DECISIONS.md` | LOCKED |
| §4 carried-over policies | Grading, late work, no curve/retakes | `courses/geology/DECISIONS.md` marked PROVISIONAL | PROVISIONAL |
| **§5 curriculum map** | Units 1–10 with U4/U8/U9 numbering | **BLOCKED — CONFLICT-03.** Unit *titles and content* migrate; **numbering does not** | **CONFLICT** |
| §5 U7–U10 expansions | Caves, Glacial, Oceans, Resources | `courses/geology/DECISIONS.md` marked PROVISIONAL | PROVISIONAL |
| §6 differentiation | Modified / Challenge, used more here | `courses/geology/DECISIONS.md` | PROVISIONAL |
| **§7 brand — palette table** | *"identical to Chemistry"* | **CUT.** Governance §8 already ordered it | **DEPRECATED** |
| §7 typography restatement | Third copy of the ladder | **CUT** — duplicate | DEPRECATED |
| §7 icon set | Hammer, magnifier, mountain, strata, wave, compass, timeline, map; reserve atom/beaker for Chemistry | `courses/geology/DECISIONS.md` + DESIGN_SYSTEM (CONFLICT-17) | **LOCKED** |
| §7 cut/colour/glue specs | Fold lines, cut margins, non-bleeding colour regions | `.claude/skills/build-document/` §activity | LOCKED |
| §7 asset types | Foldables, sequencing, labeling, organizers, timeline pages, maps | `courses/geology/DECISIONS.md` | LOCKED |
| §8 tone | Same voice, simpler sentences, lower reading level | `courses/geology/DECISIONS.md` | LOCKED |
| §9 do-not rules | Nine prohibitions | Split by scope | LOCKED |
| §10 open items | Five, including numbering and section codes | `courses/geology/DECISIONS.md` open questions | UNKNOWN |

> **`courses/geology/DECISIONS.md` is written in Phase 12 but is written *incomplete on purpose*.**
> Until CONFLICT-03, -25 and -26 close, it holds the confirmed unit titles with numbering explicitly
> marked CONFLICT, and **no Geology document is built against any `U#` code.** The empty
> `Geology/` Drive folder stays empty.

---

### 2.5 `shull-slide-deck-builder` + `references/slide-standard.md` → `build-presentation`

The one legacy skill that must be **rebuilt, not decomposed**, because what it builds was replaced.

| Legacy content | → Destination | Class |
|---|---|---|
| Deck scope: one section, 12–20 content slides | `.claude/skills/build-presentation/` | INHERITED |
| Master sequence + worked-example→solution pairing | `build-presentation` + QA_GATE | **LOCKED** |
| Slide geometry (16:9, bands, columns, rail, chip) | `brand/SHULL_DESIGN_SYSTEM.md` | INHERITED |
| **Type scale (44–54 / 30–36 / 20–22 / 19–24 …)** | **BLOCKED — CONFLICT-07.** v2's scale proposed | CONFLICT |
| **16pt hard floor** | DESIGN_SYSTEM | **LOCKED** — all sources agree |
| **The reserved-height rule** | `build-presentation` | **LOCKED** — three sources; caused a real shipped defect |
| Hard line caps (3/5 bullets, 4 terms, 4 steps, 6 rows) | `build-presentation` | INHERITED |
| "Split the slide. Never shrink type to fit." | `build-presentation` + QA_GATE | **LOCKED** |
| Spacing values | DESIGN_SYSTEM | INHERITED |
| Circles on dividers vs. squares in print | DESIGN_SYSTEM | INHERITED |
| Card colour logic (state the rule on the Slide Key slide) | `build-presentation` | INHERITED |
| Palette assignment (Parchment ground, Deep Forest dark, Bio Lime highlight) | `brand/palette-archive/` | **DEPRECATED** |
| **Build from scratch** | **DO NOT MIGRATE** — v2 mandates the twelve-layout template (CONFLICT-08) | **DEPRECATED** |
| QA raster checklist | `standards/QA_GATE.md` | INHERITED |
| *(from v2)* twelve layouts, 09/10 pairing, empty work areas, layout 12 deleted before class | `build-presentation` | INHERITED |
| *(from v2)* `SHULL_TOKENS` env-var token indirection | **`brand/tokens.json` design** — keep this pattern | INHERITED |

---

### 2.6 `shull-guided-notes-builder` → `build-document` §guided-notes

Cleanest legacy skill. Near-complete carry-over.

| Legacy content | → Destination | Class |
|---|---|---|
| "The notes and the deck are one object" | `build-document` | INHERITED |
| Locate the section deck first | `build-document` | INHERITED |
| **Scaffolding ladder (U0–3 / U4–8 / U9+)** | `build-document`; **index BLOCKED per course, CONFLICT-20** | CONFLICT |
| Cornell layout (0.6" margins, 2.0"/4.9" columns, 1pt rule) | DESIGN_SYSTEM | INHERITED |
| Section starts a new page; ends with summary + self-check | `build-document` | INHERITED |
| Open bordered box + `SHOW WORK HERE`; never ruled lines for math | `build-document` | INHERITED |
| Blanks sized to the expected answer | `build-document` | INHERITED |
| Must-write left-rule mirroring the deck's highlight block | `build-document` | INHERITED |
| `NOTICE THIS` misconception margin notes | `build-document` | INHERITED |
| Always two files: student + `_Key`, generated from one source | `build-document` + QA_GATE | **LOCKED** |
| Footer at 6.4pt | `build-document` — see CONFLICT-19 | NON-BLOCKING |
| Rule colour Moss Green | `brand/palette-archive/` | DEPRECATED |

---

### 2.7 `test-quiz-generator` + 3 references → `build-assessment`

Clean, complete, and the only legacy skill whose reference files all exist.

| Legacy content | → Destination | Class |
|---|---|---|
| `references/question-design.md` | `.claude/skills/build-assessment/references/` | INHERITED |
| `references/formatting-spec.md` | `build-assessment` + DESIGN_SYSTEM (brand parts) | INHERITED |
| `references/ohio-standards.md` | `.claude/skills/verify-content/references/` | INHERITED |
| Item → learning target → standard mapping | `build-assessment` | INHERITED |
| "A wrong standard code is worse than none" | `build-assessment` | **LOCKED** |
| Every calculation solved during generation | `build-assessment` + QA_GATE | INHERITED |
| Misconception distractors, no all/none-of-the-above, no trick wording | `build-assessment` | INHERITED |
| Parallel versions: reorder, change values, swap scenarios, **re-solve each** | `build-assessment` + QA_GATE | INHERITED |
| Key contents (answer, points, worked solution, model responses, standard code) | `build-assessment` | INHERITED |
| Course assessment shapes (Chem two-day A–D; Geo single-day MC) | `courses/*/DECISIONS.md` — **not the skill** | LOCKED |

---

### 2.8 `shull-course-librarian` → **two agents plus two skills**

The most valuable legacy artifact, and the one that becomes agents rather than a skill. Its four
jobs split cleanly along the Part 3 boundary: *planning and filing* is the Librarian; *finding what
is broken* is the Janitor.

| Legacy content | → Destination | Class |
|---|---|---|
| **Standing Project Knowledge audit on every invocation** | **Janitor agent** — becomes a repo + Drive audit | **LOCKED** |
| The five audit checks (absorbed, contradicted, superseded, orphaned, internally conflicting) | Janitor | INHERITED |
| Known-absorptions table | `change-log/` — **and it is the historical record that the librarian was right when two other files were wrong** | ARCHIVE |
| "Never delete, edit, or silently ignore. Read and report only." | **Janitor authority** | **LOCKED** |
| "Flagged for removal is not done until Matt confirms. Flag it again next time." | Janitor + Secretary | **LOCKED** |
| Job 1 — unit build plans, build order, dependency table | **Overseer agent** + `workflows/build-deliverable.md` | INHERITED |
| Build order rationale (deck → notes → practice → lab → quiz → study guide → test) | `workflows/build-deliverable.md` | **LOCKED** |
| "Nothing later introduces a term that doesn't appear earlier" | Overseer + Auditor | **LOCKED** |
| Job 2 — gap and coverage audits | Janitor | INHERITED |
| Job 3 — filing and naming | **`shelve-drive-file`, `naming`** | INHERITED |
| "Don't batch-rename without confirmation — renames break links" | **Librarian authority** | **LOCKED** |
| Job 4 — pacing against the calendar and MP deadlines | Overseer + `courses/*/DECISIONS.md` | INHERITED |
| Consistency sweep table (palette, type, grayscale, ink, chips, codes, ID fields, footers, keys, voice) | **`audit-deliverable`** + Auditor | INHERITED |
| Severity vocabulary: blocking / should-fix / nice-to-have | Auditor and Janitor output | INHERITED |
| Standing open items | `courses/*/DECISIONS.md` open questions | INHERITED |
| "A 'build me all of Unit 5' request is a plan first. Show the plan, get a yes, then build." | **Overseer** | **LOCKED** |
| Orchestration: one section at a time, each QA'd before the next | Overseer | **LOCKED** |

---

### 2.9 `shull-student` → **Researcher + Secretary agents**

The legacy learning loop already has the right shape: draft, do not apply. It splits along the
Part 3 line — *finding* is the Researcher, *turning findings into reviewable proposals* is the
Secretary.

| Legacy content | → Destination | Class |
|---|---|---|
| Scheduled sweep of recent work | **Researcher agent** + `weekly-system-review` | INHERITED |
| `references/extraction-taxonomy.md` | `.claude/skills/weekly-system-review/references/` | INHERITED |
| **"Drafts changes for approval — does not silently rewrite confirmed policy"** | Researcher authority | **LOCKED** |
| "Hold any finding that conflicts with a CONFIRMED entry for my review" | Researcher → Secretary handoff | **LOCKED** |
| Sweep report format | `reports/` template | INHERITED |
| Drafting an updated guidelines file for re-upload | **Superseded** — the Secretary commits to Git instead | DEPRECATED |
| Per-course sweeps (past-chat search can't cross projects) | Plan §21 limitation; the repo-based sweep has no such boundary | INHERITED |

**The one real change.** The legacy sweep's output was *a file for you to re-upload*, because
nothing could write to a skill. In SHULL OS the output is *a PENDING proposal plus a branch*, and
your approval is what merges it. Same discipline, durable medium.

---

### 2.10 `anti-ai` (20 lines) → a section of the standard

| Legacy content | → Destination | Class |
|---|---|---|
| Reject generic template UI; no purple/indigo gradients, no floating pill cards, no SaaS landing-page layouts | `standards/ANTI_AI_SLOP_STANDARD.md` §Interactive | INHERITED |
| "Structure is information" — grid, dividers, alignment map to real data relationships | Same | INHERITED |
| "Density matters" — teachers need to see data, not scroll past whitespace | Same. **Note it agrees with Part 12's clean-and-moderately-dense rule.** | INHERITED |
| Educational/staff tools: high-contrast type, tabular structures, predictable nav, semantic borders | Same | INHERITED |
| Technical: one styling approach; safe null handling; semantic markup | Same | INHERITED |
| **The skill's scope** | **Widened.** It becomes one section of a standard that also covers documents, slides, and voice — see CONFLICT-10 | *the defect being fixed* |

---

### 2.11 `shull-practice-set-generator` — referenced, never installed

Nothing to migrate; the spec survived as `shull-studio` §4 and in the system spec §6.1. It becomes
`build-document` §practice-set. **The lesson is worth recording in the change log:** a routing table
pointed at this skill for weeks and it never existed. `validate_layers.py`'s sibling should also
check that every skill a router names is actually present.

---

## PART 3 — Drive standards documents

| Document | → Destination | Class |
|---|---|---|
| **`SHULL_System_Governance.md`** | **`governance/GOVERNANCE.md`** (§§1–4, 6, 10) + **`governance/CHANGE_CONTROL.md`** (§§5, 9). **Adopt, do not rewrite.** | **LOCKED** |
| §7 "What I cannot do" | Plan §21 limitations + `CLAUDE.md` | LOCKED |
| §8 migration fix list | `change-log/` as the historical record; **the unworked rows become the first Secretary proposals** | ARCHIVE + action |
| **`SHULL_Slide_System_v2.md`** §1 palettes | `brand/palette-archive/slide-system-v2-amber-split.md` | DEPRECATED |
| §1 Physics exception | **BLOCKED — CONFLICT-01** | CONFLICT |
| §2 twelve layouts | `.claude/skills/build-presentation/` | INHERITED |
| §3 type scale | DESIGN_SYSTEM — **BLOCKED, CONFLICT-07** | CONFLICT |
| §4 rules carried forward | DESIGN_SYSTEM | INHERITED |
| §5 images: generated-vs-built test, sourcing, spec, style block | DESIGN_SYSTEM + Designer agent | INHERITED |
| §6 template regeneration + `SHULL_TOKENS` | `brand/tokens.json` design + `templates/slide-template/src/` | INHERITED |
| **`SHULL_Studio_Architecture_v2.md`** | **Whole file → `legacy/drive-standards/`.** It is a status snapshot, not a standard. Its content is superseded by this plan. | ARCHIVE |
| — its ⚠ "skill files are not durable storage" warning | **`governance/GOVERNANCE.md` preamble** — the reason this repository exists | **LOCKED** |
| **`SHULL_Cowork_Folder_Organization_v2.md`** | **`standards/DRIVE_ARCHITECTURE.md`** + `standards/NAMING.md` | INHERITED — **BLOCKED vs. Part 23, CONFLICT-06** |
| **`ANTI_AI_SLOP_EDUCATOR_STANDARD.md`** (21.3 KB) | **`standards/ANTI_AI_SLOP_STANDARD.md`** + `standards/VOICE.md`. **Highest-value migration in the project** (CONFLICT-10) | **LOCKED** |
| **`SHULL_PHYS_Palette_QuietVoltage.md`** | **BLOCKED — CONFLICT-01.** Either `brand/tokens.json` as a Physics overlay, or `brand/palette-archive/phys-quiet-voltage.md` | CONFLICT |
| — its §3 measured contrast method | **`brand/SHULL_DESIGN_SYSTEM.md`** — *every palette carries measured contrast ratios* — regardless of which palette wins | **INHERITED** |
| — its §4 grayscale spacing method (≥20 grey levels) | DESIGN_SYSTEM | INHERITED |
| — its §5 ink measurement (% pixels marked) | `standards/QA_GATE.md` ink check | INHERITED |
| **`CHEM_DECISIONS.md`** | **`courses/chemistry/DECISIONS.md` — adopt wholesale.** Update: close the 9.6 question; resolve the grading framing (CONFLICT-24); rewrite "Course brand exceptions: None" once the palette conflicts close | **LOCKED** |
| `_Brand/Templates/tokens.js`, `tokens.phys.js` | **`brand/tokens.json`** becomes the source; these become *generated outputs* | INHERITED |
| `_Brand/Templates/build.js` | `templates/slide-template/src/build.js` | INHERITED |
| `_Brand/Templates/Lab/build_lab.py` + `README_Lab_Template.md` | **`.claude/skills/build-lab/`** — a lab template build was already in progress on 2026-09-07; Part 17 says preserve its structural strengths | PROVISIONAL — read before building |
| `_Brand/Templates/regrade.py`, `make_art.py`, `demo_u1.js` | `scripts/` or `templates/`; **`regrade.py`'s fate depends on CONFLICT-01** | PROVISIONAL |

---

## PART 4 — What each new artifact is assembled from

Read this direction when writing the file, rather than when reading the legacy.

| New artifact | Assembled from |
|---|---|
| `CLAUDE.md` | `shull-studio` Step 0 · Governance §§1–3, 7 · Architecture v2 ⚠ warning · Part 38 |
| `brand/SHULL_DESIGN_SYSTEM.md` | Part 46 locked list · `shull-studio` §1 (visual rules, ink block) · `slide-standard.md` (geometry) · Slide System v2 §§3–5 · Quiet Voltage §§3–5 (method) · Parts 5–20 |
| `brand/tokens.json` | Part 8 course colours · Part 6 White · Part 7 Parchment · Part 8 neutrals · `tokens.js` structure · `SHULL_TOKENS` overlay pattern — **BLOCKED on CONFLICT-01, -02, -04** |
| `brand/palette-archive/` | Base palette · Slide System v2 split · per-course memo + 6 alternates · Geology earth palette · Quiet Voltage *(if superseded)* |
| `standards/ANTI_AI_SLOP_STANDARD.md` | `ANTI_AI_SLOP_EDUCATOR_STANDARD.md` · system spec §7 · `anti-ai` (UI section) · Parts 5, 20 |
| `standards/VOICE.md` | Same, voice portions · `shull-studio` §3 · course tone sections |
| `standards/NAMING.md` | `shull-studio` §2 · Folder Org v2 · Part 25 *(as a recorded proposal)* — **BLOCKED on CONFLICT-09** |
| `standards/DRIVE_ARCHITECTURE.md` | Folder Org v2 · the verified live tree · Part 23 *(as a recorded proposal)* — **BLOCKED on CONFLICT-06** |
| `standards/QA_GATE.md` | `shull-studio` §6 · system spec §9 · `slide-standard.md` raster checklist · Quiet Voltage §5 ink measurement |
| `governance/GOVERNANCE.md` | `SHULL_System_Governance.md` §§1–4, 6, 10 · Parts 2, 4, 27, 28, 47 |
| `governance/CHANGE_CONTROL.md` | Governance §§5, 9 · Part 32 |
| `config/drive.json` | The eight verified folder IDs |
| `courses/chemistry/DECISIONS.md` | `CHEM_DECISIONS.md` (wholesale) + course maps Part A corrections |
| `courses/physics/DECISIONS.md` | Course maps Part B · `shull-physics-guidelines` §§5, 8 |
| `courses/geology/DECISIONS.md` | Course maps Part C · `shull-geology-guidelines` §§2–9 — **numbering BLOCKED** |
| `.claude/agents/overseer.md` | Part 3 Overseer · librarian jobs 1, 4 · orchestration · Part 34 |
| `.claude/agents/researcher.md` | Part 3 Researcher · `shull-student` |
| `.claude/agents/designer.md` | Part 3 Designer · Parts 5–20 · Slide System v2 §5 |
| `.claude/agents/librarian.md` | Part 3 Librarian · Parts 23–25 · librarian job 3 · Folder Org v2 |
| `.claude/agents/janitor.md` | Part 3 Janitor · Part 33 · the librarian's standing audit |
| `.claude/agents/secretary.md` | Part 3 Secretary · Part 32 · Governance §5 |
| `.claude/agents/auditor.md` | Part 3 Auditor · QA gate · consistency sweep |
| `scripts/validate_layers.py` | System spec §11 |
| `scripts/validate_codes.py` | System spec §11 · Governance §6 Check 2 |
| `scripts/validate_tokens.py` | System spec §11 closing note · Part 39 |

---

## PART 5 — Migration order

Assembly order matters. Building a skill before the standard it points at guarantees the skill will
restate the rule — the exact failure this migration exists to fix.

```
1. legacy/ snapshots        nothing can be lost after this point
2. GOVERNANCE               the rules for making rules
3. tokens.json + DESIGN_SYSTEM + palette-archive   ← blocked on CONFLICT-01,-02,-04
4. remaining standards      ANTI_AI_SLOP, VOICE, NAMING, DRIVE_ARCHITECTURE, QA_GATE
5. courses/*/DECISIONS.md   Chemistry → Physics → Geology (Geology partial)
6. agents                   they can now point at something authoritative
7. skills                   they can now point at both
8. validators + hooks       enforce what the standards say
9. workflows                the completion chain
10. weekly review           last — a recurring job on a half-built system is noise
```

**Dependency check.** Steps 3 and 4 are blocked on the CRITICAL conflicts; step 5's Geology entry is
blocked on CONFLICT-03. **Steps 1 and 2 are not blocked and could begin as soon as CONFLICT-00 is
answered.**

---

## PART 6 — Migration risks

| Risk | Why it is real | Mitigation |
|---|---|---|
| **A conflicted rule gets migrated as settled** | Six palettes and three naming forms all read as authoritative in their own files | Every CONFLICT cell says BLOCKED and names the question. No best guesses. |
| **A rule is lost because it lives only in a skill that gets replaced** | The connector directive already disappeared once in a reinstall (Architecture v2, change 6) | `legacy/` snapshots first, before any decomposition |
| **A superseded palette gets resurrected** | Six palettes across three storage systems, and one specification already revived a rejected alternate | `brand/palette-archive/` with dated supersession notes; `validate_tokens.py` |
| **The new skills restate rules instead of pointing** | Every legacy skill did this; three restate the same palette | `validate_layers.py`, `validate_tokens.py`, enforced in CI |
| **Existing materials become "off-brand" overnight** | Built U1 Geology packet, regraded Physics images, Chemistry U7/U10 decks | Carry the no-retrofit policy forward and **record which existing materials use which superseded palette** (CONFLICT-15) — otherwise the Janitor's first sweep flags everything |
| **Drive operations break links** | Renames break links; a copy+trash move changes the file ID | T-3 before any move; log prior name and parent before every mutation |
| **The migration produces a to-do list nobody works** | Governance §8 is exactly that, two days old and unworked | Validators, not tables. A failing build is a mechanism; a table row is not. |

---

## PART 7 — Explicit non-goals for V1

Recording these so scope does not creep during Phase 7.

- **No new agents beyond the seven.** Part 3 says so and inspection found no demonstrated need.
- **No Reference Sheet Generator.** Never built in legacy; it is a Phase-15 candidate, not V1.
- **No autonomous weekly changes.** Part 31 and Part 47. Report-only, permanently, until you say
  otherwise.
- **No batch renaming.** Blocked on CONFLICT-03 and CONFLICT-09.
- **No Geology folder creation.** Blocked on CONFLICT-03.
- **No retiring of the installed legacy skills** until T-7 passes in Phase 14.
- **No Drive writes at all** until Phase 10, and the first writes are additive only.
- **No permanent deletion of anything, ever, without your explicit approval** — and the tooling
  cannot permanently delete Drive objects regardless.

