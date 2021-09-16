from mixers import *
from sharding import *
import sys


def smeexer_menu(seed_list):
    choice = input("""Mixer Menu
    1: Simple Fact
    2: Stepping stone mix your phrase
    3: Odd even mix 
    4: Fivio mix
    5: Odd one out mix
    6: Onion Mix
    7: Simple obfuscation (for 12-seed phrase only)
    8: New seed phrase
    9: Exit
Select one: """)
    while int(choice) in range(10):
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
            side = input("Please enter starting layer\n"
                         "Options:i,I,in,IN for inner-layer swap\n"
                         "o,O,out,OUT for outer-layer swap: "
                         )
            print(onion_ring(seed_list, side))
            smeexer_menu(seed_list)
        elif choice == '7':
            print(obfuscate(seed_list))
            smeexer_menu(seed_list)
        elif choice == '8':
            seed_list = new_input()
            smeexer_menu(seed_list)
        elif choice == '9':
            sys.exit("Thank you for using Smeexer")
        else:
            print("Please select a valid option")
            smeexer_menu(seed_list)


def sharding_menu(seed_list):
    print("------------Sharding Options------------")
    choice = input("""
        1: What is sharding?
        2: Simple sharding
        3: Shard with obfuscation
            a-Staircase sharding (up or down) 
            b-Seesaw sharding 
            c-Compass shard
            d-Box sharding
        4: Exit
        Select one: """)
    while int(choice) in range(5):
        if choice == '1':
            about_sharding()
            sharding_menu(seed_list)
        elif choice == '2':
            temp = shard(seed_list)
            for segment in temp:
                print(segment)
            temp.clear()
            sharding_menu(seed_list)
        elif choice == '3':
            shard_choice = input("Choose one of the following by entering the representing letter (a,b,c, or d): ")

            sharding_menu(seed_list)
        elif choice == '4':
            sys.exit("Thank you for using Smeexer")
        else:
            print("Please select a valid option")
            smeexer_menu(seed_list)
