"""
Script Name : test_058_navigator.py
Description : Test suite for Navigator coding challenge
Author      : @tonybnya
"""

import pytest
from challenge_058_navigator import navigate


@pytest.mark.parametrize(
    "commands, expected",
    [
        (["Visit About Us", "Back", "Forward"], "About Us"),
        (["Forward"], "Home"),
        (["Back"], "Home"),
        (["Visit About Us", "Visit Gallery"], "Gallery"),
        (["Visit About Us", "Visit Gallery", "Back", "Back"], "Home"),
        (
            ["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"],
            "Contact",
        ),
        (
            ["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"],
            "Visit Us",
        ),
        ([], "Home"),
        (["Visit About"], "About"),
        (["Visit About", "Back"], "Home"),
    ],
)
def test_navigate(commands: list[str], expected: str) -> None:
    assert navigate(commands) == expected
