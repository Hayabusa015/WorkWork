#!/usr/bin/env python3
"""Recompress a .pptx. pptxgenjs writes its zip almost uncompressed.

Found during T-7: a 13-slide deck was 591,361 bytes holding 576 KB of content, i.e.
stored, not deflated. Office XML compresses about 5:1. The rendering is unaffected -
this only changes how the parts are stored in the container.

    python3 scripts/repack_pptx.py deck.pptx

Rewrites in place. Verify afterwards with audit_slide_geometry.py and pdffonts; the
T-7 run also compared the PDF text page by page and it was identical.
"""
import os, shutil, sys, tempfile, zipfile

def main():
    src = sys.argv[1]
    before = os.path.getsize(src)
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(src) as z:
            names = z.namelist()
            z.extractall(tmp)
        out = src + ".repack"
        # [Content_Types].xml must come first for a valid OPC package.
        names.sort(key=lambda n: (n != "[Content_Types].xml", n))
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for n in names:
                p = os.path.join(tmp, n)
                if os.path.isfile(p):
                    z.write(p, n)
        shutil.move(out, src)
    after = os.path.getsize(src)
    print(f"repacked {os.path.basename(src)}: {before:,} -> {after:,} bytes "
          f"({before / after:.1f}x smaller)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
