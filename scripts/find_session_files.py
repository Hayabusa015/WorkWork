#!/usr/bin/env python3
"""List documents created in this session, as JSON. Read-only; it never touches Drive.

Used by the reconcile-session-files skill (SHULL-CHG-0028). A file counts as created in
this session when it was modified after the session-start marker that
scripts/setup-environment.sh writes (~/.shull-session-start).

    python3 scripts/find_session_files.py                 # repo, scratchpad dirs, app/data
    python3 scripts/find_session_files.py --root /some/dir
    python3 scripts/find_session_files.py --since 2026-10-15T09:00:00
"""
import argparse, datetime, glob, hashlib, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = {".docx", ".pptx", ".pdf", ".html", ".xlsx"}
SKIP_DIRS = {".git", "node_modules", "legacy", "templates", "reports", "docs", "__pycache__",
             ".assets", "previews", "fonts", ".claude", "governance", "standards", "brand"}
SKIP_NAME = ("_PREVIEW", "_TEMPLATE", "TEMPLATE_MASTER", "TEMPLATE_TEACHER_KEY")


def start_time(marker, since):
    if since:
        return datetime.datetime.fromisoformat(since).timestamp(), "--since"
    if os.path.exists(marker):
        return os.path.getmtime(marker), marker
    return None, None


def default_roots():
    roots = [REPO, os.path.join(REPO, "app", "data")]
    roots += [p for p in glob.glob("/tmp/claude-*/**/scratchpad", recursive=True) if os.path.isdir(p)]
    seen, out = set(), []
    for r in roots:
        if os.path.isdir(r) and r not in seen:
            seen.add(r); out.append(r)
    return out


def walk(root, is_repo):
    for dp, dn, fn in os.walk(root):
        # Inside the repo, skip source and system folders. Elsewhere (scratchpad, app/data) skip
        # only build noise, because a built document can legitimately sit in a folder named
        # "docs" or "templates" there.
        skip = SKIP_DIRS if is_repo else {".git", "node_modules", "__pycache__", ".assets"}
        dn[:] = [d for d in dn if d not in skip]
        for f in fn:
            if os.path.splitext(f)[1].lower() in EXT and not any(s in f for s in SKIP_NAME):
                yield os.path.join(dp, f)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--marker", default=os.path.expanduser("~/.shull-session-start"))
    ap.add_argument("--since", help="ISO time; overrides the marker")
    ap.add_argument("--root", action="append", help="directory to scan (repeatable)")
    a = ap.parse_args()

    t0, source = start_time(a.marker, a.since)
    if t0 is None:
        print(json.dumps({"error": "no session-start marker and no --since", "marker": a.marker}))
        return 2
    roots = a.root or default_roots()
    found = []
    for r in roots:
        is_repo = os.path.abspath(r) == REPO
        for p in walk(r, is_repo):
            if os.path.getmtime(p) > t0:
                found.append(p)
    found = sorted(set(found))
    out = {"session_start": datetime.datetime.fromtimestamp(t0).isoformat(timespec="seconds"),
           "start_source": source, "roots": roots,
           "files": [{"path": p, "name": os.path.basename(p), "size": os.path.getsize(p),
                      "modified": datetime.datetime.fromtimestamp(os.path.getmtime(p)).isoformat(timespec="seconds"),
                      "sha256": sha(p)} for p in found]}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
