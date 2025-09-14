"""
Script Name : test_005_is_valid_ipv4.py
Description : Tests for IPv4 Validator challenge
Author      : @tonybnya
"""
import pytest

from challenge_005_is_valid_ipv4 import is_valid_ipv4


@pytest.mark.parametrize(
    "ipv4, expected",
    [
        ("192.168.1.1", True),
        ("0.0.0.0", True),
        ("255.01.50.111", False),
        ("255.00.50.111", False),
        ("256.101.50.115", False),
        ("192.168.101.", False),
        ("192168145213", False)
    ]
)
def test_is_valid_ipv4(ipv4: str, expected: bool) -> None:
    assert is_valid_ipv4(ipv4) == expected
