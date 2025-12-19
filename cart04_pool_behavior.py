#!/usr/bin/env python3
import json

INP = "telemetry_latest.json"
OUT = "pool_behavior.json"

def main():
    t = json.load(open(INP))
    pools = t["pools"]["POOLS"]
    report = []
    for p in pools:
        report.append({
            "url": p.get("URL"),
            "accepted": p.get("Accepted"),
            "rejected": p.get("Rejected"),
            "last_share": p.get("Last Share Time")
        })
    json.dump(report, open(OUT, "w"), indent=2)

if __name__ == "__main__":
    main()
