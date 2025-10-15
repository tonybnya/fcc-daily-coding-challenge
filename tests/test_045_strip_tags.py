"""
Script Name : test_045_strip_tags.py
Description : Test suite for HTML Tag Stripper coding challenge
Author      : @tonybnya
"""

import pytest
from challenge_045_strip_tags import strip_tags


@pytest.mark.parametrize(
    "html, text",
    [
        ('<a href="#">Click here</a>', "Click here"),
        ('<p class="center">Hello <b>World</b>!</p>', "Hello World!"),
        ('<img src="cat.jpg" alt="Cat">', ""),
        (
            '<main id="main"><section class="section">section</section><section class="section">section</section></main>',
            "sectionsection",
        ),
    ],
)
def test_strip_tags(html: str, text: str) -> None:
    assert strip_tags(html) == text
