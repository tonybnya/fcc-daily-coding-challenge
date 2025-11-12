"""
Script Name : fcc_070_word_search.py
Description : Word Search
Author      : @tonybnya

Given a matrix (an array of arrays) of single letters and a word to find,
return the start and end indices of the word in the matrix.

- The given matrix will be filled with all lowercase letters (a-z).
- The word to find will always be in the matrix exactly once.
- The word to find will always be in a straight line in one of these directions:
    - left to right
    - right to left
    - top to bottom
    - bottom to top

For example, given the matrix:
[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]

And the word "cat", return:

[[0, 1], [2, 1]]

Where [0, 1] are the indices for the "c" (start of the word), and [2, 1]
are the indices for the "t" (end of the word).
"""


def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
    ]

    for i in range(rows):
        for j in range(cols):
            # check if this cell could be the start of the word
            if matrix[i][j] == word[0]:
                for dx, dy in directions:
                    x, y = i, j
                    match = True
                    for k in range(len(word)):
                        nx, ny = i + k * dx, j + k * dy
                        # out of bounds check
                        if not (0 <= nx < rows and 0 <= ny < cols):
                            match = False
                            break
                        if matrix[nx][ny] != word[k]:
                            match = False
                            break
                    if match:
                        end_x = i + (len(word) - 1) * dx
                        end_y = j + (len(word) - 1) * dy
                        return [[i, j], [end_x, end_y]]
    return None
