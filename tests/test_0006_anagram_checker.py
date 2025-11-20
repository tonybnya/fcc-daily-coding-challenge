"""
Script Name : test_0006_anagram_checker.py
Description : Test suite for Anagram Checker
Author      : @tonybnya
"""

import pytest
from fcc_0006_anagram_checker import are_anagrams


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("listen", "silent", True),
        ("School master", "The classroom", True),
        ("A gentleman", "Elegant man", True),
        ("Hello", "World", False),
        ("apple", "banana", False),
        ("cat", "dog", False),
    ],
)
def test_anagram_checker(str1: str, str2: str, expected) -> None:
    assert are_anagrams(str1, str2) == expected
