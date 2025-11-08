"""
Script Name : fcc_069_character_limit.py
Description : Character Limit
Author      : @tonybnya

In this challenge, you are given a string and need to determine if it fits in
a social media post. Return the following strings based on the rules given:

- "short post" if it fits within a 40-character limit.
- "long post" if it's greater than 40 characters and fits within an 80-character limit.
- "invalid post" if it's too long to fit within either limit.

"""


def can_post(message: str) -> str:
    n: int = len(message)
    ans: str = ""
    if n <= 40:
        ans = "short post"
    elif 40 < n <= 80:
        ans = "long post"
    else:
        ans = "invalid post"
    return ans
