"""
Script Name : challenge_007_parse_roman_numeral.py
Description : Roman Numeral Parser
Author      : @tonybnya

Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol 	Value
I 	    1
V 	    5
X 	    10
L 	    50
C 	    100
D 	    500
M 	    1000

- Numerals are read left to right.
  If a smaller numeral appears before a larger one,
  the value is subtracted. Otherwise, values are added.
"""


def parse_roman_numeral(numeral: str) -> int:
    SYMBOLS: dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    n: int = len(numeral)
    number: int = 0

    i: int = 0
    while i < n:
        if i + 1 < n and SYMBOLS.get(numeral[i], 0) < SYMBOLS.get(numeral[i + 1], 0):
            value = SYMBOLS.get(numeral[i + 1], 0) - SYMBOLS.get(numeral[i], 0)
            i += 2
        else:
            value = SYMBOLS.get(numeral[i], 0)
            i += 1
        number += value

    return number
