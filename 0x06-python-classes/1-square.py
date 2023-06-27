#!/usr/bin/python3
"""Square module

This module containes a class that defines a square and an init method that
initalizes its size

"""


class Square():
    """Defines a square"""

    def __init__(self, size):
        """Initializes attributes for a Square object

        Args:
            size (int): size of one side of the square
        """
        self.__size = size
