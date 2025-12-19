#!/usr/bin/env python3
import os, hashlib, json, time

REPOS = [
  "infinity_mongoose_bitcoin_research_miner",
  "infinity-treasury",
  "mongoose.os"
]

def hash_repo(path):
  h = hashlib.sha256()
  for dp, _, fs in os.walk(path):
    if ".git" in dp: continue
    for f in sorted(fs):
      try:
        with open(os.path.join(dp, f), "rb") as fh:
          h.update(fh.read())
      except:
        pass
  return h.hexdigest()

agg = {"ts": int(time.time()), "repos": {}}
for r in REPOS:
  p = os.path.join(os.environ["HOME"], r)
  if os.path.isdir(p):
    agg["repos"][r] = hash_repo(p)

raw = json.dumps(agg, sort_keys=True).encode()
agg["global_hash"] = hashlib.sha256(raw).hexdigest()

with open("global_state.json", "w") as f:
  json.dump(agg, f, indent=2)

print("[global] state hash:", agg["global_hash"])
