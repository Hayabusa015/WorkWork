"""Record the owner's reviewed desktop decision on the exact proposal blob."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import re
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parent))
from desktop_queue import MARKER
from repository_desk import RECORD, git, record

ACTIONS = {"approve": "APPROVED", "reject": "REJECTED", "defer": "DEFERRED", "implement": "APPROVED"}


def replace_field(text, field, value, append=False):
    patterns = [rf"^(\|\s*\*\*{field}\*\*\s*\|)[^\n]*\|\s*$",
                rf"^({field}:)[^\n]*(?:\n[ \t]+[^\n]+)*"]
    for pattern in patterns:
        if len(re.findall(pattern, text, re.M)) == 1:
            ending = " |" if pattern == patterns[0] else ""
            def replacement(match):
                old = match[0].rstrip().removesuffix("|").rstrip() if ending else match[0].rstrip()
                return (old if append else match[1]) + " " + value + ending
            return re.sub(pattern, replacement, text, count=1, flags=re.M)
    raise ValueError("Record needs manual review: " + field)


def apply(root, inputs, actor, now):
    filename, action, blob = (inputs[k] for k in ("record", "decision", "blob"))
    if not RECORD.fullmatch(filename) or action not in ACTIONS or not re.fullmatch(r"[0-9a-f]{40}", blob):
        raise ValueError("Invalid decision request.")
    if git(root, "rev-parse", "HEAD:" + filename) != blob:
        raise ValueError("This proposal changed. Refresh and review the current wording.")
    path = root / filename
    text = path.read_text(encoding="utf-8")
    item = record(path, text)["data"]
    if action == "implement":
        if item["status"] != "APPROVED" or MARKER in text:
            raise ValueError("Only an approved record without an outstanding request can be queued.")
    elif item["status"] not in ("PENDING", "DEFERRED"):
        raise ValueError("This record already has a decision.")
    note = inputs.get("note", "").strip()
    if len(note) > 1000 or any(c in note for c in "\r\n|"):
        raise ValueError("Use one line of up to 1,000 characters without a table separator.")
    if not note:
        raise ValueError("Enter your decision, including any option or condition, in your own words.")
    decision = f'{actor} via desktop, {now}: "{note}"'
    if action in ("approve", "implement"):
        decision += " " + MARKER
    status = ACTIONS[action]
    if action == "implement" and text.startswith("---\n") and not re.search(r"^Decision:", text, re.M):
        updated = text.rstrip() + "\n\nDecision: " + decision + "\n"
    else:
        updated = replace_field(text, "Decision", decision, append=(action == "implement"))
        if action != "implement":
            updated = replace_field(updated, "Status", status)
    if record(path, updated)["data"]["status"] != status:
        raise ValueError("This record format needs manual recording.")
    log = root / "change-log/CHANGELOG.md"
    old = log.read_text(encoding="utf-8")
    marker = re.search(r"^## \d{4}-", old, re.M)
    if not marker:
        raise ValueError("Change log format needs review.")
    date = now[:10]
    row = f"| {item['change_id']} | {date} | Desktop decision | {status} | `{filename}` |\n"
    entry = f"## {date} · Desktop decision\n\n| ID | Date | Change | Status | Record |\n|---|---|---|---|---|\n{row}\n"
    path.write_text(updated, encoding="utf-8")
    log.write_text(old[:marker.start()] + entry + old[marker.start():], encoding="utf-8")


def submit(cache, inputs):
    from repository_desk import MAIN, URL
    identity = subprocess.run(["gh", "api", "user", "--jq", ".login"], capture_output=True, text=True, timeout=25)
    if identity.returncode or identity.stdout.strip().lower() != "hayabusa015":
        raise ValueError("Sign in to GitHub CLI as Hayabusa015 with gh auth login.")
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        git(root, "init", "--quiet")
        alternate = root / ".git/objects/info/alternates"
        alternate.write_text((cache.resolve() / "objects").as_posix() + "\n", encoding="utf-8")
        git(root, "fetch", "--quiet", str(cache), MAIN)
        git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        # Refresh main in the isolated checkout. A normal push rejects a racing update.
        git(root, "fetch", "--quiet", URL + ".git", "refs/heads/main")
        git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        apply(root, inputs, identity.stdout.strip(), datetime.now(timezone.utc).isoformat(timespec="seconds"))
        file = inputs["record"]
        git(root, "add", "--", file, "change-log/CHANGELOG.md")
        git(root, "-c", "user.name=WorkWork Secretary Desk", "-c", "user.email=110059644+Hayabusa015@users.noreply.github.com",
            "commit", "-qm", "governance: record user decision on " + Path(file).name[:14])
        git(root, "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
            "push", URL + ".git", "HEAD:refs/heads/main")
        return git(root, "rev-parse", "HEAD")


if __name__ == "__main__":
    try:
        print(submit(Path(sys.argv[1]), json.loads(sys.stdin.read())))
    except FileNotFoundError:
        sys.exit("Install Git and GitHub CLI, then sign in with gh auth login.")
    except Exception as exc:
        sys.exit(str(exc))
