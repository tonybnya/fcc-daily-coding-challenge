"""
Script Name : fcc_0003_fibonacci_sequence.py
Description : Fibonacci Sequence
Author      : @tonybnya

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.
"""


def fibonacci_sequence(start_sequence: list[int], lenght: int) -> list[int]:
    n: int = len(start_sequence)
    sequence: list[int] = []
    if lenght == 0:
        return sequence
    if lenght <= n:
        for i in range(lenght):
            sequence.append(start_sequence[i])
        return sequence
    for num in start_sequence:
        sequence.append(num)
    i: int = len(start_sequence) - 1
    for _ in range(lenght - n):
        sequence.append(sequence[i] + sequence[i - 1])
        i += 1
    return sequence
