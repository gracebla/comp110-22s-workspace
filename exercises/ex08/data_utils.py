"""Dictionary related utility functions."""

__author__ = "730224294"

from csv import DictReader

    
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows ov a CSV into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding='utf8')
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Reduce a list of values into a simple column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented representation of a table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column based table with N rows of data."""   
    result: dict[str, list[str]] = {}
    for column in column_table:
        new_list: list[str] = []
        starting: int = 0 
        while starting < N and starting < len(column_table[column]):
            new_list.append(column_table[column][starting])
            starting += 1
        result[column] = new_list 
    return result 


def select(original: dict[str, list[str]], mutated: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in mutated:
        result[column] = original[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result: 
            result[column].append(table2[column][0])
        else: 
            result[column] = table2[column]
    return result


def count(original_list: list[str]) -> dict[str, int]:
    """Produces a dictionary that lists the number of times a value appears in a list."""
    result: dict[str, int] = {}
    for column in original_list:
        if column in result:
            result[column] += 1
        else: 
            result[column] = 1
    return result


def avg(original_dict: list[str]) -> float:
    """Takes a list of integers and produces an average for that list."""
    avg_counter: int = 0
    counter: int = 0
    for item in original_dict: 
        number: int = int(item)
        avg_counter += number
        counter += 1
    avg_counter = avg_counter // counter
    return avg_counter
