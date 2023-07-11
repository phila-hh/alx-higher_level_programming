#!/usr/bin/python3
"""
1-write_file module

This module contains the write_file() function

"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of
    characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
