#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for num in arr:
            ldx = arr.index(num)
            print("{}".format(num), end=" " if ldx != len(arr) - 1 else "")
        print()
