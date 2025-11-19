"""
Script Name : fcc_0004_space_jam.py
Description : SPACEJAM
Author      : @tonybnya

Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

- Non-alphabetical characters should remain unchanged (except for spaces).
"""


def space_jam(s: str) -> str:
    ans: str = ""
    s = s.replace(" ", "")
    for c in s:
        if c.isalpha():
            ans += c.upper() + "  "
        else:
            ans += c + "  "
    return ans.strip()
