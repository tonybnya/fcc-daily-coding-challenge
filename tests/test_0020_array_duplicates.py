"""
Script Name : test_0020_array_duplicates.py
Description : Test suite for Array Duplicates
Author      : @tonybnya
"""

import pytest
from fcc_0020_array_duplicates import find_duplicates


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], []),
        ([1, 2, 3, 4, 1, 2], [1, 2]),
        ([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4], [-6, 0, 2, 4, 5, 23])
    ]
)
def test_array_duplicates(arr: list[int], expected: list[int]) -> None:
    assert find_duplicates(arr) == expected
