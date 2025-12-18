#!/usr/bin/env python3
import time
import subprocess
import os

BASE = os.path.expanduser("~/infinity-scripts")

CARTS = [
    "cart804_feed_generator.py",
    "cart805_wallet_engine.py",
]

def run(cart):
    try:
        subprocess.run(
            ["python3", os.path.join(BASE, cart)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass

while True:
    for cart in CARTS:
        run(cart)
    time.sleep(15)  # heartbeat pulse
