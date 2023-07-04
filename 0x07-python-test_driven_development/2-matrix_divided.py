#!/usr/bin/python3
"""
2-matrix_divided module

This module contains matrix_divided() function.

"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix where each memeber has been divided by div

    Args:
        matrix (list): list of lists of integers or floats
        div (int, float): the divider, must be >= 0
    """
    m_type_emsg = "matrix must be a matrix (list of lists) of integers/floats"
    m_len_emsg = "Each row of the matrix must have the same size"
    d_type_emsg = "div must be a number"
    d_zero_emsg = "division by zero"

    if type(matrix) is not list:
        raise TypeError(m_type_emsg)

    row_len = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(m_type_emsg)
        for i in row:
            if type(i) not in (int, float):
                raise TypeError(m_type_emsg)
        if len(row) != row_len and row_len != 0:
            raise TypeError(m_len_emsg)
        row_len = len(row)

    if type(div) not in (int, float):
        raise TypeError(d_type_emsg)
    if div == 0:
        raise ZeroDivisionError(d_zero_emsg)

    return [[round(x / div, 2) for x in row] for row in matrix]
