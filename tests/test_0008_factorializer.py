"""
Script Name : test_0008_factorializer.py
Description : Test suite for Factorializer coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_0008_factorializer import factorial


@pytest.mark.parametrize("n, expected", [(0, 1), (5, 120), (20, 2432902008176640000)])
def test_factorializer(n: int, expected: int) -> None:
    assert factorial(n) == expected
