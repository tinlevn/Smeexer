from mixers import *
from sharding import *
import sys


def smeexer_menu(seed_list):
    while True:
        print("\n" + "=" * 45)
        print("          SMEEXER MIXER MENU          ")
        print("=" * 45)
        print("1: Simple Fact")
        print("2: Stepping stone mix")
        print("3: Odd even mix")
        print("4: Fivio mix")
        print("5: Odd one out mix")
        print("6: Onion ring mix")
        print("7: Simple obfuscation")
        print("8: Seed Sharding options")
        print("9: Enter new seed phrase")
        print("0: Exit")
        choice = input("Select an option: ").strip().lower()

        if choice == '1':
            print_facts()
        elif choice == '2':
            print("\nResult of Stepping Stone Mix:")
            print(" ".join(stepping_stone_mix(seed_list)))
        elif choice == '3':
            print("\nResult of Odd-Even Mix:")
            print(" ".join(odd_even(seed_list)))
        elif choice == '4':
            temp = obfuscate(seed_list)
            side = input("Enter shift direction (l/left or r/right) [default: left]: ").strip()
            print("\nResult of Fivio Mix:")
            print(" ".join(fivio_mix(temp, side)))
        elif choice == '5':
            temp = obfuscate(seed_list)
            side = input("Enter shift direction (l/left or r/right) [default: left]: ").strip()
            print("\nResult of Odd-One-Out Mix:")
            print(" ".join(odd_one_out_mix(temp, side)))
        elif choice == '6':
            layer = input("Enter starting layer (i/in for inner swap, o/out for outer swap) [default: outer]: ").strip()
            print("\nResult of Onion Ring Mix:")
            print(" ".join(onion_ring(seed_list, layer)))
        elif choice == '7':
            print("\nResult of Obfuscation (adds 12 BIP-0039 decoy words):")
            print(" ".join(obfuscate(seed_list)))
        elif choice == '8':
            sharding_menu(seed_list)
        elif choice == '9':
            seed_list = new_input()
        elif choice == '0':
            sys.exit("Thank you for using Smeexer!")
        else:
            print("Invalid selection. Please select an option from the menu.")


def sharding_menu(seed_list):
    while True:
        print("\n" + "-" * 45)
        print("          SHARDING OPTIONS          ")
        print("-" * 45)
        print("1: What is sharding?")
        print("2: Simple sharding")
        print("3: Staircase sharding")
        print("4: Compass sharding")
        print("5: Seesaw sharding")
        print("6: Box sharding")
        print("7: Return to Main Mixer Menu")
        print("0: Exit")
        choice = input("Select a sharding option: ").strip().lower()

        if choice == '1':
            about_sharding()
        elif choice == '2':
            shards = shard(seed_list)
            print("\n=== Simple Shards ===")
            for idx, s in enumerate(shards, 1):
                print(f"Shard {idx}: {' '.join(s)}")
        elif choice == '3':
            shards = staircase_shard(seed_list)
            print("\n=== Staircase Shards ===")
            for idx, s in enumerate(shards, 1):
                print(f"Shard {idx}: {' '.join(s)}")
        elif choice == '4':
            compass = compass_shard(seed_list)
            print("\n=== Compass Shards ===")
            for direction, s in compass.items():
                print(f"[{direction}]: {' '.join(s)}")
        elif choice == '5':
            seesaw = seesaw_shard(seed_list)
            print("\n=== Seesaw Shards ===")
            for name, s in seesaw.items():
                print(f"[{name}]: {' '.join(s)}")
        elif choice == '6':
            box = box_shard(seed_list)
            print("\n=== Box Grid Shards ===")
            for r_idx, row in enumerate(box, 1):
                for c_idx, cell in enumerate(row, 1):
                    print(f"Grid Cell ({r_idx},{c_idx}): {' '.join(cell)}")
        elif choice == '7':
            break
        elif choice == '0':
            sys.exit("Thank you for using Smeexer!")
        else:
            print("Invalid option. Please select an option from the menu.")
