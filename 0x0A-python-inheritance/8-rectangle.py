#!/usr/bin/python3
"""
8-rectangle module

This module contains the Rectangle class that inherits the BaseGeometry class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class"""

    def __init__(self, width, height):
        """initializes the Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
