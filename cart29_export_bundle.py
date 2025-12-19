#!/usr/bin/env python3
import json, tarfile, time, os

FILES = [
  "bitcoin_anchor.json",
  "octave_ledger.jsonl",
  "finality_log.jsonl",
  "valuation_signal.json"
]

name = f"infinity_export_{int(time.time())}.tar.gz"
with tarfile.open(name, "w:gz") as t:
    for f in FILES:
        if os.path.exists(f):
            t.add(f)

print("[export] bundle created:", name)
