#!/usr/bin/env python3

import os
import sys

from controller.euchre_game import Euchre

__file_path__ = os.path.dirname(__file__)

def main(args):
    euchre = Euchre()
    euchre.run()

if __name__ == "__main__":
    main(sys.argv[1:])
