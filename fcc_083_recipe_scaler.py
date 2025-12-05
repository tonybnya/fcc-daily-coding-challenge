"""
Script Name : fcc_083_recipe_scaler.py
Description : Recipe Scaler
Author      : @tonybnya

Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

- Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
- Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
- Return the scaled items in the same order they are given.
"""


def get_ingredients(ingredient: str) -> tuple:
    parts: list[str] = ingredient.split()
    quantity: str = parts[0]
    rest: list[str] = parts[1:]
    return quantity, rest


def normalize_number(value: float) -> str:
    txt = f"{value:.10f}".rstrip('0').rstrip('.')
    return txt


def scale_recipe(ingredients: list[str], scale: int) -> list[str]:
    scaled_items: list[str] = []
    for ingredient in ingredients:
        quantity, rest = get_ingredients(ingredient)
        if '.' in quantity:
            q: float = float(quantity)
        else:
            q: int = int(quantity)
        result: float = q * scale
        fq: str = normalize_number(result)
        scaled_items.append(f"{str(fq)} {' '.join(rest)}")
    return scaled_items
