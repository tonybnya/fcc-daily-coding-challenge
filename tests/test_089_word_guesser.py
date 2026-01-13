"""
Script Name : test_089_word_guesser.py
Description : Test suite for Word Guesser coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_089_word_guesser import compare


@pytest.mark.parametrize(
    "word, guess, expected",
    [
        ("APPLE", "POPPA", "10201"),
        ("REACT", "TRACE", "11221"),
        ("DEBUGS", "PYTHON", "000000"),
        ("JAVASCRIPT", "TYPESCRIPT", "0000222222"),
        ("ORANGE", "ROUNDS", "110200"),
        ("WIRELESS", "ETHERNET", "10021000")
    ]
)
def test_word_guesser(word: str, guess: str, expected: str) -> None:
    assert compare(word, guess) == expected
