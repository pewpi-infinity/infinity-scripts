#!/usr/bin/env python3
import hashlib, json, time

LEDGER = "octave_ledger.jsonl"

block = {
    "ts": int(time.time()),
    "token_id": "INF-OCT-BTC-0001",
    "type": "research",
    "status": "draft"
}

raw = json.dumps(block, sort_keys=True).encode()
block["hash"] = hashlib.sha256(raw).hexdigest()

with open(LEDGER, "a") as f:
    f.write(json.dumps(block) + "\n")

print("[octave] block appended:", block["hash"])
