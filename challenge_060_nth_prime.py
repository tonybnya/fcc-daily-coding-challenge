"""
Script Name : challenge_060_nth_prime.py
Description : Nth Prime
Author      : @tonybnya

A prime number is a positive integer greater than 1 that is divisible
only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number.
For example, given 5 return the 5th prime number: 11.
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    flag: bool = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


def nth_prime(n: int) -> int:
    counter, i, nth = 0, 0, 0
    while True:
        if counter == n:
            break
        if is_prime(i):
            nth = i
            counter += 1
        i += 1
    return nth
