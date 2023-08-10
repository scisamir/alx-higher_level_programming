#!/usr/bin/python3
def uppercase(str):
    strlen = 0
    for letter in str:
        strlen += 1
        let_ascii = ord(letter)
        if ord(letter) >= 97 and ord(letter) <= 122:
            let_ascii -= 32
        lett = chr(let_ascii)
        print("{}".format(lett), end='')
    print()
