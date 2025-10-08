"""
Script Name : test_038_goldilocks_zone.py
Description : Test suite for Space Week Day 5: Goldilocks Zone
Author      : @tonybnya
"""
import pytest
from challenge_038_goldilocks_zone import goldilocks_zone


@pytest.mark.parametrize(
    "mass, distances",
    [
        (1, [0.95, 1.37]),
        (0.5, [0.28, 0.41]),
        (6, [21.85, 31.51]),
        (3.7, [9.38, 13.52]),
        (20, [179.69, 259.13])
    ]
)
def test_goldilocks_zone(mass: float, distances: list[float]) -> None:
    assert goldilocks_zone(mass) == distances
