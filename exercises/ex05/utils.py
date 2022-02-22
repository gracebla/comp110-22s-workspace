"""Directory for functions only_evens, sub and concat."""

__author__ = 730224294


def only_evens(guess: list[int]) -> list[int]:
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


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Return two specific integers of a list."""
    return_list: list[int] = list()
    while a < b and a < len(a_list):
        return_list.append(a_list[a])
        a += 1
    return return_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generate new list which merges two lists together."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        new_list.append(first_list[i])
        i += 1
    counter: int = 0
    while counter < len(second_list):
        new_list.append(second_list[counter])
        counter += 1
    return new_list
