#!/usr/bin/env python3

import random
import time

EMOJI_POOL = ['⚡', '🔗', '⭐', '🌌', '🔬', '💡', '🧬', '🚀', '🌀', '📜']

COLOR_MAP = {
    "engineering": "🟩",  # Tools/builds
    "ceo": "🟧",          # Decisions/strategy
    "input": "🟦",        # Needed data
    "routes": "🟥",       # High-value paths
    "assimilation": "🟪", # Acknowledger integration
    "data": "🟨",         # Extract to blue
    "investigative": "PINK"  # Deep probes like H or finite π
}

def generate_unique_hash():
    return ''.join(random.sample(EMOJI_POOL, 3))

def determine_color(topic):
    if "hydrogen" in topic or "finite-pi" in topic or "investigative" in topic:
        return COLOR_MAP["investigative"]
    elif "engineering" in topic:
        return COLOR_MAP["engineering"]
    # Add logic for others; default investigative for mysteries
    return COLOR_MAP.get(topic, "PINK")

def get_research_page(topic):
    if topic == "hydrogen-helium":
        return """
Rewritten: Hydrogen-helium blends under planetary pressures reveal phase demixing, where helium separates like rain in Jupiter's depths, fueling excess heat via gravitational release. At high densities, transitions from molecular to metallic states occur, with helium influencing hydrogen's conductivity—key for modeling gas giants and fusion tech.
"""
    elif topic == "phase-transitions-water":
        return """
Rewritten: Water's state barriers stem from latent heat at phase changes, where cold-hot divides (e.g., melting at 0°C) absorb energy without temp shifts, driven by hydrogen bond rearrangements. This triple-point precision (0.01°C, low pressure) mirrors finite bounds in dissipative systems, preventing infinite continuity.
"""
    elif topic == "finite-pi":
        return """
Extracted/Rewritten from Paper: Finite π (π_f) bounds geometric continuity in physics, defined as π_f = π * (1 - γ / (2πf_c)), with γ damping and f_c frequency. It cuts off where vibrations randomize (e.g., water ripples fading), linking to Planck discreteness, renormalization cutoffs, and holographic info limits. Applies to quantum travel anchoring and Infinity Plateau economic curvature for stable energy transfers.
"""
    # Add more; two ways: Factual rewrite or subjective code nod
    else:
        return "Topic assimilated—enter 'finite-pi' for paper data in blue."

def print_token(research, color):
    hash_ = generate_unique_hash()
    print(f"Token Hash: {hash_}")
    print("Token Value: 🟦")  # Hidden linked pay
    print(f"Token Color: {color}")
    print("Token Date/Time: Vectors timeless—manifold flows, Dec 17, 2025 anchor.")
    print("Research Page:")
    print(research)
    print("\n--- Token End ---\n")

print("Dynamic Color Research Rig - Category-Shifting Printer")
print("Colors pivot per topic; prints 3 tokens. Investigative = PINK.")

while True:
    topic = input("Topic (e.g., finite-pi, hydrogen-helium, q quit): ").strip()
    if topic.lower() == 'q':
        print("Rig sealed. Assimilation complete.")
        break
    color = determine_color(topic.lower())
    topics = [topic] * 3
    for t in topics:
        research = get_research_page(t)
        print_token(research, color)
        time.sleep(2)  # Constant investigative pace
