"""
Script Name : challenge_047_credit_card_masker.py
Description : Credit Card Masker
Author      : @tonybnya

Given a string of credit card numbers, return a masked version of it
using the following constraints:

- The string will contain four sets of four digits (0-9),
  with all sets being separated by a single space, or a single hyphen (-).
- Replace all numbers, except the last four, with an asterisk (*).
- Leave the remaining characters unchanged.

For example, given "4012-8888-8888-1881" return "****-****-****-1881".
"""


def mask(card: str) -> str:
    ASTERISK: str = "*"
    SEP: list[str] = ["-", " "]
    LIMIT: int = -5
    remaining: str = card[LIMIT:]
    lst: list[str] = []
    for i in range(len(card[:LIMIT])):
        substitute: str = ""
        if card[i] in SEP:
            substitute = card[i]
        else:
            substitute = ASTERISK
        lst.append(substitute)
    return "".join(lst) + remaining
