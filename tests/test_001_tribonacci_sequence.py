"""
Script Name : test_001_tribonacci_sequence.py
Description : Tests for Tribonacci Sequence challenge
Author      : @tonybnya
"""
import pytest

from challenge_001_tribonacci_sequence import tribonacci


@pytest.mark.parametrize(
    "start_sequence, length, expected",
    [
        ([0, 0, 1], 20, [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]),
        ([21, 32, 43], 1, [21]),
        ([0, 0, 1], 0, []),
        ([10, 20, 30], 2, [10, 20]),
        ([10, 20, 30], 3, [10, 20, 30]),
        ([123, 456, 789], 8, [123, 456, 789, 1368, 2613, 4770, 8751, 16134])
    ]
)
def test_tribonacci(start_sequence: list[int], length: int, expected: list[int]) -> None:
    assert tribonacci(start_sequence, length) == expected
