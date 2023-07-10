#!/usr/bin/python3
"""
7-base_geometry module

This module contains the BaseGeometry class which defines the area() and
integer_validator() methods

"""


class BaseGeometry():
    """Defines a BaseGeometry class"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): string input
            value (int): the value input to be validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
