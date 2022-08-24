#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(l):
        s = ord('str[i]')
        if s >= ord('a') and s <= ord('z'):
            str[i] == chr(s - 32)
    print("{}".format(str))
