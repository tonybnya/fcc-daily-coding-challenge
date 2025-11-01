"""
Script Name : challenge_042_battle.py
Description : Battle of Words
Author      : @tonybnya

Given two sentences representing your team and an opposing team,
where each word from your team battles the corresponding word from
the opposing team, determine which team wins using the following rules:

- The given sentences will always contain the same number of words.
- Words are separated by a single space and will only contain letters.
- The value of each word is the sum of its letters.
- Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
- A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
- Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
- A word wins if its value is greater than the opposing word's value.
- The team with more winning words is the winner.

Return
"We win" if your team is the winner,
"We lose" if your team loses, and
"Draw" if both teams have the same number of wins.
"""

WORDS: dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def word_value(word: str) -> int:
    """
    Calculate the value of a word
    """
    value: int = 0
    for c in word:
        if 97 <= ord(c) <= 122:
            value += WORDS[c]
        else:
            value += WORDS[c.lower()] * 2
    return value


def battle(our_team: str, opponent: str) -> str:
    our_words: list[str] = our_team.split()
    opponent_words: list[str] = opponent.split()
    our_score: int = 0
    opponent_score: int = 0
    result: str = ""
    for i in range(len(our_words)):
        our_word_value: int = word_value(our_words[i])
        opponent_word_value: int = word_value(opponent_words[i])
        if our_word_value > opponent_word_value:
            our_score += 1
        elif our_word_value < opponent_word_value:
            opponent_score += 1
    if our_score > opponent_score:
        result = "We win"
    elif our_score < opponent_score:
        result = "We lose"
    else:
        result = "Draw"
    return result
