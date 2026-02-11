"""
Script Name : fcc_094_markdown_ordered_list_item_converter.py
Description : Markdown Ordered List Item Converter
Author      : @tonybnya

Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

- Start with zero or more spaces, followed by
- A number (1 or greater) and a period (.), followed by
- At least one space, and then
- The list item text.

If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""


def get_first_digit_index(text: str) -> int:
    for index, char in enumerate(text):
        if char.isdigit():
            return index
    return -1


def convert_list_item(markdown: str) -> str:
    if markdown and (markdown[0].isspace() or (markdown[0].isdigit() and markdown[0] != '0')):
        first_digit_index: int = get_first_digit_index(markdown)
        if first_digit_index == -1:
            return 'Invalid format'
        if markdown[first_digit_index + 1] != '.':
            return 'Invalid format'

        ptr: int = first_digit_index + 1
        while not markdown[ptr].isalnum():
            ptr += 1

        return f'<li>{markdown[ptr:]}</li>'

    return 'Invalid format'
