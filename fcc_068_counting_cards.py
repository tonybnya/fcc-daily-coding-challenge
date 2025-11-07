"""
Script Name : fcc_068_counting_cards.py
Description : Counting Cards
Author      : @tonybnya

A standard deck of playing cards has 13 unique cards in each suit.
Given an integer representing the number of cards to pick from the deck,
return the number of unique combinations of cards you can pick.

- Order does not matter.
  Picking card A then card B is the same as picking card B then card A.

For example, given 52, return 1.
There's only one combination of 52 cards to pick from a 52 card deck.
And given 2, return 1326.
There's 1326 card combinations you can end up with when picking 2 cards from the deck.
"""


def combinations(cards: int) -> int:
    n = 52  # total cards in a standard deck

    # edge cases
    if cards < 0 or cards > n:
        return 0
    if cards == 0 or cards == n:
        return 1
    if cards == 1:
        return n

    # compute combinations using product form:
    # C(n, cards) = n * (n-1) * ... * (n-cards+1) / (cards!)
    numerator = 1
    for i in range(n, n - cards, -1):
        numerator *= i

    denominator = 1
    for i in range(1, cards + 1):
        denominator *= i

    return numerator // denominator
