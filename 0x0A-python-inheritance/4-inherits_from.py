#!/usr/bin/python3
"""
4-inherits_from module

This module contains the inherits_from function

"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (Object): the object input to be checked
        a_class (Class): the class input to check the object against
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
