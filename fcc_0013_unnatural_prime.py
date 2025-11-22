"""
Script Name : fcc_0013_unnatural_prime.py
Description : Unnatural Prime
Author      : @tonybnya

Given an integer, determine if that number is a prime number or a negative prime number.

- A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
- A negative prime number is the negative version of a positive prime number.
- 1 and 0 are not considered prime numbers.
"""


def is_unnatural_prime(n: int) -> bool:
    if n < 0:
        n *= -1
    if n in (0, 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
