"""
Script Name : challenge_027_is_spam.py
Description : Spam Detector
Author      : @tonybnya

Given a phone number in the format "+A (BBB) CCC-DDDD",
where each letter represents a digit as follows:

- A represents the country code and can be any number of digits.
- BBB represents the area code and will always be three digits.
- CCC and DDDD represent the local number and will always be three
  and four digits long, respectively.

Determine if it's a spam number based on the following criteria:

- The country code is greater than 2 digits long or doesn't begin
  with a zero (0).
- The area code is greater than 900 or less than 200.
- The sum of first three digits of the local number appears within
  last four digits of the local number.
- The number has the same digit four or more times in a row
  (ignoring the formatting characters).
"""


def cleaner(s: str) -> list[int]:
    # helper function to remove formatting characters in a number
    clean_number: list[int] = []
    for c in s:
        if c.isdigit():
            clean_number.append(int(c))
    return clean_number


def is_spam(number: str) -> bool:
    # get the different parts: country and area codes + local number
    country_code, area_code, local_number = number.split()
    # get the three and four digits parts of the local number
    part1, part2 = local_number.split('-')

    # check country code is greater than 2 digits or
    # doesn't begin with a zero (0)
    if country_code[1] != '0' or len(country_code[1:]) > 2:
        return True

    # check if the area code is greater than 900 or less than 200
    if int(area_code[1:-1]) > 900 or int(area_code[1:-1]) < 200:
        return True

    # sum the first three digits of the local number and
    # check if the result is in the second part (last four digits)
    sp1 = sum(int(digit) for digit in part1)
    if str(sp1) in part2:
        return True

    # clean the number: ignoring formatting characters
    numbers: list[int] = cleaner(number)

    # check if the number has the same digit four or
    # more times in a row
    window: int = 3
    i: int = 0
    while window != len(numbers):
        if len(set(numbers[i:window+1])) == 1:
            return True
        i += 1
        window += 1

    return False
