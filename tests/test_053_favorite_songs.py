"""
Script Name : test_053_favorite_songs.py
Description : Test suite for Favorite Songs coding challenge
Author      : @tonybnya
"""

import pytest
from fcc_053_favorite_songs import favorite_songs


@pytest.mark.parametrize(
    "playlist, most_played",
    [
        (
            [
                {"title": "Sync or Swim", "plays": 3},
                {"title": "Byte Me", "plays": 1},
                {"title": "Earbud Blues", "plays": 2},
            ],
            ["Sync or Swim", "Earbud Blues"],
        ),
        (
            [
                {"title": "Skip Track", "plays": 98},
                {"title": "99 Downloads", "plays": 99},
                {"title": "Clickwheel Love", "plays": 100},
            ],
            ["Clickwheel Love", "99 Downloads"],
        ),
        (
            [
                {"title": "Song A", "plays": 42},
                {"title": "Song B", "plays": 99},
                {"title": "Song C", "plays": 75},
            ],
            ["Song B", "Song C"],
        ),
    ],
)
def test_favorite_songs(
    playlist: list[dict[str, int | str]], most_played: list[str]
) -> None:
    assert favorite_songs(playlist) == most_played
