"""
Script Name : challenge_020_number_of_files.py
Description : File Storage
Author      : @tonybnya

Given a file size, a unit for the file size, and hard drive capacity
in gigabytes (GB), return the number of files the hard drive
can store using the following constraints:

- The unit for the file size can be bytes ("B"), kilobytes ("KB"),
  or megabytes ("MB").
- Return the number of whole files the drive can fit.
- Use the following conversions:

Unit 	Equivalent
1 B 	1 B
1 KB 	1000 B
1 MB 	1000 KB
1 GB 	1000 MB

For example, given 500, "KB", and 1 as arguments,
determine how many 500 KB files can fit on a 1 GB hard drive.
"""


def number_of_files(
    file_size: float,
    file_unit: str,
    drive_size_gb: float
) -> int:
    units: dict[str, int] = {
        'MB': 1,
        'KB': 2,
        'B': 3
    }
    base: int = 1000
    power: int = 0

    if file_unit == 'MB':
        power = units.get('MB', 0)
    elif file_unit == 'KB':
        power = units.get('KB', 0)
    elif file_unit == 'B':
        power = units.get('B', 0)

    return int((drive_size_gb * (base ** power)) / file_size)
