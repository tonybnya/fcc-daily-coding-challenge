"""
Script Name : fcc_078_fingerprint_test.py
Description : Fingerprint Test
Author      : @tonybnya

Given two strings representing fingerprints, determine if they are a match using the following rules:

- Each fingerprint will consist only of lowercase letters (a-z).
- Two fingerprints are considered a match if:
    - They are the same length.
    - The number of differing characters does not exceed 10% of the fingerprint length.
"""


def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    PERCENT: int = 10

    if len(fingerprint_a) != len(fingerprint_b):
        return False

    f_len: int = len(fingerprint_a)
    num_diff_chars: int = 0

    for i in range(f_len):
        if fingerprint_a[i] != fingerprint_b[i]:
            num_diff_chars += 1

    return num_diff_chars <= (f_len * PERCENT) // 100
