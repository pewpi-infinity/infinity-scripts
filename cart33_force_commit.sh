#!/bin/sh
set -e

REPO_NAME="$(cat route_target.txt)"
REPO_PATH="$(find "$HOME" -maxdepth 4 -type d -name "$REPO_NAME" | head -n 1)"
cd "$REPO_PATH"

STATE_HASH="$(jq -r .repo_state_hash ../infinity-scripts/repo_state_hash.json 2>/dev/null || echo unknown)"
BTC_DIFF="$(jq -r .difficulty ../infinity-scripts/bitcoin_anchor.json 2>/dev/null || echo unknown)"

git add -A
git commit -m "∞ state=${STATE_HASH} btc_diff=${BTC_DIFF}" || {
  echo "[commit] no changes staged — forcing stamp"
  date > .infinity_stamp
  git add .infinity_stamp
  git commit -m "∞ stamp state=${STATE_HASH}"
}

git push origin main
echo "[commit] pushed"
