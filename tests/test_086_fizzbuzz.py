"""
Script Name : test_086_fizzbuzz.py
Description : Test suite for FizzBuzz
Author      : @tonybnya
"""

import pytest
from fcc_086_fizzbuzz import fizz_buzz


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, [1, 2]),
        (4, [1, 2, "Fizz", 4]),
        (8, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8]),
        (20, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]),
        (50, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"])
    ]
)
def test_fizzbuzz(n: int, expected: list[int | str]) -> None:
    assert fizz_buzz(n) == expected
