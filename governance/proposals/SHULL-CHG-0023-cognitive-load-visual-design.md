# SHULL-CHG-0023 — Cognitive load / visual design research, made checkable

| Field | Value |
|---|---|
| **Date** | 2026-09-16 |
| **Source** | User — requested a research session on visual design, formatting, and cognitive load, then asked for it to be added as a standard and a check |
| **Resolves** | Gap: `brand/SHULL_DESIGN_SYSTEM.md` §5–6 and `standards/ANTI_AI_SLOP_STANDARD.md` §5 already state the qualitative rule ("clean and moderately dense," "every visual element must serve a purpose") but give the Designer and Auditor nothing measurable to build or check against, and no stated mechanism for *why* clutter fails. |
| **Current Rule** | `brand/SHULL_DESIGN_SYSTEM.md` §5 "Visual density": *"Clean and moderately dense... no unnecessary empty space, no decorative clutter."* No line-length, adjacency, or highlight-consistency rule exists anywhere in `brand/` or `standards/`. `standards/ANTI_AI_SLOP_STANDARD.md` §5 "Visual tells to avoid" lists defects (rainbow palettes, decorative callouts, etc.) with no stated mechanism. `standards/QA_GATE.md` has 9 checks; none address line length, text/diagram adjacency, or highlight-color discipline outside slides. |
| **Proposed Rule** | Add three additive items (below). Nothing existing is replaced. |
| **Supersedes** | N/A — additive only |
| **Reason** | Cognitive Load Theory (Sweller) and Mayer's multimedia-learning principles are well-replicated: working memory holds ~4–7 chunks and decays in 10–20 seconds; extraneous load (poor presentation, not content difficulty) is the thing design controls; the split-attention effect shows separating a diagram from its explanatory text forces the reader to hold one in memory while hunting for the other; adequate whitespace has been shown to raise comprehension up to ~20%; 50–75 characters per line is the well-supported readable range (WCAG hard caps at 80); and the "seductive details" effect (Harp & Mayer 1998; Rey 2012 meta-analysis) shows irrelevant-but-engaging decoration *actively lowers* recall and transfer, not just wastes space. This upgrades existing SHULL rules from taste to mechanism, and gives the Auditor something to actually measure instead of judge. |
| **Affected Agents** | Auditor (new QA_GATE check to run), Designer (new build rule to apply) |
| **Affected Skills** | None edited directly — `audit-deliverable`, `apply-shull-design`, and `anti-ai-slop` all already point at the files below rather than restating them, so they inherit automatically |
| **Affected Courses** | All three (Layer 1) |
| **Risk** | Low — additive, no existing token, color, or font value changes; current SHULL fonts (Archivo, sans-serif) already comply with the readability research |
| **Recommendation** | Adopt |
| **Decision** | Approved by the user |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `brand/SHULL_DESIGN_SYSTEM.md` §5, `standards/ANTI_AI_SLOP_STANDARD.md` §5, `standards/QA_GATE.md` §10 (new), `standards/README.md` (check count 9→10) |
| **Verified** | Yes — all three additions present and each cites SHULL-CHG-0023; no token, font, or color value touched (`git diff` limited to the four files named); `standards/README.md`'s check count now matches `QA_GATE.md`'s actual section count (10). |

---

## Proposed additions

### 1. `brand/SHULL_DESIGN_SYSTEM.md` — extend §5 "Visual density"

Add after the existing paragraph:

> **Two rules follow from why clutter fails, not just that it looks bad:**
>
> - **A diagram, image, or table sits adjacent to the text that explains it** — same box, same
>   column, never separated by a page turn or a gap the reader has to search across. (Separating
>   them forces a reader to hold one in memory while hunting for the other — the split-attention
>   effect, and it measurably hurts comprehension.)
> - **Body prose targets 50–75 characters per line, never exceeding ~80.** A column that runs
>   edge-to-edge on a wide page or slide gets narrowed or split, not left wide.

### 2. `standards/ANTI_AI_SLOP_STANDARD.md` — extend §5 "Visual tells to avoid"

Add one line after the existing list:

> **Why this list is not just taste:** decorative-but-irrelevant content measurably *lowers* recall
> and transfer of the material around it — it isn't neutral. Anything that fails the §6 decoration
> test in `brand/SHULL_DESIGN_SYSTEM.md` ("must serve hierarchy, navigation, explanation, emphasis,
> identity, or visual comprehension") is actively working against the content, not just filling
> space.

### 3. `standards/QA_GATE.md` — new check, inserted as §10 (renumbering current §10 "Codes match" through §13 "Answer key exists" / §14 "Every number re-solved" accordingly, or appended as §10 ahead of "Deliverable-specific additions" — Secretary's call on exact placement)

> ## Density and adjacency
>
> - Body prose does not exceed roughly 80 characters per line. If a text column runs edge-to-edge
>   on a wide page or slide, narrow it or split it.
> - Every diagram, image, or table sits next to the text that explains it — never separated by a
>   column break or a page the student has to flip past.
> - Only one color is doing highlight/emphasis work on a given page or slide, and it means the same
>   thing everywhere it appears in that document (this generalizes the existing slide rule in
>   §12 of the design system to print documents).
> - Nothing on the page exists only to fill space. Anything that doesn't pass the §6 decoration
>   test in `brand/SHULL_DESIGN_SYSTEM.md` gets cut, not shrunk.

---

## What this does not do

- Does not touch fonts, colors, tokens, or any course's `DECISIONS.md`.
- Does not create a new agent — the Auditor already runs `QA_GATE.md` in full, and the Designer
  already treats `SHULL_DESIGN_SYSTEM.md` as build authority. No `.claude/agents/` file needs
  editing.
- Does not require a skill edit, by design — skills point at standards rather than restating them.

## Research basis (for the record)

Cognitive Load Theory (Sweller); split-attention effect; Mayer's coherence, signaling, redundancy,
and spatial-contiguity principles; whitespace-comprehension studies (Wichita State, ~20% effect);
optimal line length literature (Bringhurst; Univ. of Reading; WCAG 1.4.8); the seductive-details
effect (Harp & Mayer 1998; Rey 2012 meta-analysis); dual coding theory (Paivio); graphic-organizer
meta-analyses (large effect sizes, especially for students with learning disabilities). Full findings
summarized in chat, 2026-09-16.
