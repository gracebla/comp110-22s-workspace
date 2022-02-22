"""Directory for functions only_evens, ."""

__author__ = 730224294


def only_evens(guess: list[int]) -> list:
    """Test to return even numbers present in a list."""
    start_len: int = len(guess)
    i: int = 0
    ans: list[int] = list()
    while i < start_len:
        for item in guess: 
            if item % 2 == 0:
                ans.append(guess[i])
                i += 1
    return ans


def sub(a_list: list[int], a: int, b: int) -> list:
    """Return two specific integers of a list."""
    start_len: int = a_list[a]
    return_list: list[int] = list()
    while start_len < b:
        return_list.append(a_list[a])
        a += 1
    return return_list


def concat(first_list: list[int], second_list: list[int]) -> list:
    """Generate new list which merges two lists together."""
    i: int = 0
    while i < len(second_list):
        first_list.append(second_list[i])
        i += 1
    return first_list
