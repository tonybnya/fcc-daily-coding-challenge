"""
Script Name : test_064_count_words.py
Description : Test suite for Word Counter
Author      : @tonybnya
"""

import pytest
from fcc_064_count_words import count_words


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Hello world", 2),
        ("The quick brown fox jumps over the lazy dog.", 9),
        ("I like coding challenges!", 4),
        ("Complete the challenge in JavaScript and Python.", 7),
        ("The missing semi-colon crashed the entire internet.", 7),
    ],
)
def test_count_words(sentence: str, expected: int) -> None:
    assert count_words(sentence) == expected
