#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
