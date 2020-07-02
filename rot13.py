#!/usr/bin/env python3
"""Rot13 encode a string quickly, from the terminal.

Usage:
    rot13 <string>
    rot13 [-n=<n>] [--invert | --inverse] <string>
    rot13 --help

Options:
    -n=<n>                 Choose a different rotation [default: 13]
    -i --inverse --invert  Rotate backwards, rather than forwards [default: false].
    -h --help              Display this text.
    --version              Display the version.
"""

from internals.docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version="rot13.py 1.0")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    built = ""
    invert = arguments['--invert'] or arguments['--inverse']
    for letter in arguments['<string>']:
        if letter.isalpha():
            upper = letter.isupper()
            letter = letter.lower() 
            
            try:
                rotation = int(arguments['-n'])
            except ValueError:
                print(f"Sorry, I don't know how to read {arguments['-n']} as an integer.")
                exit(1)
            
            if invert:
                rotation = -rotation

            rotated = alphabet.index(letter) + rotation
            rotated %= len(alphabet)
            rotated = alphabet[rotated]

            if upper:
                rotated = rotated.upper()
        else:
            rotated = letter
        built += rotated

    print(built)
