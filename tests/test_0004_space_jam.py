"""
Script Name : test_0004_space_jam.py
Description : Test suite for SPACEJAM
Author      : @tonybnya
"""

import pytest
from fcc_0004_space_jam import space_jam


@pytest.mark.parametrize(
    "s, expected",
    [
        ("freeCodeCamp", "F  R  E  E  C  O  D  E  C  A  M  P"),
        ("   free   Code   Camp   ", "F  R  E  E  C  O  D  E  C  A  M  P"),
        ("Hello World?!", "H  E  L  L  O  W  O  R  L  D  ?  !"),
        ("C@t$ & D0g$", "C  @  T  $  &  D  0  G  $"),
        ("allyourbase", "A  L  L  Y  O  U  R  B  A  S  E"),
    ],
)
def test_space_jam(s: str, expected: str) -> None:
    assert space_jam(s) == expected
