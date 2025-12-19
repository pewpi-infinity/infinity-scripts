#!/data/data/com.termux/files/usr/bin/bash
set -e

BASE="$(pwd)"
OUT="$BASE/bitcoin_research"
INDEX="$OUT/README.md"

mkdir -p "$OUT"

if [ ! -f "$INDEX" ]; then
  echo "# ⛏️ Bitcoin Research Spider" > "$INDEX"
  echo "" >> "$INDEX"
fi

while true; do
  TS=$(date +"%Y-%m-%d %H:%M:%S")
  ID=$(date +"%Y%m%d_%H%M%S")
  FILE="$OUT/BTC_NODE_$ID.md"

  cat << MD > "$FILE"
# 🟧 Bitcoin Research Node $ID

🧱 Source: Infinity Miner  
⭐ Time: $TS  

## Observation
Bitcoin hash dynamics show repeating structural resonance across research domains.

## Pattern
- Hash rate ↔ entropy
- Network pressure ↔ decision routing
- Mining ↔ information compression

## Brick Impact
- Adds merchant-layer value 🧱♦️🧱
- Feeds spiderweb
- Lowers uncertainty

🇺🇲 Made in USA
MD

  echo "- [$ID](BTC_NODE_$ID.md)" >> "$INDEX"

  git add "$OUT"
  git commit -m "⛏️ BTC research node $ID" || true

  echo "⭐🧱 BTC_NODE_$ID written and committed"
  sleep 30
done
