#!/usr/bin/python3
for i in range(65, 91):
    term = ""

    if i == 90:
        term = "\n"
    print("{}".format(chr(i)), end=term)
