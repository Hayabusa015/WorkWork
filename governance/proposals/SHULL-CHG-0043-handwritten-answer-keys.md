# SHULL-CHG-0043 — Teacher answer keys get a handwritten look (pencil and pen)

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0043 |
| **Date** | 2026-10-16 |
| **Source** | User — Matt, conversation 2026-10-16. Evidence from the main session's font tests: `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hw/sheet.png` (font comparison), `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hw/demo_patrick.png`, `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hw/demo_steps.png`. The Secretary has not re-examined the images; the font findings below are the main session's report. |
| **Current Rule** | See §1 below, verbatim, with file and section. |
| **Proposed Rule** | See §2 below. Eight items (A-H), each separately approvable. H is Matt's physics scenario-sketch addendum. |
| **Supersedes** | Carves an exception out of, and does not delete: `brand/SHULL_DESIGN_SYSTEM.md` typography section ("Never substitute a font outside this stack. Never a novelty 'school' font. Never a convenient one."), and `scripts/audit_fonts.py` `ALLOWED = ("Archivo",)` (tooling, not governed, see item E). Extends `brand/tokens.json` `typography` (adds one face) and adds four colour tokens. No existing token or LOCKED value changes. |
| **Reason** | Matt wants teacher answer keys to look handwritten "for authenticity". Keys are always separate files (`standards/NAMING.md` §2), so student pages are untouched. His decisions, in his words: "Ok lets try pencil." Math (physics math, chemistry math) is in pencil; written answers and keys such as electron configuration are in pen. "I like different colors for contrast. Like draw boxes in one color and arrows in another to make different things stand out." Strike-through of a wrong attempt, "but only if its a common mistake". "show the simple algebraic steps in the answer key." (2x + 4 = 6: subtract 4 from both sides, 2x = 2, divide both sides by 2, x = 1.) "use horizontal division. Symbols with numerator and denominators.. never in-line division symbols." Matt decided ("1") that a slash inside a unit name (m/s, g/mol) is a label, not a division step, and stays inline. |
| **Affected Agents** | Builder agents that load the three key-producing skills; Auditor (new checklist lines); Secretary (implementation only, upon approval). |
| **Affected Skills** | `build-assessment`, `build-document`, `build-lab`, `verify-content`, `audit-deliverable`. **Not affected: `build-presentation`** (slides have no teacher key; student-facing worked examples stay Archivo). `naming` and `reconcile-session-files` unchanged (key-as-separate-file already stated there). |
| **Affected Courses** | All three. No course `DECISIONS.md` is touched (build mechanics, not a course fact). |
| **Risk** | Medium (brand tokens + a new font + a deliberate exception to the Archivo-only rule + five skills) |
| **Recommendation** | Approve in two stages. See §6. |
| **Decision** | Approved in two stages by Matthew Shull, 2026-10-16 ("Approve it in two stages"). |
| **Status** | **APPROVED** |
| **Implemented By** | Stage 1: pending commit |
| **Verified** | no (Stage 1 applied, not yet verified; Stage 2 not started) |

---

## 1. Current Rule — verbatim

### 1a. `brand/SHULL_DESIGN_SYSTEM.md`, typography (lines 139-151)

> `typography.primary` — **Trade Gothic Next** — is the SHULL Studio typeface, used throughout:
> presentations, documents, worksheets, labs, guided and Cornell notes, assessments, headings, labels,
> supporting material.
> [...]
> **Never substitute a font outside this stack.** Never a novelty "school" font. Never a convenient
> one.

### 1b. `brand/tokens.json`, `typography`

`primary` Trade Gothic Next (LOCKED), `fallback` Archivo (LOCKED, OFL, SHULL-CHG-0006), `condensed` Archivo Narrow (LOCKED), `lastResort` Liberation Sans (INHERITED). No handwriting face. No pencil, pen, box, or annotation colour token.

### 1c. `brand/fonts/README.md`

> **Archivo** and **Archivo Narrow** — SIL Open Font License, redistributable, committed here.

### 1d. `.claude/skills/audit-deliverable/SKILL.md` §3 (lines 45-46) and `scripts/audit_fonts.py` line 20

> `audit_fonts.py` fails a PDF that renders in anything but Archivo and names the character that
> pulled the substitute in.

`ALLOWED = ("Archivo",)`.

### 1e. `standards/QA_GATE.md` §4, §8, §9

- §4: "Would a photocopy still distinguish the categories? **If the only difference is hue, fix it.**"
- §8: "If the document has answers, the key is its own file ending `_Key`."
- §9: "Including in **each** parallel version. [...] re-solve each one from scratch."

### 1f. The insertion points (text each new item sits beside)

| File | Section (line) | Text the new item sits beside |
|---|---|---|
| `build-assessment` | "Answer keys" (37-44) | "Note common misconceptions and any grading judgment calls. **Keep teacher-only information off the student version.**" |
| `build-document` | end of the notes block (132-133) | "**Always two files** — student copy and filled key — generated from the same source so they cannot drift." |
| `build-lab` | "The rules that are not yours to change" (26-39) | "- **Two files, always.** The key is never appended to the handout." |
| `verify-content` | "Check, in this order", item 3 (19-20) | "**3. Every calculation, re-solved independently.**" |
| `audit-deliverable` | §3 (45-46) and §4 (50-53) | the `audit_fonts.py` sentence, and the checklist "Clipped text ... every number re-solved · any molecular structure not produced by ..." |

Line numbers are approximate; the Secretary re-reads them at implementation.

## 2. Proposed Rule

### Item A — Brand: four colour tokens (`brand/tokens.json`)

Add under a new top-level group `keyInk` (so they are not mistaken for course or semantic colours), four tokens: `pencil`, `pen`, `box`, `arrow`.

| Token | Role | Final candidate hex (PROVISIONAL, 2026-10-16; Matt: "pick new colors") |
|---|---|---|
| `keyInk.pencil` | Math and calculation work on a key (physics math, chemistry math) | #5A6068 (graphite-gray) |
| `keyInk.pen` | Written answers and non-math keys, e.g. electron configuration | #4A2466 (deep plum) |
| `keyInk.box` | Boxes that mark a final answer or key result | #9F1D2C (crimson) |
| `keyInk.arrow` | Arrows and other annotations (flow, "carry this", "because") | #16609A |

Main-session checks reported 2026-10-16 (not measured by the Secretary; `scripts/measure_tokens.py` produces the committed `measured` blocks): contrast on white 6.35 / 12.1 / 7.8 / 6.6; CIE distance to the nearest existing token: pencil 12.3 (`ground.footer`, the closest call), pen 42.6 (`ground.graphite`), box 28.8 (`semantic.danger`), arrow 38.5 (`ground.graphite`). `pencil` is close to `ground.footer`; the tokens stay PROVISIONAL, and reusing the existing token instead of a new one is an option for Matt.

- `status` is **PROVISIONAL** for all four, and stays PROVISIONAL until Matt confirms the hex values after seeing them on a real key.
- **Do not invent measurements.** The `measured` blocks (grayscale, contrast on white and parchment and asphalt, verdicts) must be produced by `scripts/measure_tokens.py` at implementation, as the file header requires ("never hand-edit one"). The record carries no numbers.
- Requirements the measured values must meet before the status can leave PROVISIONAL: every ink used as type clears `rules.contrastTargetText` (5.5) on white; the print-ink gate in `standards/QA_GATE.md` §5 (`scripts/audit_print_ink.py`) passes on a built sample key; `box` and `arrow` must remain distinguishable **by shape and stroke**, not colour alone, in grayscale (box is a closed rectangle, arrow is an open line with a head), consistent with `standards/QA_GATE.md` §4 and `rules.grayscaleSeparationMin`. If `box` and `arrow` measure within 20 grey levels of each other, that is acceptable only because the shape differs; the audit records it.
- One-hex rule: the hex values are written only in `brand/tokens.json`. The builder helper (item F) reads them; `scripts/validate_tokens.py` must still pass. The candidate hex values appear in this proposal for review only and must not be copied into any other file.
- **Overlap (resolved 2026-10-16):** the earlier test values for `pen` and `box` sat near Physics Deep Purple `courses.physics.secondary` (LOCKED) and Geology Rust Orange `courses.geology.secondary` (LOCKED). Matt answered "Yes to both, pick new colors"; `pen` and `box` were moved to the final values in the table above.

### Item B — Brand: Patrick Hand font (`brand/fonts/`, `brand/tokens.json` typography)

- Add Patrick Hand, SIL Open Font License, source `google/fonts` repository, directory `ofl/patrickhand`, added by SHULL-CHG-0043. Ship its OFL text as `brand/fonts/OFL-PatrickHand.txt`, matching `OFL-Archivo.txt` and `OFL-ArchivoNarrow.txt`.
- Add `typography.keyHandwriting` to `brand/tokens.json`: family "Patrick Hand", status PROVISIONAL (until Matt sees it on a real key), license OFL, source SHULL-CHG-0043, and a note: "Teacher answer keys only. Never on a student page. No superscript, subscript, arrow, or Delta glyphs; the key builder draws those."
- Update `brand/fonts/README.md` to name the new face and its purpose, and `brand/SHULL_DESIGN_SYSTEM.md` typography to add, directly after the "Never substitute" sentence: "One exception: `typography.keyHandwriting`, on teacher answer keys only (SHULL-CHG-0043)." The existing sentence stays.
- Why Patrick Hand (main session's test): in the ambiguity row (0 O 1 l I 6 b 5 S 2 Z 9 g q 7) it is the only candidate where every character is distinct. Kalam draws 1, l, I almost identically; Caveat's 5 and S are close. Candidates tested: Caveat, Kalam, Patrick Hand, Indie Flower (all OFL, from github.com/google/fonts `ofl/`). Rejected: Handlee (no multiplication or minus glyph); Reenie Beanie and Shadows Into Light (too thin and small for print). Patrick Hand has × ÷ − ° but, like all tested fonts, **no** superscript or subscript digit glyphs, arrows, or Delta.

**Implementation constraint, for Matt to decide.** The font file is binary. The Secretary has no shell and cannot download or copy a binary, and `brand/` is Secretary-only. So the `.ttf` copy needs a mechanical step by the **main session** (fetch from `google/fonts` `ofl/patrickhand`, place in `brand/fonts/`, verify the OFL text matches), done under this record once APPROVED, with the Secretary editing the text files (OFL text, README, tokens.json) around it. This is a narrow, mechanical exception to "only the Secretary writes to `brand/`". **Question for Matt: is that acceptable? The Secretary does not decide it.** If not, the alternative is that Matt places the file himself, or this item is DEFERRED.

### Item C — The rule, in ONE place: a new standard, `standards/ANSWER_KEYS.md`

One fact, one place. The full rule is written once in a new file `standards/ANSWER_KEYS.md` (recommended over extending `standards/QA_GATE.md`, which is a checklist and would bury it). `standards/README.md` gets one index row. Every skill points to it and restates nothing. Content:

1. **Scope.** Teacher answer keys only (the separate `Key` file per `standards/NAMING.md` §2). Student pages are never handwritten.
2. **Division of labour.** Math problems (physics math, chemistry math) are PENCIL (`keyInk.pencil`). Written answers and non-math keys (e.g. electron configuration) are PEN (`keyInk.pen`). Face: `typography.keyHandwriting`.
3. **Colour roles.** Boxes are `keyInk.box`; arrows and annotations are `keyInk.arrow`; boxes and arrows differ by shape as well as colour.
4. **Strike-through** shows a wrong attempt only when it is a mistake students genuinely commonly make ("but only if its a common mistake"). Never an invented mistake. A short note names the mistake. The source of "common" is the course `DECISIONS.md` misconception list or Matt; if neither supports it, no strike-through.
5. **Algebra steps.** The simple algebraic steps are shown, each step on its own line, with the operation shown on both sides. Example: 2x + 4 = 6, then subtract 4 from both sides, then 2x = 2, then divide both sides by 2, then x = 1.
6. **Division is horizontal.** Every division in a calculation step is a stacked fraction: numerator over a bar over denominator. Never the divide sign, never a slash between numbers or variables. The note "divide both sides by 2" is written in words. **Exception (Matt decided "1"):** a slash inside a unit name (m/s, g/mol) is a label, not a division step, and stays inline.
7. **Arithmetic is still re-solved.** The handwritten look changes nothing about `standards/QA_GATE.md` §9; `verify-content` re-solves every number, each parallel version included.
8. **Legibility beats authenticity.** If any character could be misread (1 / l / I, 0 / O, 5 / S, an exponent read as a coefficient), the key has failed its job and the look yields. The builder switches that character or step to Archivo; the key is never shipped ambiguous.
9. **Default stays simple.** See §6: a key that does not need the look is not required to use it beyond what the helper does automatically.

### Item D — Affected skills: pointer lines only

Each insertion is one or two lines that point to `standards/ANSWER_KEYS.md`; none restates the rule.

| Skill | Insertion |
|---|---|
| `build-assessment` | In "Answer keys", after the "teacher-only information off the student version" sentence: keys are built in the handwritten key style, see `standards/ANSWER_KEYS.md` (SHULL-CHG-0043). |
| `build-document` | After "**Always two files**": the filled key follows `standards/ANSWER_KEYS.md`. |
| `build-lab` | In "The rules that are not yours to change", after "Two files, always.": the teacher key follows `standards/ANSWER_KEYS.md`. |
| `verify-content` | Under check 3: handwritten-key arithmetic is re-solved from the problem statement exactly as before; the look is never a reason to skip a step or to trust a glyph. Also: read each handwritten step as printed, not as the builder meant it (a stacked fraction or raised digit that renders wrongly is a wrong key). |
| `audit-deliverable` | §3: `audit_fonts.py` allows `typography.keyHandwriting` on `Key` files only, and on a student file it is a fail. §4: add to the checklist "key handwriting rules per `standards/ANSWER_KEYS.md`, **visually inspected** page by page (a wrong glyph is a wrong key; no hook can see it)". |

`build-presentation` is not edited.

### Item E — Tooling the rule depends on (not governed; the Secretary does not edit `scripts/` under this record)

`scripts/audit_fonts.py` `ALLOWED = ("Archivo",)` would fail every handwritten key. It needs a key-file carve-out (allow Patrick Hand when the file name ends in `Key`; still fail it on any other file). That edit is tooling, but the **rule** it enforces (Archivo-only) is governed by `brand/SHULL_DESIGN_SYSTEM.md`, so the carve-out is a consequence of Item B and is flagged here so it is not forgotten. Likewise `scripts/audit_print_ink.py` is run unchanged on sample keys to confirm the ink budget.

### Item F — Tooling: key-writing helper (follow-on work, NOT part of the governed change)

A builder helper in `scripts/`, in the style of `scripts/science_tools.py` and `scripts/build_diagram_molecule.py`, built after approval and shown on a real key. It must: lay out pencil and pen text from the tokens; stacked fractions; raised and lowered digits (exponents and subscripts) drawn as scaled, raised or lowered text because the font has no such glyphs; wobbly vector boxes, arrows, strike-through lines and fraction bars; read all colours from `brand/tokens.json` (never a hex in the script). Not governed, no change record needed, but it gates Stage 2.

### Item H — Physics scenario sketch on the key (Matt's addendum, 2026-10-16; separately approvable)

Matt's words: "For physics. When there is a math problem and a story behind it. In the answer key could you generate an image of the story problem and label the desired given units for the problem in the answer key."

Proposed rule, written once as a section of `standards/ANSWER_KEYS.md` (Item C), pointed to from the skills:

1. **Physics keys only.** When a physics problem has a story or scenario, the key carries a small scenario sketch placed above or beside the worked solution.
2. **Labels.** Each given is labelled with value and unit; the unknown is labelled with its unit (e.g. "F = ?" or "find: net force, N").
3. **Colour roles (per Item C):** force and velocity vectors use `keyInk.arrow`; boxes use `keyInk.box`; labels are in pencil (`keyInk.pencil`) in `typography.keyHandwriting`.
4. **Built, not generated (design point, for Matt to confirm).** The sketch is BUILT from the same spec or data as the problem and the solution, from a small library of vector scene templates (cart on a track, falling or thrown object, block on a ramp, spring, circuit, and so on). It is not an AI-generated picture. Reason: `.claude/skills/build-presentation/SKILL.md` Images already says "Anything students **read** as science is hand-built," and a generated image can contradict the numbers (wrong direction, wrong value in a label) in a way nobody catches at a glance. A built sketch takes its labels from the same data as the question, so they cannot disagree. Purely decorative art may still be generated per that rule; any figure that carries a given, a unit, or an unknown is built. This refines, and does not replace, the `build-presentation` sentence.
5. **Matt's reply (2026-10-16): "Sketch is fine. Make it look like its being drawn in pencil."** This confirms the built-not-generated choice in point 4 for this item (the Decision field still reads pending until the main session records the formal approval). Rendering requirement: the sketch looks pencil-drawn, with slightly uneven strokes, doubled passes, small overshoots at corners, and graphite grain, in the `keyInk.pencil` colour. Vectors and boxes keep the arrow and box colours. Legibility still beats the look (Item C.8): the grain must never obscure a value, unit or direction. Prototype evidence: `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hw/demo_sketch.png` was not present when this record was written (the main session was still making it); the Secretary has not seen it.
6. **Out of scope for now:** chemistry story problems (Matt to be asked later) and any student-page version of the sketch.

Affected skills for Item H: `build-assessment` (Answer keys) and `build-document` (key line) as in Item D; `build-lab` only if a physics lab key carries a worked scenario problem, in which case it uses the same pointer line already placed in Item D, no extra text. `verify-content` gets one added phrase under check 3: every label on a sketch (value, unit, direction) is checked against the problem statement as it is checked for the solution. `audit-deliverable` §4 checklist: the sketch is visually inspected, and flagged if not built from the problem data. `build-presentation` is still not edited.

The sketch builder is follow-on tooling in `scripts/` (Item F family), not part of the governed change.

### Item G — Out of scope

Molecule drawing (already SHULL-CHG-0042, IMPLEMENTED), the `pint` randomized-problem generator, and the `mendeleev` cross-check. None is authorised or implied here.

## 3. Reason in short

Authenticity is Matt's call, and it costs nothing on student pages. The risk is entirely on the teacher side: a wrong glyph, a misread exponent, or an ambiguous character makes a wrong key that looks right. That is why legibility outranks look (Item C.8), why arithmetic is still re-solved (C.7), and why the audit visually inspects.

## 4. Scope limits

- **Keys only.** Student pages are unchanged and stay Archivo.
- **The font lacks superscript, subscript, arrow, and Delta glyphs.** Correctness depends on the helper drawing them. A wrong glyph is a wrong key.
- **Grayscale print.** Pencil, pen, box, and arrow all have to survive a photocopy; shapes carry the distinction, not hue alone.
- **Must not slow key production.** The default stays simple: the helper does the layout automatically from the same source as the student file; the builder does not hand-place strokes. Strike-through, boxes, and arrows are used where they help (and strike-through only for a genuine common mistake), so a plain key with pencil and pen text and stacked fractions is a complete, valid key. Where the helper cannot set something unambiguously, that line falls back to Archivo rather than blocking the key.
- **The audit line is a backstop, not a guarantee.** It relies on the Auditor looking at the rendered pages.

## 5. Conflicts with LOCKED rules (Secretary does not resolve these; Matt decides)

| # | LOCKED rule | Where | Conflict |
|---|---|---|---|
| 1 | "Never substitute a font outside this stack. Never a novelty 'school' font." (and `typography.primary`, `fallback` LOCKED) | `brand/SHULL_DESIGN_SYSTEM.md` ~line 150; `brand/tokens.json` `typography` | **CONFLICT.** Patrick Hand is outside the stack, and a handwriting face is arguably a "school" font. Item B proposes a narrow, labelled exception (keys only, PROVISIONAL), not a deletion. Approving this record is Matt's explicit decision to make that exception. |
| 2 | Archivo-only render check | `scripts/audit_fonts.py` `ALLOWED`; `audit-deliverable` §3 | Not a LOCKED token, but an enforced gate that would fail every handwritten key until Item E is done. |
| 3 | `courses.physics.secondary` and `courses.geology.secondary` (LOCKED) | `brand/tokens.json` | Candidate hex proximity to `pen` and `box` (Item A). Resolved 2026-10-16: Matt asked for new colours; final values are in Item A. |

No CONFLICT, PROVISIONAL, or UNKNOWN item is converted to LOCKED by this record. The four tokens and the font stay PROVISIONAL.

## 6. Recommendation: approve in two stages

**Stage 1 (Items A and B, plus the Item E carve-out):** tokens (PROVISIONAL, measured at implementation), Patrick Hand font and OFL text, the `typography.keyHandwriting` entry, the design-system exception sentence, the font README. Low-regret, reversible, and nothing a student sees changes. This also resolves the binary-file question (Item B) early.

**Stage 2 (Items C, D, and H):** `standards/ANSWER_KEYS.md` (including the Item H sketch section) and the five skill pointer lines, **only after** the helpers (Item F, and the scene-template sketch builder from Item H) exists and has been shown on one real key (suggest a Chemistry stoichiometry key and a Physics kinematics key, because they exercise stacked fractions, exponents, and algebra steps). Reasoning: until the helper exists, the rules would instruct builders to produce a look the system cannot produce, and the skills would tell Claude to follow a standard it cannot meet. Stage 2 also gives Matt a chance to confirm the PROVISIONAL colours and font on paper before they become rules, and to flip them from PROVISIONAL.

Approving as a single stage is also possible; the cost is rules live before the tool and an audit gate (`audit_fonts.py`) that fails keys. The Secretary recommends two stages.

## 7. Questions for Matt (one at a time as needed)

1. Is it acceptable that the main session performs the binary font copy mechanically, under this approved record (Item B)?
2. Approve in two stages (recommended) or one?
3. Item H: answered by Matt ("Sketch is fine. Make it look like its being drawn in pencil"): built, pencil-look. Needs only formal approval.
4. Should `pen` and `box` candidate colours be nudged away from the Physics purple and Geology orange (Item A)?

## 8. Not done by this record

No skill, standard, brand, or course file was edited. `change-log/CHANGELOG.md` was not edited (the main session does that when it records the decision). No font was downloaded. Proposal only; implementation waits for a committed record with `Status: APPROVED` and a verbatim `Decision:` quote (`governance/CHANGE_CONTROL.md` §4). If staged, each stage is approved and implemented as its own commit carrying SHULL-CHG-0043.

## 9. Verification plan (for the Secretary, after approval)

Stage 1:
- `brand/tokens.json` parses; four `keyInk` tokens present, each PROVISIONAL, each with a `measured` block produced by `scripts/measure_tokens.py` (no hand-written numbers); `scripts/validate_tokens.py` passes (no raw hex outside tokens.json).
- `brand/fonts/` contains the Patrick Hand file and `OFL-PatrickHand.txt`; `brand/fonts/README.md` names source (`google/fonts` `ofl/patrickhand`) and SHULL-CHG-0043.
- `scripts/audit_fonts.py` carve-out verified on one sample key (passes) and one student file (Patrick Hand fails).
- `git diff` limited to the cited brand files plus this record and the changelog row.

Stage 2:
- `standards/ANSWER_KEYS.md` exists once; `standards/README.md` indexes it; each of the five skills contains only a pointer (grep shows the rule text appears in one file).
- `scripts/validate_references.py`, `validate_agents.py`, `validate_layers.py` pass.
- A real key built with the helper is rendered and visually inspected page by page; `audit_print_ink.py` passes; the arithmetic is re-solved independently by `verify-content`.
- Fill in `Implemented By` with the commit SHA(s) and `Verified` with the result.
