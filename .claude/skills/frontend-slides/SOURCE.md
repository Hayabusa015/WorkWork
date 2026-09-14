# Source

Vendored from [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides),
commit `9906a34`, 2026-09-14. MIT licensed, © 2025 Zara Zhang — see `LICENSE`.
Not written for or by SHULL OS.

**One copy, not two.** Upstream ships its whole tree twice — once at the root and again
under `plugins/frontend-slides/skills/frontend-slides/`, byte-identical (verified with
`diff -r`). Only the root layout is vendored here; that is 81 files instead of 163, and
2.1 MB instead of 4.9 MB. Upstream's `.claude-plugin/marketplace.json` points at
`./plugins/frontend-slides`, so it is not carried either — it describes a plugin layout
this copy deliberately does not have.

## What it is

A Claude Code skill that builds **zero-dependency HTML presentations** — a single HTML
file with inline CSS/JS, on a mandatory 1920×1080 fixed stage that scales whole to the
viewport. It also ships `scripts/extract-pptx.py` (reads an existing `.pptx` into JSON;
needs `python-pptx`, already installed here) and `scripts/export-pdf.sh` (Playwright
screenshots each slide at 1920×1080 into a PDF).

## The conflict you need to know about

**This skill's design philosophy is the opposite of SHULL's, on purpose.** It tells the
model to vary fonts and palettes between decks, prefer "distinctive" faces, layer
gradients and atmospheric backgrounds, and "think outside the box" — because it is
written for one-off pitch decks where sameness is the failure.

SHULL is the other case. The palette is LOCKED per course, the face is Archivo, the
16pt floor is what a student in the back row can actually read, and consistency across
a school year is the point. Pointed at a classroom deck unconstrained, this skill will
produce something confidently off-brand.

**So it is not used unconstrained.** `bold-template-pack/templates/shull-science/`
is generated from `brand/tokens.json` by `scripts/build_slide_html_template.py` and is
the on-brand option: it carries the locked geometry, palette, type scale and floors, and
its § 5 explicitly overrides the parent skill's font/palette/background guidance. **When
building any SHULL deck, select `shull-science`.** The other ~25 templates
(sakura-chroma, retro-zine, bold-poster…) are upstream's; they are fine references for
craft and wrong for Matthew's classroom.

## Verified here, not assumed

`scripts/extract-pptx.py` was run against a real SHULL deck — `chem_u01_s01.4_isotopes`
built by `templates/slide/build_deck.js`, 13 slides. It returned all 13 with their text
and the `U01 • S01.4` footer codes intact, so it can read Matthew's existing decks.

**Known limitation:** every slide came back as `(no title)`. The SHULL builder composes
slides from positioned text boxes rather than PowerPoint's title placeholder, so the
extractor gets the words but not which box was the headline, the eyebrow or the footer.
Converting a SHULL `.pptx` into HTML would need that mapping written — the geometry in
the template's § 1 is exactly what would drive it, since the Y positions identify the
roles. Not built.

## The geometry is not a compromise

SHULL Slide System v2 is 13.333in × 7.5in. At 144 px/in that is 1920 × 1080 — the exact
rectangle this skill mandates. Every locked SHULL measurement converts by ×144 (inches)
or ×2 (points); the 16pt floor is exactly 32px. The two systems are the same rectangle
in different units, which is why an on-brand template was possible at all.

## What it does NOT replace

`templates/slide/` — the twelve-layout **.pptx** builder, confirmed under
SHULL-CHG-0013 — still stands and is untouched. This skill produces **HTML**, a
different artifact. Which of the two (or Gamma, per the 2026-09-12 open question) becomes
the way Matthew actually builds decks is an open decision, not something vendoring this
settled. Nothing here has been proposed as superseding anything.

## Not re-vendored automatically

A point-in-time copy, not a live dependency. Updating means re-pulling from upstream and
diffing by hand — and re-running the generator, since the `shull-science` template is
ours and upstream will not have it.
