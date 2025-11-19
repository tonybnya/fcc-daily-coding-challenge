"""
Script Name : fcc_0005_jbelmud_text.py
Description : Jbelmud Text
Author      : @tonybnya

Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

- The first and last letters of the words remain in place
- All letters between the first and last letter are sorted alphabetically.
- The input strings will contain no punctuation, and will be entirely lowercase.
"""


def transformer(s: str) -> str:
    if len(s) == 1:
        return s
    first_letter: str = s[0]
    last_letter: str = s[-1]
    remain: str = s[1:-1]
    lst: list[str] = list(remain)
    lst.sort()
    return first_letter + "".join(lst) + last_letter


def jbelmu(text: str) -> str:
    words: list[str] = text.split()
    lst: list[str] = []
    for word in words:
        lst.append(transformer(word))
    return " ".join(lst)
