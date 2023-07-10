#!/usr/bin/python3
"""
10-square module

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
