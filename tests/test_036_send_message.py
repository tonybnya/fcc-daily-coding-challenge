"""
Script Name : test_036_send_message.py
Description : Test suite for Phone Home
Author      : @tonybnya
"""
import pytest
from challenge_036_send_message import send_message


@pytest.mark.parametrize(
    "route, expected",
    [
        ([300000, 300000], 2.5),
        ([384400, 384400], 3.0627),
        ([54600000, 54600000], 364.5),
        ([1000000, 500000000, 1000000], 1674.3333),
        ([10000, 21339, 50000, 31243, 10000], 2.4086),
        ([802101, 725994, 112808, 3625770, 481239], 21.1597)
    ]
)
def test_send_message(route: list[int], expected: bool) -> None:
    assert send_message(route) == expected
