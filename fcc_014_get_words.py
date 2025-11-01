"""
Script Name : challenge_014_get_words.py
Description : Word Frequency
Author      : @tonybnya

Given a paragraph, return an array
of the three most frequently occurring words.

- Words in the paragraph will be separated by spaces.
- Ignore case in the given paragraph.
  For example, treat Hello and hello as the same word.
- Ignore punctuation in the given paragraph.
  Punctuation consists of commas (,), periods (.), and exclamation points (!).
- The returned array should have all lowercase words.
- The returned array should be in descending order
  with the most frequently occurring word first.
"""


def get_words(paragraph: str) -> list[str]:
    IGNORE: list[str] = [',', '.', '!']
    most_freq: list[str] = []

    hmap: dict[str, int] = {}
    for word in paragraph.split():
        if word[-1] in IGNORE:
            word = word[:-1]
        hmap[word.lower()] = hmap.get(word.lower(), 0) + 1

    tuples: list[tuple[str, int]] = sorted(hmap.items(), key=lambda item: item[1], reverse=True)

    for t in tuples[:3]:
        most_freq.append(t[0])

    return most_freq
