"""
Script Name : fcc_087_buzzfizz.py
Description : BuzzFizz
Author      : @tonybnya

Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

- Numbers that are multiples of 3 are replaced with "Fizz"
- Numbers that are multiples of 5 are replaced with "Buzz"
- Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
- All other numbers remain as integers in ascending order, starting from 1.
- The array must start at 1 and have no missing or extra elements.
"""


def is_fizz_buzz(sequence: list[int | str]) -> bool:
    expected: int | str = ""
    for i in range(1, len(sequence) + 1):
        if i % 15 == 0:
            expected = 'FizzBuzz'
        elif i % 3 == 0:
            expected = 'Fizz'
        elif i % 5 == 0:
            expected = 'Buzz'
        else:
            expected = i

        if sequence[i - 1] != expected:
            return False
    return True

