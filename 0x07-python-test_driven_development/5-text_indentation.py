#!/usr/bin/python3
"""
5-text_indentation module

This module contains text_indentation() function

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): the text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""

    print(line.lstrip(' '), end='')
