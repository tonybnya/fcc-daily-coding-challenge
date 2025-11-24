"""
Script Name : fcc_0017_unorder_of_operations.py
Description : Unorder of Operations
Author      : @tonybnya

Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

- Valid operators are +, -, *, /, and %.
"""


def evaluate(numbers: list[int], operators: list[str]) -> int:
    result: int = numbers[0]
    for i in range(1, len(numbers)):
        index: int = (i - 1) % len(operators)
        operator: str = operators[index]
        if operator == "+":
            result += numbers[i]
        elif operator == "-":
            result -= numbers[i]
        elif operator == "*":
            result *= numbers[i]
        elif operator == "/":
            result /= numbers[i]
        elif operator == "%":
            result %= numbers[i]
    return result
