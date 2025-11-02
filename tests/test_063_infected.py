"""
Script Name : test_063_infected.py
Description : Test suite for Infected
Author      : @tonybnya
"""

import pytest
from fcc_063_infected import infected


@pytest.mark.parametrize(
    "days, expected", [(1, 2), (3, 6), (8, 152), (17, 39808), (25, 5217638)]
)
def test_infected(days: int, expected: int) -> None:
    assert infected(days) == expected
