"""
Script Name : test_056_duration_formatter.py
Description : Test suite for Duration Formatter
Author      : @tonybnya
"""

import pytest
from challenge_056_duration_formatter import format


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (500, "8:20"),
        (4000, "1:06:40"),
        (1, "0:01"),
        (5555, "1:32:35"),
        (99999, "27:46:39"),
    ],
)
def test_duration_formatter(seconds: int, expected: str) -> None:
    assert format(seconds) == expected
