"""
Script Name : fcc_067_weekday_finder.py
Description : Weekday Finder
Author      : @tonybnya

Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

    "Sunday"
    "Monday"
    "Tuesday"
    "Wednesday"
    "Thursday"
    "Friday"
    "Saturday"

Be sure to ignore time zones.
"""


def get_data(date_string: str) -> tuple[int, int, int]:
    year, month, day = date_string.split("-")
    return int(year), int(month), int(day)


def get_weekday(date_string: str) -> str:
    import datetime

    DAYS: dict[int, str] = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    year, month, day = get_data(date_string)
    week_day: int = datetime.date(year, month, day).weekday()
    return DAYS.get(week_day, "")
