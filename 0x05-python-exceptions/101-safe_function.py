#!/usr/bin/python3

def safe_function(fct, *args):
    res = None

    try:
        res = fct(*args)
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return None
    return (res)
