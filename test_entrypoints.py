#!/usr/bin/env python

import os
import sys

def main():

    # Make modules in subdirectory importable
    sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Subliminal'))
    import subliminal
    subliminal.print_entry_points()


# This is the most important line: it calls the main function if this program is
# called directly.
if __name__ == "__main__":
    main()

