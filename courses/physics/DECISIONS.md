# PHYSICS — Course Decisions

**Owner:** Matthew Shull · James A. Garfield Local Schools
**Last updated:** 2026-09-08
**Authority:** This file wins over any course fact stated in a skill or standard. If a skill
disagrees with anything here, the skill is stale and gets reported, not obeyed.
**Governed by:** `governance/GOVERNANCE.md`

---

## Curriculum map — CONFIRMED (Units 0–10, 48 sections)

Source: `SHULL_Physics_Unit_Map_1.pdf`, Matt's course reference sheet. Same `U#/S#.#` grammar as
Chemistry. **This is the only authoritative copy — never build against a code not listed here.**

> **Provenance note.** The map is confirmed and its section counts verify, but the source PDF was
> **not found in Drive** during the 2026-09-07 inspection. See open question 5.

### Phase 1 — Foundations & Motion (U0–U2)

**U0 · Physics Math Review** — 4 sections
`0.1` Scientific Notation · `0.2` Significant Figures · `0.3` Algebraic Equation Manipulation ·
`0.4` Physics Graphing

**U1 · Motion in One Dimension** — 4 sections
`1.1` Distance, Displacement & Velocity · `1.2` Acceleration & Kinematic Equations ·
`1.3` Position-Velocity-Acceleration Graphing · `1.4` Free Fall

**U2 · Motion in Two Dimensions** — 3 sections
`2.1` Vectors & Vector Basics (Review) · `2.2` Vector Addition · `2.3` Projectile Motion (All Types)

### Phase 2 — Forces & Energy (U3–U5)

**U3 · Forces and Motion** — 7 sections
`3.1` Newton's Laws · `3.2` Free Body Diagrams · `3.3` Inclined Plane FBDs · `3.4` F = ma
Calculations · `3.5` Net Force & Acceleration from FBDs · `3.6` Frictional Forces ·
`3.7` Multi-Body Systems (Atwood Machines)

**U4 · Work, Energy & Power** — 4 sections
`4.1` Work & Power · `4.2` Kinetic Energy & Work-Energy Theorem · `4.3` Potential Energy
(Gravitational & Elastic) · `4.4` Conservation of Energy

**U5 · Momentum & Impulse** — 3 sections
`5.1` Momentum & Impulse · `5.2` Conservation of Momentum · `5.3` Collisions (Elastic & Inelastic)

### Phase 3 — Fields & Waves (U6–U8)

**U6 · Circular Motion & Gravitation** — 3 sections
`6.1` Tangential Velocity, Centripetal Force & Acceleration · `6.2` Universal Gravitation ·
`6.3` Torque

**U7 · Waves** — 5 sections
`7.1` Simple Harmonic Motion · `7.2` Wave Basics (Types & Characteristics) · `7.3` Superposition ·
`7.4` Standing Waves & Resonance · `7.5` Electromagnetic Waves & Light

**U8 · Optics** — 3 sections
`8.1` Reflection & Mirrors · `8.2` Refraction & Snell's Law · `8.3` Lenses

### Phase 4 — Electricity, Magnetism & Modern Physics (U9–U10)

**U9 · Electricity & Magnetism** — 6 sections
`9.1` Electric Charge & Coulomb's Law · `9.2` Electric Fields & Electric Potential ·
`9.3` Current & Ohm's Law · `9.4` DC Circuits (Series & Parallel) · `9.5` Magnetism & Magnetic
Fields · `9.6` EM Induction & Applications

**U10 · Nuclear & Modern Physics** — 6 sections
`10.1` Nuclear Structure & Stability · `10.2` Radioactive Decay · `10.3` Half-Life ·
`10.4` Mass-Energy Equivalence · `10.5` Fission & Fusion · `10.6` Applications, Risks & Benefits

**Section count:** 4+4+3 = 11 · 7+4+3 = 14 · 3+5+3 = 11 · 6+6 = 12 · **total 48.** Matches the map
header.

### What the map itself establishes

- **Physics opens with tooling, not content** — U0 is a math-review unit, structurally the same
  idea as Chemistry's U0 Foundations.
- **`2.1` is labelled (Review)** — vectors are expected knowledge entering U2, not new content.
- **U10 parallels Chemistry U15 closely** — half-life, decay types, fission and fusion,
  applications and risks appear in both. Check for reusable assets before building U10 from
  scratch, and know which students have already seen it.

---

## Sequencing — CONFIRMED, and it differs from Chemistry

> **Significant figures are taught at `U0/S0.2`, in week one, and enforced from there forward.**

This is the **opposite** of Chemistry, which deliberately delays sig figs until after midyear.
**Do not import Chemistry's "delay the math" sequencing rule into Physics.** Physics students have
not necessarily taken Chemistry, and the map teaches the tooling first on purpose.

*`shull-physics-guidelines` §5 says sig figs "follow the measurement rules already taught in
Chemistry — do not re-teach them from scratch." That is stale and contradicts the map.
See CONFLICT-05.*

---

## Physics-specific build rules — CONFIRMED as discipline standards

These are physics-content requirements, not preferences. They hold regardless of how the rest of
the course settles.

**Units.** Every numeric answer carries a unit. Every setup shows units cancelling.

**Vectors.** Any vector quantity gets a direction, always. Magnitude alone is an incomplete answer
for displacement, velocity, acceleration, force, momentum, and field strength.

**Free-body diagrams.** Object as a dot or box · one labelled arrow per force · arrows scaled to
relative magnitude · **no arrow for "motion."** This matters most across `3.2`, `3.3`, and `3.5` —
three consecutive FBD sections.

**Graph interpretation is a first-class skill, not a garnish.** Students read slope and area as
physical quantities: v-t slope is acceleration, v-t area is displacement, F-x area is work. **Build
at least one graph-reading item into every practice set** where kinematics, forces, or energy are in
play. The map gives this its own section at `1.3`, so it is taught explicitly, not absorbed.

**Sign conventions are stated explicitly** on every problem set that uses them. Declare the positive
direction in the directions, not implicitly through a diagram.

**Misconceptions to write distractors against:** heavier objects fall faster · a moving object must
have a net force on it · normal force always equals weight · centripetal force is a separate force
acting outward · energy is "used up" rather than transferred · confusing mass with weight, speed
with velocity, heat with temperature.

**Labs.** Physics labs produce a measured value with uncertainty. Require percent error against an
accepted value where one exists, and require a **specific** named source of error. "Human error" is
not an answer.

---

## Worksheets — CONFIRMED, and it differs from Chemistry

> **No work areas on Physics worksheets.** Practice sets, homework worksheets, and study guides
> carry problems and prompts only — no ruled lines, no work boxes.

Students do all calculation and reasoning in their lab notebooks. Instead, include a
**prior-knowledge and equations reminder block at the top** of the worksheet.

Pre-lab and post-lab prompts follow the same rule: procedure and prompts only, no data tables or
answer space. Students set up their own tables in the notebook as a pre-lab step.

**Flag this any time a request tries to reuse the Chemistry practice-set template unmodified for
Physics.**

---

## Ohio standards

Ohio's model Physics curriculum runs on motion, forces and momentum, energy, waves, and electricity
and magnetism — which this map covers in full, with optics and modern physics added. Tag items to a
specific standard when alignment is requested. **If the exact code is uncertain, say so rather than
guessing — a wrong standard code is worse than none.**

---

## Course brand exceptions

**None.** Physics uses Quantum Gold + Deep Purple inside the shared system, per SHULL-CHG-0002.
Values live in `brand/tokens.json`.

> *Physics briefly had a declared palette exception — "Quiet Voltage," CONFIRMED 2026-09-06 and
> superseded 2026-09-07. It is archived in `brand/palette-archive/phys-quiet-voltage.md` along with
> the materials built on it, which stay as built under the no-retrofit policy.*

---

## Carried over from Chemistry — PROVISIONAL, not confirmed for Physics

Practice progression · Cornell notes format · slide standards · handout standards · bracketed
numeric answer support · Modified/Challenge differentiation.

### Explicitly NOT carried over

- **Gradebook weights.** Chemistry's 55/20/15/7/3 split **must not** be applied to Physics without
  asking.
- **The sequencing rule.** Chemistry delays the math; Physics opens with it.

---

## Open questions

1. **Course identity.** Physics has not been placed on the rigor spectrum between Chemistry
   (highest) and Geology (intentionally lower). The map's content gives some signal — Atwood
   machines, inclined-plane FBDs, and EM induction are not a credit-recovery scope — but it has not
   been stated. *Blocks: full unit planning, not individual documents.*
2. **Algebra-only or algebra-plus-trig?** Projectile motion "all types" at `2.3` and inclined-plane
   FBDs at `3.3` both imply at least sine and cosine components. Worth confirming whether that is
   taught as trig or as resolved-component recipes.
3. **Gradebook weights** for Physics specifically.
4. **Notes-scaffolding index.** The guided-notes ladder is indexed to unit number — heavy U0–3,
   medium U4–8, light U9+. Physics has 11 units to Chemistry's 16, so the same unit number lands at
   a different point in the year. Re-indexing to *fraction of course elapsed* is proposed but is
   Matt's call. (CONFLICT-20)
5. **Where is `SHULL_Physics_Unit_Map_1.pdf`?** Cited as the source of this confirmed map, not found
   in Drive. The map itself is not in doubt — its section counts verify — but the source document
   should be located and filed.
6. **`SHULL_Physics_Pacing_Guide_20262027.pdf`** is referenced in the librarian's absorptions table
   and has not been supplied. Needed before build order can be set against the MP deadlines.
7. **Lab equipment inventory** and realistic lab frequency.
8. **Does Physics use the same five-tab binder system?**

---

## Drive status

`Physics/` holds **1 of 11** unit folders — `Unit 01 - Motion in One Dimension`, with Section 01.1
through 01.4 created. Section 01.1 has Presentations, Homework, and Guided Notes.

The map supplies the other ten unit titles, so those folders can be created:

```
Unit 00 - Physics Math Review          Unit 06 - Circular Motion & Gravitation
Unit 02 - Motion in Two Dimensions     Unit 07 - Waves
Unit 03 - Forces and Motion            Unit 08 - Optics
Unit 04 - Work, Energy & Power         Unit 09 - Electricity & Magnetism
Unit 05 - Momentum & Impulse           Unit 10 - Nuclear & Modern Physics
```

---

## Decision log

### 2026-09-08 — Physics decisions file created
Curriculum map, sequencing, discipline rules, and the worksheet rule moved here from
`SHULL_Course_Maps.md` Part B and `shull-physics-guidelines` §§5, 8. The skill's §3 (map NEEDED),
§4 (carried-over standards duplicated from the studio), and §5 sig-fig sentence are all stale and
do not migrate.
Supersedes: `shull-physics-guidelines` §§3, 4, and the §5 significant-figures sentence.
Status: CONFIRMED · SHULL-CHG-0012

### 2026-09-07 — Palette
Quantum Gold + Deep Purple , all media. Coloured type on a light ground uses
Quantum Gold Deep.
Supersedes: `SHULL_PHYS_Palette_QuietVoltage.md` (CONFIRMED 2026-09-06); `shull-studio` §1a Kinetic.
Status: CONFIRMED · SHULL-CHG-0002, SHULL-CHG-0008
