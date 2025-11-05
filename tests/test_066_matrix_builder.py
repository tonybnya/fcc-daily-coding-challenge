"""
Script Name : test_066_matrix_builder.py
Description : Test suite for Matrix Builder
Author      : @tonybnya
"""

import pytest
from fcc_066_matrix_builder import build_matrix


@pytest.mark.parametrize(
    "rows, cols, expected",
    [
        (2, 3, [[0, 0, 0], [0, 0, 0]]),
        (3, 2, [[0, 0], [0, 0], [0, 0]]),
        (4, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        (9, 1, [[0], [0], [0], [0], [0], [0], [0], [0], [0]]),
    ],
)
def test_matrix_builder(rows: int, cols: int, expected: list[list[int]]) -> None:
    assert build_matrix(rows, cols) == expected
