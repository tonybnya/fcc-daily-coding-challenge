"""
Script Name : fcc_082_lcm.py
Description : LCM
Author      : @tonybnya

Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

- Multiples of 4 are 4, 8, 12 and so on.
- Multiples of 6 are 6, 12, 18 and so on.
- 12 is the smallest number that is a multiple of both.
"""


def get_factors(num: int) -> list[int]:
    half: int = num // 2
    factors: list[int] = []
    for i in range(1, half + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors


def gcd(x: int, y: int) -> int:
    factors_x: list[int] = get_factors(x)
    factors_y: list[int] = get_factors(y)
    common_factors: list[int] = []
    for factor in factors_x:
        if factor in factors_y:
            common_factors.append(factor)
    return max(common_factors)


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)
