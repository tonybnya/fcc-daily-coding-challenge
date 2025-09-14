"""
Script Name : challenge_012_too_much_screen_time.py
Description : Screen Time
Author      : @tonybnya

Given an input array of seven integers, representing a week's time,
where each integer is the amount of hours spent on your phone that day,
determine if it is too much screen time based on these constraints:

- If any single day has 10 hours or more, it's too much.
- If the average of any three days in a row is greater than
  or equal to 8 hours, it’s too much.
- If the average of the seven days is greater than
  or equal to 6 hours, it's too much.
"""


def too_much_screen_time(hours: list[int]) -> bool:
    n: int = len(hours)

    # average of the seven days
    if sum(hours) // n >= 6:
        return True

    # average of any three days in a row
    window: int = 3
    i: int = 0
    while i < n - 2:
        # check if any hour is >= 10
        for h in hours[i: i + window]:
            if h >= 10:
                return True
        if sum(hours[i: i + window]) // window >= 8:
            return True
        i += 1
    return False
