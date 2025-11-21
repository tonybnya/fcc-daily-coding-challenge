"""
Script Name : test_0011_mile_pace.py
Description : Test suite for Mile Pace
Author      : @tonybnya
"""

import pytest
from fcc_0011_mile_pace import mile_pace


@pytest.mark.parametrize(
    "miles, duration, expected",
    [
        (3, "24:00", "08:00"),
        (1, "06:45", "06:45"),
        (2, "07:00", "03:30"),
        (26.2, "120:35", "04:36"),
    ],
)
def test_mile_pace(miles: int, duration: str, expected: str) -> None:
    assert mile_pace(miles, duration) == expected
