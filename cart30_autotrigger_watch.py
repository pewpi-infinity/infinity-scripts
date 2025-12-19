#!/usr/bin/env python3
import time, os, subprocess

WATCH = "."
STAMP = {}

def snapshot():
    s = {}
    for dp, _, fs in os.walk(WATCH):
        if ".git" in dp:
            continue
        for f in fs:
            p = os.path.join(dp, f)
            try:
                s[p] = os.path.getmtime(p)
            except:
                pass
    return s

STAMP = snapshot()
print("[watch] started — monitoring repo state")

while True:
    time.sleep(2)
    now = snapshot()
    if now != STAMP:
        STAMP = now
        subprocess.call(["./cart21_click_pipeline.sh"])
        print("[watch] change detected → pipeline run")
