"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730224294"


class Simpy:
    """Creation of new object Simpy with one attribute."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor definition."""   
        self.values = values

    def __str__(self) -> str:
        """Produce a str representation.""" 
        return f"Simpy({self.values})"

    def fill(self, value: float, number: int) -> None:
        """Fill a simpy's values with aa specific number of repeating values."""
        i: int = 0 
        answer: list[float] = []
        while i < number:
            answer.append(value)
            i += 1
        self.values = answer
      
    def arange(self, first: float, last: float, number: float = 1.0) -> None:
        """Fill in the values within a given range."""
        answer: list[float] = []
        if last > first:
            while first < last:
                answer.append(first)
                first += number
        if last < first: 
            while first > last:
                answer.append(first)
                first += number
        self.values = answer

    def sum(self) -> float:
        """Returns the sum of all items in the values list of a Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition operator to add Simpy's and floats."""
        answer: list[float] = []
        if isinstance(rhs, float):
            for number in self.values:
                answer.append(number + rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                answer.append(self.values[i] + rhs.values[i])
        return Simpy(answer)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Utilizes the power operator to produce a Simpy object raised to another power."""
        answer: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                new: float = item ** rhs
                answer.append(new)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                answer.append(self.values[i] ** rhs.values[i])
        return Simpy(answer)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Create a mask based on equality of each item in values to some other Simpy object."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask of a Simpy that shows whether the values are greater than a certain float or other Simpy."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)   
        return mask  

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[Simpy, float]:
        """Add subscription notation to Simpy."""
        answer: list[float] = []
        if isinstance(rhs, int):
            for i in range(len(self.values)):
                if i == rhs:
                    return self.values[i]
        else:
            for i in range(len(self.values)):
                if rhs[i] is True:
                    answer.append(self.values[i])
        return Simpy(answer)
