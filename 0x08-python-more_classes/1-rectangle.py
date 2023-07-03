#!/usr/bin/python3
"""Rectangle module

This module contains a class that defines a rectangle with an init method that
intializes its width and height while also checking if the values are correct.
The class also defines setter and getter methods to set and get the value of
both the width and height of the rectangle.

"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes attributes for a Rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle

        Args:
            value (int): new value for the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle

        Args:
            value (int): new value for the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
