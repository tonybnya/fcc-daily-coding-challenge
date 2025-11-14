"""
Script Name : fcc_075_is_it_the_weekend.py
Description : Is It the Weekend?
Author      : @tonybnya

Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

- The weekend starts on Saturday.
- If the given date is Saturday or Sunday, return "It's the weekend!".
- Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
- If X is 1, use "day" (singular) instead of "days" (plural).
- Make sure the calculation ignores your local timezone.
"""


def get_data(date_string: str) -> tuple[int, int, int]:
    year, month, day = date_string.split("-")
    return int(year), int(month), int(day)


def days_until_weekend(date_string: str) -> str:
    import datetime

    year, month, day = get_data(date_string)
    week_day: int = datetime.date(year, month, day).weekday()
    if week_day in (5, 6):
        return "It's the weekend!"
    gap = 5 - week_day
    if gap == 1:
        prefix = "1 day "
    else:
        prefix = f"{gap} days "

    return prefix + "until the weekend."
