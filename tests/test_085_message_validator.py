"""
Script Name : test_085_message_validator.py
Description : Test suite for Message Validator coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_085_message_validator import is_valid_message


@pytest.mark.parametrize(
    "message, validation, expected",
    [
        ("hello world", "hw", True),
        ("ALL CAPITAL LETTERS", "acl", True),
        ("Coding challenge are boring.", "cca", False),
        ("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD", True),
        ("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT", False),
    ]
)
def test_message_validator(message: str, validation: str, expected: bool) -> None:
    assert is_valid_message(message, validation) == expected
