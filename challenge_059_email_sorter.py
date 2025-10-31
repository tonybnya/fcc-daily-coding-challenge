"""
Script Name : challenge_059_email_sorter.py
Description : Email Sorter
Author      : @tonybnya

On October 29, 1971, the first email ever was sent,
introducing the username@domain format we still use.
Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort
them alphabetically by domain name first (the part after the @),
and username second (the part before the @).

- Sorting should be case-insensitive.
- If more than one email has the same domain, sort them by their username.
- Return an array of the sorted addresses.
- Returned addresses should retain their original case.

For example, given ["jill@mail.com", "john@example.com", "jane@example.com"],
return ["jane@example.com", "john@example.com", "jill@mail.com"].
"""


def sort(emails: list[str]) -> list[str]:
    # username, domain = email.split('@')
    # so username = email.split('@')[0]
    # domain = email.split('@')[1]
    # we should first sort by domain, then by username
    # if sorting is case-insensitive, so we lower() both username & domain
    return sorted(
        emails,
        key=lambda email: (email.split("@")[1].lower(), email.split("@")[0].lower()),
    )
