"""
Script Name : test_074_array_shift.py
Description : Test suite for Array Shift coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_074_array_shift import shift_array


@pytest.mark.parametrize(
    "arr, n, expected",
    [
        ([1, 2, 3], 1, [2, 3, 1]),
        ([1, 2, 3], -1, [3, 1, 2]),
        (["alpha", "bravo", "charlie"], 5, ["charlie", "alpha", "bravo"]),
        (["alpha", "bravo", "charlie"], -11, ["bravo", "charlie", "alpha"]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15, [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]),
    ],
)
def test_array_shift(arr: list[int | str], n: int, expected: list[int | str]) -> None:
    assert shift_array(arr, n) == expected
