"""Shared helpers for the SHULL OS validators."""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Never scanned. legacy/ is a verbatim snapshot; docs/ and governance/ are analysis and
# change records that legitimately quote superseded values; palette-archive exists to
# hold retired hexes.
EXCLUDED_DIRS = {
    ".git", "node_modules", "legacy", "docs", "reports",
    os.path.join("brand", "palette-archive"),
    os.path.join("governance", "proposals"),
    os.path.join("standards", "superseded"),
}

TEXT_EXT = {".md", ".html", ".css", ".js", ".py", ".json", ".txt", ".yml", ".yaml"}


def walk(subdirs=None):
    """Yield repo-relative paths of scannable text files."""
    roots = [os.path.join(REPO, d) for d in subdirs] if subdirs else [REPO]
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            rel_dir = os.path.relpath(dirpath, REPO)
            if any(rel_dir == e or rel_dir.startswith(e + os.sep) for e in EXCLUDED_DIRS):
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".git")]
            for fn in filenames:
                if os.path.splitext(fn)[1].lower() in TEXT_EXT:
                    yield os.path.relpath(os.path.join(dirpath, fn), REPO)


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


COURSE_BY_CODE = {"CHEM": "chemistry", "PHYS": "physics", "GEO": "geology"}


def section_codes(course):
    """Every U#/S#.# section code declared in a course's DECISIONS.md.

    Handles both formats in use: backticked codes (Physics, Geology) and the
    plain 'N.N Title' run-on lists adopted verbatim from Drive (Chemistry).
    Only the curriculum-map region is parsed, so margins, molarities and
    percentages elsewhere in the file are not mistaken for section codes.
    """
    path = os.path.join("courses", course, "DECISIONS.md")
    if not os.path.exists(os.path.join(REPO, path)):
        return None
    text = read(path)
    m = re.search(r"^##\s+Curriculum map.*?$(.*?)(?=^##\s+(?!#))", text, re.S | re.M)
    region = m.group(1) if m else text
    codes = set(re.findall(r"`(\d{1,2}\.\d)`", region))
    # Plain form: a code at a line start or after a separator, followed by a title word.
    codes |= set(re.findall(r"(?:^|[·|]\s*)(\d{1,2}\.\d)\s+(?=[A-Z(])", region, re.M))
    return codes


def report(name, errors, checked):
    print(f"{name}: {checked} file(s) checked")
    if errors:
        print(f"\nFAIL — {len(errors)} problem(s)")
        for e in errors:
            print("  -", e)
        return 1
    print("OK")
    return 0
