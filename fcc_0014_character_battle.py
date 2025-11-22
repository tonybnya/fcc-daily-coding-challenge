"""
Script Name : fcc_0014_character_battle.py
Description : Character Battle
Author      : @tonybnya

Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

- Characters a-z have a strength of 1-26, respectively.
- Characters A-Z have a strength of 27-52, respectively.
- Digits 0-9 have a strength of their face value.
- All other characters have a value of zero.
- Each character can only fight one battle.

For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

- "Opponent retreated" if your army has more characters than the opposing army.
- "We retreated" if the opposing army has more characters than yours.
- "We won" if your army won more battles.
- "We lost" if the opposing army won more battles.
- "It was a tie" if both armies won the same number of battles.
"""


def get_score(c: str) -> int:
    LOWERCASE: dict[str, int] = {chr(i): i - 96 for i in range(97, 123)}
    UPPERCASE: dict[str, int] = {chr(i): i - 38 for i in range(65, 91)}
    if c.isdigit():
        return int(c)
    elif c.islower():
        return LOWERCASE[c]
    elif c.isupper():
        return UPPERCASE[c]
    return 0


def battle(my_army: str, opposing_army: str) -> str:
    my_score, op_score = 0, 0
    n, m = len(my_army), len(opposing_army)
    if n > m:
        return "Opponent retreated"
    elif n < m:
        return "We retreated"
    else:
        for i in range(n):
            ms: int = get_score(my_army[i])
            os: int = get_score(opposing_army[i])
            if ms > os:
                my_score += 1
            elif ms < os:
                op_score += 1
    if my_score > op_score:
        return "We won"
    if my_score < op_score:
        return "We lost"
    return "It was a tie"
