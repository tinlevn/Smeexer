import math
from random import randint

my_file = open("bip0039.txt", "r")
content = my_file.read()

"""
Dicts and sets have an O(1)
time complexity for membership checking because 
entries are accessed via a hashing algorithm
stackoverflow.com/questions/60568734/what-is-the-time-complexity-of-checking-membership-in-tuples
"""
# List is for indexing and drawing out data
mnemonic_list = content.split()
# Set is for fast membership searching
mnemonic_set = set(mnemonic_list)


def seed_validation(seed_list):
    if len(seed_list) not in (12, 18, 24):
        print("Please enter a valid seed-phrase set")
        return False
    for i in seed_list:
        if i not in mnemonic_set:
            return False
    return True


def print_facts():
    print("Can someone guess my seed? There are 2^256 different possible 24-word mnemonic seeds. "
          "For comparison, the number of atoms on Earth is estimated to be around 2^166.\n "
          "Just let that sink in for a second. "
          "The chance of someone else being able to guess your seed is astronomically small, to say the least.")


def stepping_stone_mix(seed_list):
    set_length = len(seed_list)
    stoneMix = seed_list.copy()

    # Swapping elements
    for i in range(0, set_length, 2):
        stoneMix[i], stoneMix[i + 1] = stoneMix[i + 1], stoneMix[i]
    # One last swap
    stoneMix[-1], stoneMix[0] = stoneMix[0], stoneMix[-1]

    return stoneMix


def odd_even(seed_list):
    set_length = len(seed_list)
    oddEvenMix = seed_list.copy()

    # Swap even positions
    for i in range(2, set_length, 4):
        if i % 2 == 0:
            oddEvenMix[i], oddEvenMix[i - 2] = oddEvenMix[i - 2], oddEvenMix[i]
    # Swap odd positions
    for i in range(3, set_length, 4):
        if i % 2 != 0:
            oddEvenMix[i], oddEvenMix[i - 2] = oddEvenMix[i - 2], oddEvenMix[i]

    return oddEvenMix


# Method to add another set of phrase, usually a 12-word set
def obfuscate(seed_list):
    newRandomSeedPhrase = []

    temp_set = set(seed_list)
    # seed(1) if need to keep random state
    i = 0
    while i < 12:
        value = randint(0, 2048)
        if mnemonic_list[value] not in temp_set:
            newRandomSeedPhrase.append(mnemonic_list[value])
            i += 1
    return seed_list + newRandomSeedPhrase


# Random seed generator function
def generate_seeds(seed_list):
    random_phrase = []
    temp_set = set(seed_list)
    # seed(1)
    i = 0
    while i < 12:
        value = randint(0, 2048)
        if mnemonic_list[value] not in temp_set:
            random_phrase.append(mnemonic_list[value])
            i += 1
    return random_phrase


def fivio_mix(long_seed, side):
    true_seed_1 = long_seed[0:5]
    true_seed_2 = long_seed[5:10]
    true_seed_3 = long_seed[10:12]

    faux_seed_1 = long_seed[12:17]
    faux_seed_2 = long_seed[17:22]
    faux_seed_3 = long_seed[22:24]
    if side in {"l", "L", "left", "LEFT", "Left"}:
        return true_seed_1 + faux_seed_1 + \
               true_seed_2 + faux_seed_2 + \
               true_seed_3 + faux_seed_3
    elif side in {"r", "R", "right", "RIGHT", "Right"}:
        return faux_seed_1 + true_seed_1 + \
               faux_seed_2 + true_seed_2 + \
               faux_seed_3 + true_seed_3
    else:
        print("Please enter a valid side operation:\n"
              "Hint:l, L, left, LEFT, Left for left shift\n"
              "r,R,right,RIGHT,Right for right shift")


def odd_one_out_mix(long_seed, side):
    true_seed_1 = long_seed[0:11]
    true_seed_2 = [long_seed[11]]

    faux_seed_1 = long_seed[13:24]
    faux_seed_2 = [long_seed[12]]

    if side in {"l", "L", "left", "LEFT", "Left"}:
        return true_seed_1 + faux_seed_2 + \
               true_seed_2 + faux_seed_1
    elif side in {"r", "R", "right", "RIGHT", "Right"}:
        return faux_seed_1 + true_seed_2 + \
               faux_seed_2 + true_seed_1
    else:
        print("Please enter a valid side operation:\n"
              "Hint:l, L, left, LEFT, Left for left shift\n"
              "r,R,right,RIGHT,Right for right shift")


def onion_ring(seed_list, layer):
    set_length = len(seed_list)
    onion = seed_list.copy()

    # Only need to iterate half the length to
    # swap all elements
    ring_size = set_length // 2

    if layer in {"out", "OUT", "o", "O"}:
        start = 0
    elif layer in {"in", "IN", "i", "I"}:
        start = 1
    else:
        print("Please choose in(IN,i,I) or\
              out(OUT,o,O)")
    # Swap loop
    for i in range(start, ring_size, 2):
        onion[i], onion[-i - 1] = onion[-i - 1], onion[i]
    return onion


def new_input():
    print("Enter a new 12-word seed phrase with spaces in between: ")
    user_seed_input = input().split()
    validity = seed_validation(user_seed_input)
    if validity:
        print("Valid key set")
        return user_seed_input
    else:
        print("Not valid key set, please try again")
        new_input()
