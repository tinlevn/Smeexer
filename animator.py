import time
import sys


def animate_step(title, items, description="", delay=0.8):
    """Utility to print a step in the visual animation."""
    print("\n" + "-" * 50)
    print(f"  [STEP] {title}")
    if description:
        print(f"  Note: {description}")
    print("-" * 50)
    if isinstance(items, list):
        formatted = " | ".join([f"({i+1}) {w}" for i, w in enumerate(items)])
        print(f"  Seed Phrase State:\n  [{formatted}]")
    elif isinstance(items, dict):
        for k, v in items.items():
            formatted = " ".join(v) if isinstance(v, list) else str(v)
            print(f"  {k}: [ {formatted} ]")
    elif isinstance(items, str):
        print(f"  {items}")
    time.sleep(delay)


def animate_stepping_stone(seed_list, delay=0.6):
    print("\n" + "=" * 50)
    print("      ANIMATION: STEPPING-STONE MECHANISM      ")
    print("=" * 50)
    animate_step("Initial Input Seed Phrase", seed_list, "Original order of words.", delay)

    state = seed_list.copy()
    animate_step("Step 1: Swapping Adjacent Pairs", state, "Pairs (1,2), (3,4), (5,6) ... swap positions.", delay)
    for i in range(0, len(state) - 1, 2):
        state[i], state[i + 1] = state[i + 1], state[i]
        animate_step(f"Adjacent Swap Pair {i//2 + 1}: index {i+1} <-> {i+2}", state, f"Swapped '{state[i+1]}' and '{state[i]}'", delay)

    animate_step("Step 2: Final Anchor Swap", state, f"First word '{state[0]}' and Last word '{state[-1]}' swap.", delay)
    state[0], state[-1] = state[-1], state[0]
    animate_step("Final Stepping-Stone Result", state, "Mixing complete! First and last elements anchored across the phrase.", delay)
    return state


def animate_odd_even(seed_list, delay=0.6):
    print("\n" + "=" * 50)
    print("        ANIMATION: ODD-EVEN MECHANISM        ")
    print("=" * 50)
    animate_step("Initial Input Seed Phrase", seed_list, "Original seed phrase before Odd-Even mix.", delay)

    state = seed_list.copy()
    animate_step("Phase 1: Swapping Even Positions", state, "Positions 2, 4, 6... swap with previous even indices.", delay)
    for i in range(2, len(state), 4):
        state[i], state[i - 2] = state[i - 2], state[i]
        animate_step(f"Even-Index Swap: index {i-1} <-> {i+1}", state, f"Swapped positions {i-1} and {i+1}", delay)

    animate_step("Phase 2: Swapping Odd Positions", state, "Positions 3, 5, 7... swap with previous odd indices.", delay)
    for i in range(3, len(state), 4):
        state[i], state[i - 2] = state[i - 2], state[i]
        animate_step(f"Odd-Index Swap: index {i-1} <-> {i+1}", state, f"Swapped positions {i-1} and {i+1}", delay)

    animate_step("Final Odd-Even Result", state, "Odd-Even interleaved mix complete!", delay)
    return state


def animate_obfuscation(seed_list, dummy_words, delay=0.6):
    print("\n" + "=" * 50)
    print("         ANIMATION: OBFUSCATION MECHANISM         ")
    print("=" * 50)
    animate_step("Initial Authentic Seed Set (12 Words)", seed_list, "Your actual secret seed phrase.", delay)
    animate_step("Generated Decoy Set (12 BIP-0039 Words)", dummy_words, "Random valid BIP-0039 words from official list.", delay)

    combined = seed_list + dummy_words
    animate_step("Final Obfuscated Phrase (24 Words)", combined, "An observer cannot tell whether 12 or 24 words are genuine!", delay)
    return combined


def animate_fivio(seed_list, dummy_words, side="left", delay=0.6):
    print("\n" + "=" * 50)
    print("          ANIMATION: FIVIO MIX MECHANISM          ")
    print("=" * 50)
    animate_step("Authentic 12 Words", seed_list, "Split into 3 segments: [5 words], [5 words], [2 words]", delay)
    animate_step("Decoy 12 Words", dummy_words, "Split into 3 segments: [5 words], [5 words], [2 words]", delay)

    t1, t2, t3 = seed_list[0:5], seed_list[5:10], seed_list[10:12]
    d1, d2, d3 = dummy_words[0:5], dummy_words[5:10], dummy_words[10:12]

    if str(side).lower().startswith("l"):
        res = t1 + d1 + t2 + d2 + t3 + d3
        animate_step("Interleaving (Left Shift)", res, "Pattern: [True 5] -> [Decoy 5] -> [True 5] -> [Decoy 5] -> [True 2] -> [Decoy 2]", delay)
    else:
        res = d1 + t1 + d2 + t2 + d3 + t3
        animate_step("Interleaving (Right Shift)", res, "Pattern: [Decoy 5] -> [True 5] -> [Decoy 5] -> [True 5] -> [Decoy 2] -> [True 2]", delay)

    return res


def animate_onion_ring(seed_list, layer="outer", delay=0.6):
    print("\n" + "=" * 50)
    print("       ANIMATION: ONION RING MECHANISM       ")
    print("=" * 50)
    animate_step("Initial Input Seed Phrase", seed_list, "Concentric ring layers from outside to inside.", delay)

    state = seed_list.copy()
    start = 1 if str(layer).lower().startswith("i") else 0
    ring_size = len(state) // 2

    for i in range(start, ring_size, 2):
        opp = len(state) - i - 1
        animate_step(f"Ring Layer Swap: index {i+1} <-> index {opp+1}", state, f"Swapping outermost/innermost ring elements '{state[i]}' <-> '{state[opp]}'", delay)
        state[i], state[opp] = state[opp], state[i]

    animate_step("Final Onion Ring Result", state, "Layered symmetric swap complete!", delay)
    return state


def animate_sharding(seed_list, delay=0.6):
    print("\n" + "=" * 50)
    print("         ANIMATION: SEED SHARDING MECHANISM         ")
    print("=" * 50)
    animate_step("Original Seed Phrase", seed_list, f"Total words: {len(seed_list)}", delay)

    chunk_size = 4 if len(seed_list) == 12 else 6
    chunks = [seed_list[i:i + chunk_size] for i in range(0, len(seed_list), chunk_size)]

    for idx, c in enumerate(chunks, 1):
        animate_step(f"Chunk {idx} Extracted", c, f"Core shard piece #{idx}", delay)

    print("\nAdding decoy padding words to each shard so each looks complete...")
    time.sleep(delay)
    return chunks
