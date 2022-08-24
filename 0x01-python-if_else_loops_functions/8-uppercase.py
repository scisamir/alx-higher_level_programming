#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    length = len(str)
    for i in range(length):
        char = str[i]
        char_ord = ord(char)
        if char_ord >= ord('a') and char_ord <= ord('z'):
            up_char = char_ord - 32
            new_str += chr(up_char)
    print("{}".format(new_str)
