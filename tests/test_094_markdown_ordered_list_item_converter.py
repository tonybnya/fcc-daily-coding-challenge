"""
Script Name : test_094_markdown_ordered_list_item_converter.py
Description : Test suite for Markdown Ordered List Item Converter coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_094_markdown_ordered_list_item_converter import convert_list_item


@pytest.mark.parametrize(
    "markdown, expected",
    [
        ("1. My item", "<li>My item</li>"),
        (" 1.  Another item", "<li>Another item</li>"),
        ("1 . invalid item", "Invalid format"),
        ("2. list item text", "<li>list item text</li>"),
        (". invalid again", "Invalid format"),
        ("A. last invalid", "Invalid format"),
    ]
)
def test_markdown_ordered_list_item_converter(markdown: str, expected: str) -> None:
    assert convert_list_item(markdown) == expected
