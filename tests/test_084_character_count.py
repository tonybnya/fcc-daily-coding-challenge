"""
Script Name : test_084_character_count.py
Description : Test suite for Character Count
Author      : @tonybnya
"""

import pytest
from fcc_084_character_count import count_characters


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("hello world", ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]),
        ("I love coding challenges!", ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"]),
        ("// TODO: Complete this challenge ASAP!", ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"])
    ]
)
def test_character_count(sentence: str, expected: list[str]) -> None:
    assert count_characters(sentence) == expected
