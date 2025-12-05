"""
Script Name : test_082_lcm.py
Description : Test suite for LCM
Author      : @tonybnya
"""

import pytest
from fcc_082_lcm import lcm


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 6, 12),
        (9, 6, 18),
        (10, 100, 100),
        (13, 17, 221),
        (45, 70, 630)
    ]
)
def test_lcm(a:int, b: int, expected: int) -> None:
    assert lcm(a, b) == expected
