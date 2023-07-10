#!/usr/bin/python3
"""
11-square module

This module contains the Square class that inherits the Rectangle class

"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a Square object"""

    def __init__(self, size):
        """initializes the attributes of the Sqare object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """override the builtin __str__ method of the Rectangle class to
        return a description of the Square object"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        """computes the area of the Square object"""
        return self.__size ** 2
