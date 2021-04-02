"""
Tin Thanh Le
Junior Developer
Smeeixer 0.1
This program will mix your
cryptocurrency wallet seed phrases,
adding another layer of security for
your offline key storage
"""


from mixers import *

if __name__ == '__main__':
    print("Please enter your 12-word seed phrase with spaces in between: ")
    user_seed_input = input().split()
    validity = seed_validation(user_seed_input)
    if validity:
        print("Valid key set")
    else:
        print("Not valid key set")
    smeexer_menu(user_seed_input)
