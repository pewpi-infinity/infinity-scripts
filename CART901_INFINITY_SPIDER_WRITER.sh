#!/data/data/com.termux/files/usr/bin/bash
set -e

BASE="$HOME/infinity-runtime"
DATA="$BASE/data"
WEB="$BASE/web"
LOG="$BASE/logs"
TOKENS="$WEB/tokens"
INDEX="$WEB/SPIDER_INDEX.md"

mkdir -p "$DATA" "$WEB" "$TOKENS" "$LOG"

########################################
# LOAD STATE
########################################

STATE="$DATA/state.json"
if [ ! -f "$STATE" ]; then
  echo "❌ State not found. Run CART900 first."
  exit 1
fi

########################################
# CONTINUOUS WRITER LOOP
########################################

while true; do
  TS=$(date +"%Y%m%d_%H%M%S")
  TOKEN_ID="INF_$TS"

  python3 - << PY
import json,random,time,os

state=json.load(open("$STATE"))

topic=random.choice(state.get("topics",["unknown"]))
entropy=round(state.get("entropy",0.5),2)

emoji_pool=[
 "⭐","💫","⚡","🧠","🧱","🪐","🧲","🔗","🧬","🌞","☄️","📡","🔧","⚙️","🕵️","🍄"
]

content=f"""
# {topic} — Research Node {os.environ.get("TOKEN_ID")}

🩷 Investigative → 🟨 Extracted → 🟦 Absorbed

Entropy Level: {entropy}

{random.choice(emoji_pool)} Observation:
This node expands the web by anchoring {topic} into the Infinity brick lattice.

⭐ Pattern:
Repeated signal detected across prior nodes.

🧱 Brick Impact:
- Adds load-bearing structure
- Reduces entropy locally
- Spawns future routes

🇺🇲 Made in USA
"""

path=f"$TOKENS/{os.environ.get('TOKEN_ID')}.md"
open(path,"w").write(content)

# update state
state["entropy"]=max(0,state["entropy"]-0.05)
json.dump(state,open("$STATE","w"),indent=2)
PY

########################################
# UPDATE SPIDER INDEX
########################################

echo "- [$TOKEN_ID](tokens/$TOKEN_ID.md)" >> "$INDEX"

########################################
# AUTO-GIT ADD / COMMIT
########################################

git add "$WEB" "$DATA" || true
git commit -m "🧱⭐ Add research node $TOKEN_ID" || true

########################################
# VISUAL HEARTBEAT
########################################

echo "⭐🧱 $TOKEN_ID added to spiderweb"
sleep 20

done
