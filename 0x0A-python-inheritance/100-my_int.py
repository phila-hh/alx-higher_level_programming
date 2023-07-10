#!/usr/bin/python3
"""
100-my_int module

This module contains MyInt class that inherits the int class and inverts both
the == and != operators

"""


class MyInt(int):
    """Defines the MyInt class"""

    def __eq__(self, operator):
        """inverts the == operator"""
        return int(self) != operator

    def __ne__(self, operator):
        """inverts the != operator"""
        return int(self) == operator
