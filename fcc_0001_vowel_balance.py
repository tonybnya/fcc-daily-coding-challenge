"""
Script Name : fcc_0001_vowel_balance.py
Description : Vowel Balance
Author      : @tonybnya

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

- The string can contain any characters.
- The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
- If there's an odd number of characters in the string, ignore the center character.
"""


def num_vowels(s: str) -> int:
    vowels: int = 0
    for c in s:
        if c.lower() in "aeiou":
            vowels += 1
    return vowels


def is_balanced(s: str) -> bool:
    n: int = len(s)
    mid: int = n // 2
    vowels_in_first_half: int = num_vowels(s[:mid])
    start_second_half: int = 0
    if n % 2 == 0:
        start_second_half = mid
    else:
        start_second_half = mid + 1
    vowels_in_second_half: int = num_vowels(s[start_second_half:])
    return vowels_in_first_half == vowels_in_second_half
