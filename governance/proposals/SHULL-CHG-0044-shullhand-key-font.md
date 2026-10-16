# SHULL-CHG-0044 — Answer keys use ShullHand, a font made from Matt's own handwriting

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0044 |
| **Date** | 2026-10-16 |
| **Source** | User — Matt, conversation 2026-10-16. Evidence from the main session (the Secretary has not opened any of these files and reports them as the main session's account): font `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hf/ShullHand.ttf`, alternates map `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hf/ShullHand_alts.json`, build scripts `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hf/extract.py` and `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hf/buildfont.py`, source scan `/root/.claude/uploads/a19de678-6877-52a4-8fdc-1159a824adb2/2f90d24e-scan_mshull_2026-10-16-07-32-57.pdf` (2.4 MB), demo `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/key_demo_shull.png`, comparison `/tmp/claude-0/-home-user-WorkWork/a19de678-6877-52a4-8fdc-1159a824adb2/scratchpad/hf/compare2.png`. |
| **Current Rule** | See §1, verbatim, with file and section. |
| **Proposed Rule** | See §2. Seven items (A-G), each separately approvable. |
| **Supersedes** | `brand/tokens.json` `typography.keyHandwriting.family` = "Patrick Hand" (added by SHULL-CHG-0043 Stage 1, commit 39e663a); and the Patrick Hand paragraph of `brand/fonts/README.md`. Does not supersede, and does not touch, the "Never substitute a font outside this stack" rule or its keys-only exception (that exception already points at the token, see Item C). |
| **Reason** | Matt asked whether his own handwriting could become a font ("If I gave you handwriting of mine could you turn it into a font"), filled in the sample sheet, and then said: "ok now i just want to use that font in the answer keys." The 0043 goal was keys that look handwritten "for authenticity"; his own hand is the most direct way to get it, and it removes a third-party typeface from the system. |
| **Affected Agents** | Builder agents that produce keys (through the key helper); Auditor (visual check); Secretary (implementation only, upon approval). |
| **Affected Skills** | None directly. The five skills named in SHULL-CHG-0043 Item D are not yet edited (Stage 2 not started) and must not name a font (Item F). |
| **Affected Courses** | All three, keys only. No course `DECISIONS.md` is touched. |
| **Risk** | Low-medium. Student pages are unchanged. The risk is in the key itself: a home-made font can make a character ambiguous (Matt's "2" resembles an "a"). Mitigated by the legibility-beats-authenticity rule in SHULL-CHG-0043 Item C.8, the Patrick Hand fallback, and the visual audit. |
| **Recommendation** | Approve A, B, C (no edit), D, F, G. Items E is tooling for the main session. Keep the font PROVISIONAL until Matt sees it on a real key. See §6. |
| **Decision** | Approved by Matthew Shull, 2026-10-16 ("approve 0044, yes to all five"). |
| **Status** | **APPROVED** |
| **Implemented By** | not yet |
| **Verified** | no |

---

## 1. Current Rule — verbatim

### 1a. `brand/tokens.json`, `typography.keyHandwriting` (lines 416-423)

```json
"keyHandwriting": {
  "family": "Patrick Hand",
  "status": "PROVISIONAL",
  "license": "OFL",
  "source": "SHULL-CHG-0043",
  "scope": "teacher answer keys ONLY",
  "note": "Teacher answer keys only. Never on a student page. No superscript, subscript, arrow, or Delta glyphs; the key builder draws those."
},
```

### 1b. `brand/fonts/README.md`, Patrick Hand paragraph (lines 14-18)

> **Patrick Hand** — SIL Open Font License, committed here (`PatrickHand-Regular.ttf`,
> `OFL-PatrickHand.txt`). Source: `google/fonts` repository, `ofl/patrickhand`. Added by SHULL-CHG-0043
> (PROVISIONAL). **Teacher answer keys only, never a student page** — see `typography.keyHandwriting` in
> `brand/tokens.json`. It is deliberately outside the Archivo stack; it has no superscript, subscript,
> arrow, or Delta glyphs. sha256 of the ttf: `0f173b3e6cb6d1af25babf7f0057c5ac4ee11f9992b0469bb817e967ef4ad0fc`.

### 1c. `brand/SHULL_DESIGN_SYSTEM.md`, typography (lines 150-153)

> **Never substitute a font outside this stack.** Never a novelty "school" font. Never a convenient
> one.
>
> One exception: `typography.keyHandwriting`, on teacher answer keys only, approved in SHULL-CHG-0043 by Matt, 2026-10-16.

### 1d. `brand/fonts/` today

Archivo and Archivo Narrow files, `OFL-*.txt`, `PatrickHand-Regular.ttf`, `OFL-PatrickHand.txt`, `trade-gothic-next.conf`, `generate-statics.py`, `README.md`. No ShullHand files, no `source/` directory. `standards/ANSWER_KEYS.md` does not exist (SHULL-CHG-0043 Stage 2 not started).

## 2. Proposed Rule

### Item A — `typography.keyHandwriting` becomes ShullHand (`brand/tokens.json`)

Proposed entry (replaces 1a; same key, same position):

```json
"keyHandwriting": {
  "family": "ShullHand",
  "status": "PROVISIONAL",
  "license": "none (Matt's own handwriting; no third-party licence)",
  "source": "SHULL-CHG-0044",
  "scope": "teacher answer keys ONLY",
  "note": "Teacher answer keys only. Never on a student page. Made from Matt's handwriting sample (v0.1). Letters are separate, not joined. No superscript, subscript, arrow, sigma, or Delta glyphs; the key builder draws those. Fallback for any missing glyph: Patrick Hand."
},
```

- Status stays **PROVISIONAL** until Matt confirms the font on a real key. Nothing here makes it LOCKED.
- The family name written in the token must equal the font's internal family name; the main session confirms this at implementation (a mismatch would break `audit_fonts.py`).
- "Provenance": the glyphs are derived from Matt's own handwriting, so there is no third-party licence to carry. The provenance is this record plus the committed source (Item D).
- Scope is unchanged: teacher answer keys only.

### Item B — Font files and README (`brand/fonts/`)

1. Add `brand/fonts/ShullHand.ttf` and `brand/fonts/ShullHand_alts.json` (maps a base character to a Private Use alternate; the key helper alternates the two copies so repeated letters do not look stamped).
2. **Binary copy is a mechanical step by the main session**, under this record once APPROVED, exactly as in SHULL-CHG-0043 Item B (the Secretary has no shell and cannot copy a binary). The Secretary edits the text files around it (tokens.json, README) and records the sha256 of each file in the README. This is the same narrow exception to "only the Secretary writes to `brand/`" that Matt already accepted for 0043; it is restated here so approval of this record covers it explicitly.
3. `brand/fonts/README.md`: replace the Patrick Hand paragraph with a ShullHand paragraph (what it is, v0.1, made from Matt's handwriting, keys only, glyph gaps, sha256), and keep a shortened Patrick Hand paragraph stating it is now the fallback for any glyph ShullHand lacks.
4. **Patrick Hand files stay** (`PatrickHand-Regular.ttf`, `OFL-PatrickHand.txt`) as the fallback. `OFL-PatrickHand.txt` stays for as long as the font stays. Whether to delete Patrick Hand later is **Matt's call; this record does not decide it** (Question 2).
5. Known limits, stated plainly in the README (as reported by the main session):
   - v0.1: 138 characters plus 36 alternate "again" copies of letters and digits; cap height 700/1000 UPM, x-height about 461, space advance about 346; lowercase scaled 0.92 to match his running writing; baseline snapping per letter class.
   - Letters are separate, not joined.
   - His "2" resembles an "a". Context usually resolves it, but it is a legibility risk (see Item F and §4).
   - No sigma and no vector-arrow glyphs yet (the arrow is drawn by the builder; sigma could be added from his sentence page).
   - Colons and periods are heavy blobs.
   - No superscript or subscript glyphs; the builder draws them.

### Item C — `brand/SHULL_DESIGN_SYSTEM.md`: no change needed

Checked. The exception sentence (1c) names `typography.keyHandwriting` and does not name Patrick Hand or any font, so it already satisfies one-fact-one-place and survives this swap unchanged. **Proposed: no edit.** The Secretary does not alter that file under this record. (Optional: the sentence cites SHULL-CHG-0043 as the approval; the swap adds a second record, SHULL-CHG-0044, but the exception itself is unchanged, so no citation edit is proposed. Matt may ask for one.)

### Item D — Source material committed so the font can be regenerated

Proposed: commit the source scan and the build scripts.

- Scan: `brand/fonts/source/` (for example `brand/fonts/source/ShullHand-handwriting-sample-2026-10-16.pdf`, 2.4 MB, copied mechanically by the main session).
- Build scripts: `scripts/build_handwriting_font.py` (to be created by the main session from `extract.py` and `buildfont.py`; tooling, not governed). The font is regenerated from scan plus script.
- Reasoning: git is the only durable write path in this system (`CLAUDE.md` §5). Without the committed scan, a lost or overwritten `ShullHand.ttf` cannot be rebuilt, and v0.2 would need Matt to rewrite the sheet.
- **Privacy:** the scan is Matt's personal handwriting sample. It is the sample of his writing only (the Secretary has not seen it and cannot confirm it contains nothing else, for example a name or signature). This is a question for Matt (Question 1). If he says no, the font ships without the scan and cannot be regenerated; the record notes that.

### Item E — Tooling (not governed; main session; the Secretary does not edit `scripts/`)

Flagged so it is not forgotten, as in 0043 Item E:
- `scripts/audit_fonts.py`: the `--key` allow-list gains the ShullHand family name (and keeps Patrick Hand while it is the fallback). A student file rendering in ShullHand or Patrick Hand must still fail.
- `scripts/key_ink.py`: default key font switches to ShullHand, with Patrick Hand as per-glyph fallback. Its header comment currently says "The face is Patrick Hand (typography.keyHandwriting)"; it should read the family from the token rather than state a name.
- PDF embedding: the font-name check must match the embedded name of ShullHand (subset-prefixed names included).
- The key helper alternates the two copies from `ShullHand_alts.json`.

### Item F — Requirement on SHULL-CHG-0043 Stage 2 wording

When Stage 2 (Items C, D, H of 0043) is implemented, `standards/ANSWER_KEYS.md` and every skill pointer must refer to **"the key-handwriting face (`typography.keyHandwriting`)"** and must **never name a font**. Then a later font swap is a one-line token change, and no standard or skill goes stale. 0043 already uses the token in its Item C.2 and its audit line; this makes the requirement explicit. It binds the Secretary at Stage 2 implementation. SHULL-CHG-0043 is **not edited** by this record; this record is the cross-reference. (If the house style allows a note in 0043, Matt may ask for a one-line pointer there; that is a separate edit of an APPROVED record and is not proposed unasked.)

Legibility requirements this record adds to the Stage 2 audit line: the visual check of a key looks specifically for "2" read as "a", "1" read as "l", and a heavy colon or period read as a different mark. Where a character could be misread, the existing 0043 Item C.8 rule applies: that character or step falls back to Archivo (or Patrick Hand), and the key is never shipped ambiguous.

### Item G — Versioning

Recommendation:
- **v0.2 and later regenerated from the same committed scan and script, with the same character set and no new rule: routine regeneration**, no new record. The commit message names SHULL-CHG-0044 and the version, the README sha256 and version line are updated by the Secretary, and the Auditor visually checks one real key. It is a new font file but not a new rule.
- **A small follow-up record (SHULL-CHG-NNNN) is needed when** the change alters the rule or the inputs: a new source scan (new handwriting sample), a change of scope beyond keys, a change in the fallback policy, or removing Patrick Hand. This keeps drift visible.
- Why: the font is a build artefact of committed sources. Requiring a change record for every tweak of a colon would be ceremony; requiring one for a change of inputs or scope keeps the audit trail honest. Matt may prefer a record every time; that is his call (Question 4).
- Planned v0.2 candidates reported by the main session: sigma glyph, lighter colons and periods, more alternates.

## 3. Reason in short

Authenticity was Matt's reason for 0043. His own handwriting is the most authentic source, costs nothing in licences, and student pages are untouched. The font is home-made, so its weaknesses are real and are named above; they are handled by fallback and by the visual audit, not by hoping.

## 4. Scope limits

- **Keys only.** Student pages stay Archivo.
- **Legibility beats authenticity.** The visual audit is the backstop (a hook cannot see a misread glyph). Particular attention to "2" versus "a", "1" versus "l".
- **Handwriting is never used where legibility could fail.** Such steps fall back as in 0043 Item C.8.
- **v0.1 and PROVISIONAL.** Not a LOCKED token and not presented as settled.
- **Grayscale print.** Unchanged from 0043: ink colours and shapes carry the distinctions. The heavier colons and periods should be checked in the print-ink audit.
- **No claim of verification by the Secretary.** The Secretary has not opened the font, the scan, or the demo images; everything in Item B.5 is the main session's report.

## 5. Conflicts with LOCKED rules (Secretary does not resolve these; Matt decides)

| # | LOCKED rule | Where | Conflict |
|---|---|---|---|
| 1 | "Never substitute a font outside this stack. Never a novelty 'school' font." | `brand/SHULL_DESIGN_SYSTEM.md` lines 150-151 | **No new conflict.** The same keys-only exception Matt approved in SHULL-CHG-0043 (the 0043 §5 row 1 CONFLICT) covers whichever face the token names. This record changes which face, not the exception. Stated here because the exception was granted when the face was Patrick Hand: Matt's approval of this record is also his confirmation that the exception stays for ShullHand. |
| 2 | Archivo-only render check | `scripts/audit_fonts.py` `ALLOWED` | Tooling gate; handled by 0043 Item E (carve-out) and extended here by Item E. Not a LOCKED token. |

No LOCKED token is changed. `typography.primary`, `fallback`, and `condensed` are untouched. No CONFLICT, PROVISIONAL, or UNKNOWN item is converted to LOCKED by this record. The `keyHandwriting` entry stays PROVISIONAL.

## 6. Recommendation

Approve Items A, B, D, F, G, with Item C as "no edit" and Item E as main-session tooling. Reasons: the change is small, reversible (one commit), confined to keys, and keeps Patrick Hand as a safety net. Keep `status` PROVISIONAL until Matt sees ShullHand on a real key (a Chemistry stoichiometry key and a Physics kinematics key exercise digits, stacked fractions, and exponents, which is where "2" and the colons matter most). Item D is the one that needs Matt's personal say-so because it commits his handwriting.

Items are separately approvable. Approving A without B would leave the token naming a font that is not in the repo, so A and B should be approved together (the Secretary will say so if only one is approved).

## 7. Questions for Matt (one at a time as needed)

1. May the scan of your handwriting sample be committed to the repository (under `brand/fonts/source/`) so the font can be regenerated? Yes or no. (Recommended: yes.)
2. Keep Patrick Hand in place as the fallback for any glyph ShullHand lacks? (Recommended: yes. Deleting it is a separate decision for later.)
3. Keep ShullHand PROVISIONAL until you have seen it on a real key? (Recommended: yes.)
4. For later versions of the font (sigma, lighter colons, more alternates): routine regeneration from the committed sources, or a small change record each time? (Recommended: routine; a record only if the sample, scope, or fallback changes.)
5. Is the main session copying the font, alternates map, and scan into `brand/` mechanically under this record acceptable, as it was for Patrick Hand?

## 8. Not done by this record

No skill, standard, brand, or course file was edited. `change-log/CHANGELOG.md` was not edited (the main session does that when it records the decision). No file was copied or committed. SHULL-CHG-0043 was not edited. Proposal only; implementation waits for a committed record with `Status: APPROVED` and a verbatim `Decision:` quote (`governance/CHANGE_CONTROL.md` §4).

## 9. Verification plan (for the Secretary, after approval)

- `brand/tokens.json` parses; `typography.keyHandwriting.family` is "ShullHand", status PROVISIONAL, source SHULL-CHG-0044; `scripts/validate_tokens.py` passes.
- `brand/fonts/` contains `ShullHand.ttf` and `ShullHand_alts.json` (and `source/` only if Item D approved); the README sha256 values match the committed files; the font's internal family name equals the token's `family`.
- Patrick Hand files still present; `OFL-PatrickHand.txt` present.
- `brand/SHULL_DESIGN_SYSTEM.md` unchanged (`git diff` shows no change to it).
- `scripts/audit_fonts.py` passes a sample key rendered in ShullHand and fails the same text on a student file (main session runs it and reports).
- A sample key is rendered and visually inspected, page by page, for "2" versus "a", "1" versus "l", and colons and periods.
- `git diff` is limited to the cited brand files, this record, and the changelog row.
- Fill in `Implemented By` with the commit SHA and `Verified` with the result.
