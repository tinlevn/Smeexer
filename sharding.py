"""
Sharding implementation
Smeexer
"""
from mixers import generate_seeds


def about_sharding():
    print("""
    === About Seed Sharding ===
    According to Ben Mezrich’s biographical novel "Bitcoin Billionaires",
    which chronicles the Winklevoss twins' story:

    The twins split their private key into 3 shards - referred to as "alpha", "beta", and "charlie".
    These were stored in fireproof/waterproof envelopes and stashed in unassuming banks.
    To ensure a natural disaster does not wipe out one or more of the shards, they duplicated
    the process 4 times across 4 separate time zones for redundancy.

    Sharding allows you to split a seed phrase into multiple pieces such that individual
    shards are incomplete alone and padded with decoy BIP-0039 words for obfuscation.
    """)


def chunks(seed_list, chunk_size):
    """Yield successive n-sized chunks from list."""
    for i in range(0, len(seed_list), chunk_size):
        yield seed_list[i:i + chunk_size]


def shard(seed_list):
    """Simple sharding: splits seed phrase into chunks and pads each with random BIP-0039 words."""
    chunk_sz = 4 if len(seed_list) == 12 else 6
    dummy_count = 9 if len(seed_list) == 12 else 6
    shards = [list(segment) for segment in chunks(seed_list, chunk_sz)]
    for s in shards:
        s.extend(generate_seeds(s)[:dummy_count])
    return shards


def staircase_shard(seed_list):
    """Staircase sharding: splits true seed into chunks and combines them in staircase patterns with dummy words."""
    chunk_sz = 4 if len(seed_list) == 12 else 6
    true_chunks = [list(segment) for segment in chunks(seed_list, chunk_sz)]
    dummy_seeds = generate_seeds(seed_list)
    dummy_chunks = [list(segment) for segment in chunks(dummy_seeds, chunk_sz)]

    staircase_shards = []
    num_chunks = len(true_chunks)
    for i in range(num_chunks):
        shard_item = []
        for j in range(num_chunks):
            if j == i:
                shard_item.extend(true_chunks[j])
            else:
                shard_item.extend(dummy_chunks[j])
        staircase_shards.append(shard_item)
    return staircase_shards


def compass_shard(seed_list):
    """Compass sharding: distributes 4 seed chunks to North, South, East, West with dummy padding."""
    chunk_sz = max(1, len(seed_list) // 4)
    true_chunks = [list(segment) for segment in chunks(seed_list, chunk_sz)]
    directions = ["North", "South", "East", "West"]
    compass_dict = {}
    for idx, direction in enumerate(directions):
        if idx < len(true_chunks):
            dummy_pad = generate_seeds(true_chunks[idx])[:8]
            compass_dict[direction] = true_chunks[idx] + dummy_pad
    return compass_dict


def seesaw_shard(seed_list):
    """Seesaw sharding: alternates true seed chunks between Shard A and Shard B."""
    half = len(seed_list) // 2
    true_1, true_2 = seed_list[:half], seed_list[half:]
    dummy_1 = generate_seeds(true_1)
    dummy_2 = generate_seeds(true_2)

    shard_a = true_1 + dummy_2
    shard_b = dummy_1 + true_2
    return {"Shard A (Left True / Right Dummy)": shard_a, "Shard B (Left Dummy / Right True)": shard_b}


def box_shard(seed_list):
    """Box sharding: arranges seed into a 2x2 grid matrix with interspersed decoy chunks."""
    chunk_sz = max(1, len(seed_list) // 4)
    true_chunks = [list(segment) for segment in chunks(seed_list, chunk_sz)]
    dummies = [generate_seeds(c)[:chunk_sz] for c in true_chunks]

    box = [
        [true_chunks[0] if len(true_chunks) > 0 else [], dummies[1] if len(dummies) > 1 else []],
        [dummies[2] if len(dummies) > 2 else [], true_chunks[3] if len(true_chunks) > 3 else []]
    ]
    return box
