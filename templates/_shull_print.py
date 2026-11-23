#!/usr/bin/env python3
"""The binding side of every printed page: mirror margin and three-hole guides.

SHULL-CHG-0103. Every printed page has an inside (binding) margin, on the left of odd
pages and the right of even pages, and three faint circle outlines where a three-hole
punch lands. The numbers live in brand/tokens.json (`print.binding`, `print.holeGuides`)
and nowhere else; this module only reads them and turns them into geometry, so the Word
builders, the WeasyPrint templates and the audit all draw the same circles.

    from _shull_print import BINDING, page_width_in, text_width_in, guides

The inside margin is never one of the page-budget levers (standards/QA_GATE.md §2). A
builder that wants more room tightens its own content or its outside/top/bottom margins.
"""
import json, os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
_T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))

PAGE_W_IN, PAGE_H_IN = 8.5, 11.0     # US Letter, the only paper the builders set


def _inches(v):
    return float(str(v).strip().removesuffix("in"))


def _points(v):
    return float(str(v).strip().removesuffix("pt"))


class _Binding:
    """`print.binding` and `print.holeGuides`, resolved once."""

    def __init__(self, t):
        b, h = t["print"]["binding"], t["print"]["holeGuides"]
        self.mirror = bool(b["mirror"])
        self.inside_in = _inches(b["inside"])
        self.count = int(h["count"])
        self.diameter_in = float(h["diameterIn"])
        self.radius_in = self.diameter_in / 2
        self.centre_from_edge_in = float(h["centreFromBindingEdgeIn"])
        self.centres_from_top_in = [float(y) for y in h["centresFromTopIn"]]
        if len(self.centres_from_top_in) != self.count:
            raise SystemExit("tokens.json print.holeGuides: count and centresFromTopIn disagree")
        self.stroke_hex = t["ground"][h["stroke"]]["hex"]
        self.stroke_pt = _points(h["strokeWeight"])
        if h.get("fill", "none") != "none":
            raise SystemExit("tokens.json print.holeGuides: guides are outline only")
        self.status = b.get("status", "")


BINDING = _Binding(_T)


def text_block_in(outside_in):
    """The text block between the inside margin and the builder's own outside margin."""
    return round(PAGE_W_IN - BINDING.inside_in - outside_in, 4)


def is_odd(page_no):
    """Page 1 is a right-hand (odd) page; its binding edge is on the left."""
    return page_no % 2 == 1


def guides(page_no):
    """Circle centres (x, y) in inches from the page's top-left corner, for this page."""
    c = BINDING.centre_from_edge_in
    x = c if is_odd(page_no) else PAGE_W_IN - c
    return [(x, y) for y in BINDING.centres_from_top_in]


def hole_zone(page_no):
    """(x0, x1) in inches: binding edge to the inside margin. Only the guides go here."""
    if is_odd(page_no):
        return 0.0, BINDING.inside_in
    return PAGE_W_IN - BINDING.inside_in, PAGE_W_IN


# ---------------------------------------------------------------------------------
# HTML / WeasyPrint.

def token_margins():
    """`print.margins` top, outside and bottom, in inches. Under mirroring the token's
    left/right pair is read as inside/outside; the inside is `print.binding.inside`."""
    m = _T["print"]["margins"]
    return _inches(m["top"]), _inches(m["right"]), _inches(m["bottom"])


def _svg(page_no):
    r = BINDING.radius_in
    circles = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{BINDING.stroke_hex}" '
        f'stroke-width="{BINDING.stroke_pt / 72:.5f}"/>' for x, y in guides(page_no))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE_W_IN}in" height="{PAGE_H_IN}in" '
            f'viewBox="0 0 {PAGE_W_IN} {PAGE_H_IN}">{circles}</svg>')


def page_css(top_in, outside_in, bottom_in):
    """The @page geometry a WeasyPrint template gets, binding side included.

    All four margins are set here, mirrored: page 1 is a :right page, so its inside
    margin is on the left. The caller owns top, outside and bottom; the inside comes from
    tokens. The guides are the page background, an SVG the size of the sheet. WeasyPrint
    positions a page background from the page area, not the sheet edge, so the SVG is
    pulled back by the left and top margins to land on the sheet's own coordinates; it
    sits in the margin and never takes part in the flow.
    """
    ins = BINDING.inside_in
    out = []
    for sel, left, right, page_no in ((":right", ins, outside_in, 1),
                                      (":left", outside_in, ins, 2)):
        url = "data:image/svg+xml;charset=utf-8," + quote(_svg(page_no))
        out.append(
            f"@page {sel} {{ margin: {top_in}in {right}in {bottom_in}in {left}in; "
            f"background: url(\"{url}\") no-repeat; "
            f"background-position: -{left}in -{top_in}in; "
            f"background-size: {PAGE_W_IN}in {PAGE_H_IN}in; }}")
    return ("/* SHULL-CHG-0103 binding side, generated from brand/tokens.json "
            "(print.binding, print.holeGuides) by templates/_shull_print.py. */\n"
            + "\n".join(out) + "\n")


def inject_page_css(html, top_in, outside_in, bottom_in):
    """Put the binding rules last in <head>, so they win over the template's @page."""
    block = "<style>\n" + page_css(top_in, outside_in, bottom_in) + "</style>\n"
    i = html.lower().rfind("</head>")
    return html[:i] + block + html[i:] if i >= 0 else block + html
