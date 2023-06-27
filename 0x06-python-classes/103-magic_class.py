#!/usr/bin/python3
"""MagicClass module.

This module contains the MagicClass class written from the bytecode exercise

"""


import math


class MagicClass():
    """Defines a MagicClass object"""

    def __init__(self, radius=0):
        """Initializes attributes for the MagicClass object

        Args:
            radius (int, float): radius of the circle
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
