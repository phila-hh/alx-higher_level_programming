#!/usr/bin/python3
"""
12-pascal_triangle module

This module contains the pascal_triangle() function

"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        x = 11 ** i
        row = [int(digit) for digit in str(x)]
        triangle += [row]
    return triangle
