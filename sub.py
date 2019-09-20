#!/usr/bin/env python3

"""A program to demo substitution as a crypto technique."""

import argparse
from collections import defaultdict

key = {
    "a": "q",
    "b": "w",
    "c": "e",
    "d": "r",
    "e": "t",
    "f": "y",
    "g": "u",
    "h": "i",
    "i": "o",
    "j": "p",
    "k": "a",
    "l": "s",
    "m": "d",
    "n": "f",
    "o": "g",
    "p": "h",
    "q": "j",
    "r": "k",
    "s": "l",
    "t": "z",
    "u": "x",
    "v": "c",
    "w": "v",
    "x": "b",
    "y": "n",
    "z": "m",
}

rev_key = {value: key for key, value in key.items()}


def encrypt(string: str) -> str:
    """Sub using key."""
    return "".join([key[c] for c in string])


def decrypt(string: str) -> str:
    """Sub using reverse key."""
    return "".join([rev_key[c] for c in string])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Substitute characters in string using key."
    )
    parser.add_argument(
        "words", metavar="word", type=str, nargs="+", help="Words to encrypt/decrypt"
    )
    parser.add_argument("--decrypt", action="store_true", help="decrypt string")
    parser.add_argument("--stats", action="store_true", help="print stats of string")

    args = parser.parse_args()
    if args.decrypt:
        crypto_text = " ".join([decrypt(word.lower()) for word in args.words])
    else:
        crypto_text = " ".join([encrypt(word.lower()) for word in args.words])
    print(crypto_text)
    if args.stats:
        print("\n")
        print("Stats:")
        counts = defaultdict(int)
        for letter in crypto_text:
            counts[letter] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for letter, count in sorted_counts:
            if letter != " ":
                print(f"\t{letter} = {count}")
