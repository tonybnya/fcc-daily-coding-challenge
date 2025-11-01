"""
Script Name : test_021_number_of_videos.py
Description : Tests for Video Storage challenge
Author      : @tonybnya
"""
import pytest
from fcc_021_number_of_videos import number_of_videos


@pytest.mark.parametrize(
    "video_size, video_unit, drive_size, drive_unit, expected",
    [
        (500, "MB", 100, "GB", 200),
        (2000, "B", 1, "TB", "Invalid video unit"),
        (2000, "MB", 100000, "MB", "Invalid drive unit"),
        (500000, "KB", 2, "TB", 4000),
        (1.5, "GB", 2.2, "TB", 1466)
    ]
)
def test_number_of_videos(
    video_size: float,
    video_unit: str,
    drive_size: float,
    drive_unit: str,
    expected: int | str
) -> None:
    assert number_of_videos(
        video_size,
        video_unit,
        drive_size,
        drive_unit
    ) == expected
