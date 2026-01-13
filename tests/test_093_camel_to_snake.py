"""
Script Name : test_093_camel_to_snake.py
Description : Test suite for Camel to Snake coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_093_camel_to_snake import to_snake


@pytest.mark.parametrize(
    "camel, expected",
    [
        ("helloWorld", "hello_world"),
        ("myVariableName", "my_variable_name"),
        ("freecodecampDailyChallenges", "freecodecamp_daily_challenges")
    ]
)
def test_camel_to_snake(camel: str, expected: str) -> None:
    assert to_snake(camel) == expected
