"""
Script Name : test_041_hex_to_decimal.py
Description : Test suite for Hex to Decimal
Author      : @tonybnya
"""

import pytest
from fcc_041_hex_to_decimal import hex_to_decimal


@pytest.mark.parametrize(
    "hex, decimal",
    [
        ("0", 0),
        ("1", 1),
        ("9", 9),
        ("A", 10),
        ("F", 15),
        ("10", 16),
        ("9F", 159),
        ("A0", 160),
        ("FF", 255),
        ("100", 256),
        ("15", 21),
        ("2E", 46),
        ("A3F", 2623),
    ],
)
def test_hex_to_decimal(hex: str, decimal: int) -> None:
    assert hex_to_decimal(hex) == decimal
