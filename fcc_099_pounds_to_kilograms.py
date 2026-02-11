"""
Script Name : fcc_099_pounds_to_kilograms.py
Description : Pounds to Kilograms
Author      : @tonybnya

Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

- Replace "(lbs)" with the input number.
- Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
- 1 pound equals 0.453592 kilograms.
- If the input is 1, use "pound" instead of "pounds".
- If the converted value is 1, use "kilogram" instead of "kilograms".
"""


def convert_to_kgs(lbs: int | float) -> str:
    CONVERSION_FACTOR: float = 0.453592

    kgs: float = round(lbs * CONVERSION_FACTOR, 2)

    if lbs == 0:
        return f"0 pounds equals 0.00 kilograms."
    if lbs == 1:
        return f"1 pound equals {round(CONVERSION_FACTOR, 2)} kilograms."
    if kgs == 1:
        return f"{lbs} pounds equals 1.00 kilogram."

    return f"{lbs} pounds equals {round(kgs, 2)} kilograms."