"""
Script Name : fcc_097_date_formatter.py
Description : Date Formatter
Author      : @tonybnya

Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

- The given month will be the full English month name. For example: "January", "February", etc.
- In the return value, pad the month and day with leading zeros if necessary to ensure two digits.

For example, given "December 6, 2025", return "2025-12-06".
"""


def format_date(date_string: str) -> str:
    MONTHS: dict[str, str] = {
        'january': '01',
        'february': '02',
        'march': '03',
        'april': '04',
        'may': '05',
        'june': '06',
        'july': '07',
        'august': '08',
        'september': '09',
        'october': '10',
        'november': '11',
        'december': '12',
    }
    parts, year = date_string.split(', ')
    m, d = parts.split()

    if m.lower() in MONTHS:
        month: str = MONTHS[m.lower()]

    if len(d) == 1:
        day: str = f'0{d}'
    else:
        day: str = d

    return f'{year}-{month}-{day}'
