"""
Script Name : test_033_check_strength.py
Description : Test suite for Password Check challenge
Author      : @tonybnya
"""
import pytest
from fcc_033_check_strength import check_strength


@pytest.mark.parametrize(
    "password, expected",
    [
        ("123456", "weak"),
        ("pass!!!", "weak"),
        ("Qwerty", "weak"),
        ("PASSWORD", "weak"),
        ("PASSWORD!", "medium"),
        ("PassWord%^!", "medium"),
        ("qwerty12345", "medium"),
        ("PASSWORD!", "medium"),
        ("PASSWORD!", "medium"),
        ("S3cur3P@ssw0rd", "strong"),
        ("C0d3&Fun!", "strong")
    ]
)
def test_check_strength(password: str, expected: str) -> None:
    assert check_strength(password) == expected
