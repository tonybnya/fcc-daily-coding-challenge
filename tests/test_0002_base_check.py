"""
Script Name : test_0002_base_check.py
Description : Test suite for Base Check
Author      : @tonybnya
"""

import pytest
from fcc_0002_base_check import is_valid_number


@pytest.mark.parametrize(
    "n, base, expected",
    [
        ("10101", 2, True),
        ("10201", 2, False),
        ("76543210", 8, True),
        ("9876543210", 8, False),
        ("9876543210", 10, True),
        ("ABC", 10, False),
        ("ABC", 16, True),
        ("Z", 36, True),
        ("ABC", 20, True),
        ("4B4BA9", 16, True),
        ("5G3F8F", 16, False),
        ("5G3F8F", 17, True),
        ("abc", 10, False),
        ("abc", 16, True),
        ("AbC", 16, True),
        ("z", 36, True),
    ],
)
def test_base_check(n: str, base: int, expected: bool) -> None:
    assert is_valid_number(n, base) == expected
