"""
Script Name : test_091_ai_detector.py
Description : Test suite for AI Detector coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_091_ai_detector import detect_ai


@pytest.mark.parametrize(
    "text, expected",
    [
        ("The quick brown fox jumped over the lazy dog.", "Human"),
        ("The hypersonic brown fox - jumped (over) the lazy dog.", "Human"),
        ("Yes - you're right! I made a mistake there - let me try again.", "AI"),
        ("The extraordinary students were studying vivaciously.", "AI"),
        ("The (excited) student was (coding) in the library.", "AI")
    ]
)
def test_ai_detector(text: str, expected: str) -> None:
    assert detect_ai(text) == expected
