"""
Script Name : test_046_email_validator.py
Description : Test suite for Email Validator
Author      : @tonybnya
"""

import pytest
from challenge_046_email_validator import validate


@pytest.mark.parametrize(
    "email, expected",
    [
        ("a@b.cd", True),
        ("hell.-w.rld@example.com", True),
        (".b@sh.rc", False),
        ("example@test.c0", False),
        ("freecodecamp.org", False),
        ("develop.ment_user@c0D!NG.R.CKS", True),
        ("hello.@wo.rld", False),
        ("hello@world..com", False),
        ("git@commit@push.io", False),
    ],
)
def test_validate(email: str, expected: bool) -> None:
    assert validate(email) == expected
