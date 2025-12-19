#!/usr/bin/env python3
import json, glob, os

ANCHOR_FILE = "bitcoin_anchor.json"

if not os.path.exists(ANCHOR_FILE):
    print("[bitcoin] no anchor found — skipping")
    exit(0)

anchor = json.load(open(ANCHOR_FILE))

for f in glob.glob("*.json"):
    if f == ANCHOR_FILE:
        continue

    try:
        data = json.load(open(f))
    except Exception:
        continue

    # Case 1: dict
    if isinstance(data, dict):
        data["bitcoin_anchor"] = anchor

    # Case 2: list
    elif isinstance(data, list):
        data = {
            "data": data,
            "bitcoin_anchor": anchor
        }

    else:
        continue

    json.dump(data, open(f, "w"), indent=2)

print("[bitcoin] attribution injected (dicts + lists)")
