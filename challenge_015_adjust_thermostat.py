"""
Script Name : challenge_015_adjust_thermostat.py
Description : Thermostat Adjuster
Author      : @tonybnya

Given the current temperature of a room and a target temperature,
return a string indicating how to adjust the room temperature
based on these constraints:

- Return "heat" if the current temperature is below the target.
- Return "cool" if the current temperature is above the target.
- Return "hold" if the current temperature is equal to the target.
"""


def adjust_thermostat(temp: float, target: float) -> str:
    res: str = ''

    if temp < target:
        res = 'heat'
    elif temp > target:
        res = 'cool'
    else:
        res = 'hold'

    return res
