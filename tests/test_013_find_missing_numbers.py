"""
Script Name : test_013_find_missing_numbers.py
Description : Tests for Missing Numbers challenge
Author      : @tonybnya
"""
import pytest

from fcc_013_find_missing_numbers import find_missing_numbers


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 3, 5], [2, 4]),
        ([1, 2, 3, 4, 5], []),
        ([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]),
        ([10, 1, 10, 1, 10, 1], [2, 3, 4, 5, 6, 7, 8, 9]),
        ([3, 1, 4, 1, 5, 9], [2, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4], [11])
    ]
)
def test_find_missing_numbers(arr: list[int], expected: list[int]) -> None:
    assert find_missing_numbers(arr) == expected
