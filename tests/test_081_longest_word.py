"""
Script Name : test_081_longest_word.py
Description : Test suite for Longest Word coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_081_longest_word import longest_word


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("The quick red fox", "quick"),
        ("Hello coding challenge.", "challenge"),
        ("Do Try This At Home.", "This"),
        ("This sentence... has commas, ellipses, and an exclamation point!", "exclamation"),
        ("A tie? No way!", "tie"),
        ("Wouldn't you like to know.", "Wouldnt")
    ]
)
def test_longest_word(sentence: str, expected: str) -> None:
    assert longest_word(sentence) == expected
