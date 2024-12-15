#!/usr/bin/env python3
"""
Author : maxiaofei <maxiaofei@localhost>
Date   : 2024-12-14
Purpose: Lookup tables
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        help='Letter(s)',
                        metavar='letter',
                        nargs='+',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')

    print(lookup)

# --------------------------------------------------
if __name__ == '__main__':
    main()
