"""
Script Name : test_065_image_search.py
Description : Test suite for Image Search
Author      : @tonybnya
"""

import pytest
from fcc_065_image_search import image_search


@pytest.mark.parametrize(
    "images, term, expected",
    [
        (["dog.png", "cat.jpg", "parrot.jpeg"], "dog", ["dog.png"]),
        (
            ["Sunset.jpg", "Beach.png", "sunflower.jpeg"],
            "sun",
            ["Sunset.jpg", "sunflower.jpeg"],
        ),
        (["Moon.png", "sun.jpeg", "stars.png"], "PNG", ["Moon.png", "stars.png"]),
        (
            [
                "cat.jpg",
                "dogToy.jpeg",
                "kitty-cat.png",
                "catNip.jpeg",
                "franken_cat.gif",
            ],
            "Cat",
            ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"],
        ),
    ],
)
def test_image_search(images: list[str], term: str, expected: list[str]) -> None:
    assert image_search(images, term) == expected
