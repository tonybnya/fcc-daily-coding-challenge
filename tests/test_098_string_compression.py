"""
Script Name : test_098_string_compression.py
Description : Test suite for String Compression coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_098_string_compression import compress_string


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("yes yes yes please", "yes(3) please"),
        ("I have have have apples", "I have(3) apples"),
        ("one one three and to the the the the", "one(2) three and to the(4)"),
        ("route route route route route route tee tee tee tee tee tee", "route(6) tee(6)")
    ]
)
def test_string_compression(sentence: str, expected: str) -> None:
    assert compress_string(sentence) == expected
