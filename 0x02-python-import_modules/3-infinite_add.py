#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) >= 2:
        print(sum([int(number) for number in argv[1:]]))
    else:
        print("{:d}".format(0))
