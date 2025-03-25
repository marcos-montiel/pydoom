import sys

import globals

from doom_main import doom_main

def main():
    globals.argv = sys.argv

    doom_main()    

if __name__ == "__main__":
    main()
