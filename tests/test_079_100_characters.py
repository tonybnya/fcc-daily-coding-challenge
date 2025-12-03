"""
Script Name : test_079_100_characters.py
Description : Test suite for 100 Characters coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_079_100_characters import one_hundred


@pytest.mark.parametrize(
    "chars, expected",
    [
        ("One hundred ", "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "),
        ("freeCodeCamp ", "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC"),
        ("daily challenges ", "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge"),
        ("!", "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    ]
)
def test_100_characters(chars: str, expected: str) -> None:
    assert one_hundred(chars) == expected
