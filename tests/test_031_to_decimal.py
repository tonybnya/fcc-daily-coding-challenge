"""
Script Name : test_031_to_decimal.py
Description : Test suite for Binary to Decimal challenge
Author      : @tonybnya
"""
import pytest
from fcc_031_to_decimal import to_decimal


@pytest.mark.parametrize(
    "binary, decimal",
    [
        ("101", 5),
        ("1010", 10),
        ("10010", 18),
        ("1010101", 85)
    ]
)
def test_to_decimal(binary: str, decimal: int) -> None:
    assert to_decimal(binary) == decimal
