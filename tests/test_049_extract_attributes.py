"""
Script Name : test_049_extract_attributes.py
Description : Test suite for HTML Attribute Extractor coding challenge
Author      : @tonybnya
"""

import pytest
from challenge_049_extract_attributes import extract_attributes


@pytest.mark.parametrize(
    "element, expected",
    [
        ('<span class="red"></span>', ["class, red"]),
        ('<meta charset="UTF-8" />', ["charset, UTF-8"]),
        ("<p>Lorem ipsum dolor sit amet</p>", []),
        (
            '<input name="email" type="email" required="true" />',
            ["name, email", "type, email", "required, true"],
        ),
        (
            '<button id="submit" class="btn btn-primary">Submit</button>',
            ["id, submit", "class, btn btn-primary"],
        ),
    ],
)
def test_extract_attributes(element: str, expected: list[str]) -> None:
    assert extract_attributes(element) == expected
