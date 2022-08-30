#!/usr/bin/python3
def no_c(my_string):
    liss = []
    strg = ""
    for i in my_string:
        liss.append(i)

    cout = liss.count('C')
    coutc = liss.count('c')
    if cout == 0 and coutc == 0:
        return my_string

    if cout == 0 and coutc > 0:
        for j in range(coutc):
            liss.remove('c')

    if coutc == 0 and cout > 0:
        for k in range(cout):
            liss.remove('C')

    if coutc > 0 and cout > 0:
        for l in range(cout):
            liss.remove('C')
        for m in range(coutc):
            liss.remove('c')

    for letter in liss:
        strg += letter
    return strg
