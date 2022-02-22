"""Implementing function tests from utils."""

__author__ = 730224294

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None: 
    """Edge case that tests empty list for even integers."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_first() -> None:
    """Use case that tests short lists for even integers."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_second() -> None:
    """Second use case that tests short list for even integers."""
    xs: list[int] = [1, 5, 6]
    assert only_evens(xs) == [6]


def test_third_test_only_evens() -> None:
    """Use case that tests short lists for even integers."""
    xs: list[int] = [-2, -4, 7]
    assert only_evens(xs) == [-2, -4]


def test_sub_empty() -> None:
    """Edge case that returns empty list for empty list with no  assigned integers."""
    xs: list[int] = []
    g: int = (0)
    h: int = (0)
    assert sub(xs, g, h) == []


def first_test_sub() -> None:
    """Use test that returns designated values in short list."""
    xs: list[int] = [1]
    g: int = (1)
    h: int = (1)
    assert sub(xs, g, h) == []


def second_test_sub() -> None: 
    """Second use test that returns designated values in short list."""
    xs: list[int] = [9, 13, 3, 4, 7]
    g: int = (0)
    h: int = (2)
    assert sub(xs, g, h) == [9, 13]


def test_concat_empty() -> None:
    """Edge test that returns concacted empty list of two empty lists."""
    xs: list[int] = []
    gb: list[int] = []
    assert concat(xs, gb) == []


def first_test_concat() -> None: 
    """Use test that concats two separate lists."""
    xs: list[int] = [1, 2, 3, 4]
    gb: list[int] = [5, 6, 7]
    assert concat(xs, gb) == [1, 2, 3, 4, 5, 6, 7]


def second_test_concat() -> None: 
    """Second use test that concats two separate lists."""
    xs: list[int] = [5, 10, 15]
    gb: list[int] = [20, 25, 30]
    assert concat(xs, gb) == [5, 10, 15, 20, 25, 30]