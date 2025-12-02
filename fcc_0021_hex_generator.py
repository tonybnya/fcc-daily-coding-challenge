"""
Script Name : fcc_0021_hex_generator.py
Description : Hex Generator
Author      : @tonybnya

Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

- The function should handle "red", "green", or "blue" as an input argument.
- If the input is not one of those, the function should return "Invalid color".
- The function should return a random six-character hex color code where the input color value is greater than any of the others.
- Example of valid outputs for a given input:

Input   Output
"red"   "FF0000"
"green" "00FF00"
"blue"  "0000FF"
"""

import random


def generate_hex(color: str) -> str:
    if color not in ('red', 'green', 'blue'):
        return 'Invalid color'
    chars: str = '0123456789ABCDEF'
    ff: str = 'FF'
    if color == 'red':
        complement: list[str] = [random.choice(chars) for _ in range(4)]
        return f"{ff}{''.join(complement)}"
    elif color == 'green':
        start: list[str] = [random.choice(chars) for _ in range(2)]
        end: list[str] = [random.choice(chars) for _ in range(2)]
        return f"{''.join(start)}{ff}{''.join(end)}"
    elif color == 'blue':
        complement: list[str] = [random.choice(chars) for _ in range(4)]
        return f"{''.join(complement)}{ff}"
