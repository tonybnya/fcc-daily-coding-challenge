"""
Script Name : fcc_098_string_compression.py
Description : String Compression
Author      : @tonybnya

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

- Only consecutive duplicates are compressed.
- Words are separated by single spaces.

For example, given "yes yes yes please", return "yes(3) please".
"""


def compress_string(sentence: str) -> str:
    if not sentence:
        return ''

    words: list[str] = sentence.split(' ')
    result: list[str] = []

    current_word: str = words[0]
    count: int = 1

    for word in words[1:]:
        if word == current_word:
            count += 1
        else:
            if count > 1:
                result.append(f'{current_word}({count})')
            else:
                result.append(current_word)
            current_word = word
            count = 1

    if count > 1:
        result.append(f'{current_word}({count})')
    else:
        result.append(current_word)

    return ' '.join(result)