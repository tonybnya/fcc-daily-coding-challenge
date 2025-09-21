"""
Script Name : challenge_021_number_of_videos.py
Description : Video Storage
Author      : @tonybnya

Given a video size, a unit for the video size, a hard drive capacity,
and a unit for the hard drive, return the number of videos
the hard drive can store using the following constraints:

- The unit for the video size can be bytes ("B"), kilobytes ("KB"),
  megabytes ("MB"), or gigabytes ("GB").
- If not given one of the video units above, return "Invalid video unit".
- The unit of the hard drive capacity can be gigabytes ("GB")
  or terabytes ("TB").
- If not given one of the hard drive units above, return "Invalid drive unit".
- Return the number of whole videos the drive can fit.
- Use the following conversions:

Unit 	Equivalent
1 B 	1 B
1 KB 	1000 B
1 MB 	1000 KB
1 GB 	1000 MB
1 TB 	1000 GB

For example, given 500, "MB", 100, and "GB as arguments,
determine how many 500 MB videos can fit on a 100 GB hard drive.
"""


def conversion(
    drive_size: float,
    from_unit: str,
    to_unit: str
) -> float:
    """
    Conversion units.
    """
    base: int = 1000
    factors: dict[str, int] = {
        'GB': base ** 0,
        'MB': base ** 1,
        'KB': base ** 2,
        'B': base ** 3
    }

    if from_unit == 'TB':
        val_in_gb = drive_size * base
    else:
        val_in_gb = drive_size

    return val_in_gb * factors.get(to_unit, 0)


def number_of_videos(
    video_size: float,
    video_unit: str,
    drive_size: float,
    drive_unit: str
) -> int | str:

    if video_unit not in ('KB', 'MB', 'GB'):
        return 'Invalid video unit'

    if drive_unit not in ('GB', 'TB'):
        return 'Invalid drive unit'

    val = conversion(drive_size, drive_unit, video_unit)

    return int(val / video_size)
