"""
Script Name : test_034_stellar_classification.py
Description : Test suite for Stellar Classification
Author      : @tonybnya
"""
import pytest
from challenge_034_stellar_classification import classification


@pytest.mark.parametrize(
    "temp, expected",
    [
        (5778, "G"),
        (2400, "M"),
        (9999, "A"),
        (3700, "K"),
        (3699, "M"),
        (210000, "O"),
        (6000, "F"),
        (11432, "B")
    ]
)
def test_classification(temp: int, expected: str) -> None:
    assert classification(temp) == expected
