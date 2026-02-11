"""
Script Name : test_097_date_formatter.py
Description : Test suite for Date Formatter
Author      : @tonybnya
"""

import pytest
from fcc_097_date_formatter import format_date


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("December 6, 2025", "2025-12-06"),
        ("January 1, 2000", "2000-01-01"),
        ("November 11, 1111", "1111-11-11"),
        ("September 7, 512", "512-09-07"),
        ("May 4, 1950", "1950-05-04"),
        ("February 29, 1992", "1992-02-29")
    ]
)
def test_date_formatter(date_string: str, expected: str) -> None:
    assert format_date(date_string) == expected
