"""
Script Name : test_054_hidden_treasure.py
Description : Test suite for Hidden Treasure
Author      : @tonybnya
"""

import pytest
from fcc_054_hidden_treasure import dive


@pytest.mark.parametrize(
    "map, coordinates, expected",
    [
        ([["-", "X"], ["-", "X"], ["-", "O"]], [2, 1], "Recovered"),
        ([["-", "X"], ["-", "X"], ["-", "O"]], [2, 0], "Empty"),
        ([["-", "X"], ["-", "O"], ["-", "O"]], [1, 1], "Found"),
        ([["-", "-", "-"], ["X", "O", "X"], ["-", "-", "-"]], [1, 2], "Found"),
        ([["-", "-", "-"], ["-", "-", "-"], ["O", "X", "X"]], [2, 0], "Recovered"),
        ([["-", "-", "-"], ["-", "-", "-"], ["O", "X", "X"]], [1, 2], "Empty"),
    ],
)
def test_hidden_treasure(
    map: list[list[str]], coordinates: list[int], expected: str
) -> None:
    assert dive(map, coordinates) == expected
