#!/usr/bin/python3
def uppercase(str):
    strlen = 0
    for letter in str:
        strlen += 1
        if ord(letter) >= 97 and ord(letter) <= 122:
            print(chr(ord(letter) - 32), end='' if strlen < len(str) else "\n")
        else:
            print(letter, end='' if strlen < len(str) else "\n")
