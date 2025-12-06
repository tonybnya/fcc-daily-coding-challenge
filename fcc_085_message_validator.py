"""
Script Name : fcc_085_message_validator.py
Description : Message Validator
Author      : @tonybnya

Given a message string and a validation string, determine if the message is valid.

- A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
- Letters are case-insensitive.
- Words in the message are separated by single spaces.
"""


def is_valid_message(message: str, validation: str) -> bool:
    words: list[str] = message.split()
    if len(words) != len(validation):
        return False
    i: int = 0
    for word in words:
        if word[0].lower() != validation[i].lower():
            return False
        i += 1
    return True
