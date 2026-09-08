#!/usr/bin/env python3
"""Compute and write the contrast and grayscale measurements in brand/tokens.json.

Every colour in the palette carries its measured contrast against both grounds
and its grayscale value. A colour that enters the palette without measurements is
a defect - that rule exists because the six course colours were chosen for a dark
ground, the default background later became white, and nobody re-measured until
two days after the palette was locked.

    python3 scripts/measure_tokens.py            rewrite measurements in place
    python3 scripts/measure_tokens.py --check    exit 1 if any are stale (CI)

Never hand-edit a "measured" block.
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = os.path.join(REPO, "brand", "tokens.json")

def _grounds():
    """The three grounds every colour is measured against - read, never typed."""
    with open(TOKENS) as fh:
        g = json.load(fh)["ground"]
    return g["white"]["hex"], g["parchment"]["hex"], g["asphalt"]["hex"]


WHITE, PARCHMENT, ASPHALT = _grounds()


def _srgb(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(h):
    r, g, b = _rgb(h)
    return 0.2126 * _srgb(r) + 0.7152 * _srgb(g) + 0.0722 * _srgb(b)


def contrast(a, b):
    l1, l2 = sorted((luminance(a), luminance(b)), reverse=True)
    return round((l1 + 0.05) / (l2 + 0.05), 2)


def grayscale(h):
    r, g, b = _rgb(h)
    return round(0.299 * r + 0.587 * g + 0.114 * b)


def verdict(ratio):
    if ratio >= 7.0:
        return "body text, AAA"
    if ratio >= 5.5:
        return "body text, meets SHULL target"
    if ratio >= 4.5:
        return "body text, AA minimum only"
    if ratio >= 3.0:
        return "large text only (24px+, or 19px bold)"
    return "NOT TYPE - fill, rule, border or block only"


def measure(hexval):
    return {
        "grayscale": grayscale(hexval),
        "onWhite": contrast(hexval, WHITE),
        "onWhiteVerdict": verdict(contrast(hexval, WHITE)),
        "onParchment": contrast(hexval, PARCHMENT),
        "onAsphalt": contrast(hexval, ASPHALT),
        "onAsphaltVerdict": verdict(contrast(hexval, ASPHALT)),
    }


def walk(node):
    """Annotate every dict carrying a 'hex', recursively. Also handles 'deep'."""
    changed = False
    if isinstance(node, dict):
        if "hex" in node and isinstance(node["hex"], str):
            new = measure(node["hex"])
            if node.get("measured") != new:
                node["measured"] = new
                changed = True
        if "deep" in node and isinstance(node["deep"], str):
            new = measure(node["deep"])
            if node.get("measuredDeep") != new:
                node["measuredDeep"] = new
                changed = True
        for v in node.values():
            changed |= walk(v)
    elif isinstance(node, list):
        for v in node:
            changed |= walk(v)
    return changed


def pair_warnings(tokens):
    """Report course pairs whose display colours are too close in grayscale."""
    out = []
    floor = tokens.get("rules", {}).get("grayscaleSeparationMin", 20)
    for name, c in tokens.get("courses", {}).items():
        if "primary" not in c or "secondary" not in c:
            continue
        d = abs(grayscale(c["primary"]["hex"]) - grayscale(c["secondary"]["hex"]))
        if d < floor:
            out.append(f"{name}: display pair {d} grey levels apart (floor {floor}) "
                       f"- categorical use REQUIRES border and label differentiation")
    return out


def main():
    check = "--check" in sys.argv
    with open(TOKENS) as fh:
        tokens = json.load(fh)

    changed = walk(tokens)

    if check:
        if changed:
            print("STALE: measurements in brand/tokens.json do not match the hex values.")
            print("Run: python3 scripts/measure_tokens.py")
            return 1
        print("brand/tokens.json measurements are current.")
    else:
        with open(TOKENS, "w") as fh:
            json.dump(tokens, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"{'rewrote' if changed else 'no change to'} brand/tokens.json")

    for w in pair_warnings(tokens):
        print(f"  NOTE  {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
