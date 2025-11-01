"""
Script Name : challenge_022_digits_or_letters.py
Description : Digits vs Letters
Author      : @tonybnya

Given a string, return "digits" if the string has more digits
than letters, "letters" if it has more letters than digits,
and "tie" if it has the same amount of digits and letters.

- Digits consist of 0-9.
- Letters consist of a-z in upper or lower case.
- Ignore any other characters.
"""


def digits_or_letters(s: str) -> str:
    digits, letters = 0, 0

    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            digits += 1

    if letters == digits:
        return 'tie'

    return 'letters' if letters > digits else 'digits'
