"""
Script Name : challenge_056_duration_formatter.py
Description : Duration Formatter
Author      : @tonybnya

Given an integer number of seconds,
return a string representing the same duration in the format "H:MM:SS",
where "H" is the number of hours,
"MM" is the number of minutes,
and "SS" is the number of seconds.
Return the time using the following rules:

- Seconds: Should always be two digits.
- Minutes: Should omit leading zeros when they aren't needed.
  Use "0" if the duration is less than one minute.
- Hours: Should be included only if they're greater than zero.
"""


def format(seconds: int) -> str:
    HOURS_TO_SECONDS: int = 3600
    MINS_TO_SECONDS: int = 60
    str_duration: str = ""
    if seconds < HOURS_TO_SECONDS:
        mins, secs = divmod(seconds, MINS_TO_SECONDS)
        if len(str(secs)) == 1:
            secs = f"0{str(secs)}"
        else:
            secs = str(secs)
        mins = str(mins)
        str_duration = f"{mins}:{secs}"
    else:
        hours, remainder = divmod(seconds, HOURS_TO_SECONDS)
        mins, secs = divmod(remainder, MINS_TO_SECONDS)
        if len(str(mins)) == 1:
            mins = f"0{str(mins)}"
        else:
            mins = str(mins)
        if len(str(secs)) == 1:
            secs = f"0{str(secs)}"
        else:
            secs = str(secs)
        str_duration = f"{hours}:{mins}:{secs}"
    return str_duration
