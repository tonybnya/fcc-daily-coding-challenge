"""
Script Name : fcc_081_longest_word.py
Description : Longest Word
Author      : @tonybnya

Given a sentence string, return the longest word in the sentence.

- Words are separated by a single space.
- Only letters (a-z, case-insensitive) count toward the word's length.
- If there are multiple words with the same length, return the first one that appears.
- Return the word as it appears in the given string, with punctuation removed.
"""


def length_clean_word(word: str) -> int:
    length: int = 0
    clean_list: list[str] = []
    for c in word:
        if c.isalpha():
            length += 1
            clean_list.append(c)
    return length, ''.join(clean_list)


def longest_word(sentence: str) -> str:
    words: list[str] = sentence.split()
    longest_length, longest_word = length_clean_word(words[0])
    for word in words[1:]:
        current_length, current_word = length_clean_word(word)
        if current_length > longest_length:
            longest_word = current_word
            longest_length = current_length
    return longest_word
