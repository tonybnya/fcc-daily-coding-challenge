"""
Script Name : fcc_072_vowels_and_consonants.py
Description : Vowels and Consonants
Author      : @tonybnya

Given a string, return an array with the number of vowels and number of consonants in the string.

- Vowels consist of a, e, i, o, u in any case.
- Consonants consist of all other letters in any case.
- Ignore any non-letter characters.

For example, given "Hello World", return [3, 7].
"""


def count(s: str) -> list[int]:
    VOWELS: str = "aeiou"
    vowels, consonants = 0, 0
    for c in s:
        if c.isalpha():
            if c.lower() in VOWELS:
                vowels += 1
            else:
                consonants += 1
    return [vowels, consonants]
