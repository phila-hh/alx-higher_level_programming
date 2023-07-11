#!/usr/bin/python3
"""
9-student module

This module contains the Student class

"""


class Student():
    """defines a Student"""

    def __init__(self, first_name, last_name, age):
        """initializes the attributes of the Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
