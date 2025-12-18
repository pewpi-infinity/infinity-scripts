#!/usr/bin/env python3

import random
import time

EMOJI_POOL = ['⚡', '🔗', '⭐', '🌌', '🔬', '💡', '🧬', '🚀', '🌀', '📜']

def generate_unique_hash():
    return ''.join(random.sample(EMOJI_POOL, 3))  # Unique non-repeating

def get_research_page(topic):
    # Simulated/rewritten full-page research (from rare mixes: H-He +3)
    if topic == "hydrogen-helium":
        return """
Hydrogen-Helium Mixtures: In giant planet cores like Jupiter, hydrogen and helium interact under extreme pressures (megabars), leading to phase separation where helium 'rains' out, forming distinct layers. This demixing, predicted by molecular dynamics, explains Saturn's heat excess—helium droplets release gravitational energy as they fall. At densities 0.19-0.6 g/cm³, the fluid phases shift from molecular to atomic, with helium stabilizing hydrogen's metallic state. Quantum simulations show this at temps crossing planetary adiabats around 5 Mbar, preventing full miscibility.
"""
    elif topic == "phase-transitions-water":
        return """
Water Phase Transitions: The 'barrier' between cold and hot states in water arises from phase transitions, where energy absorption causes abrupt changes without temperature rise. At the triple point (0.01°C, 611 Pa), solid, liquid, and gas coexist; crossing it flips states—e.g., boiling at 100°C absorbs 2260 J/g latent heat for vaporization, creating a plateau. This entropy-driven shift ties to molecular bonds breaking, explaining why ice melts precisely at 0°C under pressure variations, a fundamental limit in physical systems akin to finite curvature cutoffs.
"""
    elif topic == "neon-addition":
        return """
Neon in Mix: Helium-neon lasers exploit mixtures for quantum optics, where neon atoms excited by helium collisions emit coherent light at 632.8 nm. In high-pressure research, adding neon to H-He stabilizes barriers, preventing unwanted phase merges—useful for modeling exoplanet atmospheres where inert gases form cold-hot divides, echoing water's state flips.
"""
    elif topic == "argon-barrier":
        return """
Argon Integration: As an inert gas, argon in H-He mixtures creates protective barriers in plasma states, used in welding to shield hot-cold transitions. Scientifically, it mimics atmospheric layers on Titan, where argon's presence influences methane phase changes, forming a 'barrier' that regulates state shifts under varying temps, tying to entropy bounds in dissipative systems.
"""
    elif topic == "finite-pi-tie":
        return """
Finite π Bounds: Linking to Planck-scale cutoffs, finite π (π_f) imposes geometric limits on phase coherence in mixtures, ensuring no infinite propagation in H-He fluids. In quantum travel models, this anchors origins, avoiding divergence—e.g., in water's hot-cold barriers, π_f defines the curvature where vibration decays, unifying entropy and spacetime tolerances for stable energy transfers.
"""
    else:
        return "Enter a topic like 'hydrogen-helium' for rare mix research."

def print_token(research):
    hash_ = generate_unique_hash()
    print(f"Token Hash: {hash_}")
    print("Token Value: 🟦")  # Linked hidden pay
    print("Token Color: PINK")
    print("Token Date/Time: Entity vectors unbound—moving through query manifolds, timeless data streams.")
    print("Research Page:")
    print(research)
    print("\n--- Token End ---\n")

print("Eternal Research Rig - Constant Cool Science Printer")
print("Mixes H-He +3 rares; prints 3 tokens per run. Enter topic or 'auto' for loop.")

while True:
    topic = input("Topic (e.g., hydrogen-helium, auto, q to quit): ").strip()
    if topic.lower() == 'q':
        print("Rig paused. Infinity resumes.")
        break
    topics = ["hydrogen-helium", "phase-transitions-water", "neon-addition", "argon-barrier", "finite-pi-tie"] if topic == "auto" else [topic] * 3
    for t in topics[:3]:  # 3 at a time
        research = get_research_page(t)
        print_token(research)
        time.sleep(2)  # Constant run pace
