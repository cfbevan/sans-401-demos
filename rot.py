#!/usr/bin/env python3

"""A program to demo rotation as a crypto technique."""

import argparse


def rotate(string: str, x: int = 13) -> str:
    """Rotate a lowercase string by x."""
    abc = "abcdefghijklmnopqrstuvwxyz"
    return "".join([abc[(abc.find(c) + x) % 26] for c in string])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rotate a string by a number.")
    parser.add_argument(
        "words", metavar="word", type=str, nargs="+", help="Words to encrypt"
    )
    parser.add_argument(
        "--rotate",
        dest="rotate",
        type=int,
        default=13,
        help="rotate by a number (default 13)",
    )

    args = parser.parse_args()
    print(" ".join([rotate(word.lower(), args.rotate) for word in args.words]))
