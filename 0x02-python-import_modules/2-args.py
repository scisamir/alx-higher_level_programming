#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len1 = len(argv) - 1
    if len1 == 0:
        print("0 arguments.")
    else:
        if len1 == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(len1)
        for i in range(len1):
            j = i + 1
            print("{}: {}".format(j, argv[j]))
