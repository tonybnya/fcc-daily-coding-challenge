"""
Script Name : test_010_array_diff.py
Description : Tests for Array Diff challenge
Author      : @tonybnya
"""
import pytest

from fcc_010_array_diff import array_diff


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        (["apple", "banana"], ["apple", "banana", "cherry"], ["cherry"]),
        (["apple", "banana", "cherry"], ["apple", "banana"], ["cherry"]),
        (["one", "two", "three", "four", "six"], ["one", "three", "eight"], ["eight", "four", "six", "two"]),
        (["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"], ["five", "one", "seven", "three"]),
        (["I", "like", "freeCodeCamp"], ["I", "like", "rocks"], ["freeCodeCamp", "rocks"])
    ]
)
def test_array_diff(arr1: list[str], arr2: list[str], expected: list[str]) -> None:
    assert array_diff(arr1, arr2) == expected
