#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return (res)
    return (res)
