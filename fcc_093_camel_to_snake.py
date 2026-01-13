"""
Script Name : fcc_093_camel_to_snake.py
Description : Camel to Snake
Author      : @tonybnya

Given a string in camel case, return the snake case version of the string using the following rules:

- The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
- Every uppercase letter in the camel case string starts a new word.
- Convert all letters to lowercase.
- Separate words with an underscore (_).
"""


def to_snake(camel: str) -> str:
    snake: list[str] = [None] * len(camel)
    for i, c in enumerate(camel):
        if c.isupper():
            snake[i] = f"_{c.lower()}"
        else:
            snake[i] = c

    return "".join(snake)
