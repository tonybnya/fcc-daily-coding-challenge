"""
Script Name : test_007_parse_roman_numeral.py
Description : Tests for Roman Numeral Parser challenge
Author      : @tonybnya
"""
import pytest

from challenge_007_parse_roman_numeral import parse_roman_numeral


@pytest.mark.parametrize(
    "numeral, value",
    [
        ("III", 3),
        ("IV", 4),
        ("XXVI", 26),
        ("XCIX", 99),
        ("CDLX", 460),
        ("DIV", 504),
        ("MMXXV", 2025)
    ]
)
def test_parse_roman_numeral(numeral: str, value: int) -> None:
    assert parse_roman_numeral(numeral) == value
