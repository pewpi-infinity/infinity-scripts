#!/bin/sh
set -e
./cart01_miner_telemetry_collect.py
./cart02_efficiency_analyze.py
./cart03_difficulty_snapshot.py
./cart04_pool_behavior.py
./cart05_print_research_md.py
./cart06_repo_router.py
./cart07_token_index_append.py
echo "Infinity mining research pipeline complete."
