#!/usr/bin/python3
"""
0-read_file module

This module contains the read_file() function

"""


def read_file(filename=""):
    """reads a text file and prints it in the stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
