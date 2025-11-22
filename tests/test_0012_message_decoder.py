"""
Script Name : test_0012_message_decoder.py
Description : Test suite for Message Decoder
Author      : @tonybnya
"""

import pytest
from fcc_0012_message_decoder import decode


@pytest.mark.parametrize(
    "message, shift, expected",
    [
        ("Xlmw mw e wigvix qiwweki.", 4, "This is a secret message."),
        ("Byffi Qilfx!", 20, "Hello World!"),
        ("Zqd xnt njzx?", -1, "Are you okay?"),
        ("oannLxmnLjvy", 9, "freeCodeCamp"),
    ],
)
def test_message_decoder(message: str, shift: int, expected: str) -> None:
    assert decode(message, shift) == expected
