#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO="infinity_token_buffer"
BASE="$HOME/infinity-scripts"
mkdir -p "$BASE/$REPO"
cd "$BASE/$REPO"

git init
git branch -M main
git config user.name "Infinity"
git config user.email "infinity@buffer.local"

cat > buffer.py << 'PY'
from collections import deque
import datetime, random

BUFFER_SIZE = 5
TOKENS = deque(maxlen=BUFFER_SIZE)

def add(token, text):
    TOKENS.append({
        "token": token,
        "time": datetime.datetime.utcnow().isoformat()+"Z",
        "text": text
    })

def snapshot():
    return list(TOKENS)

if __name__ == "__main__":
    for i in range(10):
        add("🧱⭐🧱", f"Sample research block {i}")
        print("Buffer:", snapshot())
PY

chmod +x buffer.py
git add buffer.py
git commit -m "Initialize rolling token buffer"
