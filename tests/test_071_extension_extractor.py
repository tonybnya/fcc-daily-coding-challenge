"""
Script Name : test_071_extension_extractor.py
Description : Test suite for Extension Extractor coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_071_extension_extractor import get_extension


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("document.txt", "txt"),
        ("README", "none"),
        ("image.PNG", "PNG"),
        (".gitignore", "gitignore"),
        ("archive.tar.gz", "gz"),
        ("final.draft.", "none"),
    ],
)
def test_extension_extractor(filename: str, expected: str) -> None:
    assert get_extension(filename) == expected
