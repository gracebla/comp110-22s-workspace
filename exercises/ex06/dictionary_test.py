"""Space to run tests for dictionary."""

__author__ = 730224294

from dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None: 
    """Use case that tests short dictionary for inverting keys and values."""
    xs: dict[str, str] = {'UNC': 'win', 'DUKE': 'lose'}
    assert invert(xs) == {'win': 'UNC', 'lose': 'DUKE'}


def test_invert_empty() -> None:
    """Edge case that tests empty dictionary for inverting."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_second() -> None: 
    """Second use case that tests short dictionary for inverting keys and values."""
    xs: dict[str, str] = {'grace': 'chocolate', 'sara': 'vanilla'}
    assert invert(xs) == {'chocolate': 'grace', 'vanilla': 'sara'}


def test_favorite_color_empty() -> None:
    """Edge case that returns empty string for most common color."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ''


def test_favorite_color() -> None:
    """Use case to return most common color."""
    xs: dict[str, str] = {'grace': 'blue', 'sarah': 'pink', 'riley': 'blue'}
    assert favorite_color(xs) == 'blue'


def test_favorite_color_second() -> None:
    """Second use case to return most common color with multiple favorite colors."""
    xs: dict[str, str] = {'grace': 'pink', 'abbie': 'pink', 'lauren': 'gray', 'scott': 'yellow', 'jim': 'yellow', 'harry': 'blue'}
    assert favorite_color(xs) == 'pink'


with pytest.raises(KeyError):
    my_dictionary = {'Grace': 'Blake', 'Kathryn': 'Blake'}
    invert(my_dictionary)


def test_count() -> None:
    """Use case to create new dictionary from a list."""
    xs: list[str] = ["apple", "bannana", "apple", "strawberry"]
    assert count(xs) == {'apple': 2, 'bannana': 1, 'strawberry': 1}


def test_count_empty() -> None: 
    """Edge case to test count function."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_second() -> None: 
    """Second use case to test count function."""
    xs: list[str] = ["UNC", "Duke", "UNC", "NC State", "NC State", "UNC"]
    assert count(xs) == {'UNC': 3, 'Duke': 1, 'NC State': 2}