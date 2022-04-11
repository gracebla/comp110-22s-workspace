"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730224294"


class Simpy:
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

        