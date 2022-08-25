#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    l = sys.argv
    if len(l) == 1:
        print("0 arguments.")
    else:
        if len(l) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(l) - 1))
        for i in range (1, len(l)):
            print("{}: {}".format(i, l[i]))
