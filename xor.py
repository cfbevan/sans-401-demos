#!/usr/bin/env python3

"""A program to demo xor as a crypto technique."""

import argparse
from random import randint


def int_to_bin_str(number: int) -> str:
    """Convert number to 8 bit binary string."""
    return bin(number)[2:].rjust(8, "0")


def char_to_bin_str(character: chr) -> str:
    """Convert character to 8 bit binary string."""
    return int_to_bin_str(ord(character))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo xor.")
    parser.add_argument("word", type=str, help="Word to encrypt")
    args = parser.parse_args()

    plain_text = args.word
    plain_bin = []
    # Generate random key equal in length to input word
    key = []
    key_bin = []
    output = []
    for letter in plain_text:
        key_part = randint(0, 255)
        key.append(key_part)
        key_bin.append(int_to_bin_str(key_part))
        # xor for output
        output.append(int_to_bin_str(key_part ^ ord(letter)))

    # Print Starting information
    print(f"Plain Text = {plain_text}")
    print("\n")
    for letter in plain_text:
        bin_letter = char_to_bin_str(letter)
        plain_bin.append(bin_letter)
        print(f"{letter} = {bin_letter}")
    print("\n")

    print(f'Plain Text = {" ".join(plain_bin)}')
    print(f'Key        = {" ".join(key_bin)}')
    print(f'--------------{"-" * (len(key) * 8 + len(key))}')

    # Xor encrypt
    print(f'Output     = {" ".join(output)}')
    print("\n" * 2)

    # Wait for input
    input("Hit Any Key")

    # Xor Decrypt
    print("\n" * 2)
    print(f'Output     = {" ".join(output)}')
    print(f'Key        = {" ".join(key_bin)}')
    print(f'--------------{"-" * (len(key) * 8 + len(key))}')
    print(f'Plain Text = {" ".join(plain_bin)}')
    print("\n")
    for letter in plain_text:
        bin_letter = char_to_bin_str(letter)
        plain_bin.append(bin_letter)
        print(f"{bin_letter} = {letter}")
    print("\n")
    print(f"Plain Text = {plain_text}")
