#!/data/data/com.termux/files/usr/bin/bash
set -e

BASE="$HOME/infinity-scripts"
echo "🔎 Scanning repos in $BASE"
cd "$BASE"

for dir in */; do
  if [ -d "$dir/.git" ]; then
    echo "🚀 Processing $dir"
    cd "$dir"

    # Ensure branch
    git branch -M main || true

    # Check remote
    if ! git remote | grep -q origin; then
      echo "⚠️ No remote for $dir — skipping remote add"
    else
      git add . || true
      git commit -m "Auto-sync Infinity cart" || true
      git push -u origin main || true
    fi

    cd "$BASE"
  fi
done

echo "✅ GLOBAL PUSH COMPLETE"
