"""
Script Name : challenge_013_find_missing_numbers.py
Description : Missing Numbers
Author      : @tonybnya

Given an array of integers from 1 to n, inclusive, return an array
of all the missing integers between 1 and n
(where n is the largest number in the given array).

- The given array may be unsorted and may contain duplicates.
- The returned array should be in ascending order.
- If no integers are missing, return an empty array.
"""


def find_missing_numbers(arr: list[int]) -> list[int]:
    # get the max of arr
    maximum: int = max(arr)

    # init an empty array to hold the missing numbers
    missing: list[int] = []

    # get a set of arr
    hset: set = set(arr)

    # iterate from 1 to max and check in set
    for i in range(1, maximum):
        if i not in hset:
            missing.append(i)
    return missing
