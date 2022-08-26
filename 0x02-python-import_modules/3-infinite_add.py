#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv

    res = 0
    for i in range (1, len(argv)):
        res = res + int(argv[i])
    print(res)
