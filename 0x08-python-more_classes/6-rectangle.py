#!/usr/bin/python3
"""Rectangle module

This module contains a class that defines a rectangle with an init method that
intializes its width and height while also checking if the values are correct.
The class also defines setter and getter methods to set and get the value of
both the width and height of the rectangle, as well as an area and perimeter
methods that compute the area and perimeter of the rectangle respectively.
A __str__ method is also present to handle the builtin class print function,
and a __repr__ method that returns a string that can be handled by the eval()
function to create a new rectangle object. A __del__ method that handles the
deletion of the rectangle object.

"""


class Rectangle():
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes attributes for a Rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __repr__(self):
        """Returns a string representation of the Rectangle to be handled by
        the builtin eval() function"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """Sets the print behaviour of the Rectangle object"""
        rect_string = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rect_string += "#"
                if i != self.__height - 1:
                    rect_string += "\n"
        return rect_string

    def __del__(self):
        """Deletes a rectangle object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Returns the area of the Rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
