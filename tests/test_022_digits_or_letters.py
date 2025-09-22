"""
Script Name : test_022_digits_or_letters.py
Description : Tests for Digits vs Letters challenge
Author      : @tonybnya
"""
import pytest
from challenge_022_digits_or_letters import digits_or_letters


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc123", "tie"),
        ("a1b2c3d", "letters"),
        ("1a2b3c4", "digits"),
        ("abc123!@#DEF", "letters"),
        ("H3110 W0R1D", "digits"),
        ("P455W0RD", "tie")
    ]
)
def test_digits_or_letters(s: str, expected: str) -> None:
    assert digits_or_letters(s) == expected
