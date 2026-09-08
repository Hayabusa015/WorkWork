#!/usr/bin/env python3
"""Generate templates/slide/tokens.generated.js from brand/tokens.json.

The slide template is built by pptxgenjs, which needs JavaScript. That is not a
licence to keep a second copy of the palette in a .js file - which is exactly what
the legacy system did, in tokens.js AND tokens.phys.js, and it is how Physics ended
up with a palette nobody had re-measured.

A hex is typed in tokens.json and nowhere else. This script is the only thing that
moves one into JavaScript, and the file it writes says so at the top.

    python3 scripts/build_slide_tokens.py
    python3 scripts/build_slide_tokens.py --check    exit 1 if the output is stale
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "brand", "tokens.json")
OUT = os.path.join(REPO, "templates", "slide", "tokens.generated.js")


def bare(h):
    """pptxgenjs wants RRGGBB with no leading hash."""
    return h.lstrip("#").upper()


def build():
    t = json.load(open(SRC))
    g, geo, ty = t["ground"], t["slideGeometry"], t["typography"]

    payload = {
        "version": t["version"],
        "ground": {k: bare(v["hex"]) for k, v in g.items()},
        "courses": {
            name: {
                "primary": bare(c["primary"]["hex"]),
                "secondary": bare(c["secondary"]["hex"]),
                "primaryDeep": bare(c["primaryDeep"]["hex"]),
                "label": name.upper(),
            }
            for name, c in t["courses"].items()
        },
        "type": ty["slideScale"],
        "fonts": {"display": ty["stack"].split(",")[0], "body": ty["stack"].split(",")[0]},
        "floor": ty["floors"]["slideContent"]["pt"],
        "geom": {
            "W": geo["widthIn"], "H": geo["heightIn"],
            "M": {"l": geo["margins"]["left"], "r": geo["margins"]["right"],
                  "t": geo["margins"]["top"], "b": geo["margins"]["bottom"]},
            "RAIL": geo["railWidthIn"],
            "eyebrowY": geo["eyebrowY"], "hairlineY": geo["hairlineY"],
            "hairlineW": geo["hairlineWidthIn"],
            "headlineY": geo["headlineY"], "headlineH": geo["headlineHeightIn"],
            "subheadY": geo["subheadY"], "bodyTopY": geo["bodyTopY"],
            "footerY": geo["footerY"], "mustWriteH": geo["mustWriteHeightIn"],
            "padX": geo["cardPaddingIn"]["horizontal"],
            "padY": geo["cardPaddingIn"]["vertical"],
        },
        "lineCaps": geo["lineCaps"],
        "darkGroundLayouts": geo["darkGroundLayouts"],
    }

    head = (
        "/* GENERATED FILE - DO NOT EDIT.\n"
        "   Written by scripts/build_slide_tokens.py from brand/tokens.json, which is the\n"
        "   only place in SHULL OS where a hex is typed. Edit tokens.json and re-run.\n"
        "   Hand-editing this file puts a colour in two places, which is the defect the\n"
        "   whole system is built to prevent. */\n\n"
    )
    return head + "module.exports = " + json.dumps(payload, indent=2) + ";\n"


def main():
    text = build()
    if "--check" in sys.argv:
        current = open(OUT).read() if os.path.exists(OUT) else ""
        if current != text:
            print("build_slide_tokens: templates/slide/tokens.generated.js is STALE - "
                  "run python3 scripts/build_slide_tokens.py", file=sys.stderr)
            return 1
        print("build_slide_tokens: generated tokens are current")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w").write(text)
    print(f"wrote {os.path.relpath(OUT, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
