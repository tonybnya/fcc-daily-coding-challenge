"""
Script Name : challenge_049_extract_attributes.py
Description : HTML Attribute Extractor
Author      : @tonybnya

Given a string of a valid HTML element,
return the attributes of the element using the following criteria:

- You will only be given one element.
- Attributes will be in the format: attribute="value".
- Return an array of strings with each attribute property and value,
  separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
- Return attributes in the order they are given.
- If no attributes are found, return an empty array.
"""


def split_attributes(s: str) -> list[str]:
    """
    Split attributes into list of attributes
    e.g. 'id="submit" class="btn btn-primary"'
         -> ['id="submit"', 'class="btn btn-primary"']
    """
    attributes: list[str] = []
    current: str = ""
    inside_quotes: bool = False
    for ch in s:
        if ch == '"':
            inside_quotes = not inside_quotes
        if ch == " " and not inside_quotes:
            if current:
                attributes.append(current)
                current = ""
        else:
            current += ch
    if current:
        attributes.append(current)
    return attributes


def get_attributes(element: str) -> list[str]:
    """
    Extract string inside open tag
    """
    inside: str = ""
    start_index: int = element.find("<")
    end_index: int = element.find(">")
    inside = element[start_index + 1 : end_index]
    if "=" not in inside:
        return []
    if inside.endswith("/"):
        inside = inside.replace("/", "")
    inside = inside.strip()
    first_space_index: int = inside.find(" ")
    return split_attributes(inside[first_space_index + 1 :])


def parse_attributes(attributes: list[str]) -> list[tuple[str, str]]:
    """
    Extract name and value in an attribute
    """
    if not attributes:
        return []
    attributes_list: list[tuple[str, str]] = []
    for attribute in attributes:
        index_eq: int = attribute.find("=")
        name: str = attribute[:index_eq]
        index_first_quote: int = attribute.find('"')
        index_last_quote: int = attribute.rfind('"')
        value: str = attribute[index_first_quote + 1 : index_last_quote]
        attributes_list.append((name, value))
    return attributes_list


def extract_attributes(element: str) -> list[str]:
    attributes: list[str] = get_attributes(element)
    if not attributes:
        return []
    attributes_list: list[tuple[str, str]] = parse_attributes(attributes)
    if not attributes_list:
        return []
    result: list[str] = []
    for attribute in attributes_list:
        name, value = attribute
        result.append(f"{name}, {value}")
    return result
