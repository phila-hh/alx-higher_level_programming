#!/usr/bin/python3
"""
1-my_list module

This module contains a class that inherits the the attributes of the list class
and also contains a method that prints a list object in a sorted manner.

"""


class MyList(list):
    """ defines a class that inherits the list class """

    def print_sorted(self):
        """prints a list in an ascendingly sorted manner"""
        print(sorted(self))
