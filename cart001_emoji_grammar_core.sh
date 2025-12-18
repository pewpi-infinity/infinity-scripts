#!/data/data/com.termux/files/usr/bin/bash
set -e

CART_NAME="emoji_grammar_core"
REPO_NAME="$CART_NAME"

mkdir -p "$REPO_NAME"
cd "$REPO_NAME"

git init
git config user.name "Infinity"
git config user.email "infinity@research.local"

cat > emoji_grammar.json << 'JSON'
{
  "anchors": {
    "🧱": "structural boundary / immutable artifact"
  },
  "domains": {
    "☢️": "nuclear / high-energy systems",
    "🍄": "regenerative / biological / growth systems",
    "⚛️": "quantum / atomic fields"
  },
  "suits": {
    "♠️": "noble / executive reasoning",
    "♦️": "merchant / valuation reasoning",
    "♣️": "engineer / builder reasoning",
    "♥️": "healer / life systems reasoning"
  },
  "states": {
    "⭐": "entropy capture",
    "✨": "refinement cycle",
    "💥": "energetic transition",
    "🥳": "sealed separation / completion"
  },
  "transforms": {
    "=": "equivalence",
    "×": "conversion",
    "→": "directional transformation"
  }
}
JSON

git add emoji_grammar.json
git commit -m "Initialize emoji grammar core"

echo "✅ CART 001 COMPLETE — emoji grammar initialized"
