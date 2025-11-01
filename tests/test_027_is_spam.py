"""
Script Name : test_027_is_spam.py
Description : Test suite for Spam Detector challenge
Author      : @tonybnya
"""
import pytest
from fcc_027_is_spam import is_spam


@pytest.mark.parametrize(
    "number, expected",
    [
        ("+0 (200) 234-0182", False),
        ("+091 (555) 309-1922", True),
        ("+1 (555) 435-4792", True),
        ("+0 (955) 234-4364", True),
        ("+0 (155) 131-6943", True),
        ("+0 (555) 135-0192", True),
        ("+0 (555) 564-1987", True),
        ("+00 (555) 234-0182", False)
    ]
)
def test_is_spam(number: str, expected: bool) -> None:
    assert is_spam(number) == expected
