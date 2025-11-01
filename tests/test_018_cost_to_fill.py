"""
Script Name : test_018_cost_to_fill.py
Description : Tests for Fill The Tank challenge
Author      : @tonybnya
"""
import pytest
from fcc_018_cost_to_fill import cost_to_fill


@pytest.mark.parametrize(
    "tank_size, fuel_level, price_per_gallon, expected",
    [
        (20, 0, 4.00, "$80.00"),
        (15, 10, 3.50, "$17.50"),
        (18, 9, 3.25, "$29.25"),
        (12, 12, 4.99, "$0.00"),
        (15, 9.5, 3.98, "$21.89")
    ]
)
def test_cost_to_fill(tank_size: float, fuel_level: float, price_per_gallon: float, expected: str) -> None:
    assert cost_to_fill(tank_size, fuel_level, price_per_gallon) == expected
