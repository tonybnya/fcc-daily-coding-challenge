"""
Script Name : test_042_battle.py
Description : Test suite for Battle of Words
Author      : @tonybnya
"""

import pytest
from fcc_042_battle import battle


@pytest.mark.parametrize(
    "our_team, opponent, expected",
    [
        ("hello world", "hello word", "We win"),
        ("Hello world", "hello world", "We win"),
        ("lorem ipsum", "kitty ipsum", "We lose"),
        ("hello world", "world hello", "Draw"),
        ("git checkout", "git switch", "We win"),
        ("Cheeseburger with fries", "Cheeseburger with Fries", "We lose"),
        ("We must never surrender", "Our team must win", "Draw"),
    ],
)
def test_battle(our_team: str, opponent: str, expected: str) -> None:
    assert battle(our_team, opponent) == expected
