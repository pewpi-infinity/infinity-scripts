#!/usr/bin/env python3

import math

# Example decay constants (placeholders from viscous damping lit)
MEDIA = {
    "Water": {"gamma": 0.01, "f_c": 5.0},   # Low damping, higher freq
    "Oil":   {"gamma": 0.15, "f_c": 2.0},
    "Tar":   {"gamma": 0.80, "f_c": 0.5}     # High damping
}

def compute_finite_pi(gamma, f_c):
    adjustment = gamma / (2 * math.pi * f_c)
    return math.pi * (1 - adjustment)

print("Finite π Across Media - Convergence Test")
print("Testing if π_f approaches universal value despite medium differences")

for medium, params in MEDIA.items():
    pi_f = compute_finite_pi(params["gamma"], params["f_c"])
    print(f"{medium:5} | γ={params['gamma']:.2f} | f_c={params['f_c']:.1f} | π_f = {pi_f:.10f}")

print("\nIf values converge in real experiments → universal finite π confirmed.")
print("Replace placeholders with your measured γ/f_c for token-grade research.")
