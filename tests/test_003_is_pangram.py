"""
Script Name : test_003_is_pangram.py
Description : Tests for Pangram challenge
Author      : @tonybnya
"""
import pytest

from fcc_003_is_pangram import is_pangram


@pytest.mark.parametrize(
    "sentence, letters, expected",
    [
        ("hello", "helo", True),
        ("hello", "hel", False),
        ("hello", "helow", False),
        ("hello world", "helowrd", True),
        ("Hello World!", "helowrd", True),
        ("Hello World!", "heliowrd", False),
        ("freeCodeCamp", "frcdmp", False),
        ("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz", True)
    ]
)
def test_is_pangram(sentence: str, letters: str, expected: bool) -> None:
    assert is_pangram(sentence, letters) == expected
