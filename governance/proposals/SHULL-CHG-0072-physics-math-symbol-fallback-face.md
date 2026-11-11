# SHULL-CHG-0072 — Physics: one named fallback face for Greek letters and math symbols Archivo lacks

> **CONFLICT with a LOCKED rule. Marked, not resolved.** The rule this would relax rests on
> `brand/tokens.json` `typography.primary` (Trade Gothic Next) and `typography.fallback` (Archivo),
> both `"status": "LOCKED"`. The prose rule in `brand/SHULL_DESIGN_SYSTEM.md` §4 carries no label of
> its own, but it states the stack those LOCKED tokens define (section 3). Only Matt can decide
> whether to open a second exception to it. His 2026-11-11 answer, quoted in section 1, chose
> "leave as symbol". It did not approve this record.
>
> **Path B (build/brand change).** The rule lives in `brand/` and is enforced by a shared script,
> although its scope is Physics only.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0072. The main session reports the ID was checked free against a fetched `origin/main` before the push of `37df80e` (branch `claude/focused-mendel-cefeca`). The Secretary could not re-check this. |
| **Date** | 2026-11-11 |
| **Source** | User. Found while building the Physics U3 guided notes, 2026-11-11. `scripts/audit_fonts.py` FAILs the rendered notes because θ and ⁻ set in Inter. Matt was offered "allow a backup font for math symbols, or spell it out as 'theta'" and answered, verbatim, 2026-11-11: "na leave as symbol". |
| **Current Rule** | `brand/SHULL_DESIGN_SYSTEM.md` §4, lines 143-153: "typography.stack Trade Gothic Next → Archivo → Liberation Sans ... **Never substitute a font outside this stack.** Never a novelty "school" font. Never a convenient one. One exception: `typography.keyHandwriting`, on teacher answer keys only, approved in SHULL-CHG-0043 by Matt, 2026-10-16." Tokens: `brand/tokens.json` lines 399-409, `typography.primary` and `typography.fallback`, both `"status": "LOCKED"` (source SHULL-CHG-0006). Enforcement: `standards/QA_GATE.md` §1, lines 26-29: "`pdffonts` on the output should show Archivo or Archivo Narrow. If it shows DejaVu or Liberation, the font substitution did not take". `scripts/audit_fonts.py` line 21: `ALLOWED = ("Archivo",)`. |
| **Proposed Rule** | Section 2. |
| **Supersedes** | Nothing is removed. It amends `brand/SHULL_DESIGN_SYSTEM.md` §4, the "One exception" sentence (adds a second exception), and `scripts/audit_fonts.py` `ALLOWED`/`KEY_ALLOWED` (adds a scoped allowance). |
| **Reason** | Physics needs θ (every incline and component problem: Fx = F cos θ, tan⁻¹) and the superscript minus (tan⁻¹, and units such as m·s⁻²). Archivo has neither U+03B8 nor U+207B. Today the renderer falls back to Inter for those glyphs, which is a font outside the stack, so the audit correctly FAILs and every Physics document carrying θ ships against the rule. Matt chose to keep the symbols rather than spell them out. The only ways to keep them and pass QA are to change the rule or to change the font. |
| **Affected Agents** | Designer (builds Physics documents with θ). Auditor (runs `audit_fonts.py`). Secretary (implements). |
| **Affected Skills** | Any skill that states the Archivo-only rule. `scripts/audit_fonts.py` docstring names QA_GATE.md, audit-deliverable, build-presentation and apply-shull-design as stating it. Each should already point at `brand/` rather than restate it. Not checked. |
| **Affected Courses** | Physics only, by scope. The rule and the script are shared. |
| **Risk** | Medium. It opens a second exception to a LOCKED rule. Mitigated by a closed glyph set, a single named face, and a per-glyph audit (section 2). A wider or vaguer allowance would be high risk. |
| **Recommendation** | Approve, with the face committed to the repository as part of the change (section 4, item 1). Without that, the render depends on whatever the container happens to have. |
| **Decision** | Approved by the user in chat, 2026-11-11: "na leave as symbol", answering the two options offered: "allow a backup font for math symbols" or "spell it out as theta". Read by the main session as choosing the backup-font option, the only symbol-keeping option offered. Overrides the LOCKED Archivo-only stack for this narrow glyph set by direct user instruction (CLAUDE.md precedence 1). Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | Partial. Decision recorded in `37df80e` (branch `claude/focused-mendel-cefeca`). Documentation and token written by the Secretary on 2026-11-11, not committed: `brand/tokens.json` `typography.mathFallback`, `brand/SHULL_DESIGN_SYSTEM.md` §4, `standards/QA_GATE.md` §1, `courses/physics/DECISIONS.md` decision log, `change-log/CHANGELOG.md` row, this record. The main session commits them. **SHA of that commit: pending, add it here.** Code follow-ups are pending (section 7). |
| **Verified** | No. Edits checked by reading the changed files only. The Secretary has no shell, so no token validator or JSON parse was run. Nothing can be verified end to end until the section 7 follow-ups land. |

---

## 1. Matt's answer (verbatim)

Offered: "allow a backup font for math symbols, or spell it out as 'theta'".

> "na leave as symbol"

2026-11-11. This chooses to keep the symbols on the page. Read literally, it does not choose
between "allow a backup font" and some other way of keeping the symbol (section 5). It is the
source of this record. It is not its approval.

## 2. Proposed Rule (verbatim, not adopted)

**2.1 Token.** Add to `brand/tokens.json` under `typography`:

```json
"mathFallback": {
  "family": "Inter",
  "status": "PROVISIONAL",
  "license": "OFL",
  "source": "SHULL-CHG-0072",
  "scope": "Physics documents only, student pages and keys",
  "glyphs": "Only characters Archivo lacks, in U+0370-03FF (Greek), U+2070-209F (superscripts and subscripts) and U+2200-22FF (mathematical operators)",
  "note": "Per-glyph fallback. Never used for running text, a word, or a digit Archivo carries."
}
```

**2.2 Brand prose.** `brand/SHULL_DESIGN_SYSTEM.md` §4, after the existing "One exception" sentence:

> A second exception: `typography.mathFallback`, per glyph, in Physics documents only, approved in
> SHULL-CHG-0072 by Matt.

(The face, scope and glyph set live in the token. The prose points at it and does not restate them.)

**2.3 QA gate pointer.** `standards/QA_GATE.md` §1, after line 31, one line in the same form:

> Physics files may also carry `typography.mathFallback` for the glyphs it names;
> `scripts/audit_fonts.py --physics` enforces it.

**2.4 Audit (code follow-up, same record).** `scripts/audit_fonts.py` gains a `--physics` flag,
combinable with `--key`. With it, a font named by `typography.mathFallback.family` is not a stray
**only if** every character set in that font falls inside the token's glyph set and is absent from
Archivo. The check is per span (PyMuPDF `get_text("dict")`, which gives the font of every span), not
per file, so a whole word set in Inter still FAILs. The script reads the family and the ranges from
`brand/tokens.json`. It does not hard-code them. Without `--physics`, behaviour is unchanged.
Tests: a Physics PDF with θ in Inter passes with `--physics` and fails without it. A Physics PDF with
a Latin letter in Inter fails either way. A key with θ passes with `--key --physics`.

## 3. The brand rules this touches

| Rule | Where | Label | Effect of this change |
|---|---|---|---|
| Trade Gothic Next is primary | `brand/tokens.json` `typography.primary` | **LOCKED** | Unchanged. Still named first. |
| Archivo is the fallback | `brand/tokens.json` `typography.fallback` | **LOCKED** (SHULL-CHG-0006) | Unchanged for every character Archivo carries. The new token covers only characters Archivo cannot set at all. |
| "Never substitute a font outside this stack" | `brand/SHULL_DESIGN_SYSTEM.md` §4 line 150 | No label in that file. It states the stack the LOCKED tokens define. | **Relaxed**, by a second named exception. This is the conflict marked in the banner. |
| Key handwriting exception | `brand/tokens.json` `typography.keyHandwriting`, §4 line 153 | PROVISIONAL (SHULL-CHG-0043/0044) | Precedent for a scoped, named exception. Unchanged. |
| Liberation Sans last resort | `brand/tokens.json` `typography.lastResort` | INHERITED | Unchanged (but see section 5, option C). |

History worth knowing: Inter was a rung in the legacy ladder (Oswald/Inter → Poppins/Lato →
Liberation Sans) that SHULL-CHG-0006 replaced with Archivo on 2026-09-07
(`docs/DECISIONS_2026-09-07.md` lines 132-151). That decision recorded Inter as **not present** in
the build container then. This record does not bring Inter back as a text face. It names it only
because it is what the renderer now falls back to for these glyphs.

## 4. Things the implementation must settle

1. **Commit the face.** Inter is not in `brand/fonts/` (checked 2026-11-11). It is presumably
   installed in the container by something other than this repository, since SHULL-CHG-0006 found it
   absent on 2026-09-07. Not verified how. If it is not committed and installed by the SessionStart
   hook like Archivo, a container without it falls back to something else and the QA render stops
   matching. Proposed: commit `Inter-Regular.ttf` (and Bold if a bold θ is needed) with
   `OFL-Inter.txt` and a sha256 line in `brand/fonts/README.md`.
2. **Matt's own machine.** `.docx`/`.pptx` files declare Trade Gothic Next. Whether Trade Gothic Next
   carries θ and ⁻, and what Word or PowerPoint substitutes if it does not, is **not verified**. A
   file opened and printed from Word may not match the PDF that passed the audit.
3. **Keys.** ShullHand v0.2 has no Greek (`brand/fonts/README.md`, "Known limits"). Whether
   `PatrickHand-Regular.ttf` carries U+03B8 and U+207B is **not verified**. If it does not, a
   handwritten θ on a key would fall to a third face. Check with fontTools before implementing.
4. **Which glyphs the audits named.** As reported to the Secretary: θ (U+03B8) and ⁻ (U+207B), both
   rendering in Inter. The audit output itself is not on disk, and the Secretary has no shell to
   re-run it. The U3 notes specs carry θ and ⁻ in about 50 places across the generator and the two
   JSON files (`templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py` line 31 marks θ "not in
   Archivo"). Re-run `audit_fonts.py` on the rendered U3 notes and paste the character list into
   `Verified:`.

## 5. Options (for the main session to put to Matt if it needs to)

| Option | What | Notes |
|---|---|---|
| **A. This record** | One named fallback face (Inter), per glyph, closed glyph set, Physics only. | Recommended. Matches what already renders, so built material does not change. |
| B. Leave the rule, accept the FAIL | Ship with a known audit failure each time. | Not recommended. A gate that always fails stops being read. |
| C. Use the stack's own last rung | Route these glyphs to Liberation Sans, which is already in the stack (INHERITED), instead of a new face. | Whether Liberation Sans carries U+207B is **not verified**. QA_GATE §1 treats Liberation in `pdffonts` as a failed substitution, so it would need the same scoped audit change. Its look differs from Archivo more than Inter's does. |
| D. Draw the glyphs | Typeset θ and ⁻ as small vector drawings, as the key builder draws arrows. | No font change. Much more build work, and the text stops being searchable. |

## 6. What this does not do

- It does not edit `brand/`, `standards/`, `scripts/audit_fonts.py` or any font file.
- It does not change any built document, template or spec.
- It does not decide the LOCKED conflict. Matt does.

(Section 6 describes the record as proposed. Implementation is in the `Implemented By` field and section 7.)

## 7. Implementation status

**Done (uncommitted, 2026-11-11):** token 2.1, brand prose 2.2, QA gate pointer 2.3, Physics
decision-log entry, CHANGELOG row (PARTIAL).

The QA gate line says `--physics` "will enforce" the token, marked pending, rather than "enforces"
as 2.3 words it. The flag does not exist yet, so the present tense would be untrue. When P1 lands,
change "will enforce it (pending, SHULL-CHG-0072)" to "enforces it".

**Pending code follow-ups (not started):**

| # | Follow-up | Where | Settles |
|---|---|---|---|
| P1 | Add a `--physics` flag to `scripts/audit_fonts.py`. It reads `typography.mathFallback` (family and ranges) from `brand/tokens.json` and checks each glyph: it allows a span in that face only if every character falls inside the token's ranges and is absent from Archivo. Add the tests listed in 2.4. | `scripts/audit_fonts.py` and its tests | 2.4 |
| P2 | Commit the Inter font files (`Inter-Regular.ttf`, plus Bold if a bold θ is needed) with `OFL-Inter.txt` and a sha256 line in `brand/fonts/README.md`. Have the SessionStart hook install it like Archivo. | `brand/fonts/` | 4.1 |
| P3 | Check with fontTools whether `PatrickHand-Regular.ttf` carries θ (U+03B8) and ⁻ (U+207B). If it lacks either, a handwritten θ on a key falls to a third face, and that needs its own decision. | `brand/fonts/` | 4.3 |

Still open and not assigned: 4.2 (Trade Gothic Next coverage on Matt's machine) and 4.4 (re-run the
audit on the rendered U3 notes and paste the character list into `Verified:`).
