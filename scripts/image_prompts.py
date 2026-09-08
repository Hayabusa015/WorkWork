#!/usr/bin/env python3
"""List every unfilled image slot in a deck spec, with a prompt for each.

SHULL_Slide_System_v2 section 5 defines the image loop: Claude supplies a prompt per
slide, Matt generates and saves it, Claude places it. Step one had no mechanism - the
T-7 audit found a deck with ten empty image wells and no way to get from the JSON to a
finished deck. This is step one.

**It does not invent subject matter.** The deck spec declares what each image is OF,
under `imageSubjects`. A slot with no declared subject gets no prompt - it gets a line
saying the author has to say what the picture is. A script guessing "a photograph that
evokes isotopes" from a headline is how a deck ends up with seven interchangeable
stock-looking images, which is the definition of slop in the standard.

    python3 scripts/image_prompts.py templates/slide/decks/<spec>.json
"""
import json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "templates", "slide"))

# Slots whose content is a hand-built figure, never a photograph. Anything a student
# reads as science - a number, a label, a formula - is built. A generated Bohr diagram
# has the wrong electron count in a way nobody catches at a glance.
BUILT_ONLY = {"diagram"}

STYLE = (
    "Photorealistic, dramatic studio photography. Matte near-black background. Warm key "
    "light from the upper left, deep shadow on the right. Shallow depth of field, soft "
    "falloff into black at the edges. No text, no labels, no numbers, no watermarks, no "
    "people. Wide 16:9 landscape, subject centred with generous negative space. Clean, "
    "editorial, museum-catalog quality."
)


def main():
    spec = json.load(open(sys.argv[1]))
    course, unit, section = spec["course"], spec["unit"], spec["section"]
    slots = __import__("subprocess").run(
        ["node", "-e",
         f'process.env.SHULL_COURSE="{course}";'
         'const b=require("./build");console.log(JSON.stringify(b.SLOTS));'],
        cwd=os.path.join(REPO, "templates", "slide"),
        capture_output=True, text=True)
    if slots.returncode:
        print(slots.stderr, file=sys.stderr); return 1
    SLOTS = json.loads(slots.stdout)

    rows, built, undeclared = [], [], []
    for i, sl in enumerate(spec["slides"], 1):
        declared = SLOTS.get(sl["master"], {})
        filled = set((sl.get("images") or {}).keys())
        for name in declared:
            if name in ("eyebrow", "code", "headline", "subhead", "number", "keyq",
                        "problem", "work", "answer", "mustwrite") or re.search(r"_[lb]$", name):
                continue
            if name in filled:
                continue
            f = sl.get("fields", {})
            subject = f.get("headline", "").replace("\n", " ")
            frame = f.get("subhead", "").replace("\n", " ")
            declared_subject = (sl.get("imageSubjects") or {}).get(name)
            if name in BUILT_ONLY:
                built.append((i, sl["master"], name, subject))
                continue
            if not declared_subject:
                undeclared.append((i, sl["master"], name, subject))
                continue
            # Named for what it is a picture of, per NAMING.md section 3 - never for the
            # slot, or two slides both want chem_u01_s1.4_concept.png.
            slug = re.sub(r"[^a-z0-9]+", "_", declared_subject.lower()).strip("_")[:34]
            fname = f"{course[:4]}_u{int(unit):02d}_s{section}_{slug}.png"
            rows.append((i, sl["master"], name, fname, declared_subject, frame))

    print(f"Image slots still empty — {course.upper()} U{int(unit):02d} S{section}\n")
    if built:
        print("HAND-BUILT, never generated:")
        for i, m, name, subject in built:
            print(f"  slide {i:>2}  {name:<10} {subject}")
            print(f"            Build it. Anything with a number or a label is built.\n")
    if undeclared:
        print("NO SUBJECT DECLARED — no prompt can be written for these:\n")
        for i, m, name, headline in undeclared:
            print(f"  slide {i:>2}  {m}  [{name}]   headline: {headline!r}")
        print('\n  Add an "imageSubjects" entry to each of these slides in the spec, saying what')
        print("  the picture is OF. A prompt guessed from a headline produces an image that could")
        print("  belong to any slide in any deck, which is the thing the standard calls slop.\n")
    if rows:
        print("GENERATE these, save under the given filename, and hand them back:\n")
        for i, m, name, fname, subject, frame in rows:
            print(f"  slide {i:>2}  {m}  [{name}]")
            print(f"    file:   _Brand/Image Library/{course.title()}/{fname}")
            print(f"    prompt: {subject}. {STYLE}\n")
    total = len(rows) + len(undeclared)
    if total:
        print(f"{total} image slot(s) outstanding. The deck is not classroom-ready until they are "
              f"placed.")
    else:
        print("No photographic slots outstanding.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
