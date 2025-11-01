"""
Script Name : challenge_045_strip_tags.py
Description : HTML Tag Stripper
Usage       : python3 challenge_045_strip_tags.py [args]
Author      : @tonybnya

Given a string of HTML code, remove the tags and return the plain text content.

- The input string will contain only valid HTML.
- HTML tags may be nested.
- Remove the tags and any attributes.

For example, '<a href="#">Click here</a>' should return "Click here".
"""


def strip_tags(html: str) -> str:
    is_text_content: bool = True
    text: str = ""
    for char in html:
        if char == "<":
            is_text_content = False
        elif char == ">":
            is_text_content = True
        elif is_text_content:
            text += char
    return text
