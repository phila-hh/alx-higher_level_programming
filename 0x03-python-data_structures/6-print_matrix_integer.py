#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:d}".format(matrix[x][y]), end="")
            print(" " if y < len(x) - 1 else "", end="")
        print()
