#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    elif len(tuple_a) == 0:
        tuple_a = 0, 0

    if len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0
    elif len(tuple_b) == 0:
        tuple_b = 0, 0

    a, *c = tuple_a
    b, *d = tuple_b

    res = a + b, c[0] + d[0]
    return res
