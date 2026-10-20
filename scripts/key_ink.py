"""Hand-written look for teacher answer keys (SHULL-CHG-0043, SHULL-CHG-0044).

A small drawing helper: pencil and pen text, stacked fractions, raised and lowered
characters, wobbly boxes / arrows / strike-throughs, and a graphite-grain pencil layer for
sketches. It draws on a Pillow canvas and saves PNG or PDF.

Rules this helper carries, so the builders do not each re-decide them:
  - Colours are the keyInk tokens in brand/tokens.json, never typed here.
  - The face is whatever typography.keyHandwriting names (teacher keys only), read from the
    token, never typed here. A character that face lacks is drawn in the fallback face, one
    character at a time. Hand fonts have no super/subscript glyphs, so those are drawn here.
  - Division in a calculation step is a stacked fraction, never a divide sign or slash.
    A slash inside a unit name (m/s, g/mol) is a label and stays inline.
  - Legibility beats the look: jitter is small and the grain never covers a value.

Markup in strings:  m/s^{2}   H_{2}O   v_{0}   10^{23}   (braces required)
"""
import math, os, random, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import science_tools as st

SC = 3                      # internal scale; output is downsampled for smooth edges
_TOK = re.compile(r"([\^_])\{([^}]*)\}")


def key_font_path(family=None):
    """The file for typography.keyHandwriting (or `family`), e.g. 'ShullHand' -> ShullHand.ttf."""
    family = family or st.tokens()["typography"]["keyHandwriting"]["family"]
    stem = family.replace(" ", "")
    for name in (f"{stem}.ttf", f"{stem}-Regular.ttf"):
        if os.path.exists(st.font_path(name)):
            return st.font_path(name)
    sys.exit(f"key-handwriting face '{family}' has no font file in brand/fonts/")


def fallback_font_path():
    kh = st.tokens()["typography"]["keyHandwriting"]
    fb = kh.get("fallback") or kh.get("fallbackFamily") or "Patrick Hand"
    return key_font_path(fb if isinstance(fb, str) else fb.get("family", "Patrick Hand"))


def ink_colours():
    k = st.tokens()["keyInk"]
    return {n: st.hex_to_rgb(k[n]["hex"]) for n in ("pencil", "pen", "box", "arrow")}


class Page:
    def __init__(self, w, h, seed=7, bg=None, font_path=None, size_scale=1.0):
        self.w, self.h = w, h
        bg = bg or st.tokens()["ground"]["white"]["hex"]
        self.img = Image.new("RGBA", (w * SC, h * SC), st.hex_to_rgb(bg) + (255,))
        self.d = ImageDraw.Draw(self.img)
        self.ink = ink_colours()
        self.rnd = random.Random(seed)
        from fontTools.ttLib import TTFont
        self.fp = font_path or key_font_path()
        self.fb = fallback_font_path()
        self.cmap = set(TTFont(self.fp).getBestCmap())
        self._fb_fonts = {}
        self.alts = {}                      # char -> private-use alternate (a second hand-written copy)
        alt_json = os.path.splitext(self.fp)[0] + "_alts.json"
        if os.path.exists(alt_json):
            import json
            self.alts = json.load(open(alt_json))
        self._flip = False
        self.k = size_scale                 # fonts differ in width; scale every hand-written size at once
        self._fonts = {}

    # ---------------------------------------------------------------- text
    def font(self, size, ch=None):
        """The hand face at this size, or the fallback face if it lacks `ch`."""
        key = round(size * SC)
        if ch is not None and ord(ch) not in self.cmap:
            if key not in self._fb_fonts:
                self._fb_fonts[key] = ImageFont.truetype(self.fb, key)
            return self._fb_fonts[key]
        if key not in self._fonts:
            self._fonts[key] = ImageFont.truetype(self.fp, key)
        return self._fonts[key]

    def _runs(self, s):
        out, pos = [], 0
        for m in _TOK.finditer(s):
            out += [(c, "n") for c in s[pos:m.start()]]
            out += [(c, m.group(1)) for c in m.group(2).replace("-", "−")]
            pos = m.end()
        return out + [(c, "n") for c in s[pos:]]

    def width(self, s, size):
        size = size * self.k
        return sum(self.font(size if k == "n" else size * 0.62, c).getlength(c) + 0.5 * SC
                   for c, k in self._runs(s)) / SC

    def text(self, x, y, s, size=34, ink="pencil", jitter=1.0):
        """Draw at (x, y) logical px, y = top of line. Returns end x (logical px)."""
        col = self.ink[ink]
        size = size * self.k
        x *= SC
        y *= SC
        for ch, k in self._runs(s):
            ft = self.font(size if k == "n" else size * 0.62, ch)
            if ch in self.alts:             # alternate between the two hand-written copies of a letter
                self._flip = not self._flip
                draw_ch = self.alts[ch] if self._flip else ch
            else:
                draw_ch = ch
            dy = {"n": 0, "^": -0.03 * size * SC, "_": 0.40 * size * SC}[k]
            w, h = int(ft.getlength(ch) + size * SC), int(size * SC * 2)
            layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            ImageDraw.Draw(layer).text((size * SC * 0.2, size * SC * 0.4), draw_ch, font=ft, fill=col + (235,))
            layer = layer.rotate(self.rnd.uniform(-1.8, 1.8) * jitter, resample=Image.BICUBIC)
            self.img.alpha_composite(layer, (int(x - size * SC * 0.2),
                                             int(y + dy - size * SC * 0.4 + self.rnd.uniform(-1, 1) * SC * jitter)))
            x += ft.getlength(draw_ch) + 0.5 * SC
        return x / SC

    # ------------------------------------------------------------- strokes
    def _wob(self, pts, amp):
        """pts in scaled px; returns them nudged by up to amp logical px."""
        r = self.rnd
        return [(x + r.uniform(-amp, amp) * SC, y + r.uniform(-amp, amp) * SC) for x, y in pts]

    def line(self, p, q, ink="pencil", w=2.2, n=14, amp=1.0, over=0.0):
        (ax, ay), (bx, by) = [(a * SC, b * SC) for a, b in (p, q)]
        L = math.hypot(bx - ax, by - ay) or 1
        ux, uy = (bx - ax) / L, (by - ay) / L
        o = over * SC
        ax, ay, bx, by = ax - ux * o, ay - uy * o, bx + ux * o, by + uy * o
        pts = [(ax + (bx - ax) * i / n, ay + (by - ay) * i / n) for i in range(n + 1)]
        self.d.line(self._wob(pts, amp), fill=self.ink[ink] + (255,), width=int(w * SC), joint="curve")

    def box(self, x0, y0, x1, y1, ink="box"):
        for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
            self.line(a, b, ink, w=2.4, over=2)

    def arrow(self, p, q, ink="arrow"):
        self.line(p, q, ink, w=2.4, n=18, amp=0.7)
        ang = math.atan2(q[1] - p[1], q[0] - p[0])
        for s in (0.45, -0.45):
            self.line(q, (q[0] - 16 * math.cos(ang + s), q[1] - 16 * math.sin(ang + s)), ink, w=2.4, n=4, amp=0.3)

    def strike(self, x0, x1, y, ink="pencil"):
        self.line((x0 - 3, y + 2), (x1 + 3, y - 3), ink, w=2.4, over=2)

    # ------------------------------------------------------- stacked rows
    def _axis(self, y, size):
        size = size * self.k
        b = self.font(size).getbbox("0", anchor="la")
        return y * SC + (b[1] + b[3]) / 2, b[1], b[3]

    def item_w(self, it, size):
        if isinstance(it, str):
            return self.width(it, size)
        if it[0] == "frac":
            return max(self.width(it[1], size), self.width(it[2], size)) + 18
        if it[0] == "sqrt":
            return self.width(it[1], size) + 30
        return self.width(it[1], size)          # (ink_name, text)

    def row(self, x, y, items, size=36, ink="pencil"):
        """A line of text and stacked fractions. items: str | (ink_name, str) | ("frac", num, den)
        | ("sqrt", inner). Returns end x. Division is always a ("frac", ...) item."""
        for it in items:
            if isinstance(it, str):
                x = self.text(x, y, it, size, ink) + 6
            elif it[0] == "frac":
                w = self.item_w(it, size)
                axis, t0, b0 = self._axis(y, size)
                gap = 12 * SC
                nw, dw = self.width(it[1], size), self.width(it[2], size)
                self.text(x + (w - nw) / 2, (axis - gap - b0) / SC, it[1], size, ink)
                self.text(x + (w - dw) / 2, (axis + gap - t0) / SC, it[2], size, ink)
                self.line((x + 3, axis / SC), (x + w - 3, axis / SC), ink, w=2.4, n=10, amp=0.4)
                x += w + 6
            elif it[0] == "sqrt":                   # a hand-drawn radical: tick, long stroke, roof
                sz = size * self.k
                top, base = y - 0.08 * sz, y + 1.05 * sz
                self.line((x, y + 0.62 * sz), (x + 7, y + 0.52 * sz), ink, w=2.2, n=3, amp=0.3)
                self.line((x + 7, y + 0.52 * sz), (x + 14, base), ink, w=2.2, n=5, amp=0.3)
                self.line((x + 14, base), (x + 24, top), ink, w=2.2, n=8, amp=0.3)
                end = self.text(x + 28, y, it[1], size, ink)
                self.line((x + 24, top), (end + 4, top), ink, w=2.2, n=10, amp=0.3)
                x = end + 10
            else:
                x = self.text(x, y, it[1], size, it[0]) + 6
        return x

    def answer(self, x, y, s, size=36, ink="pencil"):
        """The final answer, boxed. Text starts clear of the preceding '=' so the box never touches it."""
        x0 = x + 12
        x1 = self.text(x0, y, s, size, ink)
        self.box(x0 - 8, y - 5, x1 + 8, y + size * self.k * 1.45)
        return x1

    # ----------------------------------------------------- pencil sketch
    def sketch(self):
        return PencilSketch(self)

    def crop(self, h):
        """Trim the canvas to h logical px tall (builders draw on a tall page, then crop)."""
        self.h = max(1, int(h))
        self.img = self.img.crop((0, 0, self.img.width, self.h * SC))
        self.d = ImageDraw.Draw(self.img)

    def save(self, png=None, pdf=None, out_scale=2):
        im = self.img.convert("RGB").resize((self.w * out_scale, self.h * out_scale), Image.LANCZOS)
        if png:
            im.save(png)
        if pdf:
            im.save(pdf, resolution=100.0 * out_scale / 2)


class PencilSketch:
    """Strokes with doubled passes, small overshoot and graphite grain; composed onto the page."""

    def __init__(self, page):
        self.p, self.layer = page, Image.new("RGBA", page.img.size, (0, 0, 0, 0))

    def stroke(self, pts, ink="pencil", w=1.8, alpha=130, passes=2, amp=1.0):
        r = self.p.rnd
        col = self.p.ink[ink]
        for _ in range(passes):
            jp = [(x * SC + r.uniform(-amp, amp) * SC, y * SC + r.uniform(-amp, amp) * SC) for x, y in pts]
            lw = int(w * SC * r.uniform(0.8, 1.2))
            pad = lw + 2                    # draw on a layer only as big as the stroke, then place it
            x0 = max(0, int(min(p[0] for p in jp)) - pad); y0 = max(0, int(min(p[1] for p in jp)) - pad)
            x1 = min(self.layer.width, int(max(p[0] for p in jp)) + pad); y1 = min(self.layer.height, int(max(p[1] for p in jp)) + pad)
            if x1 <= x0 or y1 <= y0:
                continue
            l = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
            ImageDraw.Draw(l).line([(px - x0, py - y0) for px, py in jp], fill=col + (alpha,), width=lw, joint="curve")
            self.layer.alpha_composite(l, (x0, y0))

    def seg(self, a, b, ink="pencil", **k):
        r = self.p.rnd
        L = math.hypot(b[0] - a[0], b[1] - a[1]) or 1
        ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
        o = r.uniform(2, 6)
        a2, b2 = (a[0] - ux * o, a[1] - uy * o), (b[0] + ux * o, b[1] + uy * o)
        n = max(4, int(L / 25))
        pts = [(a2[0] + (b2[0] - a2[0]) * i / n + r.uniform(-.6, .6), a2[1] + (b2[1] - a2[1]) * i / n + r.uniform(-.6, .6))
               for i in range(n + 1)]
        self.stroke(pts, ink, **k)

    def rect(self, x0, y0, x1, y1, ink="pencil", **k):
        for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
            self.seg(a, b, ink, **k)

    def circle(self, cx, cy, rad, ink="pencil", **k):
        r = self.p.rnd
        pts = [(cx + (rad + r.uniform(-.6, .6)) * math.cos(t / 40 * 2 * math.pi * 1.06 + 0.3),
                cy + (rad + r.uniform(-.6, .6)) * math.sin(t / 40 * 2 * math.pi * 1.06 + 0.3)) for t in range(41)]
        self.stroke(pts, ink, **k)

    def vector(self, a, b, ink="arrow"):
        self.seg(a, b, ink, w=2.4, alpha=190, passes=2, amp=0.6)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        for s in (0.45, -0.45):
            self.seg(b, (b[0] - 20 * math.cos(ang + s), b[1] - 20 * math.sin(ang + s)), ink,
                     w=2.4, alpha=190, passes=1, amp=0.3)

    def dashed(self, a, b, ink="pencil", n=14):
        for i in range(0, n, 2):
            p = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
            q = (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n)
            self.stroke([p, q], ink, w=1.4, alpha=100, passes=1, amp=0.4)

    def commit(self):
        """Apply graphite grain and composite onto the page. Grain thins strokes; it never erases them."""
        import numpy as np
        a = np.array(self.layer)
        rng = np.random.default_rng(3)
        noise = rng.uniform(0.35, 1.0, a.shape[:2]).astype(np.float32)
        noise = np.array(Image.fromarray((noise * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.35 * SC)),
                         dtype=np.float32) / 255
        a[..., 3] = (a[..., 3] * np.clip(noise * 1.25, 0.45, 1)).astype(np.uint8)
        self.p.img.alpha_composite(Image.fromarray(a))
