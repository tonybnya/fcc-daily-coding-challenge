"""
Script Name : test_088_whats_my_age_again.py
Description : Test suite for What's My Age Again? coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_088_whats_my_age_again import calculate_age


@pytest.mark.parametrize(
    "birthday, expected",
    [
        ("2000-11-20", 25),
        ("2000-12-01", 24),
        ("2014-10-25", 11),
        ("1994-01-06", 31),
        ("1994-12-14", 30)
    ]
)
def test_whats_my_age_again(birthday: str, expected: int) -> None:
    assert calculate_age(birthday) == expected
