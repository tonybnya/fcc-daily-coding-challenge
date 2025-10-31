"""
Script Name : test_059_email_sorter.py
Description : Test suite for Email Sorter
Author      : @tonybnya
"""

import pytest
from challenge_059_email_sorter import sort


@pytest.mark.parametrize(
    "emails, expected",
    [
        (
            ["jill@mail.com", "john@example.com", "jane@example.com"],
            ["jane@example.com", "john@example.com", "jill@mail.com"],
        ),
        (
            ["bob@mail.com", "alice@zoo.com", "carol@mail.com"],
            ["bob@mail.com", "carol@mail.com", "alice@zoo.com"],
        ),
        (
            ["user@z.com", "user@y.com", "user@x.com"],
            ["user@x.com", "user@y.com", "user@z.com"],
        ),
        (
            ["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"],
            ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"],
        ),
        (
            [
                "simon@beta.com",
                "sammy@alpha.com",
                "Sarah@Alpha.com",
                "SAM@ALPHA.com",
                "Simone@Beta.com",
                "sara@alpha.com",
            ],
            [
                "SAM@ALPHA.com",
                "sammy@alpha.com",
                "sara@alpha.com",
                "Sarah@Alpha.com",
                "simon@beta.com",
                "Simone@Beta.com",
            ],
        ),
    ],
)
def test_059_email_sorter(emails: list[str], expected: list[str]) -> None:
    assert sort(emails) == expected
