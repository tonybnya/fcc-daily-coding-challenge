"""
Script Name : test_0014_character_battle.py
Description : Test suite for Character Battle
Author      : @tonybnya
"""

import pytest
from fcc_0014_character_battle import battle


@pytest.mark.parametrize(
    "my_army, opposing_army, expected",
    [
        ("Hello", "World", "We lost"),
        ("pizza", "salad", "We won"),
        ("C@T5", "D0G$", "We won"),
        ("kn!ght", "orc", "Opponent retreated"),
        ("PC", "Mac", "We retreated"),
        ("Wizards", "Dragons", "It was a tie"),
        ("Mr. Smith", "Dr. Jones", "It was a tie"),
    ],
)
def test_character_battle(my_army: str, opposing_army: str, expected: str) -> None:
    assert battle(my_army, opposing_army) == expected
