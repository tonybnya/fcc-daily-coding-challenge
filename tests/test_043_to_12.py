"""
Script Name : test_043_to_12.py
Description : Test suite for 24 to 12
Author      : @tonybnya
"""

import pytest
from challenge_043_to_12 import to_12


@pytest.mark.parametrize(
    "time, expected",
    [
        ("1124", "11:24 AM"),
        ("0900", "9:00 AM"),
        ("1455", "2:55 PM"),
        ("2346", "11:46 PM"),
        ("0030", "12:30 AM"),
    ],
)
def test_to_12(time: str, expected: str) -> None:
    assert to_12(time) == expected
