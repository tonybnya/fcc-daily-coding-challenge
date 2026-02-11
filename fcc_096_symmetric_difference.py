"""
Script Name : fcc_096_symmetric_difference.py
Description : Symmetric Difference
Author      : @tonybnya

Given two arrays, return a new array containing the symmetric difference of them.

- The symmetric difference between two sets is the set of values that appear in either set, but not both.
- Return the values in the order they first appear in the input arrays.
"""


def difference(arr1: list[int | str], arr2: list[int | str]) -> list[int | str]:
    from collections import OrderedDict

    od: OrderedDict = OrderedDict()

    for item in arr1 + arr2:
        od[item] = od.get(item, 0) + 1

    return [item for item, count in od.items() if count == 1]