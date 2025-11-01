"""
Script Name : test_029_get_longest_word.py
Description : Test suite for Longest Word challenge
Author      : @tonybnya
"""
import pytest
from fcc_029_get_longest_word import get_longest_word


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("coding is fun", "coding"),
        ("Coding challenges are fun and educational.", "educational"),
        ("This sentence has multiple long words.", "sentence")
    ]
)
def test_get_longest_word(sentence: str, expected: str) -> None:
    assert get_longest_word(sentence) == expected
