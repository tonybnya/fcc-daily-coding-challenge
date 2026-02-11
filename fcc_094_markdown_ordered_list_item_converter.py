"""
Script Name : fcc_094_markdown_ordered_list_item_converter.py
Description : Markdown Ordered List Item Converter
Author      : @tonybnya
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
