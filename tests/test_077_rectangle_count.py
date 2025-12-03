"""
Script Name : test_077_rectangle_count.py
Description : Test suite for Rectangle Count coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_077_rectangle_count import count_rectangles


@pytest.mark.parametrize(
    "width, height, expected",
    [
        (1, 3, 6),
        (3, 2, 18),
        (1, 2, 3),
        (5, 4, 150),
        (11, 19, 12540)
    ]
)
def test_rectangle_count(width: int, height: int, expected: int) -> None:
    assert count_rectangles(width, height) == expected
