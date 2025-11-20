"""
Script Name : fcc_0006_anagram_checker.py
Description : Anagram Checker
Author      : @tonybnya

Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

- Ignore casing and white space.
"""


def are_anagrams(str1: str, str2: str) -> bool:
    hmap1: dict[str, int] = {}
    hmap2: dict[str, int] = {}
    for c in str1:
        char: str = c.lower()
        hmap1[char] = hmap1.get(char, 0) + 1
    for c in str2:
        char: str = c.lower()
        hmap2[char] = hmap2.get(char, 0) + 1
    return hmap1 == hmap2
