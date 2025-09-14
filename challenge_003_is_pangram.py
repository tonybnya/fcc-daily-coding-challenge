"""
Script Name : challenge_003_is_pangram.py
Description : Pangram
Author      : @tonybnya

Given a word or sentence and a string of lowercase letters,
determine if the word or sentence uses all the letters from
the given set at least once and no other letters.

- Ignore non-alphabetical characters in the word or sentence.
- Ignore letter casing in the word or sentence.
"""


def is_pangram(sentence: str, letters: str) -> bool:
    words: list[str] = [c.lower() for c in sentence if c.isalpha()]
    return set(words) == set(letters)
