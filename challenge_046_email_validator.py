"""
Script Name : challenge_046_email_validator.py
Description : Email Validator
Author      : @tonybnya

Given a string, determine if it is a valid email address using the following constraints:

- It must contain exactly one @ symbol.
- The local part (before the @):
    - Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
    - Cannot start or end with a dot.
- The domain part (after the @):
    - Must contain at least one dot.
    - Must end with a dot followed by at least two letters.
- Neither the local or domain part can have two dots in a row.

"""


def dots_in_row(s: str) -> bool:
    """
    Check if a string have two dots in a row or not.
    """
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == "." and s[i + 1] == ".":
            return True
    return False


def domain_part_checker(domain_part: str) -> bool:
    """
    Validate domain part of the email
    """
    if "." not in domain_part:
        return False
    if dots_in_row(domain_part):
        return False
    _, end = domain_part.rsplit(".", 1)
    if len(end) < 2:
        return False
    if not end.isalpha():
        return False
    return True


def local_part_checker(local_part: str) -> bool:
    """
    Validate local part of the email
    """
    SPECIALS: list[str] = [".", "_", "-"]
    if local_part.startswith(".") or local_part.endswith("."):
        return False
    if dots_in_row(local_part):
        return False
    for c in local_part:
        if not (c.isalpha() or c.isdigit() or c in SPECIALS):
            return False
    return True


def validate(email: str) -> bool:
    SEP: str = "@"
    parts: list[str] = email.split(SEP)
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    return domain_part_checker(domain_part) and local_part_checker(local_part)
