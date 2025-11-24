"""
Script Name : test_0016_reverse_parenthesis.py
Description : Test suite for Reverse Parenthesis
Author      : @tonybnya
"""

import pytest
from fcc_0016_reverse_parenthesis import decode


@pytest.mark.parametrize(
    "s, expected",
    [
        ("(f(b(dc)e)a)", "abcdef"),
        ("((is?)(a(t d)h)e(n y( uo)r)aC)", "Can you read this?"),
        ("f(Ce(re))o((e(aC)m)d)p", "freeCodeCamp"),
    ],
)
def test_reverse_parenthesis(s: str, expected: str) -> None:
    assert decode(s) == expected
