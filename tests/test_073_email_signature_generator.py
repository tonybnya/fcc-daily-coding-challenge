"""
Script Name : test_073_email_signature_generator.py
Description : Test suite for Email Signature Generator
Author      : @tonybnya
"""

import pytest
from fcc_073_email_signature_generator import generate_signature


@pytest.mark.parametrize(
    "name, title, company, expected",
    [
        (
            "Quinn Waverly",
            "Founder and CEO",
            "TechCo",
            "--Quinn Waverly, Founder and CEO at TechCo",
        ),
        ("Alice Reed", "Engineer", "TechCo", ">>Alice Reed, Engineer at TechCo"),
        (
            "Tina Vaughn",
            "Developer",
            "example.com",
            "::Tina Vaughn, Developer at example.com",
        ),
        ("B. B.", "Product Tester", "AcmeCorp", ">>B. B., Product Tester at AcmeCorp"),
        (
            "windstorm",
            "Cloud Architect",
            "Atmospheronics",
            "::windstorm, Cloud Architect at Atmospheronics",
        ),
    ],
)
def test_email_signature_generator(
    name: str, title: str, company: str, expected: str
) -> None:
    assert generate_signature(name, title, company) == expected
