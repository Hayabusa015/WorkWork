#!/usr/bin/env python3
"""Export the repository's bookkeeping as JSON for the WorkWork Ledger dashboard.

    python3 scripts/branch_ledger.py [--out ledger.json] [--no-checks]

Read-only. Git is the source of truth; this only reads it. Writes three lists:

  branches    every remote branch: merged into origin/main or not, commits ahead and
              behind, last commit date and subject. What a branch holds and how it was
              handled come from reports/branch-ledger-notes.json; a branch with no
              note there shows its last commit subject.
  collisions  every Change ID carried by more than one file in governance/proposals/.
  checks      each validator's exit state and how many findings it printed.

Run `git fetch origin` first, or the answer describes a stale view.
"""
import argparse, collections, datetime, json, os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(REPO, "reports", "branch-ledger-notes.json")
VALIDATORS = ["validate_layers", "validate_codes", "validate_tokens", "validate_agents",
              "validate_schemas", "validate_references", "validate_profiles", "validate_notes"]


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True,
                          check=True).stdout.strip()


def branches():
    notes = json.load(open(NOTES)) if os.path.exists(NOTES) else {}
    out = []
    for ref in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").splitlines():
        name = ref[len("origin/"):]
        if name in ("HEAD", "main") or ref == "origin":
            continue
        ahead = int(git("rev-list", "--count", f"origin/main..{ref}"))
        behind = int(git("rev-list", "--count", f"{ref}..origin/main"))
        date, subject = git("log", "-1", "--format=%ad\x1f%s", "--date=short", ref).split("\x1f")
        note = notes.get(name, {})
        out.append({
            "name": name, "merged": ahead == 0, "ahead": ahead, "behind": behind,
            "last_date": date, "last_subject": subject,
            "course": note.get("course", "Unsorted"),
            "holds": note.get("holds", subject),
            "handled": note.get("handled", "merged" if ahead == 0 else "new"),
            "note": note.get("note", ""),
        })
    return sorted(out, key=lambda b: b["last_date"])


def collisions():
    folder = os.path.join(REPO, "governance", "proposals")
    by_id = collections.defaultdict(list)
    for fn in sorted(os.listdir(folder)):
        m = re.match(r"(SHULL-CHG-\d+)-(.*)\.md$", fn)
        if m:
            by_id[m.group(1)].append(m.group(2).replace("-", " "))
    return [{"id": k, "records": v} for k, v in sorted(by_id.items()) if len(v) > 1]


def checks():
    out = []
    for v in VALIDATORS:
        r = subprocess.run([sys.executable, os.path.join(REPO, "scripts", v + ".py")],
                           capture_output=True, text=True)
        lines = [l.strip()[2:] for l in (r.stdout + r.stderr).splitlines() if l.strip().startswith("- ")]
        files = collections.Counter(re.split(r"[:\s]", l, maxsplit=1)[0] for l in lines)
        out.append({"name": v, "passed": r.returncode == 0, "findings": len(lines),
                    "files": [{"file": f, "count": n} for f, n in files.most_common(6)],
                    "example": lines[0][:220] if lines else ""})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--no-checks", action="store_true")
    a = ap.parse_args()
    data = {
        "meta": {"synced_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                 "main_sha": git("rev-parse", "--short", "origin/main"),
                 "main_commits": int(git("rev-list", "--count", "origin/main")),
                 "main_date": git("log", "-1", "--format=%ad", "--date=short", "origin/main")},
        "branches": branches(), "collisions": collisions(),
        "checks": [] if a.no_checks else checks(),
    }
    text = json.dumps(data, indent=1, ensure_ascii=False)
    if a.out:
        open(a.out, "w").write(text + "\n")
        b = data["branches"]
        print(f"branch_ledger: {len(b)} branches, {sum(not x['merged'] for x in b)} not merged, "
              f"{len(data['collisions'])} shared Change IDs -> {a.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
