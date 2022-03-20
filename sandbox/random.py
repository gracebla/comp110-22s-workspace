"""Testing solution for Quiz02."""


def vowels_and_threes(vowels: str) -> str:
    """Random."""
    ans: str = ''
    i: int = 0
    list_1: list[str] = ['a', 'e', 'i', 'o', 'u']
    while i < len(vowels):
        if vowels[i] in list_1:
            if i % 3 != 0:
                ans += vowels[i]
        i += 1
    return ans


print(vowels_and_threes("aeiou"))

def average_grades