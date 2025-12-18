#!/usr/bin/env python3

import os, sys, subprocess

def run(cmd):
    subprocess.run(cmd, shell=True)

print("\n🟥 Infinity System Boot 🟥\n")

print("Choose OS Replacement Route:")
print("1️⃣ octave.os 🟨🦶")
print("2️⃣ mongoose.os 🛴🟥🟧🟨")
print("3️⃣ infinity-treasury.os 💿🍸")
choice = input("Select [1-3]: ").strip()

if choice == "1":
    os.environ["INF_OS"] = "octave"
elif choice == "2":
    os.environ["INF_OS"] = "mongoose"
elif choice == "3":
    os.environ["INF_OS"] = "treasury"
else:
    print("Invalid choice"); sys.exit(1)

print("\nRUN OPTIONS:")
print("🟦 Writer")
print("🟨 Scraper")
print("🟧 Website / Cart Builder")
print("🟩 Lab")
print("🟪 Marketplace")
print("🟥 Connect")

modes = input("Enter modes (comma separated): ").lower()

repo_mode = input("\nGitHub Repo per cart/system? (yes/no): ").lower().startswith("y")

os.environ["INF_MODES"] = modes
os.environ["INF_REPO_PER_CART"] = "1" if repo_mode else "0"

print("\n🟩 Booting Infinity Runtime...\n")
run("python3 ~/infinity-scripts/infinity_runtime.py")
