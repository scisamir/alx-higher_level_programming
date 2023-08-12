#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    ops = ["+", "-", "*", "/"]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)

    print("{} {} {} = {}".format(a, op, b, res))
