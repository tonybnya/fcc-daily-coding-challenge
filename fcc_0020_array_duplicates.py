"""
Script Name : fcc_0020_array_duplicates.py
Description : Array Duplicates
Author      : @tonybnya

Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

- Only include one instance of each value in the returned array.
"""


def find_duplicates(arr: list[int]) -> list[int]:
    hmap: dict[int, int] = {}
    lst: list[int] = []
    for num in arr:
        hmap[num] = hmap.get(num, 0) + 1
    for num in hmap:
        if hmap[num] > 1:
            lst.append(num)
    return sorted(lst)
