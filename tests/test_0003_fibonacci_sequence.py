"""
Script Name : fcc_0003_fibonacci_sequence.py
Description : Test suite for Fibonacci Sequence
Author      : @tonybnya
"""

import pytest
from fcc_0003_fibonacci_sequence import fibonacci_sequence


@pytest.mark.parametrize(
    "start_sequence, length, expected",
    [
        (
            [0, 1],
            20,
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
            ],
        ),
        ([21, 32], 1, [21]),
        ([0, 1], 0, []),
        ([10, 20], 2, [10, 20]),
        (
            [123456789, 987654321],
            5,
            [123456789, 987654321, 1111111110, 2098765431, 3209876541],
        ),
    ],
)
def test_fibonacci_sequence(
    start_sequence: list[int], length: int, expected: list[int]
) -> None:
    assert fibonacci_sequence(start_sequence, length) == expected
