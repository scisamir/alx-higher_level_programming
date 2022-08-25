#!/usr/bin/python3
s = ""
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            continue
        else:
            s += str[i]
