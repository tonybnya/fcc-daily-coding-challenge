"""
Script Name : test_0015_camelCase.py
Description : Test suite for camelCase
Author      : @tonybnya
"""

import pytest
from fcc_0015_camelCase import to_camel_case


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello world", "helloWorld"),
        ("HELLO WORLD", "helloWorld"),
        ("secret agent-X", "secretAgentX"),
        ("FREE cODE cAMP", "freeCodeCamp"),
        (
            "ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk",
            "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk",
        ),
    ],
)
def test_camelCase(s: str, expected: str) -> None:
    assert to_camel_case(s) == expected
