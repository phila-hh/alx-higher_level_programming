#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        return str
    elif n < 0:
        n = len(str) + n

    i = 0
    new = ""
    for c in str:
        if i != n:
            new += c
        i += 1
    return new
