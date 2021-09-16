"""
Tin Thanh Le
Junior Developer
Smeexer 0.1
This program will mix your
cryptocurrency wallet seed phrases,
adding another layer of security for
your offline (and even potentially online) key storage
"""

from menu import smeexer_menu
from mixers import new_input

if __name__ == '__main__':
    print("!------------WELCOME TO SMEEXER 0.1------------!")
    curr_list = new_input()

    # input choice for sharding or mixing
    smeexer_menu(curr_list)
