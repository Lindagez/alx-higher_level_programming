#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_arg = len(argv) - 1
    if num_arg == 1:
        print("{:d} argument:".format(num_arg))
    elif num_arg < 1:
        print("{:d} argument.".format(num_arg))
    else:
        print("{:d} arguments:".format(num_arg))
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
