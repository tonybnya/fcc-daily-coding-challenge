"""
Script Name : test_078_fingerprint_test.py
Description : Test suite for Fingerprint Test coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_078_fingerprint_test import is_match


@pytest.mark.parametrize(
    "fingerprint_a, fingerprint_b, expected",
    [
        ("helloworld", "helloworld", True),
        ("helloworld", "helloworlds", False),
        ("helloworld", "jelloworld", True),
        ("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog", True),
        ("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog", True)
    ]
)
def test_fingerprint_test(
    fingerprint_a: str,
    fingerprint_b: str,
    expected: bool
) -> None:
    assert is_match(fingerprint_a, fingerprint_b) == expected
