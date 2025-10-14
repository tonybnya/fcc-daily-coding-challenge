"""
Script Name : test_044_count.py
Description : Test suite for String Count
Author      : @tonybnya
"""

import pytest
from challenge_044_count import count


@pytest.mark.parametrize(
    "text, parameter, expected",
    [
        ("abcdefg", "def", 1),
        ("hello", "world", 0),
        ("mississippi", "iss", 2),
        ("she sells seashells by the seashore", "sh", 3),
        ("101010101010101010101", "101", 10),
    ],
)
def test_count(text: str, parameter: str, expected: int) -> None:
    assert count(text, parameter) == expected
