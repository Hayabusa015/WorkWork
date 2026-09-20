#!/usr/bin/env python3
"""Generate the Windows app icon from the SHULL OS badge artwork.

    python3 scripts/build_app_icon.py
    python3 scripts/build_app_icon.py --check    # fail if it has drifted

Reads build/icon-source.png and writes build/icon.ico, which electron-builder
picks up automatically (build/ is its default buildResources directory). The
.ico carries every size Windows asks for: the taskbar and the desktop shortcut
use 32 and 48, the installer header uses 256, and Explorer's detail view drops
to 16.

The badge is round and the artwork is square on black. Pasted straight in, the
corners stay black and the icon shows as a black tile on a taskbar. So the
circle is measured, cropped, and given an antialiased alpha mask - the mask is
built at 4x and downsampled, because a mask drawn at 16px has visible stair
steps on the rim.
"""
import os
import sys

from PIL import Image, ImageDraw

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "build", "icon-source.png")
OUT = os.path.join(REPO, "build", "icon.ico")
# The same badge, web-sized, for the app's own rail. Served by app/server.mjs.
MARK = os.path.join(REPO, "app", "public", "badge.png")
MARK_PX = 128

# Windows picks the nearest size rather than scaling, so ship the ones it asks
# for instead of one large image.
SIZES = [16, 24, 32, 48, 64, 128, 256]

# Antialiasing factor for the circular mask.
SUPERSAMPLE = 4

# Anything summing above this across RGB counts as artwork rather than the
# black ground. Low enough to catch the dark inner fill of the badge.
INK = 28


def circle_of(image):
    """Centre and radius of the round badge inside a square of black."""
    grey = image.convert("L").point(lambda v: 255 if v * 3 > INK else 0)
    box = grey.getbbox()
    if not box:
        raise SystemExit(f"build_app_icon: {SRC} looks entirely black")
    left, top, right, bottom = box
    cx, cy = (left + right) / 2, (top + bottom) / 2
    # The drop shadow makes the lit area slightly taller or wider than the disc
    # itself; the larger half-span is the one that holds the whole badge.
    radius = max(right - left, bottom - top) / 2
    return cx, cy, radius


def render():
    with Image.open(SRC) as art:
        art = art.convert("RGB")
        cx, cy, radius = circle_of(art)
        # A hair of margin so the rim is not clipped by rounding.
        radius += 2
        square = art.crop((round(cx - radius), round(cy - radius),
                           round(cx + radius), round(cy + radius)))

    side = square.width
    mask = Image.new("L", (side * SUPERSAMPLE, side * SUPERSAMPLE), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, side * SUPERSAMPLE - 1, side * SUPERSAMPLE - 1), fill=255)
    mask = mask.resize((side, side), Image.LANCZOS)

    badge = square.convert("RGBA")
    badge.putalpha(mask)

    frames = [badge.resize((n, n), Image.LANCZOS) for n in SIZES]
    return frames


def main(argv):
    if not os.path.exists(SRC):
        print(f"build_app_icon: {os.path.relpath(SRC, REPO)} is missing")
        return 1
    frames = render()

    if "--check" in argv:
        if not os.path.exists(OUT):
            print("build_app_icon: build/icon.ico missing — run scripts/build_app_icon.py")
            return 1
        with Image.open(OUT) as current:
            have = sorted(current.info.get("sizes", []))
        if have != sorted((n, n) for n in SIZES):
            print(f"build_app_icon: build/icon.ico holds {have}, expected {SIZES} — re-run the script")
            return 1
        if not os.path.exists(MARK):
            print("build_app_icon: app/public/badge.png missing — run scripts/build_app_icon.py")
            return 1
        print("build_app_icon: OK — every expected size is present")
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    frames[-1].save(OUT, format="ICO", sizes=[(n, n) for n in SIZES])
    print(f"wrote {os.path.relpath(OUT, REPO)} — {', '.join(str(n) for n in SIZES)}px")

    os.makedirs(os.path.dirname(MARK), exist_ok=True)
    frames[-1].resize((MARK_PX, MARK_PX), Image.LANCZOS).save(MARK, optimize=True)
    print(f"wrote {os.path.relpath(MARK, REPO)} — {MARK_PX}px")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
