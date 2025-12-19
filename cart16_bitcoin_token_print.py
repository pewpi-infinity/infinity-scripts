#!/usr/bin/env python3
import json

anchor = json.load(open("bitcoin_anchor.json"))

md = f"""
## Bitcoin Anchor
- Difficulty: {anchor['difficulty']}
- Epoch: {anchor['epoch']}
- Anchor Time: {anchor['last_update']}

This token derives its scarcity reference from Bitcoin.
"""

open("BITCOIN_ANCHOR.md", "w").write(md)
print("[bitcoin] token anchor printed")
