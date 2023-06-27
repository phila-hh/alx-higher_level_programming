#!/usr/bin/python3
"""Square module

This module contains a class that defines a square with an init method that
initializes its size while also checking if the given parameter value is
correct, and a setter and getter methods to set and get the size of the square
respectively. This class also defines an area method that computes and returns
the area of a square.

"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes attributes of a Square object

        Args:
            size (int): size of one side of the square
        """
        self.__size = size

    @property
    def size(self):
        """get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
