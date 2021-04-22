"""
Sharding implementation
04/02/2021
"""
from mixers import generate_seeds


def about_sharding():
    print(" According to Ben Mezrich’s biographical novel “Bitcoin Millionaires\""
          , "which chronicles the Winklevoss twins story\n"
          , "The twins split their private key into 3 shards - referred to as “alpha”, “beta”, and “Charlie”."
          , "Which were then stored in fireproof/waterproof envelopes, and stashed in unassuming banks.\n"
          , "To ensure that a natural disaster does not wipe-out one/more of the ‘shards’,"
          , "they duplicated the process 4 times, in 4 separate time zones for redundancy.\n"
          , "To all you hodl’ers, take lesson from 2 of the richest BTC investors in the world. PROTECT YOUR KEYS!\n"
          , "Source: reddit.com/r/CryptoCurrency/comments/m4gruo/til_the_winklevoss_private_keys_are_stored_on_3/ ")


#Sharding function for splitting seed phrase
def shard(seed_list):
    if len(seed_list) == 12:
        x, y, z = seed_list[0:4], seed_list[4:8], seed_list[8:12]
        d = [x, y, z]
        print(d)
    elif len(seed_list) == 24:
        w, x, y, z = seed_list[0:6], seed_list[6:12], seed_list[12:18], seed_list[18:24]
        d = [w, x, y, z]
        print(d)
    if len(seed_list) == 12:
        for i in d:
            i += generate_seeds(i)[0:9]
    elif len(seed_list) == 24:
        for i in d:
            i += generate_seeds(i)[0:6]
    return d

# def coming_soon():
