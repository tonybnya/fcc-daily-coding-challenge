"""
Script Name : test_011_reverse_sentence.py
Description : Tests for Reverse Sentence challenge
Author      : @tonybnya
"""
import pytest

from fcc_011_reverse_sentence import reverse_sentence


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("world hello", "hello world"),
        ("push commit git", "git commit push"),
        ("npm  install   apt    sudo", "sudo apt install npm"),
        ("import    default   function  export", "export function default import")
    ]
)
def test_reverse_sentence(sentence: str, expected: str):
    assert reverse_sentence(sentence) == expected
