"""
Script Name : test_087_buzzfizz.py
Description : Test suite for BuzzFizz coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_087_buzzfizz import is_fizz_buzz


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([1, 2, 3, 4], False),
        ([1, 2, "Fizz", 4, "Buzz", 7], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"], True),
    ]
)
def test_buzzfizz(sequence: list[int | str], expected: bool) -> None:
    assert is_fizz_buzz(sequence) == expected
