"""
Script Name : challenge_023_is_mirror.py
Description : String Mirror
Author      : @tonybnya

Given two strings, determine if the second string is a mirror
of the first.

- A string is considered a mirror if it contains the same letters
  in reverse order.
- Treat uppercase and lowercase letters as distinct.
- Ignore all non-alphabetical characters.
"""


def is_mirror(str1: str, str2: str) -> bool:
    n: int = len(str1)
    m: int = len(str2)
    i: int = 0
    j: int = m - 1

    while i < n and j >= 0:
        if not str1[i].isalpha():
            i += 1
        if not str2[j].isalpha():
            j -= 1
        if str1[i].isalpha() and str2[j].isalpha():
            if str1[i] != str2[j]:
                return False
            i += 1
            j -= 1

    return True
