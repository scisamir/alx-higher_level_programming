#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    res = []

    if n >= 1:
        res.append([1])
    if n >= 2:
        res.append([1, 1])
    if n > 2:
        arr = [1, 1]

        for i in range(2, n):
            new_arr = [1]

            for j in range(len(arr) - 1):
                new_arr.append(arr[j] + arr[j + 1])
            new_arr.append(1)
            arr = new_arr
            res.append(new_arr)
    return res
