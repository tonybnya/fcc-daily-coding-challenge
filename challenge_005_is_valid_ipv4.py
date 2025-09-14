"""
Script Name : challenge_005_is_valid_ipv4.py
Description : IPv4 Validator
Author      : @tonybnya

Given a string, determine if it is a valid IPv4 Address.
A valid IPv4 address consists of four integer numbers separated by dots (.).
Each number must satisfy the following conditions:

- It is between 0 and 255 inclusive.
- It does not have leading zeros (e.g. 0 is allowed, 01 is not).
- Only numeric characters are allowed.
"""


def checker(chunck: str) -> bool:
    if not chunck.isdigit():
        return False
    if int(chunck) < 0 or int(chunck) > 255:
        return False
    if chunck.startswith('0') and len(chunck) > 1:
        return False
    return True


def is_valid_ipv4(ipv4: str) -> bool:
    if '.' not in ipv4:
        return False
    if ipv4.endswith('.'):
        return False

    nums: list[str] = [x for x in ipv4.split('.')]

    return all([checker(num) for num in nums])
