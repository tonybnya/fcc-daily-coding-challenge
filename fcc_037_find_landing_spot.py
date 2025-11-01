"""
Script Name : challenge_037_find_landing_spot.py
Description : Space Week Day 4: Landing Spot
Author      : @tonybnya

In day four of Space Week,
you are given a matrix of numbers (an array of arrays),
representing potential landing spots for your rover.
Find the safest landing spot based on the following rules:

- Each spot in the matrix will contain a number from 0-9,
  inclusive.
- Any 0 represents a potential landing spot.
- Any number other than 0 is too dangerous to land.
  The higher the number, the more dangerous.
- The safest spot is defined as the 0 cell whose surrounding cells
  (up to 4 neighbors, ignore diagonals) have the lowest total danger.
- Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
- Return the indices of the safest landing spot.
  There will always only be one safest spot.

For instance, given:

[
  [1, 0],
  [2, 0]
]

Return [0, 1], the indices for the 0 in the first array.
"""


def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    directions: list[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_danger = float('inf')
    best_spot = None

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                total_danger: int = 0

                for drow, dcol in directions:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < len(matrix) and 0 <= ncol < len(matrix[0]):
                        total_danger += matrix[nrow][ncol]

                if total_danger < min_danger:
                    min_danger = total_danger
                    best_spot = [row, col]

    return best_spot
