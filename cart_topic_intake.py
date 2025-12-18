#!/usr/bin/env python3
import json, time, os

DATA_DIR = os.path.expanduser("~/site/data")
os.makedirs(DATA_DIR, exist_ok=True)

topics_raw = input("Research topics (comma separated): ").strip()

topics = [t.strip() for t in topics_raw.split(",") if t.strip()]

payload = {
    "timestamp": time.time(),
    "topics": topics,
    "state": "pink",        # investigative
    "processed": False
}

with open(f"{DATA_DIR}/active_research.json", "w") as f:
    json.dump(payload, f, indent=2)

print("🩷 Research topics registered and armed")
