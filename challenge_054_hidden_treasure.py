"""
Script Name : challenge_054_hidden_treasure.py
Description : Hidden Treasure
Author      : @tonybnya

Given a 2D array representing a map of the ocean floor that includes
a hidden treasure, and an array with the coordinates ([row, column])
for the next dive of your treasure search, return "Empty", "Found",
or "Recovered" using the following rules:

- The given 2D array will contain exactly one unrecovered treasure,
  which will occupy multiple cells.
- Each cell in the 2D array will contain one of the following values:
    - "-": No treasure.
    - "O": A part of the treasure that has not been found.
    - "X": A part of the treasure that has already been found.
- If the dive location has no treasure, return "Empty".
- If the dive location finds treasure, but at least one other part
  of the treasure remains unfound, return "Found".
- If the dive location finds the last unfound part of the treasure,
  return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]

And [2, 1] for the coordinates of the dive location, return "Recovered"
because the dive found the last unfound part of the treasure.
"""


def dive(map: list[list[str]], coordinates: list[int]) -> str:
    row, column = coordinates
    treasure: str = map[row][column]
    result: str = ""
    if treasure == "O":
        map[row][column] = "X"
        unfound = any("O" in row_ for row_ in map)
        if unfound:
            return "Found"
        return "Recovered"
    elif treasure == "-":
        result = "Empty"
    elif treasure == "X":
        result = "Found"
    return result
