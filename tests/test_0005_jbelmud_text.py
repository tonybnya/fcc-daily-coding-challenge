"""
Script Name : test_0005_jbelmud_text.py
Description : Test suite for Jbelmud Text
Author      : @tonybnya
"""

import pytest
from fcc_0005_jbelmud_text import jbelmu


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "hello wlord"),
        ("i love jumbled text", "i love jbelmud text"),
        (
            "freecodecamp is my favorite place to learn to code",
            "faccdeeemorp is my faiortve pacle to laern to cdoe",
        ),
        (
            "the quick brown fox jumps over the lazy dog",
            "the qciuk borwn fox jmpus oevr the lazy dog",
        ),
    ],
)
def test_jbelmud_text(text: str, expected: str) -> None:
    assert jbelmu(text) == expected
