#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) <= 1:
        print("0 arguments.")
    else:
        for i in range (len(argv)):
            print("{}: {}\n".format(i, argv[i]))
