"""
Script Name : challenge_011_reverse_sentence.py
Description : Reverse Sentence
Author      : @tonybnya

Given a string of words, return a new string with the words in reverse order.
For example, the first word should be at the end of the returned string,
and the last word should be at the beginning of the returned string.

- In the given string, words can be separated by one or more spaces.
- The returned string should only have one space between words.
"""


def rev(words: list[str]) -> list[str]:
    i, j = 0, len(words) - 1

    while i < j:
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1

    return words


def reverse_sentence(sentence: str) -> str:
    words: list[str] = sentence.split()
    return " ".join(rev(words))
