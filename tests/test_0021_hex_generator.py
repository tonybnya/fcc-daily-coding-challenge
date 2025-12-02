"""
Script Name : test_0021_hex_generator.py
Description : Test suite for Hex Generator coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_0021_hex_generator import generate_hex


@pytest.mark.parametrize(
    "color, expected",
    [
        ('yellow', 'Invalid color'),
        ('black', 'Invalid color'),
        ('pink', 'Invalid color'),
        ('orange', 'Invalid color')
    ]
)
def test_hex_generator(color: str, expected: str) -> None:
    assert generate_hex(color) == expected
