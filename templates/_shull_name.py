"""The SHULL filename grammar, in one place for the Python builders.

Rule: standards/NAMING.md §2 (SHULL-CHG-0024, short topics SHULL-CHG-0041). The JS builders and the app use
templates/shull_name.cjs, which implements the same grammar; both are pinned to
the same examples by their tests.

    1.2 Practice Set - Balancing.docx                  one section, short title
    1.2 Quiz A Key - Balancing.docx                    version letter, key
    Unit 1 Guided Notes - 1D Motion.docx               more than one section
    Reference - Polyatomic Ions.pdf                    course-level, whole year (SHULL-CHG-0059)
"""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_BAD = re.compile(r'[\\/:*?"<>|]')


def clean(text):
    """A topic goes in a filename: drop characters Windows and Drive sync refuse."""
    return re.sub(r"\s{2,}", " ", _BAD.sub("", str(text))).strip(" .")


MAX_TOPIC = 20


def short_title(course, key):
    """The short title for a section ("1.3") or a unit ("U1"), read from the Short titles
    table in courses/<course>/DECISIONS.md (SHULL-CHG-0041). None if there is no row: a name
    without a topic is correct, an invented or auto-shortened topic is not."""
    path = os.path.join(REPO, "courses", course, "DECISIONS.md")
    try:
        text = open(path).read()
    except OSError:
        return None
    m = re.search(r"^## Short titles\s*$(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        return None
    key = str(key).strip()
    key = "U" + key[1:].lstrip("0") if key[:1].upper() == "U" else key
    for row in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", m.group(1), re.M):
        k = row.group(1)
        k = "U" + k[1:].lstrip("0") if k[:1].upper() == "U" else k
        if k == key:
            return clean(row.group(2)) or None
    return None


def reference_titles(course):
    """The course-level topics: every row coded REF in the Short titles table of
    courses/<course>/DECISIONS.md (SHULL-CHG-0059). Empty if there are none."""
    path = os.path.join(REPO, "courses", course, "DECISIONS.md")
    try:
        text = open(path).read()
    except OSError:
        return []
    m = re.search(r"^## Short titles\s*$(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        return []
    rows = re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", m.group(1), re.M)
    return [t for t in (clean(r.group(2)) for r in rows if r.group(1).strip().upper() == "REF") if t]


def document_name(type_, sections, unit, topic=None, unit_title=None,
                  version=None, key=False, ext="docx", descriptor=None, scope=None):
    """`type_` may use underscores ("Practice_Set"); the name uses spaces.
    scope="course" is a whole-year document: Reference only, no code and no course word, because
    the folder ([Course]/Reference/) carries the course (SHULL-CHG-0059, SHULL-CHG-0024)."""
    if scope == "course":
        if str(type_) != "Reference":
            raise ValueError(f"course-level names are for Reference only, not {type_!r}")
        if version or key:
            raise ValueError("a course-level Reference takes no version or key")
        tail = clean(topic) if topic else ""
        if not tail:
            raise ValueError("a course-level name always has a topic: a REF row in the course "
                             "Short titles table")
        if len(tail) > MAX_TOPIC:
            raise ValueError(f"topic {tail!r} is {len(tail)} characters; the limit is {MAX_TOPIC}. "
                             "Use the short title from the course decisions file.")
        return f"Reference - {tail}.pdf"
    label = str(type_).replace("_", " ")
    if version:
        label += f" {version}"
    if key:
        label += " Key"
    sections = [str(s) for s in sections]
    if len(sections) == 1:
        head, tail = sections[0], topic
    else:
        head, tail = f"Unit {int(unit)}", unit_title
    name = f"{head} {label}"
    if tail:
        tail = clean(tail)
        if len(tail) > MAX_TOPIC:
            raise ValueError(f"topic {tail!r} is {len(tail)} characters; the limit is {MAX_TOPIC}. "
                             "Use the short title from the course decisions file.")
        name += f" - {tail}"
    if descriptor:
        # A word that tells two files apart (Longhand, Day 2, Version 1). Not limited, and a word
        # the short title already has is dropped.
        have = {w.lower() for w in (tail or "").split()}
        extra = " ".join(w for w in clean(descriptor).split() if w.lower() not in have)
        if extra:
            name += f" {extra}" if tail else f" - {extra}"
    return f"{name}.{ext}"
