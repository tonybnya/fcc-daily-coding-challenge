"""
Script Name : test_076_gcd.py
Description : Test suite for GCD coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_076_gcd import gcd


@pytest.mark.parametrize(
    "x, y, expected",
    [(4, 6, 2), (20, 15, 5), (13, 17, 1), (654, 456, 6), (3456, 4320, 864)],
)
def test_gcd(x: int, y: int, expected: int) -> None:
    assert gcd(x, y) == expected
