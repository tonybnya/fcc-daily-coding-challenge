"""
Script Name : test_008_build_acronym.py
Description : Tests for Acronym Builder challenge
Author      : @tonybnya
"""
import pytest

from fcc_008_build_acronym import build_acronym


@pytest.mark.parametrize(
    "s, acronym",
    [
        ("Search Engine Optimization", "SEO"),
        ("Frequently Asked Questions", "FAQ"),
        ("National Aeronautics and Space Administration", "NASA"),
        ("Federal Bureau of Investigation", "FBI"),
        ("For your information", "FYI"),
        ("By the way", "BTW"),
        ("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily", "AUHWPOTIMSH")
    ]
)
def test_build_acronym(s: str, acronym: str) -> None:
    assert build_acronym(s) == acronym
