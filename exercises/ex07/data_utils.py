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
    first_row: dict[str, str] = column_table[0]
    for column in first_row:
        new_list: list[str] = []
        starting: int = 0 
        while starting <= N:
            new_list.append(column[starting])
            starting += 1
        result[column] = column_values
   
    return result 