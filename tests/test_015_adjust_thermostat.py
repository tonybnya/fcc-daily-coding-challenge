"""
Script Name : test_015_adjust_thermostat.py
Description : Tests for Thermostat Adjuster challenge
Author      : @tonybnya
"""
import pytest
from challenge_015_adjust_thermostat import adjust_thermostat


@pytest.mark.parametrize(
    "temp, target, expected",
    [
        (68, 72, 'heat'),
        (75, 72, 'cool'),
        (72, 72, 'hold'),
        (-20.5, -10.1, 'heat'),
        (100, 99.9, 'cool'),
        (0.0, 0.0, 'hold')
    ]
)
def test_adjust_thermostat(temp: float, target: float, expected) -> None:
    assert adjust_thermostat(temp, target) == expected
