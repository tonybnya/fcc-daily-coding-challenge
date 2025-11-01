"""
Script Name : test_002_rgb_to_hex.py
Description : Tests for RGB to Hex challenge
Author      : @tonybnya
"""
import pytest

from fcc_002_rgb_to_hex import rgb_to_hex


@pytest.mark.parametrize(
    "rgb, hex",
    [
        ("rgb(255, 255, 255)", "#ffffff"),
        ("rgb(1, 11, 111)", "#010b6f"),
        ("rgb(173, 216, 230)", "#add8e6"),
        ("rgb(79, 123, 201)", "#4f7bc9"),
        ("rgb(1, 2, 3)", "#010203"),
    ]
)
def test_rgb_to_hex(rgb: str, hex: str) -> None:
    assert rgb_to_hex(rgb) == hex
