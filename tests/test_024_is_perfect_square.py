"""
Script Name : test_024_is_perfect_square.py
Description : Test suite for Perfect Square challenge
Author      : @tonybnya
"""
import pytest
from fcc_024_is_perfect_square import is_perfect_square


@pytest.mark.parametrize(
    "n, expected",
    [
        (9, True),
        (49, True),
        (1, True),
        (2, False),
        (99, False),
        (-9, False),
        (0, True),
        (25281, True)
    ]
)
def test_is_perfect_square(n: int, expected: bool) -> None:
    assert is_perfect_square(n) == expected
