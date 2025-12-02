"""
Script Name : test_0019_candlelight.py
Description : Test suite for Candlelight coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_0019_candlelight import burn_candles


@pytest.mark.parametrize(
    "candles, leftovers_needed, expected",
    [
        (7, 2, 13),
        (10, 5, 12),
        (20, 3, 29),
        (17, 4, 22),
        (2345, 3, 3517)
    ]
)
def test_candlelight(
    candles: int,
    leftovers_needed: int,
    expected: int
) -> None:
    assert burn_candles(candles, leftovers_needed) == expected
