#!/usr/bin/python3
"""
square module

This module contians the definition of the Square class

"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Defines the Sqare class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes of the Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides the builtin __str__() function to print out custom string
        representation of the Square object"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """getter method for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square object"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
