#!/usr/bin/env python3
import json, time, os

OUT = "RESEARCH_BLOCK.md"

def load(name):
    return json.load(open(name)) if os.path.exists(name) else {}

def main():
    eff = load("efficiency_report.json")
    diff = load("difficulty_snapshot.json")
    pools = load("pool_behavior.json")

    md = f"""# Infinity Research Block

## Purpose
Bitcoin miner telemetry → efficiency + network context.

## Token Block
- Token ID: 🧱🔑🧱 INF-OCT-BTC-0001
- Token Type: 🧱🔱🧱 Research / Infrastructure
- Token Value: 🧱👑🧱 UNSET
- Token Date: DEC 📹📽️🧱

## Efficiency
- Hashrate (GHS): {eff.get('hashrate_ghs')}
- Watts: {eff.get('watts')}
- GHS/W: {eff.get('ghs_per_watt')}

## Network
- Difficulty: {diff.get('difficulty')}

## Pools
{json.dumps(pools, indent=2)}

## Status
- [ ] Draft
- [ ] Needs valuation
- [ ] Needs routing
"""
    open(OUT, "w").write(md)

if __name__ == "__main__":
    main()
