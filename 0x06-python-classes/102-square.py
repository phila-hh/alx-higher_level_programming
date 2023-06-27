#!/usr/bin/python3
"""Square module

This module contains a class that defines a square with an init method that
initializes the size of the square while also checking if the given parameter
value is correct, and a method that computes and returns the area of the
square. This also has setter and getter methods to get and set the size,
as well as other methods used to compare two objects.

"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes attributes of the Square object

        Args:
            size (int): size of one side of the Square
        """
        self.__size = size

    @property
    def size(self):
        """gets or sets the size of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the Square object"""
        return self.__size ** 2

    def __eq__(self, other):
        """Sets the compare equality behavior of the Square object

        Args:
            other (Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Sets the compare less than behavior of the Square object

        Args:
            other (Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behavior of the Square object

        Args:
            other (Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() <= other.area()
