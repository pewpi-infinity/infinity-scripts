#!/data/data/com.termux/files/usr/bin/bash
set -e

BASE="$HOME/infinity-runtime"
DATA="$BASE/data"
LOG="$BASE/logs"
STATE="$DATA/state.json"

mkdir -p "$DATA" "$LOG"

########################################
# COLOR + ROLE DEFINITIONS
########################################

declare -A COLOR_ROLE=(
  [green]="engineering"
  [orange]="ceo"
  [blue]="input"
  [red]="routes"
  [yellow]="extraction"
  [purple]="assimilation"
  [pink]="investigative"
)

########################################
# BRICK DEFINITIONS
########################################

declare -A BRICKS=(
  ["🧱⭐🧱"]="peasant"
  ["🧱♦️🧱"]="merchant"
  ["🧱♥️🧱"]="clergy"
  ["🧱♠️🧱"]="noble"
  ["🧱🟨🧱"]="data"
  ["🧱🟥🧱"]="route"
  ["🧱🟪🧱"]="lock"
)

########################################
# EMOJI VERBS
########################################

declare -A VERBS=(
  ["💪💫🦾"]="collaborate"
  ["🦾💫🧱"]="force_break"
  ["⭐💫⭐"]="entropy_capture"
  ["🌻"]="regenerate"
  ["🍄"]="mutation"
)

########################################
# INIT STATE
########################################

if [ ! -f "$STATE" ]; then
cat << JSON > "$STATE"
{
  "color": "pink",
  "entropy": 0.85,
  "pressure": 0.7,
  "topics": [],
  "bricks": [],
  "locked": false
}
JSON
fi

########################################
# RESEARCH TOPIC INTAKE
########################################

echo
echo "🟥🟧🟨🟩🟦 INFINITY RESEARCH INTAKE 🟦🟩🟨🟧🟥"
echo
read -p "Enter research topics (comma separated): " TOPICS

IFS=',' read -ra TOPIC_ARRAY <<< "$TOPICS"

########################################
# WRITE STATE
########################################

python3 - << PY
import json,sys
from pathlib import Path

state = json.load(open("$STATE"))
state["topics"] = [t.strip() for t in """$TOPICS""".split(",") if t.strip()]
state["color"] = "pink"
state["entropy"] = 0.85
state["pressure"] = 0.7

json.dump(state, open("$STATE","w"), indent=2)
PY

echo "🩷 Investigative state armed"

########################################
# BRICK GENERATION
########################################

for t in "${TOPIC_ARRAY[@]}"; do
  echo "🧱 Generating brick for: $t"
  python3 - << PY
import json
state=json.load(open("$STATE"))
state["bricks"].append({
  "topic":"$t",
  "type":"🧱🟨🧱",
  "pressure":0.6,
  "color":"yellow"
})
json.dump(state, open("$STATE","w"), indent=2)
PY
done

########################################
# ENTROPY ENGINE
########################################

python3 - << PY
import json,time

state=json.load(open("$STATE"))

for brick in state["bricks"]:
    if brick["color"]=="yellow":
        brick["color"]="blue"
        brick["pressure"]-=0.2
        state["entropy"]-=0.1

if state["entropy"] < 0.5:
    state["color"]="green"
elif state["entropy"] < 0.3:
    state["color"]="purple"
    state["locked"]=True

json.dump(state, open("$STATE","w"), indent=2)
PY

########################################
# ROUTE / DECISION LOGIC
########################################

python3 - << PY
import json
state=json.load(open("$STATE"))

if state["color"]=="green":
    print("🟩 Engineering route unlocked")
elif state["color"]=="orange":
    print("🟧 CEO decision required")
elif state["color"]=="purple":
    print("🟪 Knowledge assimilated and locked")

json.dump(state, open("$STATE","w"), indent=2)
PY

########################################
# FINAL STATUS
########################################

echo
echo "⭐ INFINITY BRICK ENGINE COMPLETE ⭐"
echo "State file: $STATE"
echo "Review with: cat $STATE"
echo
