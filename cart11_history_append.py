#!/usr/bin/env python3
import json, time

SRC = "efficiency_report.json"
OUT = "history_efficiency.jsonl"

if __name__ == "__main__":
    data = json.load(open(SRC))
    data["ts"] = int(time.time())
    with open(OUT, "a") as f:
        f.write(json.dumps(data) + "\n")
