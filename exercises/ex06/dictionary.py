"""Directory for invert, favorite_color and count."""

__author__ = 730224294


def invert(first: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    return_dict: dict[str, str] = {}
    for key in first:
        if first[key] in return_dict:
            raise KeyError("Key already exists.")
        return_dict[first[key]] = key
    return return_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns most common favorite color from a dictionary of favorite colors.""" 
    return_dict: dict[str, int] = {}
    final_color: str = ''
    final_variable: int = 0
    for key in color:
        current_color = color[key] 
        if color[key] in return_dict:
            return_dict[current_color] += 1
        else: 
            return_dict[current_color] = 1
    for key in return_dict:
        if return_dict[key] > final_variable:
            final_variable = return_dict[key]
            final_color = key
    return final_color 


def count(counter: list[str]) -> dict[str, int]:
    """Creates a dictionary that shows how many times certain strings were present in a list."""
    new_dict: dict[str, int] = {}
    for item in counter:
        current_item = item
        if item in new_dict:
            new_dict[current_item] += 1 
        else: 
            new_dict[current_item] = 1 
    return new_dict
