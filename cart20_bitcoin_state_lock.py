#!/usr/bin/env python3
import json, time, hashlib, requests

difficulty = float(requests.get(
    "https://blockchain.info/q/getdifficulty", timeout=5
).text)

state = json.load(open("repo_state_hash.json"))

block = {
    "ts": int(time.time()),
    "repo_state_hash": state["repo_state_hash"],
    "bitcoin_difficulty": difficulty
}

raw = json.dumps(block, sort_keys=True).encode()
block["octave_hash"] = hashlib.sha256(raw).hexdigest()

with open("octave_ledger.jsonl", "a") as f:
    f.write(json.dumps(block) + "\n")

print("[octave] state locked to bitcoin:", block["octave_hash"])
