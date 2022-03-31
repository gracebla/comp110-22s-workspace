from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]
    
    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator."""
        # setup a result list of strings that is empty
        result: list[str] = []
        # loop through each item in self.items for each item
        if isinstance(rhs, str):
            for item in self.items:
                # for each item appent the concatenation of item and rhs to results list
                result.append(item + rhs)   
        else:
            # build ip result list by concatenating each item in self.items with corresponding item in rhs.items
            i: int = 0
            for item in self.items:
                while len(rhs.items) < i:
                    result.append(item + rhs.items[i])
                    i += 1
        # return a newlu constructed str array whose items are result
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
team: StrArray = first + last
print(result)