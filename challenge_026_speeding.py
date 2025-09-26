"""
Script Name : challenge_026_speeding.py
Description : Caught Speeding
Author      : @tonybnya

Given an array of numbers representing the speed at which vehicles
were observed traveling, and a number representing the speed limit,
return an array with two items, the number of vehicles that were
speeding, followed by the average amount beyond the speed limit
of those vehicles.

- If there were no vehicles speeding, return [0, 0].
"""


def speeding(speeds: list[int], limit: int) -> list[int | float]:
    beyonds: list[int] = []

    for speed in speeds:
        if speed > limit:
            beyonds.append(speed - limit)

    if not beyonds:
        return [0, 0]

    return [len(beyonds), sum(beyonds) / len(beyonds)]
