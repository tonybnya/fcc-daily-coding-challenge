"""
Script Name : fcc_092_miles_to_kilometers.py
Description : Miles to Kilometers
Author      : @tonybnya

Given a distance in miles as a number, return the equivalent distance in kilometers.

- The input will always be a non-negative number.
- 1 mile equals 1.60934 kilometers.
- Round the result to two decimal places.
- Remove unnecessary trailing zeros from the rounded result.
"""


def convert_to_km(miles: int | float) -> int | float:
    KM: float = 1.60934
    return round(miles * KM, 2)
