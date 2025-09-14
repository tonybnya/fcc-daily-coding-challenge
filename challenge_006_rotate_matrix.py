"""
Script Name : challenge_006_rotate_matrix.py
Description : Matrix Rotate
Author      : @tonybnya

Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise
and return it. For instance, given [[1, 2], [3, 4]], which looks like this:
1 	2
3 	4

You should return [[3, 1], [4, 2]], which looks like this:
3 	1
4 	2
"""


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    n: int = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix
