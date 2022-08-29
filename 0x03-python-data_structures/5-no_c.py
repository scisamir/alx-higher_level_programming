#!/usr/bin/python3
def no_c(my_string):
    liss = []
    strg = ""
    for i in my_string:
        liss.append(i)

    cout = liss.count('c')
    if cout == 0:
        return my_string

    for j in range(cout):
        liss.remove('c')

    for k in range(len(liss)):
        strg += liss[k]
    return strg

print(no_c("Best School"))
