"""Directory for invert, favorite_color and count."""

__author__ = 730224294


def invert(first: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    return_dict: dict[str, str] = {}
    for key in first:
        return_dict = {first[key]: key} 
    return return_dict

    