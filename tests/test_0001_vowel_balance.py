"""
Script Name : test_0001_vowel_balance.py
Description : Test suite for Vowel Balance coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_0001_vowel_balance import is_balanced


@pytest.mark.parametrize(
    "s, expected",
    [
        ("racecar", True),
        ("Lorem Ipsum", True),
        ("Kitty Ipsum", False),
        ("string", False),
        (" ", True),
        ("abcdefghijklmnopqrstuvwxyz", False),
        ("123A#b!E&*456-o.U", True),
    ],
)
def test_vowel_balance(s: str, expected: bool) -> None:
    assert is_balanced(s) == expected
