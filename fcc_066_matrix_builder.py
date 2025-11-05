"""
Script Name : fcc_066_matrix_builder.py
Description : Matrix Builder
Author      : @tonybnya

Given two integers (a number of rows and a number of columns),
return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
"""


def build_matrix(rows: int, cols: int) -> list[list[int]]:
    FILL: int = 0
    matrix: list = []
    for _ in range(rows):
        item = [FILL] * cols
        matrix.append(item)
    return matrix
