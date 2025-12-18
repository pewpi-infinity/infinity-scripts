#!/data/data/com.termux/files/usr/bin/bash
set -e

CART_NAME="emoji_chain_validator"
REPO_NAME="$CART_NAME"

mkdir -p "$REPO_NAME"
cd "$REPO_NAME"

git init
git config user.name "Infinity"
git config user.email "infinity@research.local"

cat > validator.py << 'PY'
import json
import sys

GRAMMAR_FILE = "../emoji_grammar_core/emoji_grammar.json"

def load_grammar():
    with open(GRAMMAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def validate(chain, grammar):
    known = set()
    for section in grammar.values():
        known.update(section.keys())

    unknown = [c for c in chain if c not in known and c not in ["=", "×", "→"]]
    return unknown

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validator.py \"☢️♠️🧱\"")
        sys.exit(1)

    chain = sys.argv[1]
    grammar = load_grammar()
    unknown = validate(chain, grammar)

    if unknown:
        print("❌ INVALID EMOJIS:", "".join(unknown))
    else:
        print("✅ VALID EMOJI CHAIN:", chain)
PY

git add validator.py
git commit -m "Add emoji chain validator"

echo "✅ CART 002 COMPLETE — validator online"
