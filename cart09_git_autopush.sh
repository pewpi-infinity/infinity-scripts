#!/bin/sh
set -e

if [ ! -f route_target.txt ]; then
  echo "[cart09] No route_target.txt — skipping"
  exit 0
fi

REPO_NAME="$(cat route_target.txt)"
BASE="$HOME"

echo "[cart09] locating repo: $REPO_NAME"

# Find first matching directory
REPO_PATH="$(find "$BASE" -maxdepth 3 -type d -name "$REPO_NAME" 2>/dev/null | head -n 1)"

if [ -z "$REPO_PATH" ]; then
  echo "[cart09] repo not found — skipping"
  exit 0
fi

cd "$REPO_PATH"
echo "[cart09] using $REPO_PATH"

# Initialize git if missing
if [ ! -d ".git" ]; then
  echo "[cart09] initializing git repo"
  git init
  git branch -M main
fi

# Ensure remote exists
if ! git remote | grep -q origin; then
  echo "[cart09] no remote set — skipping push"
  git add .
  git commit -m "Infinity research block (local)" || true
  exit 0
fi

git add .
git commit -m "Infinity research block update" || echo "[cart09] nothing to commit"
git push || echo "[cart09] push skipped"

