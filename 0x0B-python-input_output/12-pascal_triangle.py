#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]

    arr = [1, 1]

    if n == 2:
        return arr
    else:
        i = 2
        new_arr = [1]

        while i < n:
            for j in range(len(arr) - 1):
                new_arr.append(arr[j] + arr[j + 1])
            new_arr.append(1)
            arr = new_arr
            i += 1
        return new_arr
