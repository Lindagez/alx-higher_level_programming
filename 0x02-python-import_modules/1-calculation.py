#!/usr/bin/python3
from calculator_1 import sub, add, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    signs = "+-*/"
    SignByFun = {"-": sub, "+": add, "*": mul, "/": div}
    for i in signs:
        print("{:d} {} {:d} = {:d}".format(a, i, b, SignByFun[i](a, b))
