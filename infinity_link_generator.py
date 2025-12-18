#!/usr/bin/env python3
import random
import time
from itertools import combinations, permutations

# --- Configuration & Styling ---
# ANSI Color Codes
RESET = "\033[0m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
PINK = "\033[95m"
RED = "\033[91m"
GREEN = "\033[92m"

# The Core Vocabulary Source (Simulating a large dictionary)
CORE_VOCABULARY = set([
    "quanta", "delta", "triangulator", "finite", "infinite", "coherence", "entropy",
    "spacetime", "vibration", "geometric", "constant", "physical", "reality", "bounded",
    "quantization", "damping", "renormalization", "Bekenstein", "Planck", "Plateau",
    "economic", "curvature", "universal", "convergence", "dissipative", "quantum",
    "anchor", "origins", "system", "theory", "model", "test", "variable", "field",
    "equation", "abstract", "glory", "complicated", "token", "printer", "research"
] + [str(i) for i in range(100)]) # Add numbers for complexity

# --- Functions ---

def generate_dynamic_links(current_term, num_links=8):
    """
    Generates a dynamic set of 'Term Jumps' from the CORE_VOCABULARY.
    Uses combinations/permutations to simulate 'billions of terms in tandem rides'.
    """
    links = {}
    available_words = list(CORE_VOCABULARY - set(current_term.split('-')))

    random.shuffle(available_words)
    
    # We generate links as 2-word, 3-word, or 4-word 'tandem rides'
    for i in range(num_links):
        combo_size = random.choice([2, 3, 4])
        if len(available_words) < combo_size:
            break
            
        tandem_words = random.sample(available_words, combo_size)
        
        jump_key = random.choice("⭐⚡🔗🌌🔬💡🧬🚀🌀📜") + str(i) 
        
        term = "-".join(tandem_words).lower()
        links[jump_key] = term
        
    return links

def generate_metadata(term):
    """Generates dynamic metadata for the given term."""
    token = "".join(random.choices("🧱⭐🔑", k=3))
    color = random.choice([BLUE, CYAN, YELLOW, PINK, RED, GREEN])
    token_value = random.choice(["🟦", "🟩", "🟪", "🟧"])
    
    current_time_str = time.strftime("%Y-%m-%d %H:%M:%S")

    return f"""
{BLUE}Token {token}{RESET}
{CYAN}Token Value: {token_value}{RESET}
{PINK}Token Color: {random.choice(["BLUE", "CYAN", "YELLOW", "PINK", "RED", "GREEN"])}{RESET}
{YELLOW}Token Date/Time: {current_time_str} - quanta field state ∆ {term}{RESET}

{RED}Research Title: The {term.title()}: A Hyper-Dimensional Contextual Nexus{RESET}
"""

def print_research_summary(term):
    """Generates a dynamic, abstract summary."""
    summary = f"""
Summary (Contextual Link to {term.upper()}):
• {term.title()} explores the ultimate bounds of information.
• It links Planck scale discretizations with Bekenstein entropy caps.
• The current term is a key anchor point for the Infinity Plateau valuation model.
• Hypothesized to govern quantum tunneling and macro-scale curvature flux.
"""
    print(summary)

def print_special(term):
    """
    Prints the 'deep' dive for a selected term. (Fixes original NameError)
    """
    col = random.choice([BLUE, CYAN, YELLOW, PINK, RED, GREEN])
    hash_id = term.upper().replace('-', '_') 
    
    print("-" * 50)
    print(f"\n{col}Special Token {hash_id} - Entering Deep Context for: {YELLOW}{term}{RESET} ")
    print(f"| Term Type: Tandem Ride ({len(term.split('-'))} terms) | Status: RECALCULATING... |")
    print("-" * 50)

def main_loop(starting_term):
    """Main loop for the nonstop, infinity-style operation."""
    current_term = starting_term
    
    while True:
        try:
            # 1. Generate Metadata and Summary
            print("\n" * 2 + "=" * 80)
            print(f"~/infinity-scripts $ {CYAN}./infinity_link_generator.py{RESET}")
            print(f"Colored Infinity-Loop Token Generator - Exploring: {YELLOW}{current_term.upper()}{RESET}")
            print("=" * 80)
            
            print(generate_metadata(current_term))
            print_research_summary(current_term)

            # 2. Generate and Display Term Jumps
            current_links = generate_dynamic_links(current_term, num_links=8) 
            print("\n--- Term Jumps (Select a 'Tandem Ride' for Deep Dive) ---")
            
            link_display = []
            keys = list(current_links.keys())
            
            for key in keys:
                term = current_links[key]
                link_display.append(f"{RED}{key}{RESET} {term}")
            
            # Print the links in a readable 2-column format
            for i in range(0, len(link_display), 2):
                line = f"| {link_display[i]:<35} |"
                if i + 1 < len(link_display):
                    line += f" {link_display[i+1]:<35} |"
                else:
                    line += f" {'':<35} |"
                print(line)

            # 3. User Input and Navigation
            print("\n" + "~" * 80)
            
            example_key = random.choice(keys) if keys else "q"
            jump_input = input(f"Enter Link Key (e.g., {RED}{example_key}{RESET}, or {RED}q{RESET} to quit): ").strip()
            print("~" * 80)
            
            if jump_input.lower() == 'q':
                print(f"\n{GREEN}Exiting Infinity Loop. Last Term Explored: {current_term}{RESET}\n")
                break
            
            if jump_input in current_links:
                print_special(current_links[jump_input])
                current_term = current_links[jump_input]
                
            else:
                print(f"{RED}Invalid Link Key: {jump_input}. Re-initializing research loop.{RESET}")

        except KeyboardInterrupt:
            print(f"\n{GREEN}Caught interrupt. Exiting Infinity Loop. Last Term Explored: {current_term}{RESET}\n")
            break
        except Exception as e:
            print(f"{RED}An unexpected error occurred in the loop: {e}{RESET}")
            time.sleep(2)
            

# --- Script Execution ---
if __name__ == "__main__":
    print(f"\n{GREEN}Welcome to the Infinity Research Generator!{RESET}")
    print("This script runs non-stop, generating billions of pseudo-research links.")
    
    initial_topic = input(f"Enter the starting research concept (e.g., finite-pi): ").strip().lower()
    
    if not initial_topic:
        initial_topic = "finite-pi-token" # Default starting term
        
    main_loop(initial_topic)
