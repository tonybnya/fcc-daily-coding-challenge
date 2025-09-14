"""
Script Name : challenge_004_repeat_vowels.py
Description : Vowel Repeater
Author      : @tonybnya

Given a string, return a new version of the string where each vowel
is duplicated one more time than the previous vowel you encountered.
For instance, the first vowel in the sentence should remain unchanged.
The second vowel should appear twice in a row.
The third vowel should appear three times in a row, and so on.

- The letters a, e, i, o, and u, in either uppercase or lowercase,
  are considered vowels.
- The original vowel should keeps its case.
- Repeated vowels should be lowercase.
- All non-vowel characters should keep their original case.
"""


def repeat_vowels(s: str) -> str:
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    res: list[str] = []

    repeater: int = 0
    for c in s:
        if c.lower() in vowels:
            res.append(c + c.lower() * repeater)
            repeater += 1
        else:
            res.append(c)

    return ''.join(res)
