"""
Script Name : test_057_integer_sequence.py
Description : Test suite for Integer Sequence
Author      : @tonybnya
"""

import pytest
from challenge_057_integer_sequence import sequence


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, "12345"),
        (10, "12345678910"),
        (1, "1"),
        (27, "123456789101112131415161718192021222324252627"),
    ],
)
def test_integer_sequence(n: int, expected: str) -> None:
    assert sequence(n) == expected
