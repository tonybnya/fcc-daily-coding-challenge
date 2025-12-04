"""
Script Name : test_080_markdown_heading_converter.py
Description : Test suite for Markdown Heading Converter coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_080_markdown_heading_converter import convert


@pytest.mark.parametrize(
    "heading, expected",
    [
        ("# My level 1 heading", "<h1>My level 1 heading</h1>"),
        ("My heading", "Invalid format"),
        ("##### My level 5 heading", "<h5>My level 5 heading</h5>"),
        ("#My heading", "Invalid format"),
        ("  ###  My level 3 heading", "<h3>My level 3 heading</h3>"),
        ("####### My level 7 heading", "Invalid format"),
        ("## My #2 heading", "<h2>My #2 heading</h2>")
    ]
)
def test_markdown_heading_converter(heading: str, expected: str) -> None:
    assert convert(heading) == expected
