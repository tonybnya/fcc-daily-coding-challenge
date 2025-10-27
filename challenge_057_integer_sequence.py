"""
Script Name : challenge_057_integer_sequence.py
Description : Integer Sequence
Author      : @tonybnya

Given a positive integer,
return a string with all of the integers from 1 up to,
and including, the given number, in numerical order.

For example, given 5, return "12345".
"""


def sequence(n: int) -> str:
    string: str = ""
    for i in range(1, n + 1):
        string += str(i)
    return string
