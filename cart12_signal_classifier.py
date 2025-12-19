#!/usr/bin/env python3
import json

EFF = json.load(open("efficiency_report.json"))

ghs_w = EFF.get("ghs_per_watt", 0)

if ghs_w > 30:
    route = "infinity-treasury"
elif ghs_w > 20:
    route = "infinity_mongoose_bitcoin_research_miner"
else:
    route = "mongoose.os"

print(route)
open("route_target.txt", "w").write(route)
