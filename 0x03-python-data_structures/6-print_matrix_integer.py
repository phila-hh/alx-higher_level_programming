#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print("{}".format(matrix[x][y]), end="")
            print(" " if y < len(matrix[x]) - 1 else "", end="")
        print()
