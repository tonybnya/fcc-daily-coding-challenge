"""
Script Name : test_050_calculate_tips.py
Description : Test suite fot Tip Calculator coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_050_calculate_tips import calculate_tips


@pytest.mark.parametrize(
    "meal_price, custom_tip, expected",
    [
        ("$10.00", "25%", ["$1.50", "$2.00", "$2.50"]),
        ("$89.67", "26%", ["$13.45", "$17.93", "$23.31"]),
        ("$19.85", "9%", ["$2.98", "$3.97", "$1.79"]),
    ],
)
def test_calculate_tips(meal_price: str, custom_tip: str, expected: list[str]) -> None:
    assert calculate_tips(meal_price, custom_tip) == expected
