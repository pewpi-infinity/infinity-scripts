#!/usr/bin/env python3
import json, hashlib, time

anchor = json.load(open("bitcoin_anchor.json"))

block = {
    "ts": int(time.time()),
    "type": "INFINITY_CART",
    "bitcoin_difficulty": anchor["difficulty"],
    "epoch": anchor["epoch"]
}

raw = json.dumps(block, sort_keys=True).encode()
block["hash"] = hashlib.sha256(raw).hexdigest()

with open("octave_ledger.jsonl", "a") as f:
    f.write(json.dumps(block) + "\n")

print("[octave] bitcoin-rooted block appended:", block["hash"])
