"""
Script Name : test_023_is_mirror.py
Description : Tests for String Mirror challenge
Author      : @tonybnya
"""
import pytest
from fcc_023_is_mirror import is_mirror


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("helloworld", "helloworld", False),
        ("Hello World", "dlroW olleH", True),
        ("RaceCar", "raCecaR", True),
        ("RaceCar", "RaceCar", False),
        ("Mirror", "rorrim", False),
        ("Hello World", "dlroW-olleH", True),
        ("Hello World", "!dlroW !olleH", True)
    ]
)
def test_is_mirror(str1: str, str2: str, expected: bool) -> None:
    assert is_mirror(str1, str2) == expected
