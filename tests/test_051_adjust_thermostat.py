"""
Script Name : test_051_adjust_thermostat.py
Description : Test suite for Thermostat Adjuster 2 coding challenge
Author      : @tonybnya
"""

import pytest
from challenge_051_adjust_thermostat import adjust_thermostat


@pytest.mark.parametrize(
    "current_f, target_c, expected",
    [
        (32, 0, "Hold"),
        (70, 25, "Heat: 7.0 degrees Fahrenheit"),
        (72, 18, "Cool: 7.6 degrees Fahrenheit"),
        (212, 100, "Hold"),
        (59, 22, "Heat: 12.6 degrees Fahrenheit"),
    ],
)
def test_adjust_thermostat(current_f: int, target_c: int, expected: str) -> None:
    assert adjust_thermostat(current_f, target_c) == expected
