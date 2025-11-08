"""
Script Name : test_069_character_limit.py
Description : Test suite for Character Limit
Author      : @tonybnya
"""

import pytest
from fcc_069_character_limit import can_post


@pytest.mark.parametrize(
    "message, expected",
    [
        ("Hello world", "short post"),
        ("This is a longer message but still under eighty characters.", "long post"),
        (
            "This message is too long to fit into either of the character limits for a social media post.",
            "invalid post",
        ),
    ],
)
def test_character_limit(message: str, expected: str) -> None:
    assert can_post(message) == expected
