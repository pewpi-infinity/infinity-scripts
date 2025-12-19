#!/usr/bin/env python3
import json, time, socket, os

# CONFIG
MINER_HOST = os.getenv("MINER_HOST", "127.0.0.1")
MINER_PORT = int(os.getenv("MINER_PORT", "4028"))
OUT = "telemetry_latest.json"

def query(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((MINER_HOST, MINER_PORT))
    s.sendall(json.dumps({"command": cmd}).encode())
    data = s.recv(65535)
    s.close()
    return json.loads(data.decode())

def simulated():
    return {
        "SUMMARY": [{
            "GHS 5s": 95000.0,
            "Power": 3250,
            "Elapsed": 86400
        }]
    }

def main():
    try:
        summary = query("summary")
        pools = query("pools")
        mode = "LIVE"
    except Exception as e:
        summary = {"SUMMARY": simulated()["SUMMARY"]}
        pools = {"POOLS": []}
        mode = "SIMULATED"

    payload = {
        "mode": mode,
        "ts": int(time.time()),
        "summary": summary,
        "pools": pools
    }

    with open(OUT, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"[cart01] telemetry collected ({mode})")

if __name__ == "__main__":
    main()
