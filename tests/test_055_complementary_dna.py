"""
Script Name : test_055_complementary_dna.py
Description : Test suite for Complementary DNA
Author      : @tonybnya
"""

import pytest
from challenge_055_complementary_dna import complementary_dna


@pytest.mark.parametrize(
    "strand, expected",
    [
        ("ACGT", "TGCA"),
        ("ATGCGTACGTTAGC", "TACGCATGCAATCG"),
        ("GGCTTACGATCGAAG", "CCGAATGCTAGCTTC"),
        ("GATCTAGCTAGGCTAGCTAG", "CTAGATCGATCCGATCGATC"),
    ],
)
def test_complementary_dna(strand: str, expected: str) -> None:
    assert complementary_dna(strand) == expected
