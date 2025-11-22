"""
Script Name : test_0013_unnatural_prime.py
Description : Test suite for Unnatural Prime
Author      : @tonybnya
"""

import pytest
from fcc_0013_unnatural_prime import is_unnatural_prime


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, False),
        (-1, False),
        (19, True),
        (-23, True),
        (0, False),
        (97, True),
        (-61, True),
        (99, False),
        (-44, False),
    ],
)
def test_unnatural_prime(n: int, expected: bool) -> None:
    assert is_unnatural_prime(n) == expected
