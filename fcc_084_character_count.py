"""
Script Name : fcc_084_character_count.py
Description : Character Count
Author      : @tonybnya

Given a sentence string, return an array with a count of each character in alphabetical order.

- Treat upper and lowercase letters as the same letter when counting.
- Ignore numbers, spaces, punctuation, etc.
- Return the count and letter in the format "letter count". For instance, "a 3".
- All returned letters should be lowercase.
- Do not return a count of letters that are not in the given string.
"""


def count_characters(sentence: str) -> list[str]:
    hmap: dict[str, int] = {}
    res: list[str] = []
    for c in sentence:
        if c.isalpha():
            hmap[c.lower()] = hmap.get(c.lower(), 0) + 1
    chars: list[str] = []
    for k in hmap:
        chars.append(k)
    chars.sort()
    for c in chars:
        res.append(f"{c} {hmap[c]}")
    return res
