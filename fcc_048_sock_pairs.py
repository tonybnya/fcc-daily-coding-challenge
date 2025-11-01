"""
Script Name : challenge_048_sock_pairs.py
Description : Missing Socks
Author      : @tonybnya

Given an integer representing the number of pairs of socks you started with,
and another integer representing how many wash cycles you have gone through,
return the number of complete pairs of socks you currently have using the
following constraints:

- Every 2 wash cycles, you lose a single sock.
- Every 3 wash cycles, you find a single missing sock.
- Every 5 wash cycles, a single sock is worn out and must be thrown away.
- Every 10 wash cycles, you buy a pair of socks.
- You can never have less than zero total socks.
- Rules can overlap. For example, on wash cycle 10, you will lose a single sock,
  throw away a single sock, and buy a new pair of socks.
- Return the number of complete pairs of socks.
"""


def sock_pairs(pairs: int, cycles: int) -> int:
    socks: int = pairs * 2
    cycle: int = 1
    while cycle <= cycles:
        if cycle % 2 == 0:
            socks -= 1
        if cycle % 3 == 0:
            socks += 1
        if cycle % 5 == 0:
            socks -= 1
        if cycle % 10 == 0:
            socks += 2
        if socks < 0:
            socks = 0
        cycle += 1
    return socks // 2
