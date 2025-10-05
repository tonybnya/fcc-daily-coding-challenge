"""
Script Name : test_035_has_exoplanet.py
Description : Test suite for Exoplanet Search
Author      : @tonybnya
"""
import pytest
from challenge_035_has_exoplanet import has_exoplanet


@pytest.mark.parametrize(
    "readings, expected",
    [
        ("665544554", False),
        ("FGFFCFFGG", True),
        ("MONOPLONOMONPLNOMPNOMP", False),
        ("FREECODECAMP", True),
        ("9AB98AB9BC98A", False),
        ("ZXXWYZXYWYXZEGZXWYZXYGEE", True)
    ]
)
def test_has_exoplanet(readings: str, expected: bool) -> None:
    assert has_exoplanet(readings) == expected
