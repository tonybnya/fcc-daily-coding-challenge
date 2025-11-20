"""
Script Name : fcc_0008_factorializer.py
Description : Factorializer
Author      : @tonybnya

Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

- The factorial of zero is 1.
"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
