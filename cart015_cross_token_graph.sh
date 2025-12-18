#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO="cross_token_graph"
mkdir -p "$REPO"
cd "$REPO"

git init
git config user.name "Infinity"
git config user.email "infinity@graph.local"

cat > graph.py << 'PY'
import random

TOKENS=["🧱⭐🧱","☢️♠️🍄","⚛️♣️🧱","🧱✨⭐🧱"]

def jump(token):
    target=random.choice([t for t in TOKENS if t!=token])
    print(f"{token} → {target}")

if __name__=="__main__":
    import sys
    jump(sys.argv[1] if len(sys.argv)>1 else "🧱⭐🧱")
PY

git add graph.py
git commit -m "Initialize cross token graph walker"
echo "✅ CART 015 COMPLETE"
