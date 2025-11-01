"""
Script Name : fcc_001_tribonacci_sequence.py
Description : Tribonacci Sequence
Author      : @tonybnya

The Tribonacci sequence is a series of numbers where
each number is the sum of the three preceding ones.
When starting with 0, 0 and 1, the first 10 numbers
in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers
of a Tribonacci sequence, and an integer representing
the length of the sequence, return an array containing
the sequence of the given length.

- Your function should handle sequences of any length
  greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.
"""


def tribonacci(start_sequence: list[int], length: int) -> list[int]:
    n: int = len(start_sequence)
    sequence: list[int] = []

    if length == 0:
        return []

    if length < n:
        for i in range(length):
            sequence.append(start_sequence[i])
        return sequence

    j: int = 0
    while j < n:
        sequence.append(start_sequence[j])
        j += 1

    j -= 1
    steps: int = length - n
    k: int = 0
    while k < steps:
        sequence.append(sequence[j] + sequence[j - 1] + sequence[j - 2])
        j += 1
        k += 1
    return sequence
