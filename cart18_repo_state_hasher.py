#!/usr/bin/env python3
import os, hashlib, json, time

def hash_repo(root="."):
    h = hashlib.sha256()
    for dirpath, _, filenames in os.walk(root):
        for f in sorted(filenames):
            if ".git" in dirpath:
                continue
            try:
                with open(os.path.join(dirpath, f), "rb") as fh:
                    h.update(fh.read())
            except:
                pass
    return h.hexdigest()

state_hash = hash_repo()

record = {
    "ts": int(time.time()),
    "repo_state_hash": state_hash
}

with open("repo_state_hash.json", "w") as f:
    json.dump(record, f, indent=2)

print("[state] repo hashed:", state_hash)
