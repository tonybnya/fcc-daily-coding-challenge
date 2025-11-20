"""
Script Name : test_0007_targeted_sum.py
Description : Test suite for Targeted Sum coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_0007_targeted_sum import find_target


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4, 5], 6, [1, 2]),
        ([1, 3, 5, 6, 7, 8], 15, [4, 5]),
        ([1, 3, 5, 7], 14, "Target not found"),
    ],
)
def test_targeted_sum(arr: list[int], target: int, expected: list[int] | str) -> None:
    assert find_target(arr, target) == expected
