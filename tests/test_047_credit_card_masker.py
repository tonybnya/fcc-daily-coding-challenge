"""
Script Name : test_047_credit_card_masker.py
Description : Test suite for Credit Card Masker coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_047_credit_card_masker import mask


@pytest.mark.parametrize(
    "card, expected",
    [
        ("4012-8888-8888-1881", "****-****-****-1881"),
        ("5105 1051 0510 5100", "**** **** **** 5100"),
        ("6011 1111 1111 1117", "**** **** **** 1117"),
        ("2223-0000-4845-0010", "****-****-****-0010"),
    ],
)
def test_credit_card_masker(card: str, expected: str) -> None:
    assert mask(card) == expected
