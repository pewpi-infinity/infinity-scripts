#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO="infinity_research_batch_pusher"
BASE="$HOME/infinity-scripts"
mkdir -p "$BASE/$REPO"
cd "$BASE/$REPO"

git init
git branch -M main
git config user.name "Infinity"
git config user.email "infinity@batch.local"

cat > push.py << 'PY'
import os, datetime, random

def write_batch():
    name = f"batch_{datetime.datetime.utcnow().isoformat().replace(':','-')}.md"
    with open(name,"w",encoding="utf-8") as f:
        f.write("# Infinity Research Batch\n\n")
        for i in range(3):
            f.write(f"- 🧱⭐🧱 Research item {i}\n")
    return name

if __name__ == "__main__":
    fname = write_batch()
    print("Written batch:", fname)
PY

chmod +x push.py
git add push.py
git commit -m "Initialize batch pusher"
