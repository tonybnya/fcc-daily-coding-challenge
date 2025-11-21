"""
Script Name : test_0010_3_strikes.py
Description : Test suite for 3 Strikes
Author      : @tonybnya
"""

import pytest
from fcc_0010_3_strikes import squares_with_three


@pytest.mark.parametrize(
    "n, expected", [(1, 0), (10, 1), (100, 19), (1000, 326), (10000, 4531)]
)
def test_3_strikes(n: int, expected: int) -> None:
    assert squares_with_three(n) == expected
