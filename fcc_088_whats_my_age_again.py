"""
Script Name : fcc_088_whats_my_age_again.py
Description : What's My Age Again?
Author      : @tonybnya

Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

- Assume all birthdays are valid dates before November 27th, 2025.
- Return the age as an integer.
- Be sure to account for whether the person has already had their birthday in 2025.
"""

from datetime import datetime


def calculate_age(birthday: str) -> int:
    TARGET_DATE = datetime(2025, 11, 27)
    # Convert input birthday string to a date object
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    # Basic year difference
    age = TARGET_DATE.year - birth_date.year
    # Adjust if the person has NOT had their birthday yet in 2025
    if (TARGET_DATE.month, TARGET_DATE.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
