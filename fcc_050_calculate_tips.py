"""
Script Name : challenge_050_calculate_tips.py
Description : Tip Calculator
Author      : @tonybnya

Given the price of your meal and a custom tip percent,
return an array with three tip values; 15%, 20%, and the custom amount.

- Prices will be given in the format: "$N.NN".
- Custom tip percents will be given in this format: "25%".
- Return amounts in the same "$N.NN" format, rounded to two decimal places.

For example, given a "$10.00" meal price, and a "25%" custom tip value,
return ["$1.50", "$2.00", "$2.50"].
"""


def tip_percent(price: float, percentage: int) -> float:
    """
    Calculate the tip percent of a price.
    """
    PERCENT: int = 100
    return (price * percentage) / PERCENT


def get_percent(percent_str: str) -> int:
    """
    Get the percent from a string percent
    """
    END: int = -1
    return int(percent_str[:END])


def get_price(price_str: str) -> float:
    """
    Get the price from a string price
    """
    START: int = 1
    return float(price_str[START:])


def stringify(amount: float) -> str:
    """
    Stringify float amount
    """
    return f"${amount:.2f}"


def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    FIRST_PERCENT: int = 15
    SECOND_PERCENT: int = 20
    price: float = get_price(meal_price)
    percent: int = get_percent(custom_tip)
    amount_1: float = tip_percent(price, FIRST_PERCENT)
    amount_2: float = tip_percent(price, SECOND_PERCENT)
    amount_3: float = tip_percent(price, percent)
    return [stringify(amount_1), stringify(amount_2), stringify(amount_3)]
