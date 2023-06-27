#!/usr/bin/python3
"""Square module

This module contains a class that defines a square with an init method that
initializes its size while also checking if the given parameter value is
correct

"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes attributes of a Square object

        Args:
            size (int): size of one side of the square

        Raises:
            TypeError: if value of size is not given as integer
            ValueError: if value of size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
