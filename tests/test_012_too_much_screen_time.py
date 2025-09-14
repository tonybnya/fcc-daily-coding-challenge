"""
Script Name : test_012_too_much_screen_time.py
Description : Tests for Screen Time challenge
Author      : @tonybnya
"""
import pytest

from challenge_012_too_much_screen_time import too_much_screen_time


@pytest.mark.parametrize(
    "hours, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([7, 8, 8, 4, 2, 2, 3], False),
        ([5, 6, 6, 6, 6, 6, 6], False),
        ([1, 2, 3, 11, 1, 3, 4], True),
        ([1, 2, 3, 10, 2, 1, 0], True),
        ([3, 3, 5, 8, 8, 9, 4], True),
        ([3, 9, 4, 8, 5, 7, 6], True)
    ]
)
def test_too_much_screen_time(hours: list[int], expected: bool) -> None:
    assert too_much_screen_time(hours) == expected
