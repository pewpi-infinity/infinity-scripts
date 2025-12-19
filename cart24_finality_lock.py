#!/usr/bin/env python3
import json, time, hashlib

state = json.load(open("global_state.json"))

final = {
  "ts": int(time.time()),
  "finalized_hash": state["global_hash"],
  "note": "State finalized; immutable"
}

raw = json.dumps(final, sort_keys=True).encode()
final["lock_hash"] = hashlib.sha256(raw).hexdigest()

with open("finality_log.jsonl", "a") as f:
  f.write(json.dumps(final) + "\n")

print("[finality] locked:", final["lock_hash"])
