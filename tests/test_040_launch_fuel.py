"""
Script Name : test_040_launch_fuel.py
Description : Test suite for Space Week Day 7: Launch Fuel
Author      : @tonybnya
"""

import pytest
from challenge_040_launch_fuel import launch_fuel


@pytest.mark.parametrize(
    "payload, expected",
    [(50, 12.4), (500, 124.8), (243, 60.7), (11000, 2749.8), (6214, 1553.4)],
)
def test_launch_fuel(payload: int, expected: float) -> None:
    assert launch_fuel(payload) == expected
