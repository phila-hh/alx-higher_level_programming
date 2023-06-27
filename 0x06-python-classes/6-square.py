#!/usr/bin/python3
"""Square module

This module contains a class that defines a square with an init method that
initializes the size and position of a square while also checking if the given
parameter values are correct, and the setter and getter methods to set and get
them. This class also defines an area method that
computes and returns the are of the square, and another method that prints the
square to stdout.

"""


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes attributes of a Square object

        Args:
            size (int): size of one side of the square
            position (tuple): coordinates of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        "get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get or set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2\
                and value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of two positive\
                     integers")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' char on to the stdout"""
        if self.__size == 0:
            print()
            return

        for s in range(self.__position[1]):
            print("")

        x_pos = " " * self.__position[0]
        for i in range(self.__size):
            print("{}".format(x_pos), end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
