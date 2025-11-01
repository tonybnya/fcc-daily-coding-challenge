"""
Script Name : challenge_051_adjust_thermostat.py
Description : Thermostat Adjuster 2
Author      : @tonybnya

Given the current temperature of a room in Fahrenheit and a target temperature
in Celsius, return a string indicating how to adjust the room temperature
based on these constraints:

- Return "Heat: X degrees Fahrenheit" if the current temperature
  is below the target. With X being the number of degrees in Fahrenheit
  to heat the room to reach the target, rounded to 1 decimal place.
- Return "Cool: X degrees Fahrenheit" if the current temperature is above the
  target. With X being the number of degrees in Fahrenheit to cool the room
  to reach the target, rounded to 1 decimal place.
- Return "Hold" if the current temperature is equal to the target.

To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8
and add 32 to the result (F = (C * 1.8) + 32).
"""


def adjust_thermostat(current_f: int, target_c: int) -> str:
    target_f: float = (target_c * 1.8) + 32
    gap: float = target_f - current_f
    if gap > 0:
        return f"Heat: {gap:.1f} degrees Fahrenheit"
    if gap < 0:
        gap *= -1
        return f"Cool: {gap:.1f} degrees Fahrenheit"
    return "Hold"
