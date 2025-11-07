"""
Script Name : test_068_counting_cards.py
Description : Test suite for Counting Cards
Author      : @tonybnya
"""

import pytest
from fcc_068_counting_cards import combinations


@pytest.mark.parametrize(
    "cards, expected",
    [(52, 1), (1, 52), (2, 1326), (5, 2598960), (10, 15820024220), (50, 1326)],
)
def test_counting_cards(cards: int, expected: int) -> None:
    assert combinations(cards) == expected
