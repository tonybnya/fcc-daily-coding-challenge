"""
Script Name : fcc_0009_sum_of_squares.py
Description : Sum of Squares
Author      : @tonybnya

Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.
"""


def sum_of_squares(n: int) -> int:
    s: int = 0
    for i in range(1, n + 1):
        s += i**2
    return s
