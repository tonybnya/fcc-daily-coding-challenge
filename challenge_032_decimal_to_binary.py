"""
Script Name : challenge_032_decimal_to_binary.py
Description : Decimal to Binary
Author      : @tonybnya

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number.
To convert a decimal number to binary, repeatedly divide the number
by 2 and record the remainder. Repeat until the number is zero.
Read the remainders last recorded to first.
For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

12 in binary is 1100.
"""


def to_binary(decimal: int) -> str:
    base: int = 2
    limit: int = 0
    binary: str = ''

    while decimal > limit:
        quotient, remainder = divmod(decimal, base)
        decimal = quotient
        binary += str(remainder)

    return binary[::-1]
