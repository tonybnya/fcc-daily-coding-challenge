"""
Script Name : test_032_decimal_to_binary.py
Description : Test suite for Decimal to Binary
Author      : @tonybnya
"""
import pytest
from fcc_032_decimal_to_binary import to_binary


@pytest.mark.parametrize(
    "decimal, binary",
    [
        (5, "101"),
        (12, "1100"),
        (50, "110010"),
        (99, "1100011")
    ]
)
def test_to_binary(decimal: int, binary: str) -> None:
    assert to_binary(decimal) == binary
