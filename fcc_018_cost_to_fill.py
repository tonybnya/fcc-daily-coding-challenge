"""
Script Name : challenge_018_cost_to_fill.py
Description : Fill The Tank
Author      : @tonybnya

Given the size of a fuel tank, the current fuel level, and the price
per gallon, return the cost to fill the tank all the way.

- tankSize is the total capacity of the tank in gallons.
- fuelLevel is the current amount of fuel in the tank in gallons.
- pricePerGallon is the cost of one gallon of fuel.
- The returned value should be rounded to two decimal places
  in the format: "$d.dd".
"""


def cost_to_fill(
    tank_size: float,
    fuel_level: float,
    price_per_gallon: float
) -> str:
    size_to_fill: float = tank_size - fuel_level
    cost: float = price_per_gallon * size_to_fill
    return f'${cost:.2f}'
