#!/usr/bin/env python3
"""Render a page image of every document template for the app's Template gallery.

The gallery shows what a template actually prints, not a drawing of what it is
supposed to print. Every image here is rasterised from the real builder's real
output, so a template that has drifted shows its drift.

    python3 scripts/build_template_previews.py            # all families
    python3 scripts/build_template_previews.py worksheet  # one family
    python3 scripts/build_template_previews.py --check    # report, build nothing

Writes app/public/previews/<id>-<n>.png and app/public/previews/catalog.json.
Both are build artifacts. Never hand-edit one; re-run the script.

Requires the repository build toolchain: python-docx, weasyprint, pptxgenjs,
LibreOffice (SHULL_SOFFICE or soffice on PATH) and poppler's pdftoppm. A family
whose tools are missing is reported as unavailable and skipped — the gallery
degrades to a description card rather than failing.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "app", "public", "previews")

# Width in px of a rendered page image. A page is read at roughly a third of
# this in the gallery grid and full size in the lightbox, so this is the
# lightbox size, not the card size.
WIDTH = 900

# The five document families, in the order the gallery shows them. `app` marks
# the ones the SHULL OS build button can produce today: only the worksheet
# builder is wired into app/server.mjs. The rest build from the repository.
FAMILIES = [
    {
        "id": "worksheet",
        "name": "Worksheet / practice set",
        "course": "all",
        "app": True,
        "blurb": "One builder, one spec, three course profiles. Chemistry gets a work box per "
                 "math question; Physics refuses them; Geology refuses the equation bar. The "
                 "profile is enforced at build time, not by remembering.",
        "detail": "templates/worksheet/README.md",
        "pages": 2,
    },
    {
        "id": "notes",
        "name": "Guided / Cornell notes",
        "course": "all",
        "app": False,
        "blurb": "Strictly recall: the page a student fills in while the slide is up. The cue "
                 "column names the thing to record - a definition, a table, a sequence - and "
                 "never asks a question. Worked examples carry a bordered work area.",
        "detail": "templates/notes/README.md",
        "pages": 2,
    },
    {
        "id": "lab",
        "name": "Lab handout",
        "course": "all",
        "app": False,
        "blurb": "The locked lab structure with the content lifted out. Builds a student handout "
                 "and a separate teacher prep-and-key file, page-budget checked so a four-page "
                 "lab does not quietly become five.",
        "detail": "templates/lab/README.md",
        "pages": 2,
    },
    {
        "id": "practice",
        "name": "Activity / editable prototype",
        "course": "all",
        "app": False,
        "blurb": "Editable course-specific prototypes with a matching key file. Still prototypes "
                 "until the rendered layouts are accepted — treat what you see here as a proposal.",
        "detail": "templates/practice/build_practice.py",
        "pages": 1,
    },
    {
        "id": "slide",
        "name": "Section slide deck",
        "course": "all",
        "app": False,
        "blurb": "Twelve layouts, one file, three courses. Geometry and type scale preserved from "
                 "the approved deck; a 16pt floor on anything read from a seat.",
        "detail": "templates/slide/README.md",
        "pages": 4,
    },
]


def soffice():
    return os.environ.get("SHULL_SOFFICE") or shutil.which("soffice") or shutil.which("libreoffice")


def python_exe():
    return os.environ.get("SHULL_PYTHON") or sys.executable


def run(args, cwd=REPO, timeout=300, env=None):
    merged = dict(os.environ, PYTHONUTF8="1")
    if env:
        merged.update(env)
    return subprocess.run(args, cwd=cwd, timeout=timeout, env=merged,
                          capture_output=True, text=True, check=True)


def to_pdf(src, workdir):
    """Convert a docx/pptx to PDF with LibreOffice and return the PDF path."""
    exe = soffice()
    if not exe:
        raise RuntimeError("LibreOffice not found. Set SHULL_SOFFICE or install soffice.")
    profile = "file:///" + os.path.join(workdir, "lo").replace(os.sep, "/").lstrip("/")
    run([exe, "--headless", f"-env:UserInstallation={profile}",
         "--convert-to", "pdf", "--outdir", workdir, src], cwd=workdir, timeout=600)
    pdf = os.path.join(workdir, os.path.splitext(os.path.basename(src))[0] + ".pdf")
    if not os.path.exists(pdf):
        raise RuntimeError(f"LibreOffice produced no PDF for {os.path.basename(src)}")
    return pdf


def page_total(pdf):
    """Total pages in the source document, so the gallery can say 4 of 12."""
    if not shutil.which("pdfinfo"):
        return None
    try:
        out = run(["pdfinfo", pdf]).stdout
        return int(next(l.split(":")[1] for l in out.splitlines() if l.startswith("Pages:")))
    except Exception:
        return None


def rasterise(pdf, out_id, pages):
    """Write up to `pages` page images and return their filenames, in page order.

    A document shorter than its family's page budget is normal, not an error —
    a one-page activity stops after page one rather than failing the family.
    """
    if not shutil.which("pdftoppm"):
        raise RuntimeError("pdftoppm not found. Install poppler-utils.")
    written = []
    for n in range(1, pages + 1):
        stem = os.path.join(OUT, f"{out_id}-{n}")
        try:
            run(["pdftoppm", "-png", "-r", "110", "-f", str(n), "-l", str(n),
                 "-scale-to-x", str(WIDTH), "-scale-to-y", "-1", "-singlefile", pdf, stem])
        except subprocess.CalledProcessError:
            break
        name = f"{out_id}-{n}.png"
        if not os.path.exists(os.path.join(OUT, name)):
            break
        shrink(os.path.join(OUT, name))
        written.append(name)
    if not written:
        raise RuntimeError(f"pdftoppm produced no image for {out_id}")
    return written


def shrink(path):
    """Quantise a page image to a 128-colour palette.

    These are documents: mostly one ground colour, one ink and a course accent.
    A palette PNG carries them at about a third of the size with no visible
    loss, and the whole gallery is committed to the repository.
    """
    try:
        from PIL import Image
    except ImportError:
        return
    with Image.open(path) as im:
        im.convert("RGB").quantize(colors=128, method=Image.MEDIANCUT,
                                   dither=Image.FLOYDSTEINBERG).save(path, optimize=True)


def build_worksheet(workdir):
    """Every worksheet spec gets its own preview — the gallery picks between them."""
    specs = sorted(f for f in os.listdir(os.path.join(REPO, "templates/worksheet/specs"))
                   if f.endswith(".json"))
    items = []
    for spec in specs:
        spec_path = os.path.join(REPO, "templates/worksheet/specs", spec)
        docx = os.path.join(workdir, os.path.splitext(spec)[0] + ".docx")
        run([python_exe(), os.path.join(REPO, "templates/worksheet/build_worksheet_docx.py"),
             spec_path, docx])
        data = json.load(open(spec_path, encoding="utf-8"))
        items.append({
            "id": "worksheet-" + os.path.splitext(spec)[0],
            "title": ", ".join(s["title"] for s in data.get("sectionsContent", [])),
            "course": data.get("course", "all"),
            "spec": spec,
            "source": "templates/worksheet/specs/" + spec,
            "pdf": to_pdf(docx, workdir),
        })
    return items


def build_notes(workdir):
    specs = sorted(f for f in os.listdir(os.path.join(REPO, "templates/notes/specs"))
                   if f.endswith(".json"))
    items = []
    for spec in specs:
        spec_path = os.path.join(REPO, "templates/notes/specs", spec)
        docx = os.path.join(workdir, "notes_" + os.path.splitext(spec)[0] + ".docx")
        run([python_exe(), os.path.join(REPO, "templates/notes/build_notes_docx.py"),
             spec_path, docx])
        data = json.load(open(spec_path, encoding="utf-8"))
        sections = [s.get("title", "") for s in data.get("sectionsContent", [])]
        label = f"Unit {data.get('unit', '?')} — {sections[0]}" if sections else os.path.splitext(spec)[0]
        if len(sections) > 1:
            label += f" +{len(sections) - 1} more"
        items.append({
            "id": "notes-" + os.path.splitext(spec)[0],
            "title": label,
            "course": data.get("course", "all"),
            "spec": spec,
            "source": "templates/notes/specs/" + spec,
            "pdf": to_pdf(docx, workdir),
        })
    return items


def build_lab(workdir):
    """The lab master ships a built PDF; use it rather than re-rendering."""
    items = []
    for name, label in [("SHULL_Lab_TEMPLATE_MASTER", "Student handout"),
                        ("SHULL_Lab_TEMPLATE_TEACHER_KEY", "Teacher prep and key")]:
        pdf = os.path.join(REPO, "templates/lab", name + ".pdf")
        if not os.path.exists(pdf):
            html = os.path.join(REPO, "templates/lab", name + ".html")
            run([python_exe(), os.path.join(REPO, "templates/lab/build_lab.py"), html])
        items.append({
            "id": "lab-" + ("master" if "MASTER" in name else "key"),
            "title": label,
            "course": "all",
            "source": "templates/lab/" + name + ".html",
            "pdf": pdf,
        })
    return items


def build_practice(workdir):
    items = []
    for course in ("chemistry", "physics", "geology"):
        spec = os.path.join(REPO, "templates/practice/specs", course + ".json")
        if not os.path.exists(spec):
            continue
        out = os.path.join(workdir, "practice_" + course)
        os.makedirs(out, exist_ok=True)
        run([python_exe(), os.path.join(REPO, "templates/practice/build_practice.py"),
             spec, "--out", out])
        # The builder names its own files; take the student copy, not the key.
        produced = sorted(f for f in os.listdir(out)
                          if f.endswith(".docx") and not f.endswith("_Key.docx"))
        if not produced:
            continue
        items.append({
            "id": "practice-" + course,
            "title": course.capitalize() + " activity prototype",
            "course": course,
            "source": "templates/practice/specs/" + course + ".json",
            "pdf": to_pdf(os.path.join(out, produced[0]), out),
        })
    return items


def build_slide(workdir):
    slide_dir = os.path.join(REPO, "templates/slide")
    if not os.path.isdir(os.path.join(slide_dir, "node_modules")):
        raise RuntimeError("templates/slide/node_modules missing. Run scripts/setup-environment.sh.")
    items = []
    for course in ("chemistry", "physics", "geology"):
        pptx = os.path.join(workdir, "deck_" + course + ".pptx")
        run(["node", os.path.join(slide_dir, "build.js"), pptx],
            cwd=slide_dir, env={"SHULL_COURSE": course})
        items.append({
            "id": "slide-" + course,
            "title": course.capitalize() + " deck — twelve layouts",
            "course": course,
            "source": "templates/slide/build.js",
            "pdf": to_pdf(pptx, workdir),
        })
    return items


BUILDERS = {"worksheet": build_worksheet, "notes": build_notes, "lab": build_lab,
            "practice": build_practice, "slide": build_slide}


def main(argv):
    check = "--check" in argv
    wanted = [a for a in argv if not a.startswith("-")] or [f["id"] for f in FAMILIES]
    unknown = [w for w in wanted if w not in BUILDERS]
    if unknown:
        print("unknown family: " + ", ".join(unknown))
        print("known: " + ", ".join(BUILDERS))
        return 2

    os.makedirs(OUT, exist_ok=True)
    catalog_path = os.path.join(OUT, "catalog.json")
    previous = {}
    if os.path.exists(catalog_path):
        previous = {f["id"]: f for f in json.load(open(catalog_path, encoding="utf-8"))["families"]}

    families, failures = [], []
    for family in FAMILIES:
        entry = dict(family)
        if family["id"] not in wanted:
            # Keep what an earlier run produced instead of dropping it from the catalog.
            families.append(previous.get(family["id"], dict(entry, items=[], status="not built")))
            continue
        if check:
            families.append(dict(entry, items=previous.get(family["id"], {}).get("items", []),
                                 status="checked"))
            continue
        print(f"— {family['id']}")
        try:
            with tempfile.TemporaryDirectory() as workdir:
                items = []
                for item in BUILDERS[family["id"]](workdir):
                    pdf = item.pop("pdf")
                    images = rasterise(pdf, item["id"], family["pages"])
                    items.append(dict(item, images=images, total=page_total(pdf)))
                    print(f"  {item['id']}: {len(images)} page image(s)")
            entry["items"] = items
            entry["status"] = "built"
        except Exception as e:  # a missing tool must not fail the other four
            message = getattr(e, "stderr", "") or str(e)
            entry["items"] = []
            entry["status"] = "unavailable"
            entry["error"] = message.strip().splitlines()[-1][:300] if message.strip() else str(e)
            failures.append(f"{family['id']}: {entry['error']}")
            print(f"  unavailable — {entry['error']}")
        families.append(entry)

    if not check:
        with open(catalog_path, "w", encoding="utf-8") as fh:
            json.dump({"generated": "build_template_previews.py", "width": WIDTH,
                       "families": families}, fh, indent=2)
            fh.write("\n")

    built = sum(len(f.get("items", [])) for f in families)
    print(f"\nbuild_template_previews: {built} preview(s) across {len(families)} family/families")
    if failures:
        print(f"{len(failures)} family/families unavailable:")
        for f in failures:
            print("  -", f)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
