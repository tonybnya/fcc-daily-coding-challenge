"""
Script Name : challenge_008_build_acronym.py
Description : Acronym Builder
Author      : @tonybnya

Given a string containing one or more words,
return an acronym of the words using the following constraints:

- The acronym should consist of the first letter of each word capitalized,
  unless otherwise noted.
- The acronym should ignore the first letter of these words unless they are
  the first word of the given string: a, for, an, and, by, and of.
- The acronym letters should be returned in the order they are given.
- The acronym should not contain any spaces.
"""


def build_acronym(s: str) -> str:
    IGNORE: list[str] = ['a', 'an', 'and', 'by', 'of', 'for']

    acronym: str = ""

    words: list[str] = s.split()
    # i: int = 0
    if words[0].lower() in IGNORE:
        acronym += words[0][0].upper()
        # i += 1

    for i in range(len(words)):
        if words[i].lower() in IGNORE:
            continue
        acronym += words[i][0].upper()

    return acronym
