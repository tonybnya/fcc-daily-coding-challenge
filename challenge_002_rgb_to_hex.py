"""
Script Name : challenge_002_rgb_to_hex.py
Description : RGB to Hex
Author      : @tonybnya

Given a CSS rgb(r, g, b) color string,
return its hexadecimal equivalent.

Here are some example outputs for a given input:
Input 	                Output
"rgb(255, 255, 255)" 	"#ffffff"
"rgb(1, 2, 3)" 	        "#010203"

- Make any letters lowercase.
- Return a # followed by six characters.
  Don't use any shorthand values.
"""


def clean_rgb(rgb: str) -> list[int]:
    rgb = rgb.replace('rgb(', '').replace(')', '')
    return [int(x) for x in rgb.split(', ')]


def decompose(num: int) -> str:
    BASE: int = 16
    TABLE: dict[int, str] = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }
    hex_value: str = ""
    while num != 0:
        quotient, remainder = divmod(num, BASE)
        hex_value += TABLE.get(remainder, '')
        num = quotient
    if len(hex_value) == 1:
        return "0" + hex_value
    return hex_value[::-1]


def rgb_to_hex(rgb: str) -> str:
    hex: str = ""
    nums: list[int] = clean_rgb(rgb)
    for num in nums:
        hex += decompose(num)
    return "#" + hex
