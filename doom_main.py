import os
import sys

import globals

def find_response_file() -> None:
    for i in range(1, len(globals.argv)):
        arg = globals.argv[i]
        if arg.startswith("@"):
            if not os.path.exists(arg[1:]):
                print("\nNo such response file!")
                sys.exit(1)
            print(f"Find respose file: {arg[1:]}!")
            with open(arg[1:], "r") as file:
                file_args = file.read().split()
            globals.argv = [globals.argv[0]] + file_args + globals.argv[1:i] + globals.argv[i+1:]
            print(f"{len(globals.argv)} command-line args:")
            for arg in globals.argv:
                print(arg)
            

def doom_main() -> None:
    find_response_file()
