"""
Script Name : fcc_079_100_characters.py
Description : 100 Characters
Author      : @tonybnya

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
"""


def one_hundred(chars: str) -> str:
    length: int = len(chars)
    characters: str = ""
    repeat: int = 100 // length
    for i in range(repeat):
        characters += chars
    quotient: int = 100 // length
    remain_chars: int = 100 - (length * quotient)
    characters += chars[:remain_chars]
    return characters
