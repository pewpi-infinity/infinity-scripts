#!/data/data/com.termux/files/usr/bin/bash
set -e

BASE="$HOME/infinity-scripts"
LOG="$BASE/cart_push_report.txt"

echo "🧠 Infinity Cart Recovery Push" | tee "$LOG"
echo "📁 Scanning base: $BASE" | tee -a "$LOG"
echo "--------------------------------------" | tee -a "$LOG"

cd "$BASE"

for dir in */ ; do
  CART_DIR="${dir%/}"

  # Skip obvious non-cart folders if needed
  if [[ "$CART_DIR" == ".git" ]]; then
    continue
  fi

  echo "" | tee -a "$LOG"
  echo "🔍 Checking: $CART_DIR" | tee -a "$LOG"
  cd "$BASE/$CART_DIR"

  # 1. Init git if missing
  if [ ! -d ".git" ]; then
    echo "  ➕ Initializing git" | tee -a "$LOG"
    git init
    git branch -M main
    git config user.name "Infinity"
    git config user.email "infinity@infinity.local"
  fi

  # 2. Ensure at least one commit
  git add . || true
  git commit -m "Infinity cart sync" || true

  # 3. Check for remote
  if git remote | grep -q origin; then
    echo "  🔗 Remote exists" | tee -a "$LOG"
  else
    echo "  🌍 Creating GitHub repo: $CART_DIR" | tee -a "$LOG"

    if command -v gh >/dev/null 2>&1; then
      gh repo create "$CART_DIR" \
        --public \
        --source=. \
        --remote=origin \
        --push || echo "  ⚠️ Repo may already exist" | tee -a "$LOG"
    else
      echo "  ❌ GitHub CLI not found, skipping repo creation" | tee -a "$LOG"
      cd "$BASE"
      continue
    fi
  fi

  # 4. Push
  echo "  🚀 Pushing $CART_DIR" | tee -a "$LOG"
  git push -u origin main || echo "  ⚠️ Push failed" | tee -a "$LOG"

  cd "$BASE"
done

echo "" | tee -a "$LOG"
echo "✅ RECOVERY COMPLETE" | tee -a "$LOG"
echo "📄 Report saved to: $LOG"
