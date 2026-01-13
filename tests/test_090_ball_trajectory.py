"""
Script Name : test_090_ball_trajectory.py
Description : Test suite for Ball Trajectory coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_090_ball_trajectory import get_next_location


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]], [2, 3]),
        ([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]], [3, 0]),
        ([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]], [1, 2]),
        ([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]], [1, 1]),
        ([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]], [2, 2])
    ]
)
def test_ball_trajectory(matrix: list[list[int]], expected: list[int]) -> None:
    assert get_next_location(matrix) == expected
