#!/usr/bin/env python3
"""Render every worksheet template spec to a preview PNG for the app's template picker.

The app let you choose a template from a dropdown of titles, which tells you nothing
about what the page actually looks like. These are real renders of the real templates -
built through the same build_worksheet_docx.py -> LibreOffice -> pdftoppm path a real
document takes, so the thumbnail cannot drift from what the builder actually produces.

    python3 scripts/build_template_previews.py [outdir]

Writes <outdir>/<spec-id>.png (page 1, ~150dpi, trimmed to the page) plus a
manifest.json carrying page count and the spec's own metadata for the card.
"""
import json, os, subprocess, sys, shutil, tempfile, glob
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(REPO, "templates", "worksheet", "specs")
BUILD = os.path.join(REPO, "templates", "worksheet", "build_worksheet_docx.py")
CARD_W = 850          # wide enough to read at 2x on a card, light enough to commit
PY = os.environ.get("SHULL_PYTHON", sys.executable)
SOFFICE = os.environ.get("SHULL_SOFFICE", shutil.which("soffice"))


def render(spec_path, outdir, tmp):
    spec_id = os.path.basename(spec_path)
    stem = spec_id[:-5] if spec_id.endswith(".json") else spec_id
    docx = os.path.join(tmp, stem + ".docx")
    subprocess.run([PY, BUILD, spec_path, docx], cwd=REPO, check=True,
                   capture_output=True, timeout=180)
    subprocess.run([SOFFICE, "--headless",
                    f"-env:UserInstallation=file://{tmp}/lo",
                    "--convert-to", "pdf", "--outdir", tmp, docx],
                   check=True, capture_output=True, timeout=180)
    pdf = os.path.join(tmp, stem + ".pdf")
    # -r 150 is legible as a card thumbnail and still small enough to ship in-repo.
    subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1",
                    pdf, os.path.join(outdir, stem)], check=True, timeout=120)
    # pdftoppm suffixes the page number; normalise to <stem>.png.
    final = os.path.join(outdir, stem + ".png")
    for produced in glob.glob(os.path.join(outdir, stem + "-*.png")):
        os.replace(produced, final)
    # A 150dpi letter page is 1275px wide and ~200KB - more than a card thumbnail
    # needs, and it ships in the repo. Downscale to CARD_W and quantise: a worksheet
    # is white paper, black ink and one accent, so a 64-colour palette is lossless to
    # the eye and roughly a fifth of the bytes.
    im = Image.open(final).convert("RGB")
    im = im.resize((CARD_W, round(im.height * CARD_W / im.width)), Image.LANCZOS)
    im.quantize(colors=64, method=Image.MEDIANCUT).save(final, optimize=True)
    pages = int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True,
                               check=True).stdout.split("Pages:")[1].split()[0])
    return stem, pages


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "app", "public", "previews")
    os.makedirs(outdir, exist_ok=True)
    if not SOFFICE:
        print("build_template_previews: no soffice on PATH; set SHULL_SOFFICE", file=sys.stderr)
        return 1
    manifest = {}
    with tempfile.TemporaryDirectory() as tmp:
        for spec_path in sorted(glob.glob(os.path.join(SPECS, "*.json"))):
            spec = json.load(open(spec_path))
            spec_id = os.path.basename(spec_path)
            try:
                stem, pages = render(spec_path, outdir, tmp)
            except subprocess.CalledProcessError as e:
                print(f"  {spec_id}: FAILED — {e.stderr.decode()[:300]}", file=sys.stderr)
                continue
            sections = spec.get("sectionsContent", [])
            manifest[spec_id] = {
                "image": f"/previews/{stem}.png",
                "pages": pages,
                "course": spec.get("course"),
                "unit": spec.get("unit"),
                "sections": spec.get("sections", []),
                "docType": spec.get("docType", "Practice_Set"),
                "timeTargetMin": spec.get("timeTargetMin"),
                "questions": sum(len(s.get("questions", [])) for s in sections),
                "blocks": sorted({b["kind"] for s in sections for b in s.get("blocks", [])}),
                "hasEquations": bool(spec.get("equations") or
                                     any(s.get("equations") for s in sections)),
            }
            print(f"  {spec_id}: {pages} page(s) -> {manifest[spec_id]['image']}")
    json.dump(manifest, open(os.path.join(outdir, "manifest.json"), "w"), indent=2)
    print(f"build_template_previews: {len(manifest)} preview(s) in {outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
