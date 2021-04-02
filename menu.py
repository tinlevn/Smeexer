from mixers import *
import sys


def smeexer_menu(seed_list):
    print("------------Welcome to Smeexer 0.1------------")
    choice = input("""
    1: Fun facts (only 2 for now)
    2: Stepping stone mix your phrase
    3: Odd even mix 
    4: Fivio mix
    5: Odd one out mix
    6: Simple obfuscation (for 12-seed phrase only)
    7: New seed phrase
    8: Exit
    Select one: """)
    while choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '1':
            print_facts()
            smeexer_menu(seed_list)
        elif choice == '2':
            print(stepping_stone_mix(seed_list))
            smeexer_menu(seed_list)
        elif choice == '3':
            print(odd_even(seed_list))
            smeexer_menu(seed_list)
        elif choice == '4':
            temp = obfuscate(seed_list)
            side = input("Please enter shift direction\n"
                         "Hint:l, L, left, LEFT, Left for left shift\n"
                         "r,R,right,RIGHT,Right for right shift: ")
            print(fivio_mix(temp, side))
            smeexer_menu(seed_list)
        elif choice == '5':
            temp = obfuscate(seed_list)
            side = input("Please enter shift direction\n"
                         "Hint:l, L, left, LEFT, Left for left shift\n"
                         "r,R,right,RIGHT,Right for right shift: "
                         )
            print(odd_one_out_mix(temp, side))
            smeexer_menu(seed_list)
        elif choice == '6':
            print(obfuscate(seed_list))
            smeexer_menu(seed_list)
        elif choice == '7':
            seed_list = new_input()
            smeexer_menu(seed_list)
        elif choice == '8':
            sys.exit()
        else:
            print("Please select a valid option")
            smeexer_menu(seed_list)