"""
Script Name : test_075_is_it_the_weekend.py
Description : Test suite for Is It the Weekend?
Author      : @tonybnya
"""

import pytest
from fcc_075_is_it_the_weekend import days_until_weekend


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2025-11-14", "1 day until the weekend."),
        ("2025-01-01", "3 days until the weekend."),
        ("2025-12-06", "It's the weekend!"),
        ("2026-01-27", "4 days until the weekend."),
        ("2026-09-07", "5 days until the weekend."),
        ("2026-11-29", "It's the weekend!"),
    ],
)
def test_is_it_the_weekend(date_string: str, expected: str) -> None:
    assert days_until_weekend(date_string) == expected
