#!/usr/bin/env python3

import os
import sys

from controller.euchre_game import Euchre

__file_path__ = os.path.dirname(__file__)

def main(args):
    game = Euchre(True if len(args) > 0 and args[0].lower() == "true" else False)
    game.run()

if __name__ == "__main__":
    main(sys.argv[1:])
