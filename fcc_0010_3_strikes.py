"""
Script Name : fcc_0010_3_strikes.py
Description : 3 Strikes
Author      : @tonybnya

Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
"""


def contains_3(n: int) -> bool:
    return "3" in str(n)


def squares_with_three(n: int) -> int:
    count: int = 0
    for i in range(1, n + 1):
        square: int = i**2
        if contains_3(square):
            count += 1
    return count
