#!/usr/bin/env python3
import requests, json, time

URL = "https://blockchain.info/q/getdifficulty"
OUT = "difficulty_snapshot.json"

def main():
    d = float(requests.get(URL, timeout=5).text)
    json.dump({
        "difficulty": d,
        "ts": int(time.time())
    }, open(OUT, "w"), indent=2)

if __name__ == "__main__":
    main()
