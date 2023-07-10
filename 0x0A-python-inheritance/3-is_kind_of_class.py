#!/usr/bin/python3
"""
3-is_kind_of_class module

This module contains the is_kind_of_class function

"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj (Object): object input to be checked
        a_class (Class): class input to check the object against
    """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
