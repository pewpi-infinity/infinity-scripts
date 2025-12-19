#!/usr/bin/env python3
import json, collections, os

LOG = "intent_log.jsonl"
OUT = "intent_heatmap.json"

counts = collections.Counter()

if os.path.exists(LOG):
    for line in open(LOG):
        try:
            rec = json.loads(line)
            key = rec.get("intent","unspecified").split()[0].lower()
            counts[key] += 1
        except:
            pass

json.dump(counts, open(OUT, "w"), indent=2)
print("[heatmap] intents aggregated")
