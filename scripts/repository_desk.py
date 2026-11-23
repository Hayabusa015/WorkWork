"""Read WorkWork from a fetched ref. Run as a child of the loopback desktop server."""
import concurrent.futures
import json
import os
import time
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen

# The bundled Windows embeddable interpreter isolates sys.path from the script folder.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from desk_export import record

REPO = "Hayabusa015/WorkWork"
URL = "https://github.com/" + REPO
MAIN = "refs/remotes/origin/main"
RECORD = re.compile(r"governance/proposals/SHULL-CHG-\d{4}-[a-zA-Z0-9._-]+\.md")


def git(root, *args, binary=False):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"}, timeout=100)
    if result.returncode:
        raise ValueError(result.stderr.decode(errors="replace").strip() or "Git failed.")
    return result.stdout if binary else result.stdout.decode("utf-8", errors="replace").rstrip()


def local(root):
    if not root or not (Path(root) / ".git").exists():
        return {"connected": False}
    remote = git(root, "remote", "get-url", "origin").lower().removesuffix(".git")
    if remote not in (URL.lower(), "git@github.com:" + REPO.lower(), "ssh://git@github.com/" + REPO.lower()):
        raise ValueError("Choose a WorkWork checkout with the GitHub repository as origin.")
    return {"connected": True, "root": str(root),
            "status": git(root, "status", "--short", "--branch"),
            "branches": git(root, "for-each-ref", "--format=%(refname:short) %(upstream:track)", "refs/heads").splitlines()}


def snapshot(root):
    git(root, "fetch", "--prune", "--no-tags", URL + ".git", "+refs/heads/*:refs/remotes/origin/*")
    sha = git(root, "rev-parse", MAIN)
    tips = git(root, "for-each-ref", "--format=%(refname:short)%09%(objectname)%09%(committerdate:short)%09%(subject)", "refs/remotes/origin")
    cache = Path(root) / "desk-index.json"
    if cache.exists():
        cached = json.loads(cache.read_text(encoding="utf-8"))
        if tips == cached["tips"] and "branchProposals" in cached["snapshot"]:
            return {**cached["snapshot"], "synced": datetime.now(timezone.utc).isoformat()}
    notes = json.loads(git(root, "show", sha + ":reports/branch-ledger-notes.json"))
    branches = []
    for line in tips.splitlines():
        ref, tip, date, subject = line.split("\t", 3)
        name = ref.removeprefix("origin/")
        if name in ("HEAD", "main"):
            continue
        behind, ahead = map(int, git(root, "rev-list", "--left-right", "--count", sha + "..." + tip).split())
        branches.append({**notes.get(name, {}), "name": name, "subject": subject, "date": date,
                         "ahead": ahead, "behind": behind})
    records = []
    for row in git(root, "ls-tree", "-r", sha, "governance/proposals").splitlines():
        info, filename = row.split("\t", 1)
        if not RECORD.fullmatch(filename):
            continue
        blob = info.split()[-1]
        item = record(Path(filename), git(root, "cat-file", "blob", blob))["data"]
        records.append({**item, "blob": blob})
    branch_proposals = []
    canonical = {r["file"]: r["blob"] for r in records}
    for branch in branches:
        if branch["ahead"] == 0:
            continue
        ref = "refs/remotes/origin/" + branch["name"]
        changed = git(root, "diff", "--name-only", "--diff-filter=AM", sha + "..." + ref, "--", "governance/proposals")
        for filename in changed.splitlines():
            if not RECORD.fullmatch(filename):
                continue
            blob = git(root, "rev-parse", ref + ":" + filename)
            if canonical.get(filename) == blob:
                continue
            item = record(Path(filename), git(root, "cat-file", "blob", blob))["data"]
            branch_proposals.append({"name": branch["name"], "file": filename, "title": item["title"],
                                     "status": item["status"], "tip": git(root, "rev-parse", ref)})
    decisions = []
    for line in git(root, "log", "-30", "--format=%H%x09%s", "--grep=^governance: record user decision on", sha).splitlines():
        commit, title = line.split("\t", 1)
        files = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()
        for filename in files:
            if RECORD.fullmatch(filename):
                decisions.append({"commit": commit, "file": filename, "title": title, "status": "recorded"})
    result = {"branchProposals": branch_proposals, "decisions": decisions, "main": sha, "records": records, "branches": sorted(branches, key=lambda b: b["date"], reverse=True),
            "synced": datetime.now(timezone.utc).isoformat()}

    temp = cache.with_suffix(".tmp")
    temp.write_text(json.dumps({"tips": tips, "snapshot": result}), encoding="utf-8")
    temp.replace(cache)
    return result


def github(endpoint):
    if AUTHENTICATED:
        proc = subprocess.run(["gh", "api", "repos/" + REPO + "/" + endpoint], capture_output=True, timeout=15)
        if proc.returncode:
            raise ValueError(proc.stderr.decode(errors="replace").strip())
        return json.loads(proc.stdout)
    with urlopen(Request("https://api.github.com/repos/" + REPO + "/" + endpoint,
                         headers={"User-Agent": "WorkWork-Desktop"}), timeout=10) as response:
        return json.load(response)


def activity(sha):
    def pulls():
        rows = []
        for page in range(1, 1000):
            items = github(f"pulls?state=open&per_page=100&page={page}")
            rows.extend({"branch": p["head"]["ref"], "number": p["number"], "title": p["title"]}
                        for p in items if p["head"]["repo"] and p["head"]["repo"]["full_name"] == REPO)
            if len(items) < 100:
                return rows
    def runs(workflow, query):
        data = github("actions/workflows/" + workflow + "/runs?" + query)["workflow_runs"]
        return [{"id": r["id"], "title": r["display_title"], "status": r["conclusion"] or r["status"]} for r in data]
    jobs = {"pulls": pulls, "checks": lambda: runs("validate.yml", "branch=main&head_sha=" + sha + "&per_page=1"),
            }
    result = {}
    with concurrent.futures.ThreadPoolExecutor() as pool:
        work = {k: pool.submit(fn) for k, fn in jobs.items()}
        for k, future in work.items():
            try:
                result[k] = future.result()
            except Exception as exc:
                result[k + "Error"] = str(exc)
    return result


if __name__ == "__main__":
    mode, checkout, cache = sys.argv[1:]
    try:
        if mode == "local":
            out = local(checkout)
        else:
            root = Path(cache)
            root.mkdir(parents=True, exist_ok=True)
            if not (root / "HEAD").exists():
                git(root, "init", "--bare")
            out = snapshot(root)
            # Public anonymous API quota is shared across endpoints. Git refs still refresh every minute.
            try:
                AUTHENTICATED = subprocess.run(["gh", "auth", "status", "--hostname", "github.com"],
                                               capture_output=True, timeout=10).returncode == 0
            except (OSError, subprocess.TimeoutExpired):
                AUTHENTICATED = False
            cache_file = root / "desk-activity.json"
            old = json.loads(cache_file.read_text()) if cache_file.exists() else {}
            if AUTHENTICATED or old.get("sha") != out["main"] or time.time() - old.get("time", 0) >= 300:
                old = {"sha": out["main"], "time": time.time(), "activity": activity(out["main"])}
                tmp = cache_file.with_suffix(".tmp")
                tmp.write_text(json.dumps(old))
                tmp.replace(cache_file)
            out.update(old["activity"])
            out["activityAt"] = datetime.fromtimestamp(old["time"], timezone.utc).isoformat()
        print(json.dumps(out))
    except FileNotFoundError:
        sys.exit("Git is required. Install Git for Windows, then reopen SHULL OS.")
    except Exception as exc:
        sys.exit(str(exc))
