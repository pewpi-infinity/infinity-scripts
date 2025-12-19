#!/usr/bin/env python3
import json, time

IDX = "token_index.jsonl"

entry = {
    "token_id": "INF-OCT-BTC-0001",
    "type": "research",
    "status": "draft",
    "ts": int(time.time())
}

with open(IDX, "a") as f:
    f.write(json.dumps(entry) + "\n")
