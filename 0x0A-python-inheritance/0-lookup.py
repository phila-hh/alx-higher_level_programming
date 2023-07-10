#!/usr/bin/python3
"""
0-lookup module

This module contains a function lookup.

"""


def lookup(obj):
    """returns a list of available attributes and methods of an object

    Args:
        obj (Object): the input object
    """
    return dir(obj)
