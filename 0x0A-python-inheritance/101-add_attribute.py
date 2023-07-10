#!/usr/bin/python3
"""
101-add_attribute module

This module contains the add_attribute() function

"""


def add_attribute(obj, att, value):
    """Adds a new to attributer to an object if it is possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
