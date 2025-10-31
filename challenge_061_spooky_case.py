"""
Script Name : challenge_061_spooky_case.py
Description : SpOoKy~CaSe
Author      : @tonybnya

Given a string representing a variable name,
convert it to "spooky case" using the following constraints:

- Replace all underscores (_), and hyphens (-) with a tilde (~).
- Capitalize the first letter of the string, and every other letter after that.
  Ignore the tilde character when counting. Make all other letters lowercase.

For example, given hello_world, return HeLlO~wOrLd.
"""


def spookify(boo: str) -> str:
    lst: list[str] = [None] * len(boo)
    lst[0] = boo[0].upper()
    counter: int = 0
    for i in range(1, len(boo)):
        if boo[i] in ("_", "-"):
            lst[i] = "~"
        elif boo[i].isalpha():
            counter += 1
            if counter % 2 == 0:
                lst[i] = boo[i].upper()
            else:
                lst[i] = boo[i].lower()
    return "".join(lst)
