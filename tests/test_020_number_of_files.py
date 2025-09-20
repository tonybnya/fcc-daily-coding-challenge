"""
Script Name : test_020_number_of_files.py
Description : Tests for File Storage challenge
Author      : @tonybnya
"""
import pytest

from challenge_020_number_of_files import number_of_files


@pytest.mark.parametrize(
    "file_size, file_unit, drive_size_gb, files",
    [
        (500, "KB", 1, 2000),
        (50000, "B", 1, 20000),
        (5, "MB", 1, 200),
        (4096, "B", 1.5, 366210),
        (220.5, "KB", 100, 453514),
        (4.5, "MB", 750, 166666)
    ]
)
def test_number_of_files(
    file_size: float,
    file_unit: str,
    drive_size_gb: float,
    files: int
) -> None:
    assert number_of_files(file_size, file_unit, drive_size_gb) == files
