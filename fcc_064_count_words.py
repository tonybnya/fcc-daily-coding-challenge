"""
Script Name : fcc_064_count_words.py
Description : Word Counter
Author      : @tonybnya

Given a sentence string, return the number of words that are in the sentence.

- Words are any sequence of non-space characters and are separated by a single space.
"""


def count_words(sentence: str) -> int:
    return len(sentence.split())
