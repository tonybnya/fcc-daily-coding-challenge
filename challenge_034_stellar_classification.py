"""
Script Name : challenge_034_stellar_classification.py
Description : Space Week Day 1: Stellar Classification
Author      : @tonybnya

October 4th marks the beginning of World Space Week.
The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star
in Kelvin (K) and need to determine its stellar classification based
on the following ranges:

"O": 30,000 K or higher
"B": 10,000 K - 29,999 K
"A": 7,500 K - 9,999 K
"F": 6,000 K - 7,499 K
"G": 5,200 K - 5,999 K
"K": 3,700 K - 5,199 K
"M": 0 K - 3,699 K

Return the classification of the given star.
"""


def classification(temp: int) -> str:
    match temp:
        case _ if 0 <= temp <= 3699:
            return "M"
        case _ if 3700 <= temp <= 5199:
            return "K"
        case _ if 5200 <= temp <= 5999:
            return "G"
        case _ if 6000 <= temp <= 7499:
            return "F"
        case _ if 7500 <= temp <= 9999:
            return "A"
        case _ if 10000 <= temp <= 29999:
            return "B"
        case _ if temp >= 30000:
            return "O"
        case _:
            return "Invalid"
