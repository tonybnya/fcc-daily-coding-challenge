"""
Script Name : test_095_permutation_count.py
Description : Test suite for Permutation Count coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_095_permutation_count import count_permutations


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abb", 3),
        ("abc", 6),
        ("racecar", 630),
        ("freecodecamp", 39916800),
    ]
)
def test_permutation_count(s: str, expected: int) -> None:
    assert count_permutations(s) == expected
