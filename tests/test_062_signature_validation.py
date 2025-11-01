"""
Script Name : test_062_signature_validation.py
Description : Test suite for Signature Validation
Author      : @tonybnya
"""

import pytest
from fcc_062_signature_validation import verify


@pytest.mark.parametrize(
    "message, key, signature, expected",
    [
        ("foo", "bar", 57, True),
        ("foo", "bar", 54, False),
        ("freeCodeCamp", "Rocks", 238, True),
        ("Is this valid?", "No", 210, False),
        ("Is this valid?", "Yes", 233, True),
        ("Check out the freeCodeCamp podcast,", "in the mobile app", 514, True),
    ],
)
def test_signature_validation(
    message: str, key: str, signature: int, expected: bool
) -> None:
    assert verify(message, key, signature) == expected
