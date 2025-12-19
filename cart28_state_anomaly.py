#!/usr/bin/env python3
import json, os

LEDGER = "octave_ledger.jsonl"
OUT = "anomalies.json"

hashes = []
if os.path.exists(LEDGER):
    for line in open(LEDGER):
        try:
            rec = json.loads(line)
            h = rec.get("repo_state_hash") or rec.get("octave_hash")
            if h: hashes.append(h)
        except:
            pass

anomalies = {
    "duplicates": [h for h in set(hashes) if hashes.count(h) > 1],
    "total_blocks": len(hashes)
}

json.dump(anomalies, open(OUT, "w"), indent=2)
print("[anomaly] scan complete")
