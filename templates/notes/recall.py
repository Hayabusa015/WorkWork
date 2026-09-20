"""Guided notes are strictly recall. The build refuses a question.

    "I dont want questions about the slides in the guided notes. I wanted
     guided notes just for them to write what is on the slide. Its strictly
     recall. Record the definition, record the table, record the steps,
     record the concept etc."
                                                    — Matthew Shull, 2026-09-20

This had been stated before and came back, because it was written down nowhere
and the opposite was written down everywhere: the template README, both example
specs and the student-facing "how these notes work" box all described the cue
column as questions to quiz yourself with. A rule that only lives in a document
is not a mechanism. This is the mechanism.

The packet is the page a student fills in while the slide is up. The cue column
names the thing to record - a definition, a table, a sequence, a concept - and
the notes side is where it gets written. Asking a question there changes the
task from recording to answering, which is what a practice set is for.

Both renderers import this. One rule, one place.
"""
import re

# A question mark anywhere, or an opener that makes one. "Whole-number ratios"
# is a recall prompt and "Who discovered it?" is not, so the openers match on a
# word boundary rather than a prefix.
QUESTION_MARK = re.compile(r"\?")
OPENERS = (
    "what", "why", "how", "when", "where", "which", "who", "whom", "whose",
    "is", "are", "was", "were", "do", "does", "did", "can", "could",
    "should", "would", "will", "has", "have", "had",
)
OPENER = re.compile(r"^\s*(?:%s)\b" % "|".join(OPENERS), re.I)

# Where the rule applies. The summary box, the "still fuzzy on" prompt and the
# closing big-picture line are the student reflecting on their own notes, not
# being quizzed on a slide, and are deliberately out of scope.
FIELDS = ("cues", "notes")


def offences(spec):
    """Every question in a notes spec's cue column or notes lines.

    Returns a list of (section code, field, text). Empty means the packet is
    recall throughout.
    """
    found = []
    for section in spec.get("sectionsContent", []):
        code = section.get("code", "?")
        for row in section.get("rows", []):
            for field in FIELDS:
                for entry in row.get(field, []) or []:
                    text = entry if isinstance(entry, str) else entry.get("text", "")
                    # A must-write line is marked with a leading *; the mark is
                    # not part of the sentence.
                    body = str(text).lstrip("*").strip()
                    if QUESTION_MARK.search(body) or OPENER.match(body):
                        found.append((code, field, body))
    return found


def check(spec, builder):
    """Print the refusal and return 1, or return 0. Callers return the result."""
    found = offences(spec)
    if not found:
        return 0
    import sys
    print(f"{builder}: guided notes are strictly recall, and these are questions:",
          file=sys.stderr)
    for code, field, text in found:
        where = "cue column" if field == "cues" else "notes line"
        print(f"   {code} · {where}: {text}", file=sys.stderr)
    print("\nA guided-notes packet is what a student writes while the slide is up. Name the\n"
          "thing to record - \"Definition - singularity\", \"The three pieces of evidence\",\n"
          "\"Steps of nebular theory, in order\" - rather than asking for it. Questions about\n"
          "the material belong in a practice set or a quiz, not here.", file=sys.stderr)
    return 1


def ruled_lines(text):
    """How many ruled lines a notes line gets. One rule, both renderers.

    This used to be "a line ending in ? gets two", which the recall rule above
    makes unreachable - there are no questions left to give room to. A label the
    student writes *under* is what needs the room now: "Define protostar:",
    "Core:", "Sunspots:". A line with its blanks inline is filled in place and
    takes one.
    """
    body = str(text).lstrip("*\u270e").rstrip()
    return 2 if body.endswith(":") else 1
