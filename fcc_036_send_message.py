"""
Script Name : challenge_036_send_message.py
Description : Space Week Day 3: Phone Home
Author      : @tonybnya

For day three of Space Week, you are given an array of numbers
representing distances (in kilometers) between yourself,
satellites, and your home planet in a communication route.
Determine how long it will take a message sent through the route
to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location
  to the first satellite.
- Each subsequent value, except for the last, is the distance
  to the next satellite.
- The last value in the array is the distance from the previous
  satellite to your home planet.
- The message travels at 300,000 km/s.
- Each satellite the message passes through adds a 0.5 second
  transmission delay.
- Return a number rounded to 4 decimal places,
  with trailing zeros removed.
"""


def send_message(route: list[int]) -> float:
    SPEED: int = 300000
    DELAY: float = 0.5

    satellites: int = len(route) - 1

    t: float = 0
    for distance in route:
        elapsed_time: int = distance / SPEED
        t += elapsed_time

    delays: float = satellites * DELAY
    tt: float = t + delays

    return float(f"{tt:.4f}".rstrip('0').rstrip('.'))
