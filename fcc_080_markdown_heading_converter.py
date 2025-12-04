"""
Script Name : fcc_080_markdown_heading_converter.py
Description : Markdown Heading Converter
Author      : @tonybnya

Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

- Start with zero or more spaces, followed by
- 1 to 6 hash characters (#) in a row, then
- At least one space. And finally,
- The heading text.

The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""


def convert(heading: str) -> str:
    start: str = ""
    i: int = 0
    while not heading[i].isalpha():
        start += heading[i]
        i += 1
    if "#" not in start or " " not in start:
        return "Invalid format"
    text: str = heading[len(start):]
    hashes: str = len(start.strip())
    if hashes > 6:
        return "Invalid format"
    return f"<h{hashes}>{text}</h{hashes}>"
