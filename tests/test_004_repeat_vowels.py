"""
Script Name : test_004_repeat_vowels.py
Description : Tests for Vowel Repeater challenge
Author      : @tonybnya
"""
import pytest

from fcc_004_repeat_vowels import repeat_vowels


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello world", "helloo wooorld"),
        ("freeCodeCamp", "freeeCooodeeeeCaaaaamp"),
        ("AEIOU", "AEeIiiOoooUuuuu"),
        ("I like eating ice cream in Iceland", "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand")
    ]
)
def test_repeat_vowels(s: str, expected: str) -> None:
    assert repeat_vowels(s) == expected
