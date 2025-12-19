#!/usr/bin/env python3
import json, hashlib, time, os

ANCHOR = "bitcoin_anchor.json"
STATE = "repo_state_hash.json"
OUT = "valuation_signal.json"

if not (os.path.exists(ANCHOR) and os.path.exists(STATE)):
    print("[valuation] missing inputs — skipping")
    exit(0)

anchor = json.load(open(ANCHOR))
state = json.load(open(STATE))

difficulty = anchor.get("difficulty") or 1
# crude magnitude proxy: hash entropy (count of unique hex chars)
entropy = len(set(state["repo_state_hash"]))

signal = {
    "ts": int(time.time()),
    "repo_state_hash": state["repo_state_hash"],
    "bitcoin_difficulty": difficulty,
    "entropy": entropy,
    "valuation_score": round(entropy * (difficulty ** 0.00001), 6)
}

raw = json.dumps(signal, sort_keys=True).encode()
signal["signal_hash"] = hashlib.sha256(raw).hexdigest()

json.dump(signal, open(OUT, "w"), indent=2)
print("[valuation] signal computed:", signal["signal_hash"])
