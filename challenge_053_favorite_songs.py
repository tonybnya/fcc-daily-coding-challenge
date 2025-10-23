"""
Script Name : challenge_053_favorite_songs.py
Description : Favorite Songs
Author      : @tonybnya

Remember iPods?
The first model came out 24 years ago today, on Oct. 23, 2001.
Given an array of song objects representing your iPod playlist,
return an array with the titles of the two most played songs,
with the most played song first.

- Each object will have a "title" property (string), and a "plays" property (integer).
"""


def favorite_songs(playlist: list[dict[str, int | str]]) -> list[str]:
    plays_count: list[int] = []
    for song in playlist:
        plays_count.append(song.get("plays"))
    first: int = max(plays_count)
    second: int = -1
    for play in plays_count:
        if play > second and play < first:
            second = play
    most_played: list[str] = [""] * 2
    for song in playlist:
        if song.get("plays") == first:
            most_played[0] = song.get("title")
        elif song.get("plays") == second:
            most_played[1] = song.get("title")
    return most_played
