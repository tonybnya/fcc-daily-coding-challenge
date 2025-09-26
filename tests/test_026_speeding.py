"""
Script Name : test_026_speeding.py
Description : Test suite for Caught Speeding challenge
Author      : @tonybnya
"""
import pytest
from challenge_026_speeding import speeding


@pytest.mark.parametrize(
    "speeds, limit, expected",
    [
        ([50, 60, 55], 60, [0, 0]),
        ([58, 50, 60, 55], 55, [2, 4]),
        ([61, 81, 74, 88, 65, 71, 68], 70, [4, 8.5]),
        ([100, 105, 95, 102], 100, [2, 3.5]),
        ([40, 45, 44, 50, 112, 39], 55, [1, 57])
    ]
)
def test_speeding(
    speeds: list[int],
    limit: int,
    expected: list[int | float]
) -> None:
    assert speeding(speeds, limit) == expected
