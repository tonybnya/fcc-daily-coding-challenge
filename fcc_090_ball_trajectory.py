"""
Script Name : fcc_090_ball_trajectory.py
Description : Ball Trajectory
Author      : @tonybnya

Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

- The ball always moves in a straight line.
- The movement direction is determined by how the ball moved from 1 to 2.
- The edges of the matrix are considered walls. If the ball hits a:
  - top or bottom wall, it bounces by reversing its vertical direction.
  - left or right wall, it bounces by reversing its horizontal direction.
  - corner, it bounces by reversing both directions.
"""


def get_next_location(matrix: list[list[int]]) -> list[int]:
    rows: int = len(matrix)
    cols: int = len(matrix[0])

    prev = curr = None

    # Locate 1 and 2
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                prev = (r, c)
            elif matrix[r][c] == 2:
                curr = (r, c)

    prev_r, prev_c = prev
    curr_r, curr_c = curr

    # Direction vector
    dr = curr_r - prev_r
    dc = curr_c - prev_c

    # Predict next
    next_r = curr_r + dr
    next_c = curr_c + dc

    # Bounce logic
    if next_r < 0 or next_r >= rows:
        dr = -dr
    if next_c < 0 or next_c >= cols:
        dc = -dc

    # Final position
    return [curr_r + dr, curr_c + dc]
