"""
Script Name : test_017_generate_slug.py
Description : Slug Generator
Author      : @tonybnya
"""
import pytest
from challenge_017_generate_slug import generate_slug


@pytest.mark.parametrize(
    "string, expected",
    [
        ("helloWorld", "helloworld"),
        ("hello world!", "hello%20world"),
        (" hello-world ", "helloworld"),
        ("hello  world", "hello%20world"),
        ("  ?H^3-1*1]0! W[0%R#1]D  ", "h3110%20w0r1d")
    ]
)
def test_generate_slug(string: str, expected: str) -> None:
    assert generate_slug(string) == expected
