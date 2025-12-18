#!/data/data/com.termux/files/usr/bin/bash

ORG="pewpi-infinity"
NAME="infinity_mongoose_bitcoin_research_miner"
BASE="$HOME/infinity-treasury"
OUT="$BASE/$NAME"
RESEARCH="$OUT/RESEARCH.md"
STATE="$OUT/.content_hash"
LOG="$OUT/miner.log"
INTERVAL=120

mkdir -p "$OUT"
cd "$OUT"

git config --global user.name "Infinity"
git config --global user.email "watsonKris61@gmail.com"

if [ ! -d ".git" ]; then
  git init
  git branch -M main
fi

if ! gh repo view "$ORG/$NAME" >/dev/null 2>&1; then
  gh repo create "$ORG/$NAME" --public -y
fi

if ! git remote | grep -q origin; then
  git remote add origin "https://github.com/$ORG/$NAME.git"
fi

if [ ! -f "$RESEARCH" ]; then
cat << MD > "$RESEARCH"
# Infinity Mongoose Bitcoin Research Ledger

Append-only research ledger.
Blocks represent **real accumulated work**, not timestamps.
MD
fi

echo "[∞] Bitcoin Mongoose Research Miner ONLINE" | tee -a "$LOG"

while true; do
  TS=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

  BTC_PRICE=$(curl -s https://api.coingecko.com/api/v3/simple/price?ids=bitcoin\&vs_currencies=usd | awk -F: '{print $3}' | tr -d '},')

  TMP=$(mktemp)

  {
    echo "## Research Block $TS"
    echo
    echo "**Live Bitcoin Price (USD):** $BTC_PRICE"
    echo
    echo "### Repository State Hashes"
    echo
    for repo in "$BASE"/*/ ; do
      R=$(basename "$repo")
      [[ "$R" == "$NAME" ]] && continue
      [[ ! -d "$repo/.git" ]] && continue
      SIG=$(find "$repo" -type f \( -name "*.py" -o -name "*.md" -o -name "*.sh" \) \
            -exec sha256sum {} \; | sha256sum | awk '{print $1}')
      echo "- $R : $SIG"
    done
    echo
    echo "### Synthesis"
    echo "This block reflects live Bitcoin market conditions combined with"
    echo "the current structural state of the Infinity / Mongoose ecosystem."
    echo "Value is derived from cumulative computation + research + integration."
    echo
  } > "$TMP"

  NEW_HASH=$(sha256sum "$TMP" | awk '{print $1}')
  OLD_HASH=""
  [[ -f "$STATE" ]] && OLD_HASH=$(cat "$STATE")

  if [[ "$NEW_HASH" != "$OLD_HASH" ]]; then
    cat "$TMP" >> "$RESEARCH"
    echo "$NEW_HASH" > "$STATE"
    git add "$RESEARCH" "$STATE"
    git commit -m "∞ Bitcoin research block $TS"
    git push -u origin main
  fi

  rm "$TMP"
  sleep "$INTERVAL"
done
