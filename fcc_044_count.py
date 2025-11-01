"""
Script Name : challenge_044_count.py
Description : String Count
Author      : @tonybnya

Given two strings,
determine how many times the second string appears in the first.

- The pattern string can overlap in the first string.
  For example, "aaa" contains "aa" twice.
  The first two a's and the second two.
"""


def count(text: str, parameter: str) -> int:
    n: int = len(text)
    m: int = len(parameter)
    counter: int = 0
    for i in range(n):
        if text[i] == parameter[0]:
            if i + m <= n and text[i : i + m] == parameter:
                counter += 1
    return counter
