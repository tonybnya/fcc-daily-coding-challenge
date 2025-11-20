"""
Script Name : fcc_0007_targeted_sum.py
Description : Targeted Sum
Author      : @tonybnya

Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

- The returned array should have the indices in ascending order.
"""


def find_target(arr: list[int], target: int) -> list[int] | str:
    hmap: dict[int, int] = {}
    for i, num in enumerate(arr):
        diff: int = target - num
        if diff not in hmap:
            hmap[num] = i
        else:
            return [hmap[diff], i]
    return "Target not found"
