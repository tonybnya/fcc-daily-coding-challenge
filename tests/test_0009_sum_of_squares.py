"""
Script Name : test_0009_sum_of_squares.py
Description : Test suite for Sum of Squares
Author      : @tonybnya
"""

import pytest
from fcc_0009_sum_of_squares import sum_of_squares


@pytest.mark.parametrize(
    "n, expected", [(5, 55), (10, 385), (25, 5525), (500, 41791750), (1000, 333833500)]
)
def test_0009_of_squares(n: int, expected: int) -> None:
    assert sum_of_squares(n) == expected
