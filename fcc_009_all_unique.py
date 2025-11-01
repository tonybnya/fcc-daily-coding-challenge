"""
Script Name : challenge_009_all_unique.py
Description : Unique Characters
Author      : @tonybnya

Given a string, determine if all the characters in the string are unique.

- Uppercase and lowercase letters should be considered different characters.
"""


def all_unique(s: str) -> bool:
    verify: set = set()
    for c in s:
        if c in verify:
            return False
        verify.add(c)
    return True
