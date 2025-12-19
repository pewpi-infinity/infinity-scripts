#!/usr/bin/env python3
import shutil, os

SRC = "RESEARCH_BLOCK.md"

ROUTES = {
    "bitcoin": "../infinity_mongoose_bitcoin_research_miner",
    "treasury": "../infinity-treasury",
    "os": "../mongoose.os"
}

def main():
    dest = ROUTES["bitcoin"]
    os.makedirs(dest, exist_ok=True)
    shutil.copy(SRC, os.path.join(dest, "RESEARCH_BLOCK.md"))

if __name__ == "__main__":
    main()
