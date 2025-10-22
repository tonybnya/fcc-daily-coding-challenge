"""
Script Name : test_052_wise_speak.py
Description : Test suite for Speak Wisely, You Must
Author      : @tonybnya
"""

import pytest
from challenge_052_wise_speak import wise_speak


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("You must speak wisely.", "Speak wisely, you must."),
        ("You can do it!", "Do it, you can!"),
        (
            "Do you think you will complete this?",
            "Complete this, do you think you will?",
        ),
        ("All your base are belong to us.", "Belong to us, all your base are."),
        ("You have much to learn.", "Much to learn, you have."),
    ],
)
def test_wise_speak(sentence: str, expected: str) -> None:
    assert wise_speak(sentence) == expected
