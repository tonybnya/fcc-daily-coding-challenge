"""
Script Name : test_096_symmetric_difference.py
Description : Test suite for Symmetric Difference coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_096_symmetric_difference import difference


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        ([1, 2, 3], [3, 4, 5], [1, 2, 4, 5]),
        (["a", "b"], ["c", "b"], ["a", "c"]),
        ([1, "a", 2], [2, "b", "a"], [1, "b"]),
        ([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8])
    ]
)
def test_symmetric_difference(
    arr1: list[int | str],
    arr2: list[int | str],
    expected: list[int | str]
) -> None:
    assert difference(arr1, arr2) == expected
