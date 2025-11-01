"""
Script Name : challenge_033_check_strength.py
Description : Password Strength
Author      : @tonybnya

Given a password string, return "weak", "medium", or "strong" based
on the strength of the password.

A password is evaluated according to the following rules:

- It is at least 8 characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set:
  !, @, #, $, %, ^, &, or *.

Return "weak" if the password meets fewer than two of the rules.
Return "medium" if the password meets 2 or 3 of the rules.
Return "strong" if the password meets all 4 rules.
"""


def check_length(password) -> bool:
    return len(password) >= 8


def check_cases(password: str) -> bool:
    has_lower: bool = any(char.islower() for char in password)
    has_upper: bool = any(char.isupper() for char in password)
    return has_lower and has_upper


def check_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def check_special_chars(password: str) -> bool:
    special_chars: str = "!@#$%^&*"
    return any(char in special_chars for char in password)


def check_strength(password: str) -> str:
    rules_passed: int = sum([
        check_length(password),
        check_cases(password),
        check_digit(password),
        check_special_chars(password)
    ])

    if rules_passed < 2:
        return 'weak'
    elif rules_passed < 4:
        return 'medium'
    else:
        return 'strong'
