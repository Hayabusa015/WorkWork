#!/usr/bin/env python3
"""Fail if a hex colour is written anywhere but brand/tokens.json.

Every palette conflict in the legacy system came from the same hex being typed
into two files by hand. This is the check that makes that impossible.

    python3 scripts/validate_tokens.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, walk, read, report

HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")

# The one documented exception: var() does not resolve in SVG presentation
# attributes under WeasyPrint, so the hand-built diagram in the lab template
# carries literals. See SHULL-CHG-0010.
SVG_EXCEPTION = {"templates/lab/SHULL_Lab_TEMPLATE_MASTER.html"}
SVG_ALLOWED = {"#" + "14161B", "#" + "EDF0E5"}

# Generated from brand/tokens.json by a script - a build artifact, not a source of truth.
# Written from tokens.json by a build script, never by hand. Each one names its
# generator in its own header. tokens.generated.js also happens to store hex without
# a leading "#", so the pattern below would miss it either way - it is listed here so
# the exemption is a decision on the record rather than an accident of a regex.
GENERATED = {
    "templates/lab/shull-lab-tokens.css",       # scripts/build_lab_css.py
    "templates/slide/tokens.generated.js",      # scripts/build_slide_tokens.py
}

# This file names the exception values it permits; that is not duplication.
SELF = {"scripts/validate_tokens.py"}

SOURCE = "brand/tokens.json"

def main():
    errors, checked = [], 0
    for rel in walk():
        norm0 = rel.replace(os.sep, "/")
        if norm0 == SOURCE or norm0 in GENERATED or norm0 in SELF:
            continue
        text = read(rel)
        found = HEX.findall(text)
        if not found:
            checked += 1
            continue
        checked += 1
        norm = rel.replace(os.sep, "/")
        for h in sorted(set(found)):
            if norm in SVG_EXCEPTION and h.upper() in SVG_ALLOWED:
                continue
            line = next((i for i, l in enumerate(text.splitlines(), 1) if h in l), "?")
            errors.append(f"{norm}:{line} raw hex {h} — values belong in {SOURCE}")
    return report("validate_tokens", errors, checked)

if __name__ == "__main__":
    sys.exit(main())
