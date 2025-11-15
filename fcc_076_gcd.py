"""
Script Name : fcc_076_gcd.py
Description : GCD
Author      : @tonybnya


Given two positive integers, return their greatest common divisor (GCD).

    The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.

For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
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
