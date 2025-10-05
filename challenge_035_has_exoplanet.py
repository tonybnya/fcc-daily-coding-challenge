"""
Script Name : challenge_035_has_exoplanet.py
Description : Space Week Day 2: Exoplanet Search
Author      : @tonybnya

For the second day of Space Week, you are given a string where each
character represents the luminosity reading of a star. Determine if
the readings have detected an exoplanet using the transit method.
The transit method is when a planet passes in front of a star,
reducing its observed luminosity.

- Luminosity readings only comprise of characters 0-9 and A-Z where
  each reading corresponds to the following numerical values:
- Characters 0-9 correspond to luminosity levels 0-9.
- Characters A-Z correspond to luminosity levels 10-35.

A star is considered to have an exoplanet if any single reading is
less than or equal to 80% of the average of all readings.
For example, if the average luminosity of a star is 10, it would be
considered to have a exoplanet if any single reading is 8 or less.
"""


def has_exoplanet(readings: str) -> bool:
    luminosities: dict[str, int] = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35
    }

    s: int = sum(luminosities[char] for char in readings)
    avg: float = s / len(readings)

    for luminosity in readings:
        if luminosities[luminosity] <= (avg * 80) / 100:
            return True

    return False
