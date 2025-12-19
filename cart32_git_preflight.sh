#!/bin/sh
set -e

if [ ! -f route_target.txt ]; then
  echo "[preflight] route_target.txt missing"; exit 1
fi

REPO_NAME="$(cat route_target.txt)"
REPO_PATH="$(find "$HOME" -maxdepth 4 -type d -name "$REPO_NAME" | head -n 1)"

if [ -z "$REPO_PATH" ]; then
  echo "[preflight] repo not found: $REPO_NAME"; exit 1
fi

cd "$REPO_PATH"

if [ ! -d .git ]; then
  echo "[preflight] not a git repo, initializing"
  git init
  git branch -M main
fi

if ! git remote | grep -q origin; then
  echo "[preflight] origin remote missing"; exit 1
fi

git status --porcelain >/dev/null
echo "[preflight] OK: $REPO_PATH"
