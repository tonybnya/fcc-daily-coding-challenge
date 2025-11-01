"""
Script Name : challenge_016_capitalize.py
Description : Sentence Capitalizer
Author      : @tonybnya

Given a paragraph, return a new paragraph where the first letter
of each sentence is capitalized.

- All other characters should be preserved.
- Sentences can end with a period (.), one or more question marks (?),
  or one or more exclamation points (!).
"""


def capitalize(paragraph: str) -> str:
    res: list[str] = []
    caps: bool = True

    for c in paragraph:
        if caps and c.isalpha():
            res.append(c.upper())
            caps = False
        else:
            res.append(c)

        if c in ('!', '?', '.'):
            caps = True

    return ''.join(res)
