"""
Script Name : challenge_017_generate_slug.py
Description : Slug Generator
Author      : @tonybnya

Given a string, return a URL-friendly version of the string
using the following constraints:

- All letters should be lowercase.
- All characters that are not letters, numbers, or spaces should be removed.
- All spaces should be replaced with the URL-encoded space code %20.
- Consecutive spaces should be replaced with a single %20.
- The returned string should not have leading or trailing %20.
"""


def cleaner(s: str) -> str:
    res: list[str] = []
    for c in s:
        if c.isalnum():
            res.append(c.lower())

    return ''.join(res)


def generate_slug(string: str) -> str:
    words: list[str] = []
    space_code: str = '%20'
    for word in string.strip().split():
        words.append(cleaner(word))

    return f'{space_code}'.join(words)
