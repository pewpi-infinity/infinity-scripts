#!/usr/bin/env python3
import json, os

files = ["octave_ledger.jsonl", "finality_log.jsonl", "intent_log.jsonl"]
rows = []

for fn in files:
  if os.path.exists(fn):
    for line in open(fn):
      try:
        rows.append(json.loads(line))
      except:
        pass

html = ["<html><body><h1>Infinity State Explorer</h1><ul>"]
for r in rows:
  html.append("<li><pre>"+json.dumps(r, indent=2)+"</pre></li>")
html.append("</ul></body></html>")

open("state_explorer.html", "w").write("\n".join(html))
print("[explorer] state_explorer.html written")
