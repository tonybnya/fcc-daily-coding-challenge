"""
Script Name : test_016_capitalize.py
Description : Tests for Sentence Capitalizer challenge
Author      : @tonybnya
"""
import pytest
from fcc_016_capitalize import capitalize


@pytest.mark.parametrize(
    "paragraph, expected",
    [
        ("this is a simple sentence.", "This is a simple sentence."),
        ("hello world. how are you?", "Hello world. How are you?"),
        ("i did today's coding challenge... it was fun!!", "I did today's coding challenge... It was fun!!"),
        ("crazy!!!strange???unconventional...sentences.", "Crazy!!!Strange???Unconventional...Sentences."),
        ("there's a space before this period . why is there a space before that period ?", "There's a space before this period . Why is there a space before that period ?")
    ]
)
def test_capitalize(paragraph: str, expected: str) -> None:
    assert capitalize(paragraph) == expected
