#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")
    else:
        if num == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(num)
        for i in range(num):
            j = i + 1
            print("{}: {}".format(j, argv[j]))
