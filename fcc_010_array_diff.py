"""
Script Name : challenge_010_array_diff.py
Description : Array Diff
Author      : @tonybnya

Given two arrays with strings values, return a new array containing
all the values that appear in only one of the arrays.

- The returned array should be sorted in alphabetical order.
"""


def array_diff(arr1: list[str], arr2: list[str]) -> list[str]:
    diff: list[str] = []
    hmap: dict[str, int] = {}

    for s in arr1:
        hmap[s] = hmap.get(s, 0) + 1

    for s in arr2:
        hmap[s] = hmap.get(s, 0) + 1

    for key, val in hmap.items():
        if val == 1:
            diff.append(key)

    return sorted(diff)
