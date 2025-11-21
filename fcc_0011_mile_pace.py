"""
Script Name : fcc_0011_mile_pace.py
Description : Mile Pace
Author      : @tonybnya

Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

- Add leading zeros when needed.
"""


def get_mins_and_secs(duration: str) -> tuple[int, int]:
    d: list[str] = duration.split(":")
    mins: int = int(d[0])
    secs: int = int(d[1])
    return mins, secs


def mile_pace(miles: int | float, duration: str) -> str:
    mins, secs = get_mins_and_secs(duration)
    time_in_seconds: int = (mins * 60) + secs
    time_passed = time_in_seconds // miles
    q, r = divmod(time_passed, 60)
    if isinstance(q, float):
        q = int(q)
    if isinstance(r, float):
        r = int(r)
    r_mins: str = str(q)
    r_secs: str = str(r)
    if len(r_mins) == 1:
        r_mins = "0" + r_mins
    if len(r_secs) == 1:
        r_secs = "0" + r_secs
    return f"{r_mins}:{r_secs}"
