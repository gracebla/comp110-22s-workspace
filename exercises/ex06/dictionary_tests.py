"""Space to run tests for dictionary."""

__author__ = 730224294

from dictionary import invert


def test_invert() -> None: 
    """Use case that tests short dictionary for inverting keys and values."""
    xs: dict[str, str] = {'UNC': 'win', 'DUKE': 'lose'}
    assert invert(xs) == {'win': 'UNC', 'lose': 'DUKE'}


def test_invert_empty() -> None:
    """Edge case that tests empty list for inverting."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}
