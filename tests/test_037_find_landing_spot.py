"""
Script Name : test_037_find_landing_spot.py
Description : Test suite for Landing Spot challenge
Author      : @tonybnya
"""
import pytest
from fcc_037_find_landing_spot import find_landing_spot


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 0], [2, 0]], [0, 1]),
        ([[9, 0, 3], [7, 0, 4], [8, 0, 5]], [1, 1]),
        ([[1, 2, 1], [0, 0, 2], [3, 0, 0]], [2, 2]),
        ([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]], [2, 1])
    ]
)
def test_find_landing_spot(
    matrix: list[list[int]],
    expected: list[int]
) -> None:
    assert find_landing_spot(matrix) == expected
