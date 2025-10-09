"""
Script Name : test_039_moon_phase.py
Description : Test suite for Space Week Day 6: Moon Phase
Author      : @tonybnya
"""
import pytest
from challenge_039_moon_phase import moon_phase


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2000-01-12", "New"),
        ("2000-01-13", "Waxing"),
        ("2014-10-15", "Full"),
        ("2012-10-21", "Waning"),
        ("2022-12-14", "New")
    ]
)
def test_moon_phase(
    date_string: str,
    expected: str
) -> None:
    assert moon_phase(date_string) == expected
