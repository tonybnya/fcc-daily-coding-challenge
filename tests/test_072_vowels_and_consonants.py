"""
Script Name : test_072_vowels_and_consonants.py
Description : Test suite for Vowels and Consonants
Author      : @tonybnya
"""

import pytest
from fcc_072_vowels_and_consonants import count


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", [3, 7]),
        ("JavaScript", [3, 7]),
        ("Python", [1, 5]),
        ("freeCodeCamp", [5, 7]),
        ("Hello, World!", [3, 7]),
        ("The quick brown fox jumps over the lazy dog.", [11, 24]),
    ],
)
def test_vowels_and_consonants(s: str, expected: list[int]) -> None:
    assert count(s) == expected
