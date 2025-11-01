"""
Script Name : test_019_number_of_photos.py
Description : Tests for Photo Storage challenge
Author      : @tonybnya
"""
from typing import Union

import pytest
from fcc_019_number_of_photos import number_of_photos


@pytest.mark.parametrize(
    "photo_size_mb, drive_size_gb, expected",
    [
        (1, 1, 1000),
        (2, 1, 500),
        (4, 256, 64000),
        (3.5, 750, 214285),
        (3.5, 5.5, 1571)
    ]
)
def test_number_of_photos(
    photo_size_mb: Union[float, int],
    drive_size_gb: Union[float, int],
    expected: int
) -> None:
    assert number_of_photos(photo_size_mb, drive_size_gb) == expected
