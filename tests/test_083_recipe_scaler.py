"""
Script Name : test_083_recipe_scaler.py
Description : Test suite for Recipe Scaler
Author      : @tonybnya
"""

import pytest
from fcc_083_recipe_scaler import scale_recipe


@pytest.mark.parametrize(
    "ingredients, scale, expected",
    [
        (["2 C Flour", "1.5 T Sugar"], 2, ["4 C Flour", "3 T Sugar"]),
        (["4 T Flour", "1 C Milk", "2 T Oil"], 1.5, ["6 T Flour", "1.5 C Milk", "3 T Oil"]),
        (["3 C Milk", "2 C Oats"], 0.5, ["1.5 C Milk", "1 C Oats"]),
        (["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5, ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar", "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"])
    ]
)
def test_recipe_scaler(ingredients: list[str], scale: int, expected: list[str]) -> None:
    assert scale_recipe(ingredients, scale) == expected
