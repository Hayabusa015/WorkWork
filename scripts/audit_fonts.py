#!/usr/bin/env python3
"""Fail a PDF that renders in anything but the brand face.

    python3 scripts/audit_fonts.py out.pdf

The rule is stated in four places - QA_GATE.md, audit-deliverable, build-presentation,
apply-shull-design - and until now was enforced in none of them. Every one of them says
the same thing: DejaVu or Liberation in `pdffonts` means the substitution did not take
and the classroom copy has different metrics from the one that was checked.

The usual cause is one character. A single U+2610 checkbox pulls a whole second font
into the file, and the fallback face is what actually prints - so the box a student
sees is not the box that was designed. This names the character, not just the font,
because "DejaVuSans is present" is not actionable and "the checkbox pulled it in" is.
"""
import os, re, subprocess, sys
from fontTools.ttLib import TTFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = ("Archivo",)


def brand_cmap():
    chars = set()
    for name in ("Archivo-Regular.ttf", "Archivo-Bold.ttf"):
        tt = TTFont(os.path.join(REPO, "brand", "fonts", name))
        chars |= set(tt.getBestCmap())
    return chars


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    pdf = sys.argv[1]
    out = subprocess.run(["pdffonts", pdf], capture_output=True, text=True).stdout
    fonts = []
    for line in out.strip().split("\n")[2:]:
        if line.strip():
            fonts.append(line.split()[0].split("+")[-1])
    strays = [f for f in fonts if not any(f.startswith(a) for a in ALLOWED)]

    print(f"audit_fonts: {os.path.basename(pdf)}")
    for f in fonts:
        print(f"   {'STRAY  ' if f in strays else 'ok     '}{f}")

    if not strays:
        print("\nOK — Archivo only.")
        return 0

    # Name the characters that cannot be set in the brand face, so the fix is one edit
    # rather than a hunt.
    import pymupdf
    have = brand_cmap()
    doc = pymupdf.open(pdf)
    missing = {}
    for page in doc:
        for ch in page.get_text():
            if ch.isspace() or ord(ch) in have:
                continue
            missing.setdefault(ch, 0)
            missing[ch] += 1
    print(f"\nFAIL — {len(strays)} substituted face(s): {', '.join(sorted(set(strays)))}")
    if missing:
        print("Characters Archivo cannot set:")
        for ch, n in sorted(missing.items(), key=lambda x: -x[1]):
            print(f"   {ch!r}  U+{ord(ch):04X}  ×{n}")
    else:
        print("No stray characters found - the substitution is a style (an italic or a "
              "weight) the shipped files do not cover, not a glyph.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
