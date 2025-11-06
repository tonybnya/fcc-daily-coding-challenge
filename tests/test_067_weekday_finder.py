"""
Script Name : test_067_weekday_finder.py
Description : Test suite for Weekday Finder
Author      : @tonybnya
"""

import pytest
from fcc_067_weekday_finder import get_weekday


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2025-11-06", "Thursday"),
        ("1999-12-31", "Friday"),
        ("1111-11-11", "Saturday"),
        ("2112-12-21", "Wednesday"),
        ("2345-10-01", "Monday"),
    ],
)
def test_weekday_finder(date_string: str, expected: str) -> None:
    assert get_weekday(date_string) == expected
