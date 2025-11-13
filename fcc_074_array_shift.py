"""
Script Name : fcc_074_array_shift.py
Description : Array Shift
Author      : @tonybnya

Given an array and an integer representing how many positions to shift the array, return the shifted array.

- A positive integer shifts the array to the left.
- A negative integer shifts the array to the right.
- The shift wraps around the array.

For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""


def right_shift(arr: list[int | str], n: int) -> None:
    for _ in range(n):
        last_element: int | str = arr.pop()
        arr.insert(0, last_element)


def left_shift(arr: list[int | str], n: int) -> None:
    for _ in range(n):
        first_element: int | str = arr.pop(0)
        arr.append(first_element)


def shift_array(arr: list[int | str], n: int) -> list[int | str]:
    if n < 0:
        n *= -1
        right_shift(arr, n)
    else:
        left_shift(arr, n)
    return arr
