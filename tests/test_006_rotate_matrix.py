"""
Script Name : test_006_rotate_matrix.py
Description : Tests for Matrix Rotate challenge
Author      : @tonybnya
"""
import pytest

from fcc_006_rotate_matrix import rotate


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1]], [[1]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[0, 1, 0], [1, 0, 1], [0, 0, 0]], [[0, 1, 0], [0, 0, 1], [0, 1, 0]])
    ]
)
def test_rotate(matrix: list[list[int]], expected: list[list[int]]) -> None:
    assert rotate(matrix) == expected
