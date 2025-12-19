#!/usr/bin/env python3
import json, time, hashlib, sys

INTENT = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "unspecified"

record = {
  "ts": int(time.time()),
  "intent": INTENT
}

raw = json.dumps(record, sort_keys=True).encode()
record["intent_hash"] = hashlib.sha256(raw).hexdigest()

with open("intent_log.jsonl", "a") as f:
  f.write(json.dumps(record) + "\n")

print("[intent] tagged:", record["intent_hash"])
