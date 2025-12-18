#!/usr/bin/env python3

import os, time, subprocess

MODES = os.getenv("INF_MODES","")
OSMODE = os.getenv("INF_OS","")
REPO = os.getenv("INF_REPO_PER_CART") == "1"

def run(cart):
    subprocess.run(
        ["python3", f"~/infinity-scripts/{cart}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

print(f"🧠 OS MODE: {OSMODE}")
print(f"🎛 MODES: {MODES}")
print(f"📦 Repo-per-cart: {REPO}")

if "writer" in MODES:
    run("cart_writer.py")

if "scraper" in MODES:
    run("cart_scraper.py")

if "website" in MODES or "builder" in MODES:
    run("cart_site_builder.py")

if "lab" in MODES:
    run("cart_lab.py")

if "market" in MODES:
    run("cart_marketplace.py")

if "connect" in MODES:
    run("cart_connect.py")

print("💜 Infinity Runtime Active")

while True:
    time.sleep(20)

def check_research():
    subprocess.run(
        ["python3", os.path.expanduser("~/infinity-scripts/cart_research_engine.py")],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

check_research()
