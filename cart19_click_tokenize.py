#!/usr/bin/env python3
import json, time, hashlib

state = json.load(open("repo_state_hash.json"))

token = {
    "token_id": hashlib.sha256(
        f"{state['repo_state_hash']}{time.time()}".encode()
    ).hexdigest()[:16],
    "type": "STATE_CLICK",
    "repo_hash": state["repo_state_hash"],
    "ts": int(time.time())
}

with open("token_index.jsonl", "a") as f:
    f.write(json.dumps(token) + "\n")

print("[token] click tokenized:", token["token_id"])
