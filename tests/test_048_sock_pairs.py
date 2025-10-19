"""
Script Name : test_048_sock_pairs.py
Description : Test suite for Missing Socks coding challenge
Author      : @tonybnya
"""

import pytest
from challenge_048_sock_pairs import sock_pairs


@pytest.mark.parametrize(
    "pairs, cycles, expected",
    [(2, 5, 1), (1, 2, 0), (5, 11, 4), (6, 25, 3), (1, 8, 0)],
)
def test_sock_pairs(pairs: int, cycles: int, expected: int) -> None:
    assert sock_pairs(pairs, cycles) == expected
