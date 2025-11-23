"""
Script Name : fcc_0015_camelCase.py
Description : camelCase
Author      : @tonybnya

Given a string, return its camel case version using the following rules:

- Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
- The first word should be all lowercase.
- Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
- All spaces and separators should be removed.
"""


def to_camel_case(s: str) -> str:
    import re

    words: list[str] = re.split(r"[ _-]", s)
    i: int = 0
    while True:
        if not words[i]:
            i += 1
        break
    camelCase: str = words[i].lower()
    for word in words[i + 1 :]:
        camelCase += word.title()
    return camelCase
