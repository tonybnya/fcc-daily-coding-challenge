"""
Script Name : challenge_028_get_headings.py
Description : CSV Header Parser
Author      : @tonybnya

Given the first line of a comma-separated values (CSV) file,
return an array containing the headings.

- The first line of a CSV file contains headings separated by commas.
- Remove any leading or trailing whitespace from each heading.
"""


def get_headings(csv: str) -> list[str]:
    return list(map(lambda hv: hv.strip(), csv.split(',')))
