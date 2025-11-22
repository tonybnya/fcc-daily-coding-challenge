"""
Script Name : fcc_0012_message_decoder.py
Description : Message Decoder
Author      : @tonybnya

Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

- A positive number means the message was shifted forward in the alphabet.
- A negative number means the message was shifted backward in the alphabet.
- Case matters, decoded characters should retain the case of their encoded counterparts.
- Non-alphabetical characters should not get decoded.
"""


def shifter(c: str, shift: int) -> str:
    ALPHABET: int = 26
    if not c.isalpha():
        return c
    base: str = "A" if c.isupper() else "a"
    # if c.isupper():
    #     base = "A"
    # elif c.islower():
    #     base = "a"
    index: int = ord(c) - ord(base)
    decoded_index: int = (index - shift) % ALPHABET
    return chr(decoded_index + ord(base))


def decode(message: str, shift: int) -> str:
    decoded_chars: list[str] = []
    for c in message:
        decoded_chars.append(shifter(c, shift))
    return "".join(decoded_chars)
