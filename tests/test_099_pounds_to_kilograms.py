"""
Script Name : test_099_pounds_to_kilograms.py
Description : Test suite for Pounds to Kilograms coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_099_pounds_to_kilograms import convert_to_kgs


@pytest.mark.parametrize(
    "lbs, expected",
    [
        (1, "1 pound equals 0.45 kilograms."),
        (0, "0 pounds equals 0.00 kilograms."),
        (100, "100 pounds equals 45.36 kilograms."),
        (2.5, "2.5 pounds equals 1.13 kilograms."),
        (2.20462, "2.20462 pounds equals 1.00 kilogram.")
    ]
)
def test_pounds_to_kilograms(lbs: int | float, expected: str) -> None:
    assert convert_to_kgs(lbs) == expected
