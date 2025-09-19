"""
Script Name : challenge_019_number_of_photos.py
Description : Photo Storage
Author      : @tonybnya

Given a photo size in megabytes (MB), and hard drive capacity
in gigabytes (GB), return the number of photos the hard drive
can store using the following constraints:

- 1 gigabyte equals 1000 megabytes.
- Return the number of whole photos the drive can store.
"""
from typing import Union
from math import floor


def number_of_photos(
    photo_size_mb: Union[float, int],
    drive_size_gb: Union[float, int]
) -> int:
    return floor((drive_size_gb * 1000) / photo_size_mb)
