"""
Script Name : challenge_030_format_number.py
Description : Phone Number Formatter
Author      : @tonybnya

Given a string of ten digits, return the string as a phone number
in this format: "+D (DDD) DDD-DDDD".
"""


def format_number(number: str) -> str:
    phonenumber = ''

    phonenumber += '+' + number[0] + ' '
    phonenumber += '(' + number[1:4] + ')' + ' '
    phonenumber += number[4:7] + '-' + number[7:]

    return phonenumber
