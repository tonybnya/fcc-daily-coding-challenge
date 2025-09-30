"""
Script Name : test_030_format_number.py
Description : Test suite for Phone Number Formatter challenge
Author      : @tonybnya
"""
import pytest
from challenge_030_format_number import format_number


@pytest.mark.parametrize(
    "number, phonenumber",
    [
        ("05552340182", "+0 (555) 234-0182"),
        ("15554354792", "+1 (555) 435-4792"),
        ("04441234567", "+0 (444) 123-4567"),
        ("16667778888", "+1 (666) 777-8888"),
        ("07771234567", "+0 (777) 123-4567"),
        ("19998887766", "+1 (999) 888-7766"),
        ("03334567890", "+0 (333) 456-7890"),
        ("12223334444", "+1 (222) 333-4444"),
        ("01112223334", "+0 (111) 222-3334"),
        ("18885551234", "+1 (888) 555-1234")
    ]
)
def test_format_number(number: str, phonenumber: str) -> None:
    assert format_number(number) == phonenumber
