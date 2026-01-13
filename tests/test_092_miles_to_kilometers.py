"""
Script Name : test_092_miles_to_kilometers.py
Description : Test suite for Miles to Kilometers coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_092_miles_to_kilometers import convert_to_km


@pytest.mark.parametrize(
    "miles, expected",
    [
        (1, 1.61),
        (21, 33.8),
        (3.5, 5.63),
        (0, 0),
        (0.621371, 1)
    ]
)
def test_092_miles_to_kilometers(miles: int | float, expected: int | float) -> None:
    assert convert_to_km(miles) == expected
