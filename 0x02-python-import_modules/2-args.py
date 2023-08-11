#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    args = len(argv) - 1

    print("{}".format(args), end=' ')
    print("{}".format("argument" if args == 1 else "arguments"), end='')
    print("{}".format(":" if args >= 1 else "."))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
