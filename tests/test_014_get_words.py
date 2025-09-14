"""
Script Name : test_014_get_words.py
Description : Tests for Word Frequency challenge
Author      : @tonybnya
"""
import pytest

from challenge_014_get_words import get_words


@pytest.mark.parametrize(
    "paragraph, expected",
    [
        ("Coding in Python is fun because coding Python allows for coding in Python easily while coding", ["coding", "python", "in"]),
        ("I like coding. I like testing. I love debugging!", ["i", "like", "coding"]),
        ("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!", ["debug", "test", "deploy"])
    ]
)
def test_get_words(paragraph: str, expected: list[str]) -> None:
    assert get_words(paragraph) == expected
