"""
Script Name : challenge_055_complementary_dna.py
Description : Complementary DNA
Author      : @tonybnya

Given a string representing a DNA sequence,
return its complementary strand using the following rules:

- DNA consists of the letters "A", "C", "G", and "T".
- The letters "A" and "T" complement each other.
- The letters "C" and "G" complement each other.

For example, given "ACGT", return "TGCA".
"""


def complementary_dna(strand: str) -> str:
    COMPLEMENTS: dict[str, str] = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A",
    }
    complementary: str = ""
    for nucleotide in strand:
        complementary += COMPLEMENTS.get(nucleotide)
    return complementary
