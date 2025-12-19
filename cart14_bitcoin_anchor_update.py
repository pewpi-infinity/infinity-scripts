#!/usr/bin/env python3
import requests, json, time

ANCHOR = "bitcoin_anchor.json"

difficulty = float(requests.get(
    "https://blockchain.info/q/getdifficulty", timeout=5
).text)

anchor = json.load(open(ANCHOR))
anchor.update({
    "difficulty": difficulty,
    "epoch": int(time.time() // (2016 * 600)),
    "last_update": int(time.time())
})

json.dump(anchor, open(ANCHOR, "w"), indent=2)
print("[bitcoin] anchor updated")
