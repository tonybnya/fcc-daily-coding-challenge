"""
Script Name : challenge_024_is_perfect_square.py
Description : Perfect Square
Author      : @tonybnya

Given an integer, determine if it is a perfect square.

- A number is a perfect square if you can multiply an integer
  by itself to achieve the number.
  For example, 9 is a perfect square because
  you can multiply 3 by itself to get it.
"""


def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    return int(n ** 0.5) ** 2 == n
