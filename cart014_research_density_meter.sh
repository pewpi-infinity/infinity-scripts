#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO="research_density_meter"
mkdir -p "$REPO"
cd "$REPO"

git init
git config user.name "Infinity"
git config user.email "infinity@density.local"

cat > density.py << 'PY'
def density(words, links):
    score = words + (links*20)
    if score < 500: return "🟦 Thin"
    if score < 2000: return "🟩 Growing"
    if score < 8000: return "🟪 Dense"
    return "🟥 Bank-Grade"

if __name__=="__main__":
    import sys
    w=int(sys.argv[1]) if len(sys.argv)>1 else 500
    l=int(sys.argv[2]) if len(sys.argv)>2 else 5
    print("Research Density:",density(w,l))
PY

git add density.py
git commit -m "Add research density meter"
echo "✅ CART 014 COMPLETE"
