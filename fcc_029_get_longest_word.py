"""
Script Name : challenge_029_get_longest_word.py
Description : Longest Word
Author      : @tonybnya

Given a sentence, return the longest word in the sentence.

- Ignore periods (.) when determining word length.
- If multiple words are ties for the longest, return the first one
  that occurs.
"""


def get_longest_word(sentence: str) -> str:
    words: list[str] = sentence.split()

    longest: str = ''

    for word in words:
        word = word.replace('.', '')
        if len(word) > len(longest):
            longest = word

    return longest
