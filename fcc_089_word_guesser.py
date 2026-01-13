"""
Script Name : fcc_089_word_guesser.py
Description : Word Guesser
Author      : @tonybnya

Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

- The secret word and guess will only consist of uppercase letters ("A" to "Z");
- For each letter in the guess, replace it with a number according to how it matches the secret word:
    - "2" if the letter is in the secret word and in the correct position.
    - "1" if the letter is in the secret word but in the wrong position.
- Each letter in the secret word can be used at most once.
- Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
- If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.- "0" if the letter is not in the secret word.

For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").
"""


def compare(word: str, guess: str) -> str:
    code: list[str] = ['0'] * len(word)
    hmap: dict[str, int] = {}

    for letter in word:
        hmap[letter] = hmap.get(letter, 0) + 1

    for i, letter in enumerate(guess):
        if word[i] == letter:
            code[i] = '2'
            hmap[letter] -= 1

    for i, letter in enumerate(guess):
        if code[i] == '0' and letter in hmap and hmap[letter] > 0:
            code[i] = '1'
            hmap[letter] -= 1

    return ''.join(code)

