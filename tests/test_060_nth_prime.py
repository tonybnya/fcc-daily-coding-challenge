"""
Script Name : test_060_nth_prime.py
Description : Test suite for Nth Prime
Author      : @tonybnya
"""

import pytest
from fcc_060_nth_prime import nth_prime


@pytest.mark.parametrize(
    "n, expected", [(5, 11), (10, 29), (16, 53), (99, 523), (1000, 7919)]
)
def test_nth_prime(n: int, expected: int) -> None:
    assert nth_prime(n) == expected
