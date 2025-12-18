#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO="infinity_ownership_ledger"
mkdir -p "$REPO"
cd "$REPO"

git init
git config user.name "Infinity"
git config user.email "infinity@ownership.local"

cat > ledger.py << 'PY'
import json, os, datetime

FILE="ownership.json"

def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE,"r",encoding="utf-8"))

def register(token, owner):
    data=load()
    data.append({
        "token":token,
        "owner":owner,
        "time":datetime.datetime.utcnow().isoformat()+"Z"
    })
    json.dump(data,open(FILE,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print("🧾 Ownership recorded:",token,"→",owner)

if __name__=="__main__":
    import sys
    register(sys.argv[1] if len(sys.argv)>1 else "🧱⭐🧱",
             sys.argv[2] if len(sys.argv)>2 else "researcher")
PY

git add ledger.py
git commit -m "Initialize ownership ledger"
echo "✅ CART 013 COMPLETE"
