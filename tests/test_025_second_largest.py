"""
Script Name : test_025_second_largest.py
Description : Test suite for 2nd Largest challenge
Author      : @tonybnya
"""
import pytest
from challenge_025_second_largest import second_largest


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4], 3),
        ([20, 139, 94, 67, 31], 94),
        ([2, 3, 4, 6, 6], 4),
        ([10, -17, 55.5, 44, 91, 0], 55.5),
        ([1, 0, -1, 0, 1, 0, -1, 1, 0], 0)
    ]
)
def test_second_largest(arr: list[int], expected: int) -> None:
    assert second_largest(arr) == expected
