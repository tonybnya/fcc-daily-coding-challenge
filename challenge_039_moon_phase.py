"""
Script Name : challenge_039_moon_phase.py
Description : Space Week Day 6: Moon Phase
Author      : @tonybnya

For day six of Space Week,
you will be given a date in the format "YYYY-MM-DD" and need to determine
the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

- "New": days 1 - 7
- "Waxing": days 8 - 14
- "Full": days 15 - 21
- "Waning": days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

- Use "2000-01-06" as a reference new moon (day 1 of the cycle)
  to determine the phase of the given day.
- You will not be given any dates before the reference date.
- Return the correct phase as a string.
"""

def date_cleaner(date_string: str) -> dict[str, int]:
    """
    Clean the date string to easily extract year, month, day.
    """
    year, month, day = map(int, date_string.split('-'))
    return {
        'year': year,
        'month': month,
        'day': day,
    }


def get_diff_days(date_string: str) -> int:
    """
    Calculate the number of days between two dates.
    """
    from datetime import date

    REFERENCE_DATE: str = '2000-01-06'
    datemap_ref: dict[str, int] = date_cleaner(REFERENCE_DATE)
    datemap_input: dict[str, int] = date_cleaner(date_string)

    return (date(**datemap_input) - date(**datemap_ref)).days


def moon_phase(date_string: str) -> str:
    LUNAR_CYCLE: int = 28

    cycle_day: int = (get_diff_days(date_string) % LUNAR_CYCLE) + 1

    match cycle_day:
        case _ if 1 <= cycle_day <= 7:
            return 'New'
        case _ if 8 <= cycle_day <= 14:
            return 'Waxing'
        case _ if 15 <= cycle_day <= 21:
            return 'Full'
        case _ if 22 <= cycle_day <= 28:
            return 'Waning'
        case _:
            return 'Invalid'
