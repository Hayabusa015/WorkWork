#!/usr/bin/env python3
"""Generate static Archivo instances from the variable font.

LibreOffice embeds the two-axis Archivo[wdth,wght] variable font as a Type 3
font, which rasterises badly and does not survive a print pipeline cleanly.
Static instances embed as TrueType. Run this after updating the variable source.

    python3 brand/fonts/generate-statics.py
"""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = os.path.dirname(os.path.abspath(__file__))
WEIGHTS = [("Regular", 400), ("Medium", 500), ("SemiBold", 600), ("Bold", 700)]
SOURCES = [("Archivo[wdth,wght].ttf", ""), ("Archivo-Italic[wdth,wght].ttf", "Italic")]

for src, suffix in SOURCES:
    path = os.path.join(HERE, src)
    if not os.path.exists(path):
        raise SystemExit(f"missing variable source: {src}")
    for name, wght in WEIGHTS:
        font = TTFont(path)
        inst = instancer.instantiateVariableFont(
            font, {"wght": wght, "wdth": 100}, inplace=False, updateFontNames=True
        )
        out = os.path.join(HERE, f"Archivo-{name}{suffix}.ttf")
        inst.save(out)
        print(f"  {os.path.basename(out):30} {os.path.getsize(out):>8}")

print("\nArchivo Narrow needs no instancing - its single-axis variable font "
      "already embeds as TrueType.")
