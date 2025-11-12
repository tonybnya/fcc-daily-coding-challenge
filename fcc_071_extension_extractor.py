"""
Script Name : fcc_071_extension_extractor.py
Description : Extension Extractor
Author      : @tonybnya

Given a string representing a filename, return the extension of the file.

- The extension is the part of the filename that comes after the last period (.).
- If the filename does not contain a period or ends with a period, return "none".
- The extension should be returned as-is, preserving case.
"""


def get_extension(filename: str) -> str:
    if "." not in filename or filename.endswith("."):
        return "none"
    return filename.split(".")[-1]
