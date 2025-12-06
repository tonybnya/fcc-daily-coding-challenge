"""
Script Name : fcc_086_fizzbuzz.py
Description : FiZZBuzz
Author      : @tonybnya

Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

- 3 with "Fizz".
- 5 with "Buzz".
- 3 and 5 with "FizzBuzz".
"""


def fizz_buzz(n: int) -> list[int | str]:
    arr: list[int | str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            arr.append('FizzBuzz')
        elif i % 3 == 0:
            arr.append('Fizz')
        elif i % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(i)
    return arr
