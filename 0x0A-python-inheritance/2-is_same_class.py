#!/usr/bin/python3
"""
2-is_same_class module

This module contains the is_same_class function

"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a specified class

    Args:
        obj (Object): object input to be checked
        a_class (Class): class input to check the object against
    """
    return (type(obj) is a_class)
