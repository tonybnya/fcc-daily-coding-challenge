"""
Script Name : challenge_025_second_largest.py
Description : 2nd Largest
Author      : @tonybnya

Given an array, return the second largest distinct number.
"""


def second_largest(arr: list[int]) -> int:
    # sort
    arr.sort()

    largest: int = arr[-1]
    second: int = 0

    # traverse backwards
    i: int = len(arr) - 2
    while i >= 0:
        if arr[i] == largest:
            i -= 1
        else:
            second = arr[i]
            break

    return second
