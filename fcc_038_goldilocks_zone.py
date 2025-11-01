"""
Script Name : challenge_038_goldilocks_zone.py
Description : Space Week Day 5: Goldilocks Zone
Author      : @tonybnya

For the fifth day of Space Week,
you will calculate the "Goldilocks zone" of a star
- the region around a star where conditions are
  "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and
end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

1. Find the luminosity of the star by raising its mass to the power of 3.5.
2. The start of the zone is 0.95 times the square root of its luminosity.
3. The end of the zone is 1.37 times the square root of its luminosity.

- Return the distances rounded to two decimal places.

For example, given 1 as a mass, return [0.95, 1.37].
"""


def goldilocks_zone(mass: float) -> list[float]:
    from math import sqrt

    POWER: float = 3.5
    START_TIMES = 0.95
    END_TIMES = 1.37

    luminosity: float = mass ** POWER

    s: float = START_TIMES * sqrt(luminosity)
    e: float = END_TIMES * sqrt(luminosity)

    start: float = float(f"{s:.2f}")
    end: float = float(f"{e:.2f}")

    return [start, end]
