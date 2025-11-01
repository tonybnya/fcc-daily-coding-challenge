"""
Script Name : test_061_spooky_case.py
Description : Test suite for Spooky Case
Author      : @tonybnya
"""

import pytest
from fcc_061_spooky_case import spookify


@pytest.mark.parametrize(
    "boo, expected",
    [
        ("hello_world", "HeLlO~wOrLd"),
        ("Spooky_Case", "SpOoKy~CaSe"),
        ("TRICK-or-TREAT", "TrIcK~oR~tReAt"),
        ("c_a-n_d-y_-b-o_w_l", "C~a~N~d~Y~~b~O~w~L"),
        ("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts", "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"),
    ],
)
def test_spooky_case(boo: str, expected: str) -> None:
    assert spookify(boo) == expected
