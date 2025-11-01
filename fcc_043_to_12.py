"""
Script Name : challenge_043_to_12.py
Description : 24 to 12
Author      : @tonybnya

Given a string representing a time of the day in the 24-hour format of "HHMM",
return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

- The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
"""

AM: dict[str, int] = {
    "00": 12,
    "01": 1,
    "02": 2,
    "03": 3,
    "04": 4,
    "05": 5,
    "06": 6,
    "07": 7,
    "08": 8,
    "09": 9,
    "10": 10,
    "11": 11,
}

PM: dict[str, int] = {
    "12": 12,
    "13": 1,
    "14": 2,
    "15": 3,
    "16": 4,
    "17": 5,
    "18": 6,
    "19": 7,
    "20": 8,
    "21": 9,
    "22": 10,
    "23": 11,
}


def clean_hour(hour: str) -> int:
    return int(hour)


def get_time(time: str) -> tuple[str, str]:
    return time[:2], time[2:]


def to_12(time: str) -> str:
    RESET_POINT: int = 12
    hour, min = get_time(time)
    suffix: str = ""
    if clean_hour(hour) < RESET_POINT:
        suffix = "AM"
        h = AM[hour]
    else:
        suffix = "PM"
        h = PM[hour]
    time_format: str = f"{str(h)}:{min} {suffix}"
    return time_format
