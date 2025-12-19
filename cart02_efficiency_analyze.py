#!/usr/bin/env python3
import json, math

INP = "telemetry_latest.json"
OUT = "efficiency_report.json"

def main():
    t = json.load(open(INP))
    s = t["summary"]["SUMMARY"][0]
    hashrate = float(s.get("GHS 5s", 0))
    watts = float(s.get("Power", 0))
    eff = (hashrate / watts) if watts > 0 else 0
    out = {
        "hashrate_ghs": hashrate,
        "watts": watts,
        "ghs_per_watt": round(eff, 4)
    }
    json.dump(out, open(OUT, "w"), indent=2)

if __name__ == "__main__":
    main()
