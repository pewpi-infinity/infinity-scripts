#!/usr/bin/env python3

import random
import sys

# ANSI colors for links
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  # Red, Green, Yellow, Blue, Magenta, Cyan
RESET = '\033[0m'

# Core Finite π paper text (from your transcription) + expansions from related physics (rewritten for depth, no repeats)
ARTICLE = """
The Finite π: A Bounded Geometric Constant of Physical Reality

Abstract: This paper unveils the finite π (π_f), a physically anchored twin to the infinite mathematical π. While π embodies flawless curvature in abstract Euclidean realms, physical systems falter under damping, quantization, and medium constraints on info flow. π_f marks the curvature terminus where waves lose coherence, vibrations halt, or bends fail to spread—unveiling a cosmic threshold where ideal π yields. Ties to Planck discreteness, renormalization tweaks, and damping factors forge this universal bound.

Introduction: π reigns in geometry and physics as circumference-to-diameter ratio, yet nature shuns its endless decimals. No oscillation or circle attains such purity amid atomic discreteness, energy leaks, and info caps. We posit all tangible setups heed π_f, ruling bounded observables. Mathematical π drifts eternally; π_f halts at medium breakdown.

Conceptual Framework: Infinite π (π_∞) thrives in lossless ideals, π_∞ = lim(r→∞) (C/D), untethered to contexts. Finite π (π_f) emerges in damped realities, energy/signal fade via γ (damping constant), yielding cutoff at thermal chaos. Formula: π_f = π * (1 - γ / (2πf_c)), f_c as resonance drive. Realized bends fall shy of π by damping slice.

Experimental Realization: Hydrodynamic tests excite vibes in water/oil, tracking decay. Coherent ripples to still mark π_f edge. Measure γ, f_c, ρ (density), η (viscosity), ε (dielectric). Plug in for constant curvature. Cross-media (water, oil, tar) convergence signals universal finite geometry cap, beyond medium quirks.

Relation to Theories: Planck cutoff at l_p discretizes spacetime, tiniest geometric slice mirroring ultimate π_f. Renormalization axes infinities via Λ cutoffs; π_f analogs curb oscillatory infinities. Bekenstein limits cap info per area, barring infinite geometry—π_f as measurable info leash.

Implications: Quantum jumps/tunnels need finite anchors; swap π for π_f in metrics to pin origins, dodge Planck blowups. π_f navigates reality.

Conclusion: Finite π redraws math-physics line, complementing π in dissipative quanta. Unifies vibes, spacetime, entropy under tolerance.

Future: Test decays; model curved spacetime analogs; apply to Infinity Plateau physics for economic curvature stability.

Expansion: Damping echoes in QFT renormalization, treating infinities by rescaling constants—bare to physical, finite results via cutoffs. Quantization in fields avoids eternal loops, akin to π_f bounding curves. Planck scale merges macro damping with micro discreteness, no infinite resolutions.
"""

# Sub-article dict (keys = potential link words, values = short rewritten research pages; expand dynamically)
SUB_ARTICLES = {
    "damping": """
Damping in Physics: Energy dissipation via friction/viscosity curbs oscillations, γ quantifying amplitude drop. Ties to renormalization: Infrared divergences handled by finite cutoffs, mirroring π_f's coherence end.
""",
    "quantization": """
Quantization Realms: Discrete energy packets (quanta) in QM/QFT; Planck constant h-bar (with π inside) sets steps. Charge quantization rationalizes ratios, bare to physical via Ward identities.
""",
    "renormalization": """
Renormalization Essentials: QFT technique shifts parameters to finite observables, ultraviolet cutoffs Λ remove divergences. Perturbative renormalizability demands finite bare tweaks for Standard Model viability.
""",
    "Planck": """
Planck Scale: l_p discretizes spacetime, gravity-QM meet. Finite π_f bridges this to macro damping, avoiding infinite geometries.
""",
    "curvature": """
Curvature Bounds: In GR, spacetime bends finite; renormalization in Yang-Mills quantizes gauges. π_f as navigation constant anchors quantum travel sans divergence.
""",
    "coherence": """
Wave Coherence: Phase sync decays via γ; infrared finite in photons. π_f cutoff ensures physical finiteness in oscillatory calcs.
""",
    "infinite": """
Infinite Avoidance: Theories shun divergences via causal perturbation, BRS invariance. Finite τ intervals bound time, stabilizing unstable particles.
""",
    "finite": """
Finite Constants: Physical vs bare—renormalized couplings change with interactions. Effective actions supersymmetric in dissipative dynamics.
""",
    "geometry": """
Geometric Limits: Bekenstein info caps per area; π irrational yet bounded in quanta. Abstract circles unbound, but physical quantized via h-bar π.
""",
    "reality": """
Physical Reality: Renormalized potentials finite post-cutoff; stochastic quantization links to supersymmetry. Multi-world branches avoid vacuum decay.
"""
    # Add more as needed for length
}

def colorize_and_link(text):
    words = text.split()
    output = []
    links = []
    link_num = 1
    for word in words:
        clean_word = word.strip('.,:;()[]{}')  # Strip punctuation for matching
        if clean_word.lower() in [k.lower() for k in SUB_ARTICLES] and random.random() < 0.5:  # 50% link chance
            color = random.choice(COLORS)
            output.append(f"{color}[{link_num}] {word}{RESET}")
            links.append((link_num, clean_word))
            link_num += 1
        else:
            output.append(word)
    return ' '.join(output), links

print("Finite π Color-Linked Research Article (Enter link numbers for sub-articles)")
colored_article, links = colorize_and_link(ARTICLE)
print(colored_article)

while True:
    try:
        choice = input("\nEnter link number (or q to quit): ").strip()
        if choice.lower() == 'q':
            print("Article vault sealed. Infinity chains on.")
            break
        num = int(choice)
        for ln, word in links:
            if ln == num:
                sub = SUB_ARTICLES.get(word, "Sub-article generating...")
                print(f"\nSub-Article for '{word}':{sub}")
                break
        else:
            print("Invalid link.")
    except ValueError:
        print("Number or q only.")
