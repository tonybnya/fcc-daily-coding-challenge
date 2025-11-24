"""
Script Name : fcc_0016_reverse_parenthesis.py
Description : Reverse Parenthesis
Author      : @tonybnya

Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

- All characters inside each pair of parentheses should be reversed.
- Parentheses should be removed from the final result.
- If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
- Assume all parentheses are evenly balanced and correctly nested.
"""


def decode(s: str) -> str:
    stack: list[str] = []

    for ch in s:
        if ch != ")":
            # push any non-')' character onto the stack
            stack.append(ch)
        else:
            # we hit ')', so we build the substring inside the last '('
            substring: list[str] = []

            # pop until '('
            while stack and stack[-1] != "(":
                substring.append(stack.pop())

            # pop the '(' itself
            stack.pop()

            # substring currently has the characters inside parentheses but reversed
            # reverse again to get correct order, then push back
            for c in substring:
                stack.append(c)

    # final decoded result is whatever remains in the stack
    return "".join(stack)
