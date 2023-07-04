#!/usr/bin/python3
"""
4-print_square module

This module contains print_square() function

"""


def print_square(size):
    """
    Prints a square with the character # to the stdout

    Args:
        size (int): the length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + '\n') * size, end='')
