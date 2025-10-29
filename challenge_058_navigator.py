"""
Script Name : challenge_058_navigator.py
Description : Navigator
Author      : @tonybnya

On October 28, 1994, Netscape Navigator was released,
helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator,
return the current page you are on after executing all the commands
using the following rules:

- You always start on the "Home" page,
  which will not be included in the commands array.
- Valid commands are:
    - "Visit Page": Where "Page" is the name of the page you are visiting.
      For example, "Visit About" takes you to the "About" page. When you visit
      a new page, make sure to discard any forward history you have.
    - "Back": Takes you to the previous page in your history or stays
      on the current page if there isn't one.
    - "Forward": Takes you forward in the history to the page you came
      from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
"""


def get_page(command: str) -> str:
    """
    Get the page in a string command.
    """
    return command.split(" ", 1)[-1]


def navigate(commands: list[str]) -> str:
    current_page: str = "Home"
    back_history: list[str] = []
    forward_history: list[str] = []
    for command in commands:
        if command.startswith("Visit"):
            page = get_page(command)
            back_history.append(current_page)
            current_page = page
            forward_history.clear()
        elif command == "Back":
            if back_history:
                forward_history.append(current_page)
                current_page = back_history.pop()
        elif command == "Forward":
            if forward_history:
                back_history.append(current_page)
                current_page = forward_history.pop()
    return current_page
