"""
Script Name : test_028_get_headings.py
Description : Test suite for CSV Header Parser challenge
Author      : @tonybnya
"""
import pytest
from challenge_028_get_headings import get_headings


@pytest.mark.parametrize(
    "csv, expected",
    [
        (
            "name,age,city",
            ["name", "age", "city"]
        ),
        (
            "first name,last name,phone",
            ["first name", "last name", "phone"]
        ),
        (
            "username , email , signup date ",
            ["username", "email", "signup date"]
        )
    ]
)
def test_get_headings(csv: str, expected: list[str]) -> None:
    assert get_headings(csv) == expected
