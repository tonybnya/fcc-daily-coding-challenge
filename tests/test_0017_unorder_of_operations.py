"""
Script Name : test_0017_unorder_of_operations.py
Description : Test suite for Unorder of Operations
Author      : @tonybnya
"""

import pytest
from fcc_0017_unorder_of_operations import evaluate


@pytest.mark.parametrize(
    "numbers, operators, expected",
    [
        ([5, 6, 7, 8, 9], ["+", "-"], 3),
        ([17, 61, 40, 24, 38, 14], ["+", "%"], 38),
        ([20, 2, 4, 24, 12, 3], ["*", "/"], 60),
        ([11, 4, 10, 17, 2], ["*", "*", "%"], 30),
        ([33, 11, 29, 13], ["/", "-"], -2),
    ],
)
def test_unorder_of_operations(
    numbers: list[int], operators: list[str], expected: int
) -> None:
    assert evaluate(numbers, operators) == expected
