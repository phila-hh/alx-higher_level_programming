#!/usr/bin/python3
"""
100-append_after module

This module contains the append_after() function

"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific
    string"""
    text = ""
    with open(filename, mode="r") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as f:
        f.write(text)
