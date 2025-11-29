"""
Script Name : test_0018_second_best.py
Description : Test suite for Second Best
Author      : @tonybnya
"""

import pytest
from fcc_0018_second_best import get_laptop_cost


@pytest.mark.parametrize(
    "laptops, budget, expected",
    [
        ([1500, 2000, 1800, 1400], 1900, 1800),
        ([1500, 2000, 2000, 1800, 1400], 1900, 1800),
        ([2099, 1599, 1899, 1499], 2200, 1899),
        ([2099, 1599, 1899, 1499], 1000, 0),
        ([1200, 1500, 1600, 1800, 1400, 2000], 1450, 1400),
    ],
)
def test_second_best(laptops: list[int], budget: int, expected: int) -> None:
    assert get_laptop_cost(laptops, budget) == expected
