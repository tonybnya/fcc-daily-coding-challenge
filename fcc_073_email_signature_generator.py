"""
Script Name : fcc_073_email_signature_generator.py
Description : Email Signature Generator
Author      : @tonybnya

Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

- The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
    - A-I: Use >> as the prefix.
    - J-R: Use -- as the prefix.
    - S-Z: Use :: as the prefix.
- A comma and space (, ) should follow the name.
- The title and company should follow the comma and space, separated by " at " (with spaces around it).

For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
"""


def generate_signature(name: str, title: str, company: str) -> str:
    SEP_1: str = ", "
    SEP_2: str = " at "
    PREFIX_1: str = "abcdefghi"
    PREFIX_2: str = "jqlmnopqr"
    PREFIX_3: str = "stuvwxyz"
    prefix: str = ""
    first_letter_name: str = name[0]
    if first_letter_name.lower() in PREFIX_1:
        prefix = ">>"
    elif first_letter_name.lower() in PREFIX_2:
        prefix = "--"
    elif first_letter_name.lower() in PREFIX_3:
        prefix = "::"
    return prefix + name + SEP_1 + title + SEP_2 + company
