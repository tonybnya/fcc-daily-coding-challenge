"""
Script Name : fcc_095_permutation_count.py
Description : Permutation Count
Author      : @tonybnya

Given a string, return the number of distinct permutations that can be formed from its characters.

- A permutation is any reordering of the characters in the string.
- Do not count duplicate permutations.
- If the string contains repeated characters, repeated arrangements should only be counted once.
- The string will contain only letters (A-Z, a-z).

For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def count_permutations(s: str) -> int:
    hmap: dict[str, int] = {}

    # Count the total characters in the string
    n: int = len(s)

    # Count how many times each character appears
    for c in s:
        hmap[c] = hmap.get(c, 0) + 1

    # Compute the factorial of the total length
    fact_total: int = factorial(n)

    # Divide by the factorial of each repeated character count
    fact_repeated_chars: int = 1
    for c in hmap:
        if hmap[c] > 1:
            fact_repeated_chars *= factorial(hmap[c])

    return fact_total // fact_repeated_chars
