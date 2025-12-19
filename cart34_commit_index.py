#!/usr/bin/env python3
import subprocess, json, time

commit = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd="."
).decode().strip()

record = {
  "ts": int(time.time()),
  "git_commit": commit
}

with open("commit_index.jsonl", "a") as f:
  f.write(json.dumps(record) + "\n")

print("[index] git commit recorded:", commit)
