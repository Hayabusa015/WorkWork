"""The SHULL filename grammar, in one place for the Python builders.

Rule: standards/NAMING.md §2 (SHULL-CHG-0024). The JS builders and the app use
templates/shull_name.cjs, which implements the same grammar; both are pinned to
the same examples by their tests.

    1.2 Practice Set - Balancing Equations.docx        one section
    1.2 Quiz A Key - Balancing Equations.docx          version letter, key
    Unit 1 Guided Notes - Motion in One Dimension.docx more than one section
"""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_BAD = re.compile(r'[\\/:*?"<>|]')


def clean(text):
    """A topic goes in a filename: drop characters Windows and Drive sync refuse."""
    return re.sub(r"\s{2,}", " ", _BAD.sub("", str(text))).strip(" .")


def section_title(course, code):
    """A section's topic, read from the course's DECISIONS.md. None if not found —
    a name without a topic is correct; an invented topic is not."""
    path = os.path.join(REPO, "courses", course, "DECISIONS.md")
    try:
        text = open(path).read()
    except OSError:
        return None
    end = text.find("## Course sequencing rules")
    text = text[:end] if end > 0 else text
    pat = re.compile(r"(?:^|[·|])\s*`?%s`?\s+([^·|\n]+)" % re.escape(str(code)), re.M)
    m = pat.search(text)
    if not m:
        return None
    return clean(m.group(1).replace("`EXT`", "")) or None


def document_name(type_, sections, unit, topic=None, unit_title=None,
                  version=None, key=False, ext="docx"):
    """`type_` may use underscores ("Practice_Set"); the name uses spaces."""
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
        name += f" - {clean(tail)}"
    return f"{name}.{ext}"
