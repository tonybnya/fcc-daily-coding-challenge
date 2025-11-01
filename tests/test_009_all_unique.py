"""
Script Name : test_009_all_unique.py
Description : Tests for Unique Characters challenge
Author      : @tonybnya
"""
import pytest

from fcc_009_all_unique import all_unique


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", True),
        ("aA", True),
        ("QwErTy123!@", True),
        ("~!@#$%^&*()_+", True),
        ("hello", False),
        ("freeCodeCamp", False),
        ("!@#*$%^&*()aA", False)
    ]
)
def test_all_unique(s: str, expected: bool) -> None:
    assert all_unique(s) == expected
