"""
Script Name : fcc_0018_second_best.py
Description : Second Best
Author      : @tonybnya

Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

1. The second most expensive laptop if it is within your budget, or
2. The most expensive laptop that is within your budget, or
3. 0 if no laptops are within your budget.

- Duplicate prices should be ignored.
"""


def get_laptop_cost(laptops: list[int], budget: int) -> int:
    # all unique prices sorted descending
    unique_prices: list[int] = sorted(set(laptops), reverse=True)

    # try second-most-expensive overall
    if len(unique_prices) >= 2:
        second_best = unique_prices[1]
        if second_best <= budget:
            return second_best

    # fallback: return most expensive within budget
    affordable: list[int] = [p for p in unique_prices if p <= budget]
    if affordable:
        return max(affordable)

    # nothing within budget
    return 0
